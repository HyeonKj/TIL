# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:14:23 2022

@author: user
"""

import re
start_date = "2020 year 6/20**3"
start_lst = re.split('\D+', start_date)

print(start_lst)
