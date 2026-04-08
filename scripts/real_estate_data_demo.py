# 房地产数据演示

import akshare as ak
import pandas as pd

print("=== 房地产数据演示 ===")

# 获取房价数据
try:
    real_estate_house_price = ak.real_estate_house_price()
    print("\n房价数据:")
    print(real_estate_house_price.head())
    # 保存数据
    real_estate_house_price.to_csv("real_estate_house_price.csv", index=False, encoding="utf-8-sig")
    print("\n房价数据已保存到 real_estate_house_price.csv")
except Exception as e:
    print(f"获取房价数据失败: {e}")

# 获取房地产投资数据
try:
    real_estate_investment = ak.real_estate_investment()
    print("\n房地产投资数据:")
    print(real_estate_investment.head())
    # 保存数据
    real_estate_investment.to_csv("real_estate_investment.csv", index=False, encoding="utf-8-sig")
    print("\n房地产投资数据已保存到 real_estate_investment.csv")
except Exception as e:
    print(f"获取房地产投资数据失败: {e}")

print("\n=== 演示完成 ===")
