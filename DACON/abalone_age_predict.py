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

        