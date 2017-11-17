
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

#import json file
purchasedata = "purchase_data.json"
purchasedataDF = pd.read_json(purchasedata)
#purchasedataDF.head()


# Player Count
# Total Number of Players

# In[3]:

# take value counts on SN and print the len to get total player count

playercount = purchasedataDF["SN"].value_counts()
playercount = len(playercount)
playercount


# Purchasing Analysis (Total)
# 
# Number of Unique Items
# 
# Average Purchase Price
# 
# Total Number of Purchases
# 
# Total Revenue

# In[4]:

# number of unique items. Take value count of Item ID and print len to get Item Name Count
itemName = purchasedataDF["Item ID"].value_counts()
itemcount = len(itemName)
itemcount


# In[5]:

#Average Purchase Price. Take the mean of the Price column
averageprice = purchasedataDF["Price"].mean()
averageprice


# In[6]:

#Total Number of Purchases. Take a count of all Item IDs
totalPurchases = purchasedataDF["Item ID"].count()
totalPurchases


# In[7]:

#Total Revenue
totalrevenue = purchasedataDF["Price"].sum()
totalrevenue


# Gender Demographics
# 
# Percentage and Count of Male Players
# 
# Percentage and Count of Female Players
# 
# Percentage and Count of Other / Non-Disclosed

# In[8]:

#percentage and count of male players
gender = purchasedataDF.loc[purchasedataDF["Gender"]=="Male"]
malegender = gender["SN"].value_counts()
malecount = len(malegender)
malecount


# In[9]:

#Percentage and Count of Female Players
gender = purchasedataDF.loc[purchasedataDF["Gender"]=="Female"]
femalegender = gender["SN"].value_counts()
femalecount = len(femalegender)
femalecount


# In[10]:

#Percentage and Count of Other / Non-Disclosed
gender = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
othergender = gender["SN"].value_counts()
othercount = len(othergender)
othercount


# Purchasing Analysis (Gender)
# 
# The below each broken by gender
# 
# Purchase Count
# 
# Average Purchase Price
# 
# Total Purchase Value
# 
# Normalized Totals

# In[11]:

# Male Purchase Count
malepurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
malepurchase = malepurchase["Item ID"].count()
print(malepurchase)

# Male Average Purchase Price
maleaverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
maleaverage = maleaverage["Price"].mean()
print(maleaverage)

# Total Purchase Value
maletotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
maletotal = maletotal["Price"].sum()
print(maletotal)

# Normalized Male Totals


# In[12]:

# Female Purchase Count
femalepurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femalepurchase = femalepurchase["Item ID"].count()
print(femalepurchase)

# Female Average Purchase Price
femaleaverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femaleaverage = femaleaverage["Price"].mean()
print(femaleaverage)

# Total Female Purchase Value
femaletotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femaletotal = femaletotal["Price"].sum()
print(femaletotal)

# Normalized Female Totals


# In[13]:

# Other Purchase Count
otherpurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
otherpurchase = otherpurchase["Item ID"].count()
print(otherpurchase)

# Other Average Purchase Price
otheraverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
otheraverage = otheraverage["Price"].mean()
print(otheraverage)

# Total Other Purchase Value
othertotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
othertotal = othertotal["Price"].sum()
print(othertotal)

# Normalized Other Totals


# Age Demographics
# 
# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
# 
# Purchase Count
# 
# Average Purchase Price
# 
# Total Purchase Value
# 
# Normalized Totals

# In[14]:

# Bins are 0 to 10, 10 to 14, 15 to 19, 20 to 24, 25 to 29, 30 to 34, 35+
bins = [0, 10, 15, 20, 25, 30, 35, 100]

# Create the names for the bins
group_names = ['< 10', '10 - 14', '15 - 19 ', '20 - 24', '25 - 29', '30 - 34', '35 +']


# In[17]:

# Cut age and place the scores into bins
# append column at the end of original data frame for age group
purchasedataDF["Age Group"] = pd.cut(purchasedataDF["Age"], bins, labels=group_names)
purchasedataDF.head()


# In[18]:

