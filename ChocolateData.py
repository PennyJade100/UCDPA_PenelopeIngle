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

