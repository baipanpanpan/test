#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#datetime: 20:19
#email: 18222202652@163.com
#author: 小明


from openpyxl import load_workbook

wb = load_workbook("test_data.xlsx")

sh = wb["login_case"]