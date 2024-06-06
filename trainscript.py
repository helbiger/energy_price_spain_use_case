import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import missingno as mno

import warnings
warnings.filterwarnings("ignore")
import logging
logging.disable(logging.CRITICAL)


import datetime
from TSF_Package import TSF
# from darts import TimeSeries, concatenate
# from darts.dataprocessing.transformers import Scaler
# from darts.models import TransformerModel
# from darts.metrics import mape, rmse
# from darts.utils.timeseries_generation import datetime_attribute_timeseries
# from darts.utils.likelihood_models import QuantileRegression


pd.set_option("display.precision",2)
np.set_printoptions(precision=2, suppress=True)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv("/workspaces/TSF/example_usage/energy/train_df.csv", header=0, parse_dates=["time"])
df = df.set_index("time")
df = df.drop(columns=["Unnamed: 0"])

future_data_exogen = df[df.index >= "2018-12-30 23:00:00+00:00"]
df = df[df.index < "2018-12-30 23:00:00+00:00"]

df = df.reset_index()

# Parameters
date_column = "time"
label_column = "price" #if aggregating then add _aggregationMethod (eg. "sales_sum")

time_format = "%Y-%m-%d %H:%M:%S" #format guideline https://strftime.org/ -> eg. 2016-01-06 00:00:00 would be "%Y-%m-%d %H:%M:%S"

# Config = None
# Preprocess config
frequency = 'H'
aggregate = False

# Train config
FcHorizon = 24
exogen = True
effort = 3
metric = "SMAPE" 
out_of_sample = True
choose_optimizer = "all"
ebm_only = True
blend_models = False

# Explain config
explainibility_on = True
explain_global = True
explain_local = True

# --------------------------------------------- TSF Workflow --------------------------------------------------------

tsf = TSF(
    data = df,
    frequency = frequency,
    date_column=date_column,
    label_column = label_column,
    title = "test")


# future_data_exogen = tsf.data[label_column].tshift(lag_len)
#     future_data_exogen = future_data_exogen.rename("Last year STD") 
# else:
#     print("Data is too short to create lags for this cluster")
#     tsf.data = tsf.data

future_data_exogen = future_data_exogen.drop(columns=[label_column])
if type(future_data_exogen) == pd.Series:
    future_data_exogen = future_data_exogen.to_frame()
            

tsf.preprocess(
format = time_format,
exogen = exogen,
normalize = False,
aggregate=aggregate,
all_mean=True,)


tsf.select_best_model(
    FcHorizon,
    effort = effort,
    metric = metric,
    out_of_sample = out_of_sample,
    choose_optimizer=choose_optimizer,
    blend_best_model=blend_models,
    quick_interpret_result=ebm_only,
    explainable_models=explainibility_on,
    future_data_exogen = future_data_exogen)


print("Train:", len(tsf.train_data))
print("Test:", len(tsf.test_data))
print("Future:", len(tsf.future_data))

pred1 = tsf.AutoML.best_optimizer.predict(on_final=False, fh = FcHorizon)
pred2 = tsf.AutoML.best_optimizer.predict(on_final=True, fh = FcHorizon)
pred = pd.concat([pred1, pred2], axis=0)

actuals = tsf.test_data

# csv_name = filter_name + "_prediction_" + cluster + "_" + str(FcHorizon) + "_" + str(frequency) + ".csv"
pred.to_csv("/workspaces/TSF/example_usage/energy/prediction.csv")

concat_df = pd.concat([actuals, pred], axis=1)
concat_df.to_csv("/workspaces/TSF/example_usage/energy/concat_df.csv")