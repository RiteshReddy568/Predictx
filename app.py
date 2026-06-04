import time
import joblib
import serial
import threading
import pandas as pd
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from utils.alerts import send_telegram_alert

app = Flask(__name__)
# fallback encryption session key
app.secret_key = "industrial_local_only_secret_key"

model = joblib.load('model.pkl')

machines = {
    "motor_01": {
        "name": "Conveyor Motor 01",
        "port": "COM3",  
        "status": "INACTIVE",
        "last_seen": 0,
        "vibration": 0.0, "temperature": 0.0, "current": 0.0, "voltage": 0.0,
        "prediction_status": "STARTING..."
    },
    "motor_02": {
        "name": "Exhaust Fan Motor 02",
        "port": "COM4",
        "status": "INACTIVE",
        "last_seen": 0,
        "vibration": 0.0, "temperature": 0.0, "current": 0.0, "voltage": 0.0,
        "prediction_status": "DISCONNECTED"
    }
}

STATUS_MAP = {
    0: "NORMAL",
    1: "HIGH TEMPERATURE",
    2: "MOTOR OBSTRUCTION",
    3: "VOLTAGE FLUCTUATION"
}

def serial_worker(machine_id):
    m_config = machines[machine_id]
    print(f"🔄 Starting background telemetry scanner for {m_config['name']} on {m_config['port']}")
    
    while True:
        try:
            ser = serial.Serial(m_config['port'], 115200, timeout=1)
            time.sleep(2)  # Allow port initialization to stabilize
            print(f"✅ Hardware connection bound successfully to {machine_id}")
            
            while True:
                line = ser.readline().decode(errors='ignore').strip()
                if not line or ',' not in line:
                    continue

                parts = line.split(',')
                if len(parts) == 4:
                    values = list(map(float, parts))
                    
                    
                    m_config["vibration"] = values[0]
                    m_config["temperature"] = values[1]
                    m_config["current"] = values[2]
                    m_config["voltage"] = values[3]
                    m_config["last_seen"] = time.time()  # Heartbeat stamp
                    
                    
                    df = pd.DataFrame([values], columns=['vibration', 'temperature', 'current', 'voltage'])
                    prediction_id = int(model.predict(df)[0])
                    
                    status_text = STATUS_MAP.get(prediction_id, "UNKNOWN FAULT")
                    m_config["prediction_status"] = status_text

                    
                    if prediction_id != 0:
                        send_telegram_alert(f"{m_config['name']}: {status_text}", *values)

        except Exception as e:
            
            time.sleep(2)


threading.Thread(target=serial_worker, args=("motor_01",), daemon=True).start()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('fleet_status'))
        else:
            error = 'Invalid credentials. Access Denied.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('fleet_status'))

@app.route('/fleet')
def fleet_status():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('fleet.html')

@app.route('/dashboard/<machine_id>')
def machine_dashboard(machine_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if machine_id not in machines:
        return "System configuration mismatch.", 404
    return render_template('index.html', machine_id=machine_id)


@app.route('/api/fleet/status')
def get_fleet_telemetry():
    current_time = time.time()
    for m_id, m_data in machines.items():
        if current_time - m_data['last_seen'] < 4.0:
            m_data['status'] = 'ACTIVE'
        else:
            m_data['status'] = 'INACTIVE'
            m_data['prediction_status'] = 'PORT DISCONNECTED'
    return jsonify(machines)

@app.route('/api/status/<machine_id>')
def get_machine_telemetry(machine_id):
    current_time = time.time()
    m_data = machines.get(machine_id)
    if not m_data:
        return jsonify({"error": "Profile Missing"}), 404
    if current_time - m_data['last_seen'] < 4.0:
        m_data['status'] = 'ACTIVE'
    else:
        m_data['status'] = 'INACTIVE'
        m_data['prediction_status'] = 'PORT DISCONNECTED'
    return jsonify(m_data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)