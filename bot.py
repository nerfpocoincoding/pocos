import requests
import time

URL = "https://discord.com/api/v9"

# Dicionário com 5 tokens e mensagens personalizadas
TOKENS = {
    "MTQ0MDc5NjE5NjQ5ODE3ODA1Mw.G4Yfpl.3NAn6GmhVew_i0oY3KExTIR_t31K-9QaOM5XUY": "TRADING: 1x dragon caneloni regular 250m, 1x garama and madung dung rainbow 700m,3x regular ketupat 35m each,1x fragrama and chocrama 1.2b,2x la taco combination, 700m and 840m,5x nuclearo dinosauro 15m, 60m, 45m, 165m and 210m,7x esok sekolah 30m, 300m (rainbow), 45m diamond, 120m, 150m, 90m and 180m,MOSTLY LOOKING FOR OGS OR RAINBOW DRAGONS, DONT DM IF UR NGF, no reply=nty",
    "MTQyNTQxODUxNDc4NDg1MDA4Mg.GEBoLn.nn8qofffE9l2lmw259cKW34mYIzJlDJOcUVVuI": "looking for the following brainrots: dragons 250m+, garamas 150m+, ketupats 70m+, capitano mobys 160m+, la casa boo 300m+, burger 150m+, meowl, elephant, specially overpaying for brainrots with candy, lava, galaxy and rainbow mutations, dm me if u got, strictly ngf",
    "MTQxNTA4MzUzNjc1ODczOTE0Ng.G-P2L8.QJ_eZWEnS1In10agKhQX-zqdvLdUNz8RyQ2lRY": "lf offers for my: garama 300m brazil mut, blackhole goat 6.4m rb, la jolly grande base, lava tralalelitos, also trading robux via pls donate or ingame gamepass, ngf we may use middleman",
    "MTQwNzM5MzQyMDA0OTEyNTQ0OA.GUzPus.Go6OKfpiEl3qKT5GoSipZQrivX9-lq85x89fnU": "overpaying for: ketchuru, garama, rare or 500m+ brainrots, we use server mm"
}

CHANNEL_IDS = ["1451612831450529802"]

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

