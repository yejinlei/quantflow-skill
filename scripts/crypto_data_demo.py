#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
加密货币数据演示脚本

使用Akshare获取加密货币历史数据和实时行情
"""

import akshare as ak
import pandas as pd
from datetime import datetime


def get_crypto_hist():
    """获取加密货币历史数据"""
    print("=== 加密货币历史数据 ===")
    try:
        # 示例：获取比特币历史数据
        crypto_hist_df = ak.crypto_currency_hist(
            symbol="bitcoin",
            start_date="2024-01-01",
            end_date=datetime.now().strftime("%Y-%m-%d")
        )
        print(f"获取到 {len(crypto_hist_df)} 条比特币历史数据")
        print("前5条数据:")
        print(crypto_hist_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"crypto_hist_bitcoin_{timestamp}.csv"
        crypto_hist_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return crypto_hist_df
    except Exception as e:
        print(f"获取加密货币历史数据失败: {e}")
        return None


def get_crypto_spot():
    """获取加密货币实时行情"""
    print("\n=== 加密货币实时行情 ===")
    try:
        # 获取加密货币实时行情
        crypto_spot_df = ak.crypto_currency_spot()
        print(f"获取到 {len(crypto_spot_df)} 条加密货币实时行情数据")
        print("前5条数据:")
        print(crypto_spot_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"crypto_spot_{timestamp}.csv"
        crypto_spot_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return crypto_spot_df
    except Exception as e:
        print(f"获取加密货币实时行情失败: {e}")
        return None


def main():
    """主函数"""
    print("加密货币数据演示脚本")
    print("=" * 50)
    
    # 获取加密货币历史数据
    get_crypto_hist()
    
    # 获取加密货币实时行情
    get_crypto_spot()
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
