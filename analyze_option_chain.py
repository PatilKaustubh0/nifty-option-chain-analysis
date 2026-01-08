import pandas as pd
from fetch_option_chain import fetch_option_chain

# Optional: sample JSON to use if NSE blocks
SAMPLE_DATA = {
    "records": {
        "expiryDates": ["08-Jan-2026"],
        "data": [
            {
                "strikePrice": 20000,
                "expiryDate": "08-Jan-2026",
                "CE": {"openInterest": 15000},
                "PE": {"openInterest": 12000}
            },
            {
                "strikePrice": 20100,
                "expiryDate": "08-Jan-2026",
                "CE": {"openInterest": 18000},
                "PE": {"openInterest": 16000}
            },
            {
                "strikePrice": 20200,
                "expiryDate": "08-Jan-2026",
                "CE": {"openInterest": 10000},
                "PE": {"openInterest": 20000}
            }
        ]
    }
}


def analyze_nifty_option_chain():
    data = fetch_option_chain()
    
    # Defensive check
    if not data or "records" not in data or not data["records"]["data"]:
        print("NSE response blocked or invalid. Using sample data instead.")
        data = SAMPLE_DATA

    records = data["records"]["data"]
    expiry_dates = data["records"]["expiryDates"]

    current_expiry = expiry_dates[0]  # nearest expiry

    ce_oi = {}
    pe_oi = {}

    for item in records:
        if item.get("expiryDate") != current_expiry:
            continue

        strike = item.get("strikePrice")

        if "CE" in item and item["CE"] is not None:
            ce_oi[strike] = item["CE"].get("openInterest", 0)

        if "PE" in item and item["PE"] is not None:
            pe_oi[strike] = item["PE"].get("openInterest", 0)

    ce_df = pd.DataFrame(ce_oi.items(), columns=["Strike", "CE_OI"])
    pe_df = pd.DataFrame(pe_oi.items(), columns=["Strike", "PE_OI"])

    max_ce = ce_df.loc[ce_df["CE_OI"].idxmax()]
    max_pe = pe_df.loc[pe_df["PE_OI"].idxmax()]

    difference = abs(max_ce["CE_OI"] - max_pe["PE_OI"])

    print("\nNIFTY OPTION CHAIN ANALYSIS")
    print("----------------------------")
    print(f"Current Expiry Date : {current_expiry}")
    print(f"Max CALL OI Strike  : {int(max_ce['Strike'])}, OI = {int(max_ce['CE_OI'])}")
    print(f"Max PUT OI Strike   : {int(max_pe['Strike'])}, OI = {int(max_pe['PE_OI'])}")
    print(f"OI Difference       : {int(difference)}")


if __name__ == "__main__":
    analyze_nifty_option_chain()
