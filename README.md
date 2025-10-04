# eBay Order Analysis

A simple Python project for **downloading and analyzing your eBay orders** using the official eBay RESTful API.  
It fetches your orders from the last 3 months and exports them to an Excel file.

---

## 📦 Features
- Fetch eBay orders via REST API
- Supports date filtering (e.g., last 3 months)
- Converts raw JSON into a clean DataFrame
- Exports results to Excel (`.xlsx`)
- Easily extendable for further data analysis (e.g., sales trends, visualization)

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/ebay-order-analysis.git
cd ebay-order-analysis
pip install -r requirements.txt


🔑 Configuration

You need to create a .env file inside the config/ folder with your eBay Access Token:

# config/.env
EBAY_ACCESS_TOKEN=YOUR_EBAY_ACCESS_TOKEN


⚠️ Never share your .env file or commit it to GitHub.
The .gitignore already excludes it by default.

🚀 Usage

Run the main script:

python main.py


This will:

Fetch orders from the last 90 days

Convert the data to a table

Save it as ebay_orders_last3months.xlsx

📁 Project Structure
ebay_order_analysis/
│
├── config/
│   └── .env                  # Your eBay Access Token (not in GitHub)
│
├── ebay_api/
│   ├── __init__.py
│   └── orders.py             # API request functions
│
├── analysis/
│   ├── __init__.py
│   └── transform.py          # JSON -> DataFrame conversion
│
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignore cache, logs, secrets
└── README.md                 # Project documentation