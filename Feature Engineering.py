# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:42:32 2019

@author: heyup
"""
import os
import pandas as pd
import numpy as np

os.chdir('C:\\Users\\heyup\\Documents\\DSO562\\NY Property Data')

# Load data
#d = pd.read_csv("NY property data.csv")
d = pd.read_csv("NY Property Data Cleaned.csv")

#d.info()
print(d.isnull().sum()) # No missing values

columns = ['RECORD','LTFRONT2','LTDEPTH2','BLDFRONT2','BLDDEPTH2','STORIES2','FULLVAL2','AVLAND2','AVTOT2', 'ZIP2', 'TAXCLASS', 'B']

d = d.loc[:,columns]
d.columns.values

d.columns = ['RECORD', 'LTFRONT', 'LTDEPTH', 'BLDFRONT', 'BLDDEPTH',
       'STORIES', 'FULLVAL', 'AVLAND', 'AVTOT', 'ZIP', 'TAXCLASS',
       'B']

print(d.isnull().sum()) # No missing values

# Sample non-null data
# =============================================================================
# d = d.loc[(d['FULLVAL']>0) & (d['AVLAND']>0) & (d['AVTOT']>0) & (d['LTFRONT'])>0 & (d['LTDEPTH']>0) & (d['BLDFRONT']>0) & (d['BLDDEPTH']>0) & (d['STORIES']>0),\
#           columns].dropna(how='any').sample(frac=0.1)
# 
# d = d.loc[d['LTDEPTH']>0,:]
# d = d.loc[d['BLDFRONT']>0,:]
# d=d.loc[d['BLDDEPTH']>0,:]
# =============================================================================

# Create 3 sizes
# =============================================================================
# d['LTFRONT'].describe()
# d['LTDEPTH'].describe()
# d['BLDFRONT'].describe()
# d['BLDDEPTH'].describe()
# d['STORIES'].describe()
# =============================================================================
#s1
d['LOTAREA'] = d['LTFRONT']*d['LTDEPTH']
#s2
d['BLDAREA'] = d['BLDFRONT']*d['BLDDEPTH']
#s3
d['BLDVOL'] = d['BLDFRONT']*d['BLDDEPTH']*d['STORIES']

# Create 9 core variables
# =============================================================================
# V1=FULLVAL
# V2=AVLAND
# V3=AVTOT
# =============================================================================
#r1 = v1/s1
d['r1']=d['FULLVAL'] / d['LOTAREA']
#r2=v1/s2
d['r2']=d['FULLVAL']/d['BLDAREA']
#r3=v1/s3
d['r3']=d['FULLVAL']/d['BLDVOL']
#r4=v2/s1
d['r4']=d['AVLAND']/d['LOTAREA']
#r5=v2/s2
d['r5']=d['AVLAND']/d['BLDAREA']
#r6=v2/s3
d['r6']=d['AVLAND']/d['BLDVOL']
#r7=v3/s1
d['r7']=d['AVTOT']/d['LOTAREA']
#r8=v3/r2
d['r8']=d['AVTOT']/d['BLDAREA']
#r9=v3/r3
d['r9']=d['AVTOT']/d['BLDVOL']

# Create 45 variables

# Grouping1: ZIP5

r1_zip5 = d.groupby(['ZIP'])['r1'].agg(['mean'])
r2_zip5 = d.groupby(['ZIP'])['r2'].agg(['mean'])
r3_zip5 = d.groupby(['ZIP'])['r3'].agg(['mean'])
r4_zip5 = d.groupby(['ZIP'])['r4'].agg(['mean'])
r5_zip5 = d.groupby(['ZIP'])['r5'].agg(['mean'])
r6_zip5 = d.groupby(['ZIP'])['r6'].agg(['mean'])
r7_zip5 = d.groupby(['ZIP'])['r7'].agg(['mean'])
r8_zip5 = d.groupby(['ZIP'])['r8'].agg(['mean'])
r9_zip5 = d.groupby(['ZIP'])['r9'].agg(['mean'])


d['r1_zip5'] = d.apply(lambda x: x['r1'] / (r1_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r2_zip5'] = d.apply(lambda x: x['r2'] / (r2_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r3_zip5'] = d.apply(lambda x: x['r3'] / (r3_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r4_zip5'] = d.apply(lambda x: x['r4'] / (r4_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r5_zip5'] = d.apply(lambda x: x['r5'] / (r5_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r6_zip5'] = d.apply(lambda x: x['r6'] / (r6_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r7_zip5'] = d.apply(lambda x: x['r7'] / (r7_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r8_zip5'] = d.apply(lambda x: x['r8'] / (r8_zip5.loc[x['ZIP'],'mean']), axis=1)
d['r9_zip5'] = d.apply(lambda x: x['r9'] / (r9_zip5.loc[x['ZIP'],'mean']), axis=1)

# Grouping2: ZIP3
d['ZIP3'] = d['ZIP'].astype(str).str[:3]

r1_zip3 = d.groupby(['ZIP3'])['r1'].agg(['mean'])
r2_zip3 = d.groupby(['ZIP3'])['r2'].agg(['mean'])
r3_zip3 = d.groupby(['ZIP3'])['r3'].agg(['mean'])
r4_zip3 = d.groupby(['ZIP3'])['r4'].agg(['mean'])
r5_zip3 = d.groupby(['ZIP3'])['r5'].agg(['mean'])
r6_zip3 = d.groupby(['ZIP3'])['r6'].agg(['mean'])
r7_zip3 = d.groupby(['ZIP3'])['r7'].agg(['mean'])
r8_zip3 = d.groupby(['ZIP3'])['r8'].agg(['mean'])
r9_zip3 = d.groupby(['ZIP3'])['r9'].agg(['mean'])

d['r1_zip3'] = d.apply(lambda x: x['r1'] / (r1_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r2_zip3'] = d.apply(lambda x: x['r2'] / (r2_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r3_zip3'] = d.apply(lambda x: x['r3'] / (r3_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r4_zip3'] = d.apply(lambda x: x['r4'] / (r4_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r5_zip3'] = d.apply(lambda x: x['r5'] / (r5_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r6_zip3'] = d.apply(lambda x: x['r6'] / (r6_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r7_zip3'] = d.apply(lambda x: x['r7'] / (r7_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r8_zip3'] = d.apply(lambda x: x['r8'] / (r8_zip3.loc[x['ZIP3'],'mean']), axis=1)
d['r9_zip3'] = d.apply(lambda x: x['r9'] / (r9_zip3.loc[x['ZIP3'],'mean']), axis=1)


# Grouping3: Tax class


r1_tax = d.groupby(['TAXCLASS'])['r1'].agg(['mean'])
r2_tax = d.groupby(['TAXCLASS'])['r2'].agg(['mean'])
r3_tax = d.groupby(['TAXCLASS'])['r3'].agg(['mean'])
r4_tax = d.groupby(['TAXCLASS'])['r4'].agg(['mean'])
r5_tax = d.groupby(['TAXCLASS'])['r5'].agg(['mean'])
r6_tax = d.groupby(['TAXCLASS'])['r6'].agg(['mean'])
r7_tax = d.groupby(['TAXCLASS'])['r7'].agg(['mean'])
r8_tax = d.groupby(['TAXCLASS'])['r8'].agg(['mean'])
r9_tax = d.groupby(['TAXCLASS'])['r9'].agg(['mean'])

d['r1_tax'] = d.apply(lambda x: x['r1'] / (r1_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r2_tax'] = d.apply(lambda x: x['r2'] / (r2_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r3_tax'] = d.apply(lambda x: x['r3'] / (r3_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r4_tax'] = d.apply(lambda x: x['r4'] / (r4_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r5_tax'] = d.apply(lambda x: x['r5'] / (r5_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r6_tax'] = d.apply(lambda x: x['r6'] / (r6_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r7_tax'] = d.apply(lambda x: x['r7'] / (r7_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r8_tax'] = d.apply(lambda x: x['r8'] / (r8_tax.loc[x['TAXCLASS'],'mean']), axis=1)
d['r9_tax'] = d.apply(lambda x: x['r9'] / (r9_tax.loc[x['TAXCLASS'],'mean']), axis=1)

# Grouping4: Borough


r1_b = d.groupby(['B'])['r1'].agg(['mean'])
r2_b = d.groupby(['B'])['r2'].agg(['mean'])
r3_b = d.groupby(['B'])['r3'].agg(['mean'])
r4_b = d.groupby(['B'])['r4'].agg(['mean'])
r5_b = d.groupby(['B'])['r5'].agg(['mean'])
r6_b = d.groupby(['B'])['r6'].agg(['mean'])
r7_b = d.groupby(['B'])['r7'].agg(['mean'])
r8_b = d.groupby(['B'])['r8'].agg(['mean'])
r9_b = d.groupby(['B'])['r9'].agg(['mean'])

d['r1_b'] = d.apply(lambda x: x['r1'] / (r1_b.loc[x['B'],'mean']), axis=1)
d['r2_b'] = d.apply(lambda x: x['r2'] / (r2_b.loc[x['B'],'mean']), axis=1)
d['r3_b'] = d.apply(lambda x: x['r3'] / (r3_b.loc[x['B'],'mean']), axis=1)
d['r4_b'] = d.apply(lambda x: x['r4'] / (r4_b.loc[x['B'],'mean']), axis=1)
d['r5_b'] = d.apply(lambda x: x['r5'] / (r5_b.loc[x['B'],'mean']), axis=1)
d['r6_b'] = d.apply(lambda x: x['r6'] / (r6_b.loc[x['B'],'mean']), axis=1)
d['r7_b'] = d.apply(lambda x: x['r7'] / (r7_b.loc[x['B'],'mean']), axis=1)
d['r8_b'] = d.apply(lambda x: x['r8'] / (r8_b.loc[x['B'],'mean']), axis=1)
d['r9_b'] = d.apply(lambda x: x['r9'] / (r9_b.loc[x['B'],'mean']), axis=1)


# Grouping5: no grouping
r1_all = d['r1'].mean()
r2_all = d['r2'].mean()
r3_all = d['r3'].mean()
r4_all = d['r4'].mean()
r5_all = d['r5'].mean()
r6_all = d['r6'].mean()
r7_all = d['r7'].mean()
r8_all = d['r8'].mean()
r9_all = d['r9'].mean()


d['r1_all'] = d.apply(lambda x: x['r1'] / r1_all, axis=1)
d['r2_all'] = d.apply(lambda x: x['r2'] / r2_all, axis=1)
d['r3_all'] = d.apply(lambda x: x['r3'] / r3_all, axis=1)
d['r4_all'] = d.apply(lambda x: x['r4'] / r4_all, axis=1)
d['r5_all'] = d.apply(lambda x: x['r5'] / r5_all, axis=1)
d['r6_all'] = d.apply(lambda x: x['r6'] / r6_all, axis=1)
d['r7_all'] = d.apply(lambda x: x['r7'] / r7_all, axis=1)
d['r8_all'] = d.apply(lambda x: x['r8'] / r8_all, axis=1)
d['r9_all'] = d.apply(lambda x: x['r9'] / r9_all, axis=1)


# Export
d.to_csv("NY Property Data Full.csv",index=True)

d.columns.values
d.isna().sum()
d.describe()
