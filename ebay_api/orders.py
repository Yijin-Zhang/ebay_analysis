import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("EBAY_ACCESS_TOKEN")
BASE_URL = "https://api.ebay.com"  # 如果测试用sandbox改成 https://api.sandbox.ebay.com

def get_orders(start_date, end_date, limit=50):
    """
    获取订单列表
    start_date, end_date: ISO8601 格式时间字符串
    """
    url = f"{BASE_URL}/sell/fulfillment/v1/order"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    params = {
        "filter": f"creationdate:[{start_date}..{end_date}]",
        "limit": limit
    }

    all_orders = []
    offset = 0

    while True:
        params["offset"] = offset
        resp = requests.get(url, headers=headers, params=params)

        if resp.status_code != 200:
            print("Error:", resp.status_code, resp.text)
            break

        data = resp.json()
        orders = data.get("orders", [])
        all_orders.extend(orders)

        # 检查是否还有下一页
        if "href" in data and "next" in data.get("links", [{}])[0].get("rel", ""):
            offset += limit
        else:
            break

    return all_orders
