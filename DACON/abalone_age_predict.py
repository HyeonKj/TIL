# Basic Library
import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, QuantileTransformer

scaler1 = StandardScaler()
scaler2 = MinMaxScaler()
scaler3 = QuantileTransformer()
def feature_num_scaler(train_df, test_df):
    for num_col in num_cols:
        
        scaler1.fit(train[[num_col]])
        train_df[num_col+'#scaler1'] = scaler1.transform(train[[num_col]])
        test_df[num_col+'#scaler1'] = scaler1.transform(test_df[[num_col]])
        train_df[num_col+'#scaler1'] = train_df[num_col+'#scaler1'].replace(0.0, 0.001)
        test_df[num_col+'#scaler1'] = test_df[num_col+'#scaler1'].replace(0.0, 0.001)
        
        scaler2.fit(train[[num_col]])
        train_df[num_col+'#scaler2'] = scaler2.transform(train[[num_col]])
        test_df[num_col+'#scaler2'] = scaler2.transform(test_df[[num_col]])
        train_df[num_col+'#scaler2'] = train_df[num_col+'#scaler2'].replace(0.0, 0.001)
        test_df[num_col+'#scaler2'] = test_df[num_col+'#scaler2'].replace(0.0, 0.001)
        
        scaler3.fit(train[[num_col]])
        train_df[num_col+'#scaler3'] = scaler3.transform(train[[num_col]])
        test_df[num_col+'#scaler3'] = scaler3.transform(test_df[[num_col]])
        train_df[num_col+'#scaler3'] = train_df[num_col+'#scaler3'].replace(0.0, 0.001)
        test_df[num_col+'#scaler3'] = test_df[num_col+'#scaler3'].replace(0.0, 0.001)
        
        train_df[num_col+'#log2'] = np.log2(train_df[num_col])
        test_df[num_col+'#log2'] = np.log2(test_df[num_col])
        train_df[num_col+'#log2'] = train_df[num_col+'#log2'].replace(0.0, 0.006)
        test_df[num_col+'#log2'] = test_df[num_col+'#log2'].replace(0.0, 0.006)
        
        train_df[num_col+'#log'] = np.log(train_df[num_col])
        test_df[num_col+'#log'] = np.log(test_df[num_col])
        train_df[num_col+'#log'] = train_df[num_col+'#log'].replace(0.0, 0.004)
        test_df[num_col+'#log'] = test_df[num_col+'#log'].replace(0.0, 0.004)
        
        train_df[num_col+'#log10'] = np.log10(train_df[num_col])
        test_df[num_col+'#log10'] = np.log10(test_df[num_col])
        train_df[num_col+'#log10'] = train_df[num_col+'#log10'].replace(0.0, 0.002)
        test_df[num_col+'#log10'] = test_df[num_col+'#log10'].replace(0.0, 0.002)

def feature_cat_generation(df):

    for cat_col in cat_cols:
        for num_col in num_cols:        
            new_name = cat_col + "#mean#" + num_col
            grouped = df.groupby(cat_col)[num_col].mean()
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#std#" + num_col
            grouped = df.groupby(cat_col)[num_col].std(ddof = 1)
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#var#" + num_col
            grouped = df.groupby(cat_col)[num_col].var(ddof = 1)
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#max#" + num_col
            grouped = df.groupby(cat_col)[num_col].max()
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#min#" + num_col
            grouped = df.groupby(cat_col)[num_col].min()
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#ptp#" + num_col
            grouped = df.groupby(cat_col)[num_col].agg(np.ptp)
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#median" + num_col
            grouped = df.groupby(cat_col)[num_col].median()
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#skew" + num_col
            grouped = df.groupby(cat_col)[num_col].skew()
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#percentile_10" + num_col
            grouped = df.groupby(cat_col)[num_col].agg(lambda x: np.percentile(x, 10))
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#percentile_50" + num_col
            grouped = df.groupby(cat_col)[num_col].agg(lambda x: np.percentile(x, 50))
            df[new_name] = df[cat_col].map(grouped)

            new_name = cat_col + "#percentile_90" + num_col
            grouped = df.groupby(cat_col)[num_col].agg(lambda x: np.percentile(x, 90))
            df[new_name] = df[cat_col].map(grouped)
    
    return df

