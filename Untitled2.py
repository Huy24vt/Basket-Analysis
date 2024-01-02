#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mlxtend


# In[2]:


#Firstly, we need to import the data and set up the relevant libraries for our analysis.
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")


# In[3]:


# Load dataset
data_ = pd.read_excel(r"C:\Users\ACER\Downloads\online+retail\Online Retail.xlsx")
data = data_.copy()
data.head()


# In[30]:


# I will narrow down the dataset by including only transactions from Germany.
data = data[data["Country"]=="Germany"]


# In[31]:


#Since the 'Description' column contains some noise, such as 'Mannual' or 'Postage,' we need to address these issues.
data = data[data["Description"].str.len() > 9]


# In[32]:


#Now, let's examine the number of unique StockCodes and Descriptions. It appears that some StockCodes represent more than one product or description.print(data.StockCode.nunique())
print(data.StockCode.nunique())
print(data.Description.nunique())


# In[33]:


#I want each StockCode to represent only one description, so we need to address this issue.
df = data[["StockCode","Description"]].drop_duplicates()
df = df.groupby(["StockCode"]).agg({"Description":"count"}).reset_index()
df = df[df["Description"]>1]
#Let's delete products with more than one Description:
data = data[~data["StockCode"].isin(df["StockCode"])]


# In[34]:


#Let's review the number of unique StockCode and Description. Now each StockCode represents only 1 Description
print(data.StockCode.nunique())
print(data.Description.nunique())


# In[35]:


#Next, Preparing Invoice-Product Matrix fot ARL(Association Rule Learning) Data Structure
def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['InvoiceNo', "StockCode"])['Quantity'].sum().unstack().fillna(0).             applymap(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0).             applymap(lambda x: 1 if x > 0 else 0)


# In[36]:


inv_pro_df = create_invoice_product_df(data, id=True)
inv_pro_df.head()


# In[37]:


#Determination of Association Rules
#Calculate the support values for every possible configuration of items (thereshold of support has been chosen 0.01 (1%))
frequent_itemsets = apriori(inv_pro_df, min_support=0.01, use_colnames=True)


# In[38]:


# And here is our rules
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
rules.sort_values("support",ascending=False).head(5)


# In[ ]:




