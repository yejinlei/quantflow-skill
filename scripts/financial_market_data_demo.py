# 金融市场数据演示

import akshare as ak
import pandas as pd

print("=== 金融市场数据演示 ===")

# 获取银行间利率
try:
    financial_market_interbank_rate = ak.financial_market_interbank_rate()
    print("\n银行间利率数据:")
    print(financial_market_interbank_rate.head())
    # 保存数据
    financial_market_interbank_rate.to_csv("financial_market_interbank_rate.csv", index=False, encoding="utf-8-sig")
    print("\n银行间利率数据已保存到 financial_market_interbank_rate.csv")
except Exception as e:
    print(f"获取银行间利率失败: {e}")

# 获取上海银行间同业拆放利率
try:
    financial_market_shibor = ak.financial_market_shibor()
    print("\n上海银行间同业拆放利率数据:")
    print(financial_market_shibor.head())
    # 保存数据
    financial_market_shibor.to_csv("financial_market_shibor.csv", index=False, encoding="utf-8-sig")
    print("\n上海银行间同业拆放利率数据已保存到 financial_market_shibor.csv")
except Exception as e:
    print(f"获取上海银行间同业拆放利率失败: {e}")

print("\n=== 演示完成 ===")