train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")
submission = pd.read_csv("../data/sample_submission.csv")

train = train.drop('id', axis=1)
test = test.drop('id', axis=1)

# 전체 무게 - (껍질 무게 + 껍질이 아닌 무게) Feature 생성
train['Water Weight'] = train['Whole Weight'] - (train['Shucked Weight'] + train['Shell Weight'])
test['Water Weight'] = test['Whole Weight'] - (test['Shucked Weight'] + test['Shell Weight'])

# 0.005보다 낮은 수는 0.005로 대체
train.loc[train[(train['Water Weight']<0.0005)].index, "Water Weight"] = 0.0005
test.loc[test[(test['Water Weight']<0.0005)].index, "Water Weight"] = 0.0005

# 0.01 값을 0.0으로 대체
train = train.replace(0.0, 0.01)
test = test.replace(0.0, 0.01)

cat_cols = []
num_cols = []
for col in train.columns:
    if train[col].dtypes=='object':
        cat_cols.append(col)
    elif train[col].dtypes=='float64':
        num_cols.append(col)

feature_num_scaler(train, test)

cat_cols = []
num_cols = []
for col in train.columns:
    if train[col].dtypes=='object':
        cat_cols.append(col)
    elif train[col].dtypes=='float64':
        num_cols.append(col)

for num_col_first in num_cols:
    for num_col_second in num_cols:
        if (num_col_first != num_col_second):
            train[num_col_first+'/'+num_col_second] = train[num_col_first] / train[num_col_second]
            train[num_col_first+'*'+num_col_second] = train[num_col_first] * train[num_col_second]
            test[num_col_first+'/'+num_col_second] = test[num_col_first] / test[num_col_second]
            test[num_col_first+'*'+num_col_second] = test[num_col_first] * test[num_col_second]

feature_cat_generation(train)
feature_cat_generation(test)

train.to_csv('../data/train_f1.csv', index=False)
test.to_csv('../data/test_f1.csv', index=False)

train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")
submission = pd.read_csv("../data/sample_submission.csv")

train = train.drop('id', axis=1)
test = test.drop('id', axis=1)

train['Weight Ratio'] = train['Shucked Weight'] / train['Whole Weight']
test['Weight Ratio'] = test['Shucked Weight'] / test['Whole Weight']

train['Foreign Body'] = train['Whole Weight'] - (train['Shucked Weight'] + train['Viscra Weight'] + train['Shell Weight'])
test['Foreign Body'] = test['Whole Weight'] - (test['Shucked Weight'] + test['Viscra Weight'] + test['Shell Weight'])
train.loc[train[(train['Foreign Body']<0.0005)].index, "Foreign Body"] = 0.0005
test.loc[test[(test['Foreign Body']<0.0005)].index, "Foreign Body"] = 0.0005

train = train.replace(0.0, 0.01)
test = test.replace(0.0, 0.01)

cat_cols = []
num_cols = []
for col in train.columns:
    if train[col].dtypes=='object':
        cat_cols.append(col)
    elif train[col].dtypes=='float64':
        num_cols.append(col)


feature_num_scaler(train, test)

cat_cols = []
num_cols = []
for col in train.columns:
    if train[col].dtypes=='object':
        cat_cols.append(col)
    elif train[col].dtypes=='float64':
        num_cols.append(col)
        
for num_col_first in num_cols:
    for num_col_second in num_cols:
        if (num_col_first != num_col_second):
            train[num_col_first+'/'+num_col_second] = train[num_col_first] / train[num_col_second]
            train[num_col_first+'*'+num_col_second] = train[num_col_first] * train[num_col_second]
            test[num_col_first+'/'+num_col_second] = test[num_col_first] / test[num_col_second]
            test[num_col_first+'*'+num_col_second] = test[num_col_first] * test[num_col_second]

feature_cat_generation(train)
feature_cat_generation(test)

train.to_csv('../data/train_f2.csv', index=False)
test.to_csv('../data/test_f2.csv', index=False)