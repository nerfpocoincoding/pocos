import requests
import time

URL = "https://discord.com/api/v9"

# paste ur tokens here
TOKENS = {
    "token_1": "TRADING: 1x dragon caneloni regular 250m, 1x garama and madung dung rainbow 700m,3x regular ketupat 35m each,1x fragrama and chocrama 1.2b,2x la taco combination, 700m and 840m,5x nuclearo dinosauro 15m, 60m, 45m, 165m and 210m,7x esok sekolah 30m, 300m (rainbow), 45m diamond, 120m, 150m, 90m and 180m,MOSTLY LOOKING FOR OGS OR RAINBOW DRAGONS, DONT DM IF UR NGF, no reply=nty",
    "token_2": "looking for the following brainrots: dragons 250m+, garamas 150m+, ketupats 70m+, capitano mobys 160m+, la casa boo 300m+, burger 150m+, meowl, elephant, specially overpaying for brainrots with candy, lava, galaxy and rainbow mutations, dm me if u got, strictly ngf",
    "token_3": "lf offers for my: garama 300m brazil mut, blackhole goat 6.4m rb, la jolly grande base, lava tralalelitos, also trading robux via pls donate or ingame gamepass, ngf we may use middleman",
    "token_4": "overpaying for: ketchuru, garama, rare or 500m+ brainrots, we use server mm"
}

CHANNEL_IDS = ["channel_id"]

def send_message(token: str, channel_id: str, content: str) -> bool:
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.post(f"{URL}/channels/{channel_id}/messages", headers=headers, json={"content": content})
    if resp.status_code == 429:
        retry = resp.json().get("retry_after", 5)
        print(f"[{token}] Rate limited. Waiting {retry} seconds.")
        time.sleep(retry)
        return False
    if 200 <= resp.status_code < 300:
        print(f"[{token}] Message sent to {channel_id}")
        return True
    print(f"[{token}] Failed for {channel_id}: {resp.status_code} {resp.text}")
    return False

while True:
    for token, message in TOKENS.items():
        for cid in CHANNEL_IDS:
            send_message(token, cid, message)
            time.sleep(5)
    time.sleep(20)

