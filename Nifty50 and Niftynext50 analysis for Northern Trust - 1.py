#!/usr/bin/env python
# coding: utf-8

# ### Import the required library
# 

# In[2]:


import pandas as pd


# ### Import the data files

# Set the working directory

# In[3]:


pwd


# In[4]:


cd D:\nifty50 and niftynext50 data


# Read the csv files

# In[5]:


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


# In[6]:


nifty50_sep.head(20)


# ### Sorting the dataframes in descending order by 'Monthly Return' 

# In[132]:


nifty50_sep_byperformance=nifty50_sep.sort_values(by='Monthly Return', ascending=False)
nifty50_oct_byperformance=nifty50_oct.sort_values(by='Monthly Return', ascending=False)
nifty50_nov_byperformance=nifty50_nov.sort_values(by='Monthly Return', ascending=False)
nifty50_dec_byperformance=nifty50_dec.sort_values(by='Monthly Return', ascending=False)
nifty50_jan_byperformance=nifty50_jan.sort_values(by='Monthly Return', ascending=False)
nifty50_feb_byperformance=nifty50_feb.sort_values(by='Monthly Return', ascending=False)
niftynext50_sep_byperformance=niftynext50_sep.sort_values(by='Monthly Return', ascending=False)
niftynext50_oct_byperformance=niftynext50_oct.sort_values(by='Monthly Return', ascending=False)
niftynext50_nov_byperformance=niftynext50_nov.sort_values(by='Monthly Return', ascending=False)
niftynext50_dec_byperformance=niftynext50_dec.sort_values(by='Monthly Return', ascending=False)
niftynext50_jan_byperformance=niftynext50_jan.sort_values(by='Monthly Return', ascending=False)
niftynext50_feb_byperformance=niftynext50_feb.sort_values(by='Monthly Return', ascending=False)


# ### Extracting top 5 stocks 

# In[133]:


nifty50_sep_topstocks=nifty50_sep_byperformance.iloc[:5,[1,5,9]]
nifty50_oct_topstocks=nifty50_oct_byperformance.iloc[:5,[1,5,9]]
nifty50_nov_topstocks=nifty50_nov_byperformance.iloc[:5,[1,5,9]]
nifty50_dec_topstocks=nifty50_dec_byperformance.iloc[:5,[1,5,9]]
nifty50_jan_topstocks=nifty50_jan_byperformance.iloc[:5,[1,5,9]]
nifty50_feb_topstocks=nifty50_feb_byperformance.iloc[:5,[1,5,9]]
niftynext50_sep_topstocks=niftynext50_sep_byperformance.iloc[:5,[1,5,9]]
niftynext50_oct_topstocks=niftynext50_oct_byperformance.iloc[:5,[1,5,9]]
niftynext50_nov_topstocks=niftynext50_nov_byperformance.iloc[:5,[1,5,9]]
niftynext50_dec_topstocks=niftynext50_dec_byperformance.iloc[:5,[1,5,9]]
niftynext50_jan_topstocks=niftynext50_jan_byperformance.iloc[:5,[1,5,9]]
niftynext50_feb_topstocks=niftynext50_feb_byperformance.iloc[:5,[1,5,9]]


# ### Serialise 

# In[134]:


nifty50_sep_topstocks=nifty50_sep_topstocks.set_index('Security Name')
nifty50_oct_topstocks=nifty50_oct_topstocks.set_index('Security Name')
nifty50_nov_topstocks=nifty50_nov_topstocks.set_index('Security Name')
nifty50_dec_topstocks=nifty50_dec_topstocks.set_index('Security Name')
nifty50_jan_topstocks=nifty50_jan_topstocks.set_index('Security Name')
nifty50_feb_topstocks=nifty50_feb_topstocks.set_index('Security Name')
niftynext50_sep_topstocks=niftynext50_sep_topstocks.set_index('Security Name')
niftynext50_oct_topstocks=niftynext50_oct_topstocks.set_index('Security Name')
niftynext50_nov_topstocks=niftynext50_nov_topstocks.set_index('Security Name')
niftynext50_dec_topstocks=niftynext50_dec_topstocks.set_index('Security Name')
niftynext50_jan_topstocks=niftynext50_jan_topstocks.set_index('Security Name')
niftynext50_feb_topstocks=niftynext50_feb_topstocks.set_index('Security Name')


# ### Final Output

# #### 1. Nifty50 top stocks: September 2018 

# In[135]:


nifty50_sep_topstocks


# #### 2. Nifty50 top stocks: October 2018 

# In[136]:


nifty50_oct_topstocks


# #### 3. Nifty50 top stocks: November 2018 

# In[137]:


nifty50_nov_topstocks


# #### 4. Nifty50 top stocks: December 2018 

# In[138]:


nifty50_dec_topstocks


