# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:57:31 2019

@author: heyup
"""

import os
import pandas as pd
import numpy as np

os.chdir('C:\\Users\\heyup\\Documents\\DSO562\\NY Property Data')

# Load data
d = pd.read_csv("NY property data.csv")
#d1 = d.loc[d['ZIP'].notnull(),["RECORD","TAXCLASS", "ZIP", "FULLVAL", "AVLAND", "AVTOT", \
#           'LTFRONT','LTDEPTH','BLDFRONT','BLDDEPTH', 'STORIES','BLDGCL','B']]

d1 = d.loc[:,["RECORD","TAXCLASS", "ZIP", "FULLVAL", "AVLAND", "AVTOT", \
           'LTFRONT','LTDEPTH','BLDFRONT','BLDDEPTH', 'STORIES','BLDGCL','B']]

# Convert 0 to NaNs
d1.loc[d1['FULLVAL']==0, 'FULLVAL'] = np.nan
d1.loc[d1['AVLAND']==0, 'AVLAND'] = np.nan
d1.loc[d1['AVTOT']==0, 'AVTOT'] = np.nan

d1.loc[d1['LTFRONT']==0, 'LTFRONT'] = np.nan
d1.loc[d1['LTDEPTH']==0, 'LTDEPTH'] = np.nan
d1.loc[d1['BLDFRONT']==0, 'BLDFRONT'] = np.nan
d1.loc[d1['BLDDEPTH']==0, 'BLDDEPTH'] = np.nan
d1.loc[d1['STORIES']==0, 'STORIES'] = np.nan

d1['ZIP'].isna().sum() # 29890
d1['FULLVAL'].isna().sum() # 13007 na values
d1['AVLAND'].isna().sum() # 13009
d1['AVTOT'].isna().sum() # 13007
d1['LTFRONT'].isna().sum() # 169108
d1['LTDEPTH'].isna().sum() # 170128
d1['BLDFRONT'].isna().sum() # 228815
d1['BLDDEPTH'].isna().sum() # 228853
d1['STORIES'].isna().sum() # 56264

# ZIP
zip_group = d.groupby(['B'])['ZIP'].agg({'Count':'count','Median1':'median'}).reset_index()
d1 = pd.merge(d1, zip_group, left_on='B', right_on='B', how='left' )

d1['ZIP2'] = d1.apply(lambda x: x['Median1'] if pd.isna(x['ZIP']) else x['ZIP'], axis=1)

#test = d1.loc[d1['ZIP'].isna(),['B','Count', 'Median1','ZIP','ZIP2']]
#np.sum(d1['ZIP2']!=d1['ZIP'])
#d1['ZIP2'].isna().sum()

d1 = d1.drop(['Count','Median1'], axis=1)


# FULLVAL
# 1424 groups 
fullval_group = d1.groupby(['TAXCLASS','ZIP2'])['FULLVAL'].agg({'Count':'count','Median1':'median'}).reset_index()
# 338 out of 1421 have fewer than 10 records
#fullval_group.loc[fullval_group['Count']<10,:].head()
# Calculate median of each ZIP2
fullval_group2 = d1.groupby('ZIP2')['FULLVAL'].agg({'Median2':'median'}).reset_index()
d2 = pd.merge(d1, fullval_group, left_on=['TAXCLASS','ZIP2'], right_on=['TAXCLASS','ZIP2'], how='left' )
d2 = pd.merge(d2, fullval_group2, left_on='ZIP2', right_on='ZIP2', how='left')

def fullval_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['FULLVAL'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['FULLVAL'])):
        return x['Median2']
    else:
        return x['FULLVAL']
    

d2['FULLVAL2'] = d2.apply(fullval_fillna, axis=1)

#test = d2.loc[d2['FULLVAL'].isna(),['TAXCLASS','ZIP2','Count', 'Median1', 'Median2', 'FULLVAL','FULLVAL2']]
#np.sum(d2['FULLVAL2']!=d2['FULLVAL'])
#d2['FULLVAL2'].isna().sum()
d2 = d2.drop(['Count','Median1','Median2'], axis=1)
del(d1)

# AVLAND
avland_group = d2.groupby(['TAXCLASS','ZIP2'])['AVLAND'].agg({'Count':'count','Median1':'median'}).reset_index()
avland_group2 = d2.groupby('ZIP2')['AVLAND'].agg({'Median2':'median'}).reset_index()

d3 = pd.merge(d2, avland_group, left_on=['TAXCLASS','ZIP2'], right_on=['TAXCLASS','ZIP2'], how='left' )
d3 = pd.merge(d3, avland_group2, left_on='ZIP2', right_on='ZIP2', how='left')

def avland_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['AVLAND'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['AVLAND'])):
        return x['Median2']
    else:
        return x['AVLAND']

d3['AVLAND2'] = d3.apply(avland_fillna, axis=1)

#test = d3.loc[d3['AVLAND'].isna(),['TAXCLASS','ZIP2','Count', 'Median1', 'Median2', 'AVLAND','AVLAND2']]
#np.sum(d3['AVLAND2']!=d3['AVLAND'])
#d3['AVLAND2'].isna().sum()

d3 = d3.drop(['Count','Median1','Median2'], axis=1)
del(d2)

# AVTOT
avtot_group = d3.groupby(['TAXCLASS','ZIP2'])['AVTOT'].agg({'Count':'count','Median1':'median'}).reset_index()
avtot_group2 = d3.groupby('ZIP2')['AVTOT'].agg({'Median2':'median'}).reset_index()

d4 = pd.merge(d3, avland_group, left_on=['TAXCLASS','ZIP2'], right_on=['TAXCLASS','ZIP2'], how='left' )
d4 = pd.merge(d4, avland_group2, left_on='ZIP2', right_on='ZIP2', how='left')

def avtot_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['AVTOT'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['AVTOT'])):
        return x['Median2']
    else:
        return x['AVTOT']

d4['AVTOT2'] = d4.apply(avtot_fillna, axis=1)

#test = d4.loc[d4['AVTOT'].isna(),['TAXCLASS','ZIP2','Count', 'Median1', 'Median2', 'AVTOT','AVTOT2']]
#np.sum(d4['AVTOT2']!=d4['AVTOT'])
#d4['AVTOT2'].isna().sum()

d4 = d4.drop(['Count','Median1','Median2'], axis=1)
del(d3)


# LTFRONT
ltfront_group = d4.groupby(['BLDGCL'])['LTFRONT'].agg({'Count':'count','Median1':'median'}).reset_index()
ltfront_group2 = d4.groupby('TAXCLASS')['LTFRONT'].agg({'Median2':'median'}).reset_index()

d5 = pd.merge(d4, ltfront_group, left_on='BLDGCL', right_on='BLDGCL', how='left' )
d5 = pd.merge(d5, ltfront_group2, left_on='TAXCLASS', right_on='TAXCLASS', how='left')

def ltfront_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['LTFRONT'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['LTFRONT'])):
        return x['Median2']
    else:
        return x['LTFRONT']
    
d5['LTFRONT2'] = d5.apply(ltfront_fillna, axis=1)

#test = d5.loc[d5['LTFRONT'].isna(),['TAXCLASS','BLDGCL','Count', 'Median1', 'Median2', 'LTFRONT','LTFRONT2']]
#np.sum(d5['LTFRONT2']!=d5['LTFRONT'])
#d5['LTFRONT2'].isna().sum()

d5 = d5.drop(['Count','Median1','Median2'], axis=1)
del(d4)

# LTDEPTH
ltdepth_group = d5.groupby(['BLDGCL'])['LTDEPTH'].agg({'Count':'count','Median1':'median'}).reset_index()
ltdepth_group2 = d5.groupby('TAXCLASS')['LTDEPTH'].agg({'Median2':'median'}).reset_index()


d6 = pd.merge(d5, ltdepth_group, left_on='BLDGCL', right_on='BLDGCL', how='left' )
d6 = pd.merge(d6, ltdepth_group2, left_on='TAXCLASS', right_on='TAXCLASS', how='left')

def ltdepth_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['LTDEPTH'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['LTDEPTH'])):
        return x['Median2']
    else:
        return x['LTDEPTH']

d6['LTDEPTH2'] = d6.apply(ltdepth_fillna, axis=1)

#test = d6.loc[d6['LTDEPTH'].isna(),['TAXCLASS','BLDGCL','Count', 'Median1', 'Median2', 'LTDEPTH','LTDEPTH2']]
#np.sum(d6['LTDEPTH2']!=d6['LTDEPTH'])
#d6['LTDEPTH2'].isna().sum()

d6 = d6.drop(['Count','Median1','Median2'], axis=1)
del(d5)

# BLDFRONT
bldfront_group = d6.groupby(['BLDGCL'])['BLDFRONT'].agg({'Count':'count','Median1':'median'}).reset_index()
bldfront_group2 = d6.groupby('TAXCLASS')['BLDFRONT'].agg({'Median2':'median'}).reset_index()


d7 = pd.merge(d6, bldfront_group, left_on='BLDGCL', right_on='BLDGCL', how='left' )
d7 = pd.merge(d7, bldfront_group2, left_on='TAXCLASS', right_on='TAXCLASS', how='left')

def bldfront_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['BLDFRONT'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['BLDFRONT'])):
        return x['Median2']
    else:
        return x['BLDFRONT']

d7['BLDFRONT2'] = d7.apply(bldfront_fillna, axis=1)

#test = d7.loc[d7['BLDFRONT'].isna(),['TAXCLASS','BLDGCL','Count', 'Median1', 'Median2', 'BLDFRONT','BLDFRONT2']]
#np.sum(d7['BLDFRONT2']!=d7['BLDFRONT'])
#d7['BLDFRONT2'].isna().sum()

d7 = d7.drop(['Count','Median1','Median2'], axis=1)
del(d6)


# BLDDEPTH
blddepth_group = d7.groupby(['BLDGCL'])['BLDDEPTH'].agg({'Count':'count','Median1':'median'}).reset_index()
blddepth_group2 = d7.groupby('TAXCLASS')['BLDDEPTH'].agg({'Median2':'median'}).reset_index()


d8 = pd.merge(d7, blddepth_group, left_on='BLDGCL', right_on='BLDGCL', how='left' )
d8 = pd.merge(d8, blddepth_group2, left_on='TAXCLASS', right_on='TAXCLASS', how='left')

def blddepth_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['BLDDEPTH'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['BLDDEPTH'])):
        return x['Median2']
    else:
        return x['BLDDEPTH']

d8['BLDDEPTH2'] = d8.apply(blddepth_fillna, axis=1)

#test = d8.loc[d8['BLDDEPTH'].isna(),['TAXCLASS','BLDGCL','Count', 'Median1', 'Median2', 'BLDDEPTH','BLDDEPTH2']]
#np.sum(d8['BLDDEPTH2']!=d8['BLDDEPTH'])
#d8['BLDDEPTH2'].isna().sum()


d8 = d8.drop(['Count','Median1','Median2'], axis=1)
del(d7)

# STORIES
stories_group = d8.groupby(['BLDGCL'])['STORIES'].agg({'Count':'count','Median1':'median'}).reset_index()
stories_group2 = d8.groupby('TAXCLASS')['STORIES'].agg({'Median2':'median'}).reset_index()


d9 = pd.merge(d8, stories_group, left_on='BLDGCL', right_on='BLDGCL', how='left' )
d9 = pd.merge(d9, stories_group2, left_on='TAXCLASS', right_on='TAXCLASS', how='left')

def stories_fillna(x):
    if (x['Count'] >= 10 and pd.isna(x['STORIES'])):
        return x['Median1']
    elif (x['Count'] < 10 and pd.isna(x['STORIES'])):
        return x['Median2']
    else:
        return x['STORIES']

d9['STORIES2'] = d9.apply(stories_fillna, axis=1)

#test = d9.loc[d9['STORIES'].isna(),['TAXCLASS','BLDGCL','Count', 'Median1', 'Median2', 'STORIES','STORIES2']]
#np.sum(d9['STORIES2']!=d9['STORIES'])
#d9['STORIES2'].isna().sum()

d9 = d9.drop(['Count','Median1','Median2'], axis=1)
del(d8)


# Export
d9.columns.values
d9.to_csv("NY Property Data Cleaned.csv", index=True)

