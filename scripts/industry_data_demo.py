# 行业经济数据演示

import akshare as ak
import pandas as pd

print("=== 行业经济数据演示 ===")

# 获取火力发电量
try:
    thermal_power_generation = ak.industry_energy_thermal_power_generation()
    print("\n火力发电量数据:")
    print(thermal_power_generation.head())
    # 保存数据
    thermal_power_generation.to_csv("thermal_power_generation.csv", index=False, encoding="utf-8-sig")
    print("\n火力发电量数据已保存到 thermal_power_generation.csv")
except Exception as e:
    print(f"获取火力发电量失败: {e}")

# 获取火力发电装机容量
try:
    thermal_power_installed_capacity = ak.industry_energy_thermal_power_installed_capacity()
    print("\n火力发电装机容量数据:")
    print(thermal_power_installed_capacity.head())
    # 保存数据
    thermal_power_installed_capacity.to_csv("thermal_power_installed_capacity.csv", index=False, encoding="utf-8-sig")
    print("\n火力发电装机容量数据已保存到 thermal_power_installed_capacity.csv")
except Exception as e:
    print(f"获取火力发电装机容量失败: {e}")

print("\n=== 演示完成 ===")
