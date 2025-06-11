import time
import requests

BOT_TOKEN = "8037820704:AAHD9njw_pb6hOGmJMOznyENnOrNJPAZ4SM"
CHAT_ID = "7699375774"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram error: {e}")

def simulate_buy(token):
    send_telegram_message(f"🟢 [SIMULATION] Achat simulé du token {token}")

def scan_tokens():
    tokens = ["PEPEMOON", "FLOKINU", "RUGFREE"]
    for token in tokens:
        print(f"Scanning {token}...")
        simulate_buy(token)
        time.sleep(5)

def main():
    send_telegram_message("✅ Bot Solana SIMULATION démarré.")
    while True:
        scan_tokens()
        time.sleep(30)

if __name__ == "__main__":
    main()