# #### 5. Nifty50 top stocks: January 2019 

# In[139]:


nifty50_jan_topstocks


# #### 6. Nifty50 top stocks: February 2019

# In[140]:


nifty50_feb_topstocks


# #### 7. Niftynext50 top stocks: September 2018 

# In[141]:


niftynext50_sep_topstocks


# #### 8. Niftynext50 top stocks: October 2018 

# In[142]:


niftynext50_nov_topstocks


# #### 9. Niftynext50 top stocks: November 2018 

# In[143]:


niftynext50_oct_topstocks


# #### 10. Niftynext50 top stocks: December 2018 

# In[144]:


niftynext50_dec_topstocks


# #### 11. Niftynext50 top stocks: January 2019

# In[145]:


niftynext50_jan_topstocks


# #### 12. Niftynext50 top stocks: February 2019 

# In[146]:


niftynext50_feb_topstocks


# # -----------------------------------------------------------------------------------------------------------

# # Detailed Analysis

# ## 1. Nifty50 : September 2018

# ### Exploratory Data Analysis 

# In[19]:


nifty50_sep.head()


# In[20]:


nifty50_sep.columns


# In[21]:


nifty50_sep.shape


# In[22]:


nifty50_sep.info()


# Summary Statistics

# In[23]:


nifty50_sep.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[24]:


nifty50_sep_byperformance=nifty50_sep.sort_values(by='Monthly Return', ascending=False)


# In[25]:


nifty50_sep_byperformance.head()


# Extracting top 5 stocks

# In[26]:


nifty50_sep_topstocks=nifty50_sep_byperformance.iloc[:5,[1,5,9]]


# In[27]:


nifty50_sep_topstocks


# ## 2. Nifty50 : October 2018

# ### Exploratory Data Analysis 

# In[28]:


nifty50_oct.head()


# In[29]:


nifty50_oct.columns


# In[30]:


nifty50_oct.info()


# Summary Statistics

# In[31]:


nifty50_oct.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[32]:


nifty50_oct_byperformance=nifty50_oct.sort_values(by='Monthly Return', ascending=False)


# In[33]:


nifty50_oct_byperformance.head()


# Extracting top 5 stocks

# In[34]:


nifty50_oct_topstocks=nifty50_oct_byperformance.iloc[:5,[1,5,9]]


# In[35]:


nifty50_oct_topstocks


# ## 3. Nifty50 : November 2018

# ### Exploratory Data Analysis 

# In[36]:


nifty50_nov.head()


# In[37]:


nifty50_nov.columns


# In[38]:


nifty50_nov.info()


# Summary Statistics

# In[39]:


nifty50_nov.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[40]:


nifty50_nov_byperformance=nifty50_nov.sort_values(by='Monthly Return', ascending=False)


# In[41]:


nifty50_nov_byperformance.head()


# Extracting top 5 stocks

# In[42]:


nifty50_nov_topstocks=nifty50_nov_byperformance.iloc[:5,[1,5,9]]


# In[43]:


nifty50_nov_topstocks


# ## 4. Nifty50 : December 2018

# ### Exploratory Data Analysis 

# In[44]:


nifty50_dec.head()


# In[45]:


nifty50_dec.columns


# In[46]:


nifty50_dec.info()


# Summary Statistics

# In[47]:


nifty50_dec.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[48]:


nifty50_dec_byperformance=nifty50_dec.sort_values(by='Monthly Return', ascending=False)


# In[49]:


nifty50_dec_byperformance.head()


# Extracting top 5 stocks

# In[50]:


nifty50_dec_topstocks=nifty50_dec_byperformance.iloc[:5,[1,5,9]]


# In[51]:


nifty50_dec_topstocks


# ## 5. Nifty50 : January 2019

# ### Exploratory Data Analysis 

# In[52]:


nifty50_jan.head()


# In[53]:


nifty50_jan.columns


# In[54]:


nifty50_jan.info()


# Summary Statistics

# In[55]:


nifty50_jan.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[56]:


nifty50_jan_byperformance=nifty50_jan.sort_values(by='Monthly Return', ascending=False)


# In[57]:


nifty50_jan_byperformance.head()


# Extracting top 5 stocks

# In[58]:


nifty50_jan_topstocks=nifty50_jan_byperformance.iloc[:5,[1,5,9]]


# In[59]:


nifty50_jan_topstocks


# ## 6. Nifty50 : February 2019

# ### Exploratory Data Analysis 

# In[60]:


nifty50_feb.head()


# In[61]:


nifty50_feb.columns


# In[62]:


nifty50_feb.info()


# Summary Statistics

# In[63]:


nifty50_feb.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[64]:


nifty50_feb_byperformance=nifty50_feb.sort_values(by='Monthly Return', ascending=False)


# In[65]:


