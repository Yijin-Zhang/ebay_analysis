import pandas as pd

def orders_to_dataframe(orders):
    """
    把 eBay API 返回的订单 JSON 转成 pandas DataFrame
    """
    records = []
    for order in orders:
        records.append({
            "orderId": order.get("orderId"),
            "creationDate": order.get("creationDate"),
            "buyer": order.get("buyer", {}).get("username"),
            "total": order.get("pricingSummary", {}).get("total", {}).get("value"),
            "currency": order.get("pricingSummary", {}).get("total", {}).get("currency"),
            "status": order.get("orderFulfillmentStatus")
        })
    return pd.DataFrame(records)
