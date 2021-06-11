import plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\code\python\pro-103\covid_data.csv")
fig = px.funnel(df, x="date", y="cases",color="country",title='Corona Cases')
plotly.offline.plot(fig)