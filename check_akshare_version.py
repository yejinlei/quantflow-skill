#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查Akshare版本和可用模块
"""

import akshare as ak
import pkgutil

print('Akshare version:', ak.__version__)
print('\nAvailable modules:')
for _, name, _ in pkgutil.iter_modules(ak.__path__):
    print(f'- {name}')
