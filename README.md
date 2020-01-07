### Three Observable Trends based on the Analysis

1. Males are by far the most significant demographic more amount than females and others. They make up more than 80% of the players and account for more then 80% of the total revenue.

2. Players from the ages of 20-24 spend are 50% of the player base and spend the most of all age groups.


3. Items priced over 4 dollars make the most revenue despite not having as many sales. For example the most sold item Arcane Gem at a price of 2.23 sold 11 times but only grossed 24.53 in revenue. The most profitable item Orenmir at 4.95 an item only sold 6 times but generated 29.70 in revenue. Raising the price of some items may lead to a higher revenue total.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
#import json file
purchasedata = "purchase_data.json"
purchasedataDF = pd.read_json(purchasedata)
purchasedataDF.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count
* Total Number of Players


```python
# take value counts on SN and print the len to get total player count

playercount = purchasedataDF["SN"].value_counts()
playercount = len(playercount)
playercountDF = pd.DataFrame({"Total Players":[playercount]})
playercountDF
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)
* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue


```python
# number of unique items. Take value count of Item ID and print len to get Item Name Count
itemName = purchasedataDF["Item ID"].value_counts()
itemcount = len(itemName)
```


```python
#Average Purchase Price. Take the mean of the Price column
averageprice = purchasedataDF["Price"].mean()
```


```python
#Total Number of Purchases. Take a count of all Item IDs
totalPurchases = purchasedataDF["Item ID"].count()
```


```python
#Total Revenue
totalrevenue = purchasedataDF["Price"].sum()
```


```python
#Create new Data Frame with values and formats
purchanalysisDF = pd.DataFrame({
    "Number of Unique Items":[itemcount],
    "Average Price":[averageprice],
    "Number of Purchases":[totalPurchases],
    "Total Revenue":[totalrevenue]})
purchanalysisDF["Average Price"] = purchanalysisDF["Average Price"].map("${0:,.2f}".format)
purchanalysisDF["Total Revenue"] = purchanalysisDF["Total Revenue"].map("${0:,.2f}".format)
purchanalysisDF                                     
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
      <td>780</td>
      <td>183</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics
* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed


```python
#percentage and count of male players
gender = purchasedataDF.loc[purchasedataDF["Gender"]=="Male"]
malegender = gender["SN"].value_counts()
malecount = len(malegender)

percentmale = (malecount / playercount)*100
```


```python
#Percentage and Count of Female Players
gender = purchasedataDF.loc[purchasedataDF["Gender"]=="Female"]
femalegender = gender["SN"].value_counts()
femalecount = len(femalegender)

percentfemale = (femalecount / playercount)*100
```


```python
#Percentage and Count of Other / Non-Disclosed
gender = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
othergender = gender["SN"].value_counts()
othercount = len(othergender)

percentother = (othercount / playercount)*100
```


```python
gendertypes = purchasedataDF["Gender"].unique()
```


```python
#Create new Data Frame with Gender Analysis
gendhanalysisDF = pd.DataFrame({"Gender":gendertypes,
    "Percentage of Players":[percentmale, percentfemale, percentother],
    "Total Count":[malecount,femalecount,othercount]})
gendhanalysisDF["Percentage of Players"] = gendhanalysisDF["Percentage of Players"].map("{0:,.2f}%".format)
gendhanalysisDF.set_index(["Gender"])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Gender)
* The below each broken by gender
* Purchase Count
* Average Purchase Price
* Total Purchase Value



```python
# Male Purchase Count
malepurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
malepurchase = malepurchase["Item ID"].count()

# Male Average Purchase Price
maleaverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
maleaverage = maleaverage["Price"].mean()

# Total Purchase Value
maletotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Male"]
maletotal = maletotal["Price"].sum()
```


```python
# Female Purchase Count
femalepurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femalepurchase = femalepurchase["Item ID"].count()

# Female Average Purchase Price
femaleaverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femaleaverage = femaleaverage["Price"].mean()

# Total Female Purchase Value
femaletotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Female"]
femaletotal = femaletotal["Price"].sum()
```


```python
# Other Purchase Count
otherpurchase = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
otherpurchase = otherpurchase["Item ID"].count()

# Other Average Purchase Price
otheraverage = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
otheraverage = otheraverage["Price"].mean()

# Total Other Purchase Value
othertotal = purchasedataDF.loc[purchasedataDF["Gender"] == "Other / Non-Disclosed"]
othertotal = othertotal["Price"].sum()
```


```python
#Create new Data Frame with Gender Analysis
genpurchanalysisDF = pd.DataFrame({"Gender":gendertypes,
    "Purchase Count":[malepurchase, femalepurchase, otherpurchase],
    "Average Purchase Price":[maleaverage, femaleaverage, otheraverage],                                 
    "Total Purchase Value":[maletotal, femaletotal, othertotal]})
genpurchanalysisDF["Average Purchase Price"] = genpurchanalysisDF["Average Purchase Price"].map("${0:,.2f}".format)
genpurchanalysisDF["Total Purchase Value"] = genpurchanalysisDF["Total Purchase Value"].map("${0:,.2f}".format)
genpurchanalysisDF.set_index(["Gender"])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>$2.95</td>
      <td>633</td>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>$2.82</td>
      <td>136</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.25</td>
      <td>11</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics
* The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
* Purchase Count
* Average Purchase Price
* Total Purchase Value


```python
# Bins are 0 to 10, 10 to 14, 15 to 19, 20 to 24, 25 to 29, 30 to 34, 35+
bins = [0, 10, 15, 20, 25, 30, 35, 100]

# Create the names for the bins
group_names = ['< 10', '10 - 14', '15 - 19 ', '20 - 24', '25 - 29', '30 - 34', '35 +']

```


