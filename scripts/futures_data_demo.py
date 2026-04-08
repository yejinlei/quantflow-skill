#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
期货数据演示脚本

使用Akshare获取期货实时行情、历史数据和合约信息
"""

import akshare as ak
import pandas as pd
from datetime import datetime
import threading
import time
import json

# 全局变量存储最新数据
latest_data = {
    'data': None,
    'timestamp': None,
    'error': None
}

# 手动更新指定品种的数据
def update_data_for_symbol(symbol):
    print(f"[{datetime.now()}] 正在更新 {symbol} 期货数据...")
    try:
        # 获取期货实时行情
        df = ak.futures_zh_realtime()
        
        if df is not None and not df.empty:
            # 筛选指定品种的期货合约（如RU、TA、CU等）
            symbol_df = df[df['symbol'].str.startswith(symbol, na=False)].copy()
            
            if not symbol_df.empty:
                # 按成交量排序，找出主力合约
                symbol_df = symbol_df.sort_values('volume', ascending=False)
                
                # 计算市场概况
                total_volume = symbol_df['volume'].sum()
                total_hold = symbol_df['position'].sum()
                avg_price = symbol_df['trade'].mean()
                min_price = symbol_df['trade'].min()
                max_price = symbol_df['trade'].max()
                price_range = max_price - min_price
                
                up_contracts = len(symbol_df[symbol_df['changepercent'] > 0])
                down_contracts = len(symbol_df[symbol_df['changepercent'] < 0])
                flat_contracts = len(symbol_df[symbol_df['changepercent'] == 0])
                
                # 构建返回数据
                data = {
                    '查询时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    '主力合约': {
                        '合约代码': symbol_df.iloc[0]['symbol'],
                        '最新价': float(symbol_df.iloc[0]['trade']),
                        '涨跌': float(symbol_df.iloc[0]['trade'] - symbol_df.iloc[0]['prevsettlement']),
                        '涨跌幅': float(symbol_df.iloc[0]['changepercent'] * 100),
                        '开盘价': float(symbol_df.iloc[0]['open']),
                        '最高价': float(symbol_df.iloc[0]['high']),
                        '最低价': float(symbol_df.iloc[0]['low']),
                        '昨收': float(symbol_df.iloc[0]['preclose']),
                        '成交量': int(symbol_df.iloc[0]['volume']),
                        '持仓量': int(symbol_df.iloc[0]['position'])
                    },
                    '市场概况': {
                        '总成交量': int(total_volume),
                        '总持仓量': int(total_hold),
                        '平均价格': float(avg_price),
                        '价格区间': {
                            '最低': float(min_price),
                            '最高': float(max_price),
                            '价差': float(price_range)
                        },
                        '涨跌分布': {
                            '上涨': up_contracts,
                            '下跌': down_contracts,
                            '平盘': flat_contracts
                        }
                    },
                    '所有合约': []
                }
                
                # 添加所有合约数据
                for _, row in symbol_df.iterrows():
                    data['所有合约'].append({
                        'symbol': row['symbol'],
                        'last': float(row['trade']),
                        'change': float(row['trade'] - row['prevsettlement']),
                        'change_pct': float(row['changepercent'] * 100),
                        'open': float(row['open']),
                        'high': float(row['high']),
                        'low': float(row['low']),
                        'volume': int(row['volume']),
                        'hold': int(row['position'])
                    })
                
                # 更新全局变量
                global latest_data
                latest_data = {
                    'data': data,
                    'timestamp': datetime.now(),
                    'error': None
                }
                
                print(f"[{datetime.now()}] 数据更新成功，获取到 {len(symbol_df)} 个 {symbol} 合约")
            else:
                print(f"[{datetime.now()}] 未找到 {symbol} 期货数据")
                # 不使用模拟数据，保持data为None
                latest_data = {
                    'data': None,
                    'timestamp': datetime.now(),
                    'error': f'未找到 {symbol} 期货数据，可能是因为非交易时间或数据源问题'
                }
        else:
            print(f"[{datetime.now()}] 获取期货数据失败")
            # 不使用模拟数据，保持data为None
            latest_data = {
                'data': None,
                'timestamp': datetime.now(),
                'error': '获取期货数据失败，可能是网络连接问题'
            }
    except Exception as e:
        print(f"[{datetime.now()}] 更新数据时出错: {e}")
        # 不使用模拟数据，保持data为None
        latest_data = {
            'data': None,
            'timestamp': datetime.now(),
            'error': f'更新数据时出错: {str(e)}'
        }

# 后台线程定期更新数据
def update_data():
    while True:
        try:
            # 默认更新天然橡胶数据
            update_data_for_symbol('RU')
        except Exception as e:
            print(f"[{datetime.now()}] 后台更新数据时出错: {e}")
        
        # 每10秒更新一次
        time.sleep(10)

# 启动数据更新线程
data_thread = threading.Thread(target=update_data, daemon=True)
data_thread.start()


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


def get_futures_real_time_data(symbol='RU'):
    """获取指定期货品种的实时数据"""
    print(f"\n=== {symbol} 期货实时数据 ===")
    # 手动触发一次数据更新
    update_data_for_symbol(symbol)
    
    if latest_data['data']:
        print(f"{symbol} 期货实时数据获取成功：")
        print(f"查询时间: {latest_data['data']['查询时间']}")
        print(f"主力合约: {latest_data['data']['主力合约']['合约代码']}")
        print(f"最新价: {latest_data['data']['主力合约']['最新价']:.2f}")
        print(f"涨跌幅: {latest_data['data']['主力合约']['涨跌幅']:.2f}%")
        print(f"成交量: {latest_data['data']['主力合约']['成交量']} 手")
        print(f"持仓量: {latest_data['data']['主力合约']['持仓量']} 手")
        
        print(f"\n市场概况:")
        print(f"总成交量: {latest_data['data']['市场概况']['总成交量']} 手")
        print(f"总持仓量: {latest_data['data']['市场概况']['总持仓量']} 手")
        print(f"平均价格: {latest_data['data']['市场概况']['平均价格']:.2f}")
        print(f"价格区间: {latest_data['data']['市场概况']['价格区间']['最低']:.2f} - {latest_data['data']['市场概况']['价格区间']['最高']:.2f}")
        
        print(f"\n涨跌分布:")
        print(f"上涨合约: {latest_data['data']['市场概况']['涨跌分布']['上涨']} 个")
        print(f"下跌合约: {latest_data['data']['市场概况']['涨跌分布']['下跌']} 个")
        print(f"平盘合约: {latest_data['data']['市场概况']['涨跌分布']['平盘']} 个")
        
        # 保存数据
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"futures_real_time_{symbol}_{timestamp}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(latest_data['data'], f, ensure_ascii=False, indent=2)
        print(f"\n数据已保存到: {filename}")
        
        return latest_data['data']
    else:
        error_message = latest_data.get('error', '数据加载中，请稍候再试')
        print(f"获取实时数据失败：{error_message}")
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
    
    # 获取天然橡胶期货实时数据
    get_futures_real_time_data('RU')
    
    # 获取螺纹钢期货实时数据
    get_futures_real_time_data('RB')
    
    # 获取铜期货实时数据
    get_futures_real_time_data('CU')
    
    print("\n演示完成！")


if __name__ == "__main__":
    main()
