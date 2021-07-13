# Import required Libraries for data cleaning in Python
import pandas as pd
import numpy as np
import os

# Find working directory for project
os.getcwd()

# Set working directory to Local project folder on Desktop
os.chdir(r"C:\Users\35387\Desktop\Diploma Data Analysis\Project Assignment")

# Check new working directory is correct
os.getcwd()

# Suppress warning in Jupyter Notebook
import warnings
warnings.filterwarnings("ignore")

# Import the database csv. file from Local Desktop
# Use pandas for DataFrames instead of numpy arrays due to the multiple data types (integers, floats & strings)
# and a large set of data
Choc_data = pd.read_csv("chocolate.csv", encoding = "ISO-8859-1")

# Step 3: Data Understanding
# Start by displaying a small portion of your database - display top 5 rows
print(Choc_data.head())

# Let's assess further with displaying top 10 row
print(Choc_data.head(10))

# As an additional preliminary insight - Display bottom 5 rows
print(Choc_data.tail(5))

# Check the shape of the dataset - This will tell us how many rows and columns we have
print(Choc_data.shape)
# There are 2224 rows and 21 columns of data

# What type of data are we working with?
print(type(Choc_data))

# Use indexing to find out what the names of the Columns are (which correlate to the above dataset displays)
Choc_data.columns

# List of column names
for col in Choc_data.columns:
    print(col)

#Change column 'Unnamed :0' to 'ID'
Choc_data1=Choc_data.rename(columns={'Unnamed: 0': 'ID'})
print(Choc_data1.head(1))

# Check the level of the primary key within the dataset
print(len(Choc_data1.ID.unique()))
# There are 2224 rows and 21 columns of data in Choc_data1
# We can see the number of rows in column "ID" correlates to the number of columns shown in the Choc_data1 -
# This column is primary key column

# What datatypes are each of our columns?
Choc_data1.dtypes
# We have mostly objects (strings) columns, 4no. interger column & 2no. float column

# Step 4: Data Subsetting
print(type(Choc_data1))

# View current column names
cols=list(Choc_data1.columns.values)
print(cols)

#Rename column heading for easier reading
Choc_data1.columns=['ID','Ref','Maker', 'MakerLocation', 'ReviewDate', 'BeanOrigin_Country', 'BarName', 'CocoaPercent', 'Rating', 'IngredientCount','Beans','CocoaButter', 'Vanilla', 'Lecithin', 'Salt', 'Sugar', 'Sweetner', 'Taste1', 'Taste2','Taste3', 'Taste4']
Choc_data2=Choc_data1
print(Choc_data2.head(1))

## Access only 1no. column
print(Choc_data2["Rating"].head())

## Access only 1no. column second time
print(Choc_data2["BeanOrigin_Country"].head())

## Access top 3 rows and 2 no. Columns - Maker & Rating
print(Choc_data2.loc[:4, ["BeanOrigin_Country", "Rating"]])

print(Choc_data2.ID.unique())

# Lets find all the values in the column (Maker)
print(Choc_data2.loc[:, ["Maker"]])

print(type(Choc_data2.loc[0]))

# Find missing values
missing_values_count = Choc_data2.isnull()
print(missing_values_count)

# ForthTaste has a high percent of null values in rows
# Drop rows which have null values
# check shape of original data set and new data set after dropping
droprows = Choc_data2.dropna()
print(Choc_data2.shape, droprows.shape)
#This confirms 1982 rows were deleted from the dataset

# drop these columns
dropcolumns = Choc_data2.dropna(axis=1)
print(Choc_data2.shape, dropcolumns.shape)
# keeps all rows but eliminates the null values columns (3no. - SecondTaste, ThirdTaste, ForthTaste)

print(Choc_data2.head())
# Can now see the NaN values

# fill all missing values with zero (0)
cleaned_data=Choc_data2.fillna(0)
print(cleaned_data.isnull().sum())

# Cannot clean data with mean, median or mode - these columns do not have integers or floats
# Fill all missing values to the value that comes next in the same column
cleaned_data = Choc_data2.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_data.isnull().sum())

