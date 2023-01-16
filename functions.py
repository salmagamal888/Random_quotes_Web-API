# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:12:38 2023

@author: dell
"""

import json
import pandas as pd

def json_to_df(file):
    with open(file) as f:
        js_file=json.load(f)
        
    return pd.DataFrame(js_file)
