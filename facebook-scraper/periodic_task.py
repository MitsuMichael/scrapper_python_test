#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

cmd="python facebook_scraper.py -g fifamoivoizana -f data/out.csv -p 100"

while True:
    os.system(cmd)
    time.sleep(600)

