#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#datetime: 20:42
#email: 18222202652@163.com
#author: 小明

import unittest


from BeautifulReport import BeautifulReport


if __name__ == "__main__":
    ts = unittest.TestLoader().discover('./testcase')
    br= BeautifulReport(ts)
    br.report("report/report.html")