nifty50_feb_byperformance.head()


# Extracting top 5 stocks

# In[66]:


nifty50_feb_topstocks=nifty50_feb_byperformance.iloc[:5,[1,5,9]]


# In[67]:


nifty50_feb_topstocks


# ## 7. Niftynext50 : September 2018

# ### Exploratory Data Analysis 

# In[68]:


niftynext50_sep.head()


# In[69]:


niftynext50_sep.columns


# In[70]:


niftynext50_sep.info()


# Summary Statistics

# In[71]:


niftynext50_sep.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[72]:


niftynext50_sep_byperformance=niftynext50_sep.sort_values(by='Monthly Return', ascending=False)


# In[73]:


niftynext50_sep_byperformance.head()


# Extracting top 5 stocks

# In[74]:


niftynext50_sep_topstocks=niftynext50_sep_byperformance.iloc[:5,[1,5,9]]


# In[75]:


niftynext50_sep_topstocks


# ## 8. Niftynext50 : October 2018

# ### Exploratory Data Analysis 

# In[76]:


niftynext50_oct.head()


# In[77]:


niftynext50_oct.columns


# In[78]:


niftynext50_oct.info()


# Summary Statistics

# In[79]:


niftynext50_oct.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[80]:


niftynext50_oct_byperformance=niftynext50_oct.sort_values(by='Monthly Return', ascending=False)


# In[81]:


niftynext50_oct_byperformance.head()


# Extracting top 5 stocks

# In[82]:


niftynext50_oct_topstocks=niftynext50_oct_byperformance.iloc[:5,[1,5,9]]


# In[83]:


niftynext50_oct_topstocks


# ## 9. Niftynext50 : November 2018

# ### Exploratory Data Analysis 

# In[84]:


niftynext50_nov.head()


# In[85]:


niftynext50_nov.columns


# In[86]:


niftynext50_nov.info()


# Summary Statistics

# In[87]:


niftynext50_nov.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[88]:


niftynext50_nov_byperformance=niftynext50_nov.sort_values(by='Monthly Return', ascending=False)


# In[89]:


niftynext50_nov_byperformance.head()


# Extracting top 5 stocks

# In[90]:


niftynext50_nov_topstocks=niftynext50_nov_byperformance.iloc[:5,[1,5,9]]


# In[91]:


niftynext50_nov_topstocks


# ## 10. Niftynext50 : December 2018

# ### Exploratory Data Analysis 

# In[92]:


niftynext50_dec.head()


# In[93]:


niftynext50_dec.columns


# In[94]:


niftynext50_dec.info()


# Summary Statistics

# In[95]:


niftynext50_dec.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[96]:


niftynext50_dec_byperformance=niftynext50_dec.sort_values(by='Monthly Return', ascending=False)


# In[97]:


niftynext50_dec_byperformance.head()


# Extracting top 5 stocks

# In[98]:


niftynext50_dec_topstocks=niftynext50_dec_byperformance.iloc[:5,[1,5,9]]


# In[99]:


niftynext50_dec_topstocks


# ## 11. Niftynext50 : January 2019

# ### Exploratory Data Analysis 

# In[100]:


niftynext50_jan.head()


# In[101]:


niftynext50_jan.columns


# In[102]:


niftynext50_jan.info()


# Summary Statistics

# In[103]:


niftynext50_jan.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[104]:


niftynext50_jan_byperformance=niftynext50_jan.sort_values(by='Monthly Return', ascending=False)


# In[105]:


niftynext50_jan_byperformance.head()


# Extracting top 5 stocks

# In[106]:


niftynext50_jan_topstocks=niftynext50_jan_byperformance.iloc[:5,[1,5,9]]


# In[107]:


niftynext50_jan_topstocks


# ## 12. Niftynext50 : February 2019

# ### Exploratory Data Analysis 

# In[108]:


niftynext50_feb.head()


# In[109]:


niftynext50_feb.columns


# In[110]:


niftynext50_feb.info()


# Summary Statistics

# In[111]:


niftynext50_feb.describe()


# ### Top 5 stocks by performance 

# Arranging the stocks in descending order by Monthly Returns

# In[112]:


niftynext50_feb_byperformance=niftynext50_feb.sort_values(by='Monthly Return', ascending=False)


# In[113]:


niftynext50_feb_byperformance.head()


# Extracting top 5 stocks

# In[114]:


niftynext50_feb_topstocks=niftynext50_feb_byperformance.iloc[:5,[1,5,9]]


# In[115]:


niftynext50_feb_topstocks


# # -------------------------------------------------------------------

# In[118]:


import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)


# In[119]:


plotly.tools.set_credentials_file(username='Devanshi', api_key='1a7VAfB8ovyuue1c2ujf')


# In[151]:


nifty50_sep.head(10)


# In[ ]:




