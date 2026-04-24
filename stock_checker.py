import time
import requests
from bs4 import BeautifulSoup

# =========================
# CONFIG
# =========================
URL = "PASTE_NINTENDO_PRODUCT_URL_HERE"
CHECK_INTERVAL = 300  # seconds (5 minutes)
DISCORD_WEBHOOK = "PASTE_YOUR_DISCORD_WEBHOOK_URL"

# =========================
# FUNCTION: Send Discord alert
# =========================
def send_discord_alert(message):
    data = {"content": message}
    requests.post(DISCORD_WEBHOOK, json=data)

# =========================
# FUNCTION: Check stock
# =========================
def check_stock():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text().lower()

    if "sold out" in text or "out of stock" in text:
        return False
    if "add to cart" in text or "buy now" in text:
        return True

    return False

# =========================
# MAIN LOOP
# =========================
def main():
    already_alerted = False

    while True:
        try:
            in_stock = check_stock()
            print("In stock:", in_stock)

            if in_stock and not already_alerted:
                send_discord_alert(f"🚨 In stock! {URL}")
                already_alerted = True

            if not in_stock:
                already_alerted = False

        except Exception as e:
            print("Error:", e)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
