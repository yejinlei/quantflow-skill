#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票数据获取示例脚本
"""

import akshare as ak
import pandas as pd
import os
import datetime
import threading
import time
from datetime import datetime as dt

# 全局变量存储最新数据
latest_data = {
    'data': None,
    'timestamp': None,
    'error': None
}

# 手动更新指定股票的数据
def update_data_for_stock(stock_code):
    print(f"[{dt.now()}] 正在更新 {stock_code} 股票数据...")
    try:
        # 获取所有股票实时行情
        df = ak.stock_zh_a_spot()
        
        if df is not None and not df.empty:
            # 筛选指定股票的数据
            # 处理股票代码格式，去除交易所前缀
            stock_code_clean = stock_code.replace('sh', '').replace('sz', '')
            stock_df = df[df['代码'] == stock_code_clean].copy()
            
            if not stock_df.empty:
                # 获取股票数据
                stock_data = stock_df.iloc[0]
                
                # 构建返回数据
                data = {
                    '查询时间': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
                    '股票信息': {
                        '代码': stock_data['代码'],
                        '名称': stock_data['名称'],
                        '最新价': float(stock_data['最新价']),
                        '涨跌额': float(stock_data['涨跌额']),
                        '涨跌幅': float(stock_data['涨跌幅']),
                        '买入': float(stock_data['买入']),
                        '卖出': float(stock_data['卖出']),
                        '昨收': float(stock_data['昨收']),
                        '今开': float(stock_data['今开']),
                        '最高': float(stock_data['最高']),
                        '最低': float(stock_data['最低']),
                        '成交量': int(stock_data['成交量']),
                        '成交额': float(stock_data['成交额']),
                        '时间戳': stock_data['时间戳']
                    }
                }
                
                # 更新全局变量
                global latest_data
                latest_data = {
                    'data': data,
                    'timestamp': dt.now(),
                    'error': None
                }
                
                print(f"[{dt.now()}] 数据更新成功，获取到股票 {stock_code} 的数据")
            else:
                print(f"[{dt.now()}] 未找到股票 {stock_code} 的数据")
                # 不使用模拟数据，保持data为None
                latest_data = {
                    'data': None,
                    'timestamp': dt.now(),
                    'error': f'未找到股票 {stock_code} 的数据，可能是因为非交易时间或数据源问题'
                }
        else:
            print(f"[{dt.now()}] 获取股票数据失败")
            # 不使用模拟数据，保持data为None
            latest_data = {
                'data': None,
                'timestamp': dt.now(),
                'error': '获取股票数据失败，可能是网络连接问题'
            }
    except Exception as e:
        print(f"[{dt.now()}] 更新数据时出错: {e}")
        # 不使用模拟数据，保持data为None
        latest_data = {
            'data': None,
            'timestamp': dt.now(),
            'error': f'更新数据时出错: {str(e)}'
        }

# 后台线程定期更新数据
def update_data():
    while True:
        try:
            # 默认更新上证指数数据
            update_data_for_stock('sh000001')
        except Exception as e:
            print(f"[{dt.now()}] 后台更新数据时出错: {e}")
        
        # 每10秒更新一次
        time.sleep(10)

# 启动数据更新线程
data_thread = threading.Thread(target=update_data, daemon=True)
data_thread.start()


def get_stock_list():
    """
    获取股票列表
    """
    try:
        data = ak.stock_info_a_code_name()
        print("股票列表获取成功：")
        print(data.head())
        return data
    except Exception as e:
        print(f"获取股票列表失败：{e}")
        return None


def get_daily_data(symbol, start_date, end_date):
    """
    获取股票日线数据
    """
    try:
        # 尝试使用不同的接口获取日线数据
        data = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start_date, end_date=end_date, adjust="qfq")
        print(f"{symbol}日线数据获取成功：")
        print(data.head())
        return data
    except Exception as e:
        print(f"获取日线数据失败：{e}")
        return None


def get_spot_data():
    """
    获取股票实时行情数据
    """
    try:
        data = ak.stock_zh_a_spot()
        print("股票实时行情数据获取成功：")
        print(data.head())
        return data
    except Exception as e:
        print(f"获取实时行情数据失败：{e}")
        return None


def get_real_time_data(stock_code='sh000001'):
    """
    获取指定股票的实时数据
    """
    # 手动触发一次数据更新
    update_data_for_stock(stock_code)
    
    if latest_data['data']:
        print(f"股票 {stock_code} 实时数据获取成功：")
        print(latest_data['data'])
        return latest_data['data']
    else:
        error_message = latest_data.get('error', '数据加载中，请稍候再试')
        print(f"获取实时数据失败：{error_message}")
        return None


def get_financial_data(symbol):
    """
    获取财务指标数据
    """
    try:
        # 尝试使用不同的接口获取财务数据
        data = ak.stock_financial_analysis_indicator(symbol=symbol)
        print(f"{symbol}财务指标数据获取成功：")
        print(data.head())
        return data
    except Exception as e:
        print(f"获取财务指标数据失败：{e}")
        return None


def get_news(symbol):
    """
    获取股票新闻
    """
    try:
        data = ak.stock_news_em(symbol=symbol)
        print(f"{symbol}新闻获取成功：")
        print(data.head())
        return data
    except Exception as e:
        print(f"获取股票新闻失败：{e}")
        return None


def main():
    """
    主函数
    """
    print("===== akshare 股票数据获取示例 =====")
    
    # 获取股票列表
    stock_list = get_stock_list()
    
    if stock_list is not None:
        # 获取第一只股票的代码
        symbol = stock_list['code'].iloc[0]
        print(f"\n使用股票代码：{symbol}")
        
        # 获取日线数据（最近30天）
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
        print(f"\n1. 获取日线数据：{start_date} 至 {end_date}")
        get_daily_data(symbol, start_date, end_date)
        
        # 获取实时行情数据
        print("\n2. 获取股票实时行情数据")
        get_spot_data()
        
        # 获取指定股票的实时数据
        print(f"\n3. 获取指定股票的实时数据：{symbol}")
        get_real_time_data(symbol)
        
        # 获取上证指数的实时数据
        print("\n4. 获取上证指数的实时数据")
        get_real_time_data('sh000001')
        
        # 获取财务数据
        print(f"\n5. 获取财务指标数据：{symbol}")
        get_financial_data(symbol)
        
        # 获取股票新闻
        print(f"\n6. 获取股票新闻：{symbol}")
        get_news(symbol)


if __name__ == "__main__":
    main()