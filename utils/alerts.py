import requests
import time

TOKEN = "8790247629:AAFokG2rAV4ELLVQajmOkvP5EZf4wUNoIF0" 
CHAT_ID = "8223979964"

last_sent_time = 0

def send_telegram_alert(fault_description, vibration, temperature, current, voltage):
    global last_sent_time
    
    
    if time.time() - last_sent_time < 10:
        return

    message = (f"⚠️ *MACHINE INCIDENT REPORT*\n"
               f"🚨 *Alert State:* `{fault_description}`\n\n"
               f"Vibration: `{vibration:.2f} mm/s`\n"
               f"Temp: `{temperature:.2f} °C`\n"
               f"Current: `{current:.2f} A`\n"
               f"Voltage: `{voltage:.2f} V`")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}

    try:
        requests.post(url, json=payload, timeout=5)
        last_sent_time = time.time()
    except Exception as e:
        print(f"Telegram Alert Transmission Failed: {e}")