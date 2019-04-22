#!/usr/bin/env python
# coding: utf-8

# #### Import the required libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# #### Set the working directory 

# In[3]:


cd D:\nifty50 and niftynext50 data


# #### Read the csv files 

# In[4]:


nifty50_sep=pd.read_csv("nifty50_sep.csv", index_col=0)
nifty50_oct=pd.read_csv("nifty50_oct.csv", index_col=0)
nifty50_nov=pd.read_csv("nifty50_nov.csv", index_col=0)
nifty50_dec=pd.read_csv("nifty50_dec.csv", index_col=0)
nifty50_jan=pd.read_csv("nifty50_jan.csv", index_col=0)
nifty50_feb=pd.read_csv("nifty50_feb.csv", index_col=0)
niftynext50_sep=pd.read_csv("niftynext50_sep.csv", index_col=0)
niftynext50_oct=pd.read_csv("niftynext50_oct.csv", index_col=0)
niftynext50_nov=pd.read_csv("niftynext50_nov.csv", index_col=0)
niftynext50_dec=pd.read_csv("niftynext50_dec.csv", index_col=0)
niftynext50_jan=pd.read_csv("niftynext50_jan.csv", index_col=0)
niftynext50_feb=pd.read_csv("niftynext50_feb.csv", index_col=0)


# #### Multiply weightage with Monthly Return divided by 100, to obtain a new column 'Total Return'

# In[5]:


nifty50_sep['Total Return']=nifty50_sep['Weightage (%)']*nifty50_sep['Monthly Return']/100
nifty50_oct['Total Return']=nifty50_oct['Weightage (%)']*nifty50_oct['Monthly Return']/100
nifty50_nov['Total Return']=nifty50_nov['Weightage (%)']*nifty50_nov['Monthly Return']/100
nifty50_dec['Total Return']=nifty50_dec['Weightage (%)']*nifty50_dec['Monthly Return']/100
nifty50_jan['Total Return']=nifty50_jan['Weightage (%)']*nifty50_jan['Monthly Return']/100
nifty50_feb['Total Return']=nifty50_feb['Weightage (%)']*nifty50_feb['Monthly Return']/100
niftynext50_sep['Total Return']=niftynext50_sep['Weightage (%)']*niftynext50_sep['Monthly Return']/100
niftynext50_oct['Total Return']=niftynext50_oct['Weightage (%)']*niftynext50_oct['Monthly Return']/100
niftynext50_nov['Total Return']=niftynext50_nov['Weightage (%)']*niftynext50_nov['Monthly Return']/100
niftynext50_dec['Total Return']=niftynext50_dec['Weightage (%)']*niftynext50_dec['Monthly Return']/100
niftynext50_jan['Total Return']=niftynext50_jan['Weightage (%)']*niftynext50_jan['Monthly Return']/100
niftynext50_feb['Total Return']=niftynext50_feb['Weightage (%)']*niftynext50_feb['Monthly Return']/100


# #### Find the summation of the Total Returns for every month 

# In[6]:


nifty50_sep_TR=nifty50_sep['Total Return'].sum()
nifty50_oct_TR=nifty50_oct['Total Return'].sum()
nifty50_nov_TR=nifty50_nov['Total Return'].sum()
nifty50_dec_TR=nifty50_dec['Total Return'].sum()
nifty50_jan_TR=nifty50_jan['Total Return'].sum()
nifty50_feb_TR=nifty50_feb['Total Return'].sum()
niftynext50_sep_TR=niftynext50_sep['Total Return'].sum()
niftynext50_oct_TR=niftynext50_oct['Total Return'].sum()
niftynext50_nov_TR=niftynext50_nov['Total Return'].sum()
niftynext50_dec_TR=niftynext50_dec['Total Return'].sum()
niftynext50_jan_TR=niftynext50_jan['Total Return'].sum()
niftynext50_feb_TR=niftynext50_feb['Total Return'].sum()


# In[7]:


niftynext50_feb_TR


# #### Create two new dataframes for each index with first column being a list of months and second column being the respective total returns 

# In[21]:


totalreturns_nifty50=pd.DataFrame({'Month':['Sep','Oct','Nov','Dec','Jan','Feb'],
                                   'Total Returns (nifty50)':[nifty50_sep_TR,nifty50_oct_TR,nifty50_nov_TR, 
                                                    nifty50_dec_TR,nifty50_jan_TR,nifty50_feb_TR]})

totalreturns_niftynext50=pd.DataFrame({'Month':['Sep','Oct','Nov','Dec','Jan','Feb'],
                                       'Total Returns (niftynext50)':[niftynext50_sep_TR,niftynext50_oct_TR,niftynext50_nov_TR, 
                                                        niftynext50_dec_TR,niftynext50_jan_TR,niftynext50_feb_TR]})


# In[8]:


totalreturns_niftynext50


# #### Set the column 'Month' as index 

# In[56]:


totalreturns_nifty50=totalreturns_nifty50.set_index('Month')
totalreturns_nifty50


# In[57]:


totalreturns_niftynext50=totalreturns_niftynext50.set_index('Month')
totalreturns_niftynext50


# #### Obtain the plot using plotly 

# In[55]:


import plotly.plotly as py
import plotly.graph_objs as go

# Create and style traces
trace0 = go.Scatter(
    x = totalreturns_nifty50['Month'],
    y = totalreturns_nifty50['Total Returns (nifty50)'],
    name = 'NIFTY 50',
    line = dict(
        color = ('rgb(150, 20, 20)'),
        width = 4)
)
trace1 = go.Scatter(
x = totalreturns_niftynext50['Month'],
    y = totalreturns_niftynext50['Total Returns (niftynext50)'],
    name = 'NIFTY Next 50',
    line = dict(
        color = ('rgb(215, 2, 2)'),
        width = 4,)
)

data = [trace0, trace1]

# Edit the layout
layout = dict(title = 'NIFTY 50 Returns vs NIFTY Next 50 Returns',
              xaxis = dict(title = 'Month'),
              yaxis = dict(title = 'Total Returns'),
              )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='total nifty returns')