# Duplicated values need to be removed
drop_duplicates = Choc_data2.drop_duplicates()
print(Choc_data2.shape, drop_duplicates.shape)
# no rows are exactly the same in the dataset - no duplicates

Choc_data2.drop_duplicates()
print(Choc_data2.shape)
#Still no duplicates - as above, so maybe delete this entry.

# How many countries of bean origin are there and what are the names of the Countries?
print(Choc_data2.drop_duplicates(subset=["BeanOrigin_Country"]))
#There are a total of 62 different Countries of Origin for the cocao beans

# Create list of all 62 Countries names in Alphabetical order
List_OriginCountries=Choc_data2["BeanOrigin_Country"].unique()
print(sorted(List_OriginCountries))

# What are the available percentages of cocao in the chocolates on the market? Short them in ascending order.
List_Cocoa_Percents=Choc_data2["CocoaPercent"].unique()
print(sorted(List_Cocoa_Percents))

# How many different percentages are there on the market?
Count_percentages=Choc_data2["CocoaPercent"].nunique()
print(Count_percentages)

# Half way through project i realised i did not have a second file to merge with the main dataframe.
# I created a dummy file in excel which lists random 0's and 1's for the question: Does the chocolate contains nuts
# Import the database csv. file from Local Desktop
Choc_nuts = pd.read_csv("chocolate_nuts.csv", encoding = "ISO-8859-1")
print(Choc_nuts.head())

Choc_data3 = pd.merge(Choc_data2,Choc_nuts,on="ID") #inner join
print(Choc_data3.head(2))

print(Choc_data3.shape, Choc_nuts.shape)
print(Choc_data3.shape)
# 2nd dataframe Choc_nuts contains the same number of rows and 2no. columns
# New merged dataframe, Choc_DataFinal, now has an additional column of information - if nuts are included or excluded.

#The columns of interest to us are the ID, Rating, BeanOrigin_Country, CocoaPercent
# .loc[] always returns a copy so the original dataframe is never modified.
Choc_DataFinal = Choc_data3.loc[:, ['ID', 'BeanOrigin_Country', 'Rating', 'CocoaPercent', 'Taste1', 'Taste2', 'Taste3', 'Taste4']]

# What is the lowest & highest rating for the chocolates?
# sort - ascending ratings order
Choc_DataFinal.sort_values(by=["Rating"], inplace=True)
print(Choc_DataFinal.head(3))

print(Choc_DataFinal.tail(3))

# Filter ratings to show only rows with ratings of 4 - the highest rating in the dataset
print(Choc_DataFinal[(Choc_DataFinal["Rating"]>=4)])
# We see that 101 rows of the data contains ratings of 4

# not sure why i put this in
print(Choc_DataFinal.iloc[1])

# Create new dataframe without changing original which contains only the information pertaining to chocolates rated 4
Choc_Ratings = Choc_DataFinal[(Choc_DataFinal["Rating"]>=4)]
print(Choc_Ratings.head(1))

print(type(Choc_Ratings))

# What country of bean origin's corelate to the ratings of 4?
# Print out country names and how many times each is mentioned.
print(Choc_Ratings['BeanOrigin_Country'].value_counts(ascending=True))

# Madagascar, Peru and Venezuela are the top rating countries for bean origin.
# What cocoa percentage relates to a rating of 4
print(Choc_Ratings['CocoaPercent'].value_counts(ascending=True))

# 72, 75 & 70 percent are the top rated cocoa percentages
Choc_Cocoa=Choc_Ratings['CocoaPercent'].value_counts(ascending=True)
# input rows which correlate to cocoa percentages of 70, 72 & 75
#Top_Cocoa=Choc_Cocoa

print(Choc_Ratings['Taste1'].value_counts(ascending=True))

print(Choc_Ratings['Taste2'].value_counts(ascending=True))



print(Choc_Ratings['Taste3'].value_counts(ascending=True))

print(Choc_Ratings['Taste4'].value_counts(ascending=True))

# Need to sum the number of times each of the taste types is mentioned in all four taste columns
Choc_Tastes = Choc_Ratings.filter(['Taste1','Taste2','Taste3','Taste4'], axis=1)
print(Choc_Tastes.head())

