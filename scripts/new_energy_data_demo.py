# 新能源数据演示

import akshare as ak
import pandas as pd

print("=== 新能源数据演示 ===")

# 获取新能源汽车销量
try:
    new_energy_vehicle_sales = ak.new_energy_vehicle_sales()
    print("\n新能源汽车销量数据:")
    print(new_energy_vehicle_sales.head())
    # 保存数据
    new_energy_vehicle_sales.to_csv("new_energy_vehicle_sales.csv", index=False, encoding="utf-8-sig")
    print("\n新能源汽车销量数据已保存到 new_energy_vehicle_sales.csv")
except Exception as e:
    print(f"获取新能源汽车销量失败: {e}")

# 获取新能源汽车产量
try:
    new_energy_vehicle_production = ak.new_energy_vehicle_production()
    print("\n新能源汽车产量数据:")
    print(new_energy_vehicle_production.head())
    # 保存数据
    new_energy_vehicle_production.to_csv("new_energy_vehicle_production.csv", index=False, encoding="utf-8-sig")
    print("\n新能源汽车产量数据已保存到 new_energy_vehicle_production.csv")
except Exception as e:
    print(f"获取新能源汽车产量失败: {e}")

print("\n=== 演示完成 ===")
