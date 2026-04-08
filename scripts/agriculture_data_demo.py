# 农业数据演示

import akshare as ak
import pandas as pd

print("=== 农业数据演示 ===")

# 获取粮食产量
try:
    agriculture_grain_production = ak.agriculture_grain_production()
    print("\n粮食产量数据:")
    print(agriculture_grain_production.head())
    # 保存数据
    agriculture_grain_production.to_csv("agriculture_grain_production.csv", index=False, encoding="utf-8-sig")
    print("\n粮食产量数据已保存到 agriculture_grain_production.csv")
except Exception as e:
    print(f"获取粮食产量失败: {e}")

# 获取农作物种植面积
try:
    agriculture_crop_planting_area = ak.agriculture_crop_planting_area()
    print("\n农作物种植面积数据:")
    print(agriculture_crop_planting_area.head())
    # 保存数据
    agriculture_crop_planting_area.to_csv("agriculture_crop_planting_area.csv", index=False, encoding="utf-8-sig")
    print("\n农作物种植面积数据已保存到 agriculture_crop_planting_area.csv")
except Exception as e:
    print(f"获取农作物种植面积失败: {e}")

print("\n=== 演示完成 ===")
