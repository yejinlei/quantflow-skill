# 全球经济数据演示

import akshare as ak
import pandas as pd

print("=== 全球经济数据演示 ===")

# 获取全球经济指标
try:
    global_economic_indicator = ak.global_economic_indicator()
    print("\n全球经济指标数据:")
    print(global_economic_indicator.head())
    # 保存数据
    global_economic_indicator.to_csv("global_economic_indicator.csv", index=False, encoding="utf-8-sig")
    print("\n全球经济指标数据已保存到 global_economic_indicator.csv")
except Exception as e:
    print(f"获取全球经济指标失败: {e}")

# 获取国家经济指标
try:
    global_economic_indicator_country = ak.global_economic_indicator_country()
    print("\n国家经济指标数据:")
    print(global_economic_indicator_country.head())
    # 保存数据
    global_economic_indicator_country.to_csv("global_economic_indicator_country.csv", index=False, encoding="utf-8-sig")
    print("\n国家经济指标数据已保存到 global_economic_indicator_country.csv")
except Exception as e:
    print(f"获取国家经济指标失败: {e}")

print("\n=== 演示完成 ===")
