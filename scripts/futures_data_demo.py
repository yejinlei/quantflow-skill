#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
期货数据演示脚本

使用Akshare获取期货实时行情、历史数据和合约信息
"""

import akshare as ak
import pandas as pd
from datetime import datetime


def get_futures_realtime():
    """获取期货实时行情"""
    print("=== 期货实时行情 ===")
    try:
        # 获取期货实时行情
        futures_realtime_df = ak.futures_zh_realtime()
        print(f"获取到 {len(futures_realtime_df)} 条期货实时行情数据")
        print("前5条数据:")
        print(futures_realtime_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"futures_realtime_{timestamp}.csv"
        futures_realtime_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return futures_realtime_df
    except Exception as e:
        print(f"获取期货实时行情失败: {e}")
        return None


def get_futures_daily():
    """获取期货日线数据"""
    print("\n=== 期货日线数据 ===")
    try:
        # 示例：获取螺纹钢期货日线数据
        symbol = "rb2410"
        futures_daily_df = ak.futures_zh_daily(symbol=symbol)
        print(f"获取到 {len(futures_daily_df)} 条 {symbol} 日线数据")
        print("前5条数据:")
        print(futures_daily_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"futures_daily_{symbol}_{timestamp}.csv"
        futures_daily_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return futures_daily_df
    except Exception as e:
        print(f"获取期货日线数据失败: {e}")
        return None


def get_futures_contract_info():
    """获取期货合约信息"""
    print("\n=== 期货合约信息 ===")
    try:
        # 获取上期所期货合约信息
        futures_contract_info_df = ak.futures_contract_info_shfe()
        print(f"获取到 {len(futures_contract_info_df)} 条上期所期货合约信息")
        print("前5条数据:")
        print(futures_contract_info_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"futures_contract_info_shfe_{timestamp}.csv"
        futures_contract_info_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return futures_contract_info_df
    except Exception as e:
        print(f"获取期货合约信息失败: {e}")
        return None


def main():
    """主函数"""
    print("期货数据演示脚本")
    print("=" * 50)
    
    # 获取期货实时行情
    get_futures_realtime()
    
    # 获取期货日线数据
    get_futures_daily()
    
    # 获取期货合约信息
    get_futures_contract_info()
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
