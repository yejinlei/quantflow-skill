# 交通运输数据演示

import akshare as ak
import pandas as pd

print("=== 交通运输数据演示 ===")

# 获取航空客运量
try:
    transportation_air_passenger = ak.transportation_air_passenger()
    print("\n航空客运量数据:")
    print(transportation_air_passenger.head())
    # 保存数据
    transportation_air_passenger.to_csv("transportation_air_passenger.csv", index=False, encoding="utf-8-sig")
    print("\n航空客运量数据已保存到 transportation_air_passenger.csv")
except Exception as e:
    print(f"获取航空客运量失败: {e}")

# 获取铁路货运量
try:
    transportation_railway_freight = ak.transportation_railway_freight()
    print("\n铁路货运量数据:")
    print(transportation_railway_freight.head())
    # 保存数据
    transportation_railway_freight.to_csv("transportation_railway_freight.csv", index=False, encoding="utf-8-sig")
    print("\n铁路货运量数据已保存到 transportation_railway_freight.csv")
except Exception as e:
    print(f"获取铁路货运量失败: {e}")

print("\n=== 演示完成 ===")
