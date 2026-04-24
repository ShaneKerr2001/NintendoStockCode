import time
import requests
from bs4 import BeautifulSoup

# =========================
# CONFIG
# =========================
NES_URL = "https://www.nintendo.com/us/store/products/nintendo-entertainment-system-controllers/?srsltid=AfmBOopSMrprIKeVhINLC74saYiuO5kfC3kTKFFxEsp2Ef274xSYsWLA"
SNES_URL = "https://www.nintendo.com/us/store/products/super-nintendo-entertainment-system-controller/?srsltid=AfmBOoqmcNUCUBPn1jf0FAlEyNApfy0f2iWBVPcDHcflk9bHFBjRoAOA"
CHECK_INTERVAL = 900  # seconds (15 minutes)

NES_DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1497089285097128027/kCzcCqAQgXeKc1bbOsue4JSGT_-KCt_ZzKdY26Z6v0QP5zD8hIBhbHCP4LkuEUqb3JZj"
SNES_DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1497087951178432654/zNMYR5-HycxIbwlzYcsGO5vIdiEcGYK_BHZWig8xSmTTTTk1SZnShwFzyYMaJ_-0F7rA"

# =========================
# FUNCTION: Send Discord alert
# =========================
def send_SNES_alert():
    data = {
        "content": "🚨 SNES controller is BACK IN STOCK!\n" + SNES_URL
    }
    requests.post(SNES_DISCORD_WEBHOOK, json=data)

def send_NES_alert():
    data = {
        "content": "🚨 NES controller is BACK IN STOCK!\n" + NES_URL
    }
    requests.post(NES_DISCORD_WEBHOOK, json=data)


def main():
    nes_alerted = False
    snes_alerted = False

    while True:
        try:
            # Check NES
            nes_in_stock = check_NES_stock()
            print("NES in stock:", nes_in_stock)

            if nes_in_stock and not nes_alerted:
                send_NES_alert()
                nes_alerted = True

            if not nes_in_stock:
                nes_alerted = False

            # Check SNES
            snes_in_stock = check_SNES_stock()
            print("SNES in stock:", snes_in_stock)

            if snes_in_stock and not snes_alerted:
                send_SNES_alert()
                snes_alerted = True

            if not snes_in_stock:
                snes_alerted = False

        except Exception as e:
            print("Error:", e)

        time.sleep(CHECK_INTERVAL)

def test_discord():
    print("Sending test alerts...")
    send_NES_alert()
    send_SNES_alert()

if __name__ == "__main__":
    test_discord()
