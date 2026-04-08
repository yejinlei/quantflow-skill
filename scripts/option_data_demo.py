#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
期权数据演示脚本

使用Akshare获取期权实时行情和历史数据，以及天然橡胶期货实时行情
"""

import akshare as ak
import pandas as pd
from datetime import datetime
import json
import os


def get_option_realtime():
    """获取期权实时行情"""
    print("=== 期权实时行情 ===")
    try:
        # 获取期权实时行情
        option_realtime_df = ak.option_zh_sina_spot()
        print(f"获取到 {len(option_realtime_df)} 条期权实时行情数据")
        print("前5条数据:")
        print(option_realtime_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"option_realtime_{timestamp}.csv"
        option_realtime_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return option_realtime_df
    except Exception as e:
        print(f"获取期权实时行情失败: {e}")
        return None


def get_option_daily():
    """获取期权日线数据"""
    print("\n=== 期权日线数据 ===")
    try:
        # 示例：获取沪深300ETF期权日线数据
        symbol = "510300C2406M04000"
        option_daily_df = ak.option_zh_sina_daily(symbol=symbol)
        print(f"获取到 {len(option_daily_df)} 条 {symbol} 日线数据")
        print("前5条数据:")
        print(option_daily_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"option_daily_{symbol}_{timestamp}.csv"
        option_daily_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return option_daily_df
    except Exception as e:
        print(f"获取期权日线数据失败: {e}")
        return None


def main():
    """主函数"""
    print("期权数据演示脚本")
    print("=" * 50)
    
    # 获取期权实时行情
    get_option_realtime()
    
    # 获取期权日线数据
    get_option_daily()
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
