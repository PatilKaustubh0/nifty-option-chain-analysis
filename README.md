NIFTY Option Chain Analysis

A simple Python project to fetch and analyze NIFTY index option chain data from the NSE India website.  
The script identifies:

- Strike price with maximum CALL Open Interest (OI)  
- Strike price with maximum PUT Open Interest (OI)  
- Difference between the maximum CALL and PUT OI  

This helps identify potential **support and resistance levels** in the NIFTY index.

---

Features

- Dynamically fetches the **nearest expiry option chain**  
- Calculates **max CALL OI and max PUT OI**  
- Calculates **OI difference** between CALL and PUT  
- Uses **fallback sample data** if NSE blocks automated requests  
- Outputs results clearly to the console  

---

Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `requests`
