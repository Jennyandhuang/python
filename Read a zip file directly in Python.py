#!/usr/bin/env python
# coding: utf-8

#import packages
import pandas as pd
import os
import zipfile

#change directory
os.chdir('/Users/ChiHuang/Documents/python/python files')
os.listdir()

#read zip file
zf=zipfile.ZipFile('411512_835452_compressed_2019-Nov.csv.zip','r')

#get the zip file name contained
zipfile.ZipFile.namelist(zf)

#choose the csv file to read under zip file
df = pd.read_csv(zf.open('2019-Nov.csv'))

