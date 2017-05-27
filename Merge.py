# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

macro = pd.read_csv("data/macro/macro.csv")
train = pd.read_csv("data/train/train.csv")
merged = macro.merge(train, on='timestamp')
merged.to_csv("merged.csv", index=False)