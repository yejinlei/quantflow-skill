#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
债券数据演示脚本

使用Akshare获取中国债券基本信息和历史数据
"""

import akshare as ak
import pandas as pd
from datetime import datetime


def get_bond_basic():
    """获取中国债券基本信息"""
    print("=== 中国债券基本信息 ===")
    try:
        # 获取中国债券基本信息
        bond_basic_df = ak.bond_zh_cn_basic()
        print(f"获取到 {len(bond_basic_df)} 条中国债券基本信息数据")
        print("前5条数据:")
        print(bond_basic_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bond_basic_{timestamp}.csv"
        bond_basic_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return bond_basic_df
    except Exception as e:
        print(f"获取中国债券基本信息失败: {e}")
        return None


def get_bond_hist():
    """获取中国债券历史数据"""
    print("\n=== 中国债券历史数据 ===")
    try:
        # 示例：获取国债历史数据
        bond_hist_df = ak.bond_zh_cn_hist(
            symbol="101601",
            start_date="2024-01-01",
            end_date=datetime.now().strftime("%Y-%m-%d")
        )
        print(f"获取到 {len(bond_hist_df)} 条国债历史数据")
        print("前5条数据:")
        print(bond_hist_df.head())
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bond_hist_101601_{timestamp}.csv"
        bond_hist_df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"数据已保存到: {filename}")
        
        return bond_hist_df
    except Exception as e:
        print(f"获取中国债券历史数据失败: {e}")
        return None


def main():
    """主函数"""
    print("债券数据演示脚本")
    print("=" * 50)
    
    # 获取中国债券基本信息
    get_bond_basic()
    
    # 获取中国债券历史数据
    get_bond_hist()
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