groupitemcount = purchasedataDF.groupby("Age Group")["Item Name"].count()
groupitemcount


# In[19]:

grouppriceaverage = purchasedataDF.groupby("Age Group")["Price"].mean()
grouppriceaverage


# In[20]:

groupsumvalue = purchasedataDF.groupby("Age Group")["Price"].sum()
groupsumvalue


# Top Spenders
# 
# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# 
# SN
# 
# Purchase Count
# 
# Average Purchase Price
# 
# Total Purchase Value

# In[21]:

# groupby SN, sum the price, and then reset index
SNtop5sum = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].sum())
SNtop5sum.reset_index(inplace = True)


# In[22]:

# groupby SN, count the price, and then reset index
SNtop5count = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].count())
SNtop5count.reset_index(inplace = True)


# In[23]:

# groupby SN, mean of the price, and then reset index
SNtop5mean = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].mean())
SNtop5mean.reset_index(inplace = True)


# In[24]:

# merge sum and count tables together on SN
mergeSN = pd.merge(SNtop5sum, SNtop5count, on = "SN")

# merge the sum/count frame created with the mean on SN
mergeSN2 = pd.merge(mergeSN, SNtop5mean, on = "SN")

#rename columns accordingly and print top 5
mergeSN2.columns = ["SN","Total Purchase Value", "Total Count","Average Count"]
mergeSN2.head(5)


# Most Popular Items
# 
# 
# Identify the 5 most popular items by purchase count, then list (in a table):
# 
# Item ID
# 
# Item Name
# 
# 
# Purchase Count
# 
# Item Price
# 
# Total Purchase Value

# In[25]:

# groupby Item ID, count the price, and then reset index
ItemIDcount = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].count())
ItemIDcount.reset_index(inplace = True)


# In[26]:

# groupby Item ID, sum the price, and then reset index
ItemIDsum = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].sum())
ItemIDsum.reset_index(inplace = True)


# In[28]:

#merge ItemID count and sum dataframes
mergeItem = pd.merge(ItemIDcount, ItemIDsum, on = "Item ID")

#create new dataframe with just item ID, item name, and price of item
ItemNamePrice = pd.DataFrame(purchasedataDF[["Item ID","Item Name","Price"]])

#merge item count/sum table with new dataframe just created to to add the name and price
mergeItemTable = pd.merge(ItemNamePrice,mergeItem, on = "Item ID")

#rename columns and then sort by purchase count
mergeItemTable.columns = ["Item ID","Item Name", "Item Price","Purchase Count","Total Purchase Value"]
mergeItemTable = mergeItemTable.sort_values(["Purchase Count"], ascending = False)

#drop duplicate items and print top 5
mergeItemTableDup = mergeItemTable.drop_duplicates()
mergeItemTableDup.head()


# Most Profitable Items
# 
# 
# Identify the 5 most profitable items by total purchase value, then list (in a table):
#     
# Item ID
# 
# Item Name
# 
# Purchase Count
# 
# Item Price
# 
# Total Purchase Value

# In[29]:

# create new table with price, item id, and item name
ProfitTable = pd.DataFrame(purchasedataDF[["Price","Item ID","Item Name"]])
ProfitTableDF = ProfitTable.drop_duplicates()


# In[30]:

# groupby  Item ID, count the price, sort by price
ProfitCount = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].count())
ProfitCount.reset_index(inplace = True)


# In[31]:

# groupby Item ID, sum the price, sort by price
ProfitSum = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].sum())
ProfitSum.reset_index(inplace = True)


# In[32]:

# merge profit table DF and profit counts on Item ID
profitmerge = pd.merge(ProfitTableDF, ProfitCount, on = "Item ID")

# merge profitmerge and profit sums on Item ID
profitmerge2 = pd.merge(profitmerge, ProfitSum, on = "Item ID")

# rename columns
profitmerge2.columns = ["Price", "Item ID", "Item Name", "Purchase Count","Total Purchase Value"]

# sort on Price and print top 5
profitmergeTable = profitmerge2.sort_values(["Price"], ascending = False)
profitmergeTable.head()

