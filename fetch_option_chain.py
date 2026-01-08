import requests
import time

NSE_HOME = "https://www.nseindia.com"
NSE_API = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"


def fetch_option_chain(retries=3):
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain",
        "Connection": "keep-alive"
    }

    for attempt in range(retries):
        try:
            # Step 1: Get cookies
            session.get(NSE_HOME, headers=headers, timeout=10)
            time.sleep(2)

            # Step 2: Fetch option chain
            response = session.get(NSE_API, headers=headers, timeout=10)
            data = response.json()

            if "records" in data:
                return data

            print(f"Attempt {attempt + 1}: NSE blocked response, retrying...")
            time.sleep(3)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed:", e)
            time.sleep(3)

    return {}
