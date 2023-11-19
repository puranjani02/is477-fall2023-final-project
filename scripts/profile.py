import pandas as pd
from ydata_profiling import ProfileReport
import os

#reading the prepared csv file 
df=pd.read_csv('data/wine.csv')

profile = ProfileReport(df, title="Profiling Report")

if os.path.exists('profiling')==0:
    os.mkdir('profiling')
profile.to_file("profiling/report.html")
