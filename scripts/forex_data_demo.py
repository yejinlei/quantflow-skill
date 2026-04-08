#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外汇数据演示脚本

使用Akshare获取外汇现货报价和汇率历史数据
"""

import akshare as ak
import pandas as pd
from datetime import datetime


def get_forex_spot():
    """获取外汇现货报价"""
    print("=== 外汇现货报价 ===")
    try:
        # 获取外汇现货报价
        forex_spot_df = ak.forex_spot_quote()
        print(f"获取到 {len(forex_spot_df)} 条外汇现货报价数据")
        print("前5条数据:")
        print(forex_spot_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"forex_spot_{timestamp}.csv"
        forex_spot_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return forex_spot_df
    except Exception as e:
        print(f"获取外汇现货报价失败: {e}")
        return None


def get_forex_history():
    """获取汇率历史数据"""
    print("\n=== 汇率历史数据 ===")
    try:
        # 示例：获取美元对人民币汇率历史数据
        forex_history_df = ak.forex_rate_history(
            symbol="usd-cny",
            start_date="2024-01-01",
            end_date=datetime.now().strftime("%Y-%m-%d")
        )
        print(f"获取到 {len(forex_history_df)} 条美元对人民币汇率历史数据")
        print("前5条数据:")
        print(forex_history_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"forex_history_usd-cny_{timestamp}.csv"
        forex_history_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return forex_history_df
    except Exception as e:
        print(f"获取汇率历史数据失败: {e}")
        return None


def main():
    """主函数"""
    print("外汇数据演示脚本")
    print("=" * 50)
    
    # 获取外汇现货报价
    get_forex_spot()
    
    # 获取汇率历史数据
    get_forex_history()
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
