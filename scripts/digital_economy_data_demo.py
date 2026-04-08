# 数字经济数据演示

import akshare as ak
import pandas as pd

print("=== 数字经济数据演示 ===")

# 获取互联网用户数
try:
    digital_economy_internet_user = ak.digital_economy_internet_user()
    print("\n互联网用户数数据:")
    print(digital_economy_internet_user.head())
    # 保存数据
    digital_economy_internet_user.to_csv("digital_economy_internet_user.csv", index=False, encoding="utf-8-sig")
    print("\n互联网用户数数据已保存到 digital_economy_internet_user.csv")
except Exception as e:
    print(f"获取互联网用户数失败: {e}")

# 获取移动用户数
try:
    digital_economy_mobile_user = ak.digital_economy_mobile_user()
    print("\n移动用户数数据:")
    print(digital_economy_mobile_user.head())
    # 保存数据
    digital_economy_mobile_user.to_csv("digital_economy_mobile_user.csv", index=False, encoding="utf-8-sig")
    print("\n移动用户数数据已保存到 digital_economy_mobile_user.csv")
except Exception as e:
    print(f"获取移动用户数失败: {e}")

print("\n=== 演示完成 ===")