```python
# Cut age and place the scores into bins
# append column at the end of original data frame for age group
purchasedataDF["Age Group"] = pd.cut(purchasedataDF["Age"], bins, labels=group_names)
purchasedataDF.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35 +</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30 - 34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20 - 24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20 - 24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#percentage of players and count of players by bins
#bincount = pd.DataFrame(purchasedataDF["Age Group"].value_counts())
#binpercent = pd.DataFrame((bincount/playercount)*100)

#AgeDF = pd.DataFrame({
#    "Count":bincount,
#    "Percent":binpercent})
#AgeDF
```


```python
#item count per group
groupitemcount = purchasedataDF.groupby("Age Group")["Item Name"].count()
```


```python
#price average per group
grouppriceaverage = purchasedataDF.groupby("Age Group")["Price"].mean()
```


```python
#total purchase per group
groupsumvalue = purchasedataDF.groupby("Age Group")["Price"].sum()
```


```python
#Create new Data Frame with Age Groups Analytics
AgeDemographics = pd.DataFrame({
    "Item Count":groupitemcount,
    "Average Price":grouppriceaverage,
    "Total Revenue":groupsumvalue})

AgeDemographics["Average Price"] = AgeDemographics["Average Price"].map("${0:,.2f}".format)
AgeDemographics["Total Revenue"] = AgeDemographics["Total Revenue"].map("${0:,.2f}".format)
AgeDemographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Item Count</th>
      <th>Total Revenue</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>$2.87</td>
      <td>78</td>
      <td>$224.15</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>$2.87</td>
      <td>184</td>
      <td>$528.74</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>$2.96</td>
      <td>305</td>
      <td>$902.61</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>$2.89</td>
      <td>76</td>
      <td>$219.82</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>$3.07</td>
      <td>58</td>
      <td>$178.26</td>
    </tr>
    <tr>
      <th>35 +</th>
      <td>$2.90</td>
      <td>47</td>
      <td>$136.13</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>$3.02</td>
      <td>32</td>
      <td>$96.62</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders
* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
* SN
* Purchase Count
* Average Purchase Price
* Total Purchase Value


```python
# groupby SN, sum the price, and then reset index
SNtop5sum = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].sum())
SNtop5sum.reset_index(inplace = True)
```


```python
# groupby SN, count the price, and then reset index
SNtop5count = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].count())
SNtop5count.reset_index(inplace = True)
```


```python
# groupby SN, mean of the price, and then reset index
SNtop5mean = pd.DataFrame(purchasedataDF.groupby("SN")["Price"].mean())
SNtop5mean.reset_index(inplace = True)
```


```python
# merge sum and count tables together on SN
mergeSN = pd.merge(SNtop5sum, SNtop5count, on = "SN")

# merge the sum/count frame created with the mean on SN
mergeSN2 = pd.merge(mergeSN, SNtop5mean, on = "SN")

#rename columns accordingly and print top 5
mergeSN2.columns = ["SN","Total Purchase Value", "Total Count","Average Count"]
mergeSN2 = mergeSN2.set_index(["SN"])
mergeSN2.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Total Count</th>
      <th>Average Count</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>6.70</td>
      <td>3</td>
      <td>2.233333</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>5.80</td>
      <td>3</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.27</td>
      <td>1</td>
      <td>1.270000</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items
* Identify the 5 most popular items by purchase count, then list (in a table):
* Item ID
* Item Name
* Purchase Count
* Item Price
* Total Purchase Value


```python
# groupby Item ID, count the price, and then reset index
ItemIDcount = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].count())
ItemIDcount.reset_index(inplace = True)

```


```python
# groupby Item ID, sum the price, and then reset index
ItemIDsum = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].sum())
ItemIDsum.reset_index(inplace = True)

```


```python
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
mergeItemTableDup = mergeItemTableDup.set_index(["Item ID"])
mergeItemTableDup.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items
* Identify the 5 most profitable items by total purchase value, then list (in a table):
* Item ID
* Item Name
* Purchase Count
* Item Price
* Total Purchase Value


```python
# create new table with price, item id, and item name
ProfitTable = pd.DataFrame(purchasedataDF[["Price","Item ID","Item Name"]])
ProfitTableDF = ProfitTable.drop_duplicates()
```


```python
 # groupby  Item ID, count the price, sort by price
ProfitCount = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].count())
ProfitCount.reset_index(inplace = True)
```


```python
# groupby Item ID, sum the price, sort by price
ProfitSum = pd.DataFrame(purchasedataDF.groupby("Item ID")["Price"].sum())
ProfitSum.reset_index(inplace = True)
```


```python
# merge profit table DF and profit counts on Item ID
profitmerge = pd.merge(ProfitTableDF, ProfitCount, on = "Item ID")

# merge profitmerge and profit sums on Item ID
profitmerge2 = pd.merge(profitmerge, ProfitSum, on = "Item ID")

# rename columns
profitmerge2.columns = ["Price", "Item ID", "Item Name", "Purchase Count","Total Purchase Value"]

# sort on Price and print top 5
profitmergeTable = profitmerge2.sort_values(["Price"], ascending = False)
profitmergeTable = profitmergeTable.set_index(["Item ID"])
profitmergeTable.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32</th>
      <td>4.95</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>177</th>
      <td>4.89</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4</td>
      <td>19.56</td>
    </tr>
    <tr>
      <th>103</th>
      <td>4.87</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>173</th>
      <td>4.83</td>
      <td>Stormfury Longsword</td>
      <td>5</td>
      <td>24.15</td>
    </tr>
    <tr>
      <th>42</th>
      <td>4.82</td>
      <td>The Decapitator</td>
      <td>3</td>
      <td>14.46</td>
    </tr>
  </tbody>
</table>
</div>


