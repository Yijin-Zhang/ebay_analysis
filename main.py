from datetime import datetime, timedelta
from ebay_api.orders import get_orders
from analysis.transform import orders_to_dataframe
import pandas as pd

if __name__ == "__main__":
    # 获取最近三个月时间范围
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=90)

    start_str = start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    end_str = end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    # 调用 API 获取订单
    orders = get_orders(start_str, end_str)

    # 转换成 DataFrame
    df = orders_to_dataframe(orders)

    # 保存成 Excel
    output_path = "ebay_orders_last3months.xlsx"
    df.to_excel(output_path, index=False)
    print(f"✅ 已获取 {len(df)} 个订单，保存到 {output_path}")
