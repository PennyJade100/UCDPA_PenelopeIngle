# STEP 1 - Import Data
# Import required Libraries for data cleaning in Python
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean


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

# STEP 2: Data Cleaning
#What type of data are we working with?
print(type(Choc_data))

# Start by displaying a small portion of your database - display top 5 rows
Choc_data.head()

# As an additional preliminary insight - Display bottom 5 rows
print(Choc_data.tail(5))

# Check the shape of the dataset - This will tell us how many rows and columns we have
print(Choc_data.shape)
# There are 2224 rows and 21 columns of data

# Use interating to find the list of column names
for col in Choc_data.columns:
    print(col)

# Keep columns relevant to the analysis and drop the rest
Choc_data1=Choc_data.drop(['ref', 'company','company_location', 'review_date', 'specific_bean_origin_or_bar_name','counts_of_ingredients', 'beans', 'cocoa_butter', 'vanilla', 'lecithin', 'salt', 'sugar', 'sweetener_without_sugar', 'first_taste', 'second_taste', 'third_taste', 'fourth_taste'], axis = 1)
print(Choc_data1.head(1))

#Change column 'Unnamed :0' to 'ID'
Choc_data2=Choc_data1.rename(columns={'Unnamed: 0': 'ID', 'country_of_bean_origin' : 'BeanOrigin', 'cocoa_percent':'CocoaPercent', 'rating':'Rating'})
print(Choc_data2.head(1))

# Check the level of the primary key within the dataset
print(len(Choc_data2.ID.unique()))
# There are 2224 rows and 21 columns of data in Choc_data1
# This column is primary key column

# What datatypes are each of our columns?
print(Choc_data2.dtypes)
# 2no. floats, 1 object/string, & 1 integer types

# Check the new dataframe still contains 2224 rows and 4 rows.
print(Choc_data2.shape)

# Find missing values
missing_values_count = Choc_data2.isnull()
missing_values_count

# Number of missing values in each column - count the no. of null values present
# True = 1 and False = 0 - the isnull.sum sums up all the trues and falses.
missing_values_count = Choc_data2.isnull().sum()
missing_values_count

# Double check : Drop rows which have null values
# check shape of original data set and new data set after dropping
droprows = Choc_data2.dropna()
print(Choc_data2.shape, droprows.shape)
# This confirms no rows were deleted

# Duplicated values need to be removed
drop_duplicates = Choc_data2.drop_duplicates()
print(Choc_data2.shape, drop_duplicates.shape)
# no rows are exactly the same in the dataset - no duplicates

# double check
Choc_data2.drop_duplicates()
print(Choc_data2.shape)
# Still no duplicates

# STEP 3: Data Understanding/Manipulation
# Access only 1no. column
print(Choc_data2["Rating"].head())

#Access only 1no. column second time
print(Choc_data2["BeanOrigin"].head())

# Access top 3 rows and 2 no. Columns - Maker & Rating
print(Choc_data2.loc[:4, ["BeanOrigin", "Rating"]])

print(Choc_data2.ID.unique())

print(type(Choc_data2.loc[0]))

# How many countries of bean origin are there and what are the names of the Countries?
print(Choc_data2.drop_duplicates(subset=["BeanOrigin"]))
#There are a total of 62 different Countries of Origin for the cocao beans

# Create list of all 62 Countries names in Alphabetical order
List_OriginCountries=Choc_data2["BeanOrigin"].unique()
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

print(Choc_data3.shape, Choc_nuts.shape, Choc_data2.shape)
print(Choc_data3.shape)
# 2nd dataframe Choc_nuts contains the same number of rows and 2no. columns
# New merged dataframe, Choc_DataFinal, now has an additional column of information - if nuts are included or excluded.

# What is the lowest & highest rating for the chocolates?
# sort - ascending ratings order
Choc_data3.sort_values(by=["Rating"], inplace=True)
print(Choc_data3.head(3))

# Filter ratings to show only rows with ratings of 4 - the highest rating in the dataset
print(Choc_data3[(Choc_data3["Rating"]>=4)])
# We see that 101 rows of the data contains ratings of 4

# Create new dataframe without changing original which contains only the information pertaining to chocolates rated 4
Choc_Ratings = Choc_data3[(Choc_data3["Rating"]>=4)]
print(Choc_Ratings.head(1))

print(type(Choc_Ratings))

# What country of bean origin's corelate to the ratings of 4?
# Print out country names and how many times each is mentioned.
print(Choc_Ratings['BeanOrigin'].value_counts(ascending=False))

Choc_Ratings2=Choc_Ratings['BeanOrigin'].value_counts(ascending=False)
print(Choc_Ratings2)

Choc_Cocoa=Choc_Ratings['CocoaPercent'].value_counts(ascending=False)
print(Choc_Cocoa)
# 70, 75 & 72 percent are the top 3 no. rated cocoa percentages

# Import the taste dataset csv. file from Local Desktop
Choc_taste= pd.read_csv("chocolate_taste_dataset.csv", encoding = "ISO-8859-1")

# Check what the dataset looks like
Choc_taste.head()

# STEP 4: Data visualisation/manipulation
# What is the Rating distribution of the chocolates
import matplotlib.pyplot as plt
import numpy as np

# What is the Rating distribution of the chocolates
import matplotlib.pyplot as plt
import numpy as np

# Change font stype
plt.rcParams.update({'font.family':'fantasy'})

# unit area ellipse
rx, ry = 3., 1.
area = rx * ry * np.pi
theta = np.arange(0, 2 * np.pi + 0.01, 0.1)
verts = np.column_stack([rx / area * np.cos(theta), ry / area * np.sin(theta)])

X=Choc_data3["Rating"]
Y=Choc_data3["ID"]

fig, ax = plt.subplots()
ax.scatter(X, Y, marker=verts, c='green')
ax.set_xlabel('Chocolate Ratings', labelpad=10,fontsize='15', horizontalalignment='center')
ax.set_ylabel('Chocolate Samples', labelpad=10, fontsize='15', horizontalalignment='center')
ax.set_title('Rating Distribution of Chocolates', pad =20, fontsize='18')

plt.show()

# What are the top 5 countries of cocoa bean production with Premium ratings?
Top_OriginCountries = Choc_Ratings['BeanOrigin'].value_counts().sort_values(ascending=False).head(5)
Top_OriginCountries = pd.DataFrame(Top_OriginCountries)
Top_OriginCountries = Top_OriginCountries.reset_index() # dataframe with top 5 companies

# Change font stype
plt.rcParams.update({'font.family':'fantasy'})

# Plotting (change colour of bar chart to blue hues from seaborn)
sns.set()
plt.figure(figsize=(10,4))
sns.barplot(x='index', y='BeanOrigin', data=Top_OriginCountries, palette="Blues_d")
plt.xlabel("\nCocoa Bean Origin Country", fontsize='15', horizontalalignment='center')
plt.ylabel("No. of Chocolates Rated 4", fontsize='15', horizontalalignment='center')
plt.title("Top 5 Countries of Cocoa Bean Origin (Premium Rating)\n", fontweight='bold', fontsize='18', horizontalalignment='center')
plt.show()

# What does the distribution of the cocoa content look like among the chococlates rated 4

Percent_mean= Choc_Ratings["CocoaPercent"].mean()
Std_Dev=Choc_Ratings['CocoaPercent'].std()
x = Percent_mean + Std_Dev * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * Std_Dev)) *
     np.exp(-0.5 * (1 / Std_Dev * (bins - Percent_mean))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('% Cocoa', fontsize='15', labelpad=10)
ax.set_ylabel('Standard Deviation', fontsize='15', labelpad=10)
ax.set_title(r'Distribution of Cocoa Percent', fontsize='17', pad=20)

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

Choc_Cocoa=Choc_Ratings['CocoaPercent'].value_counts(ascending=False)
print(Choc_Cocoa.head(3))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# what are the 5 most popular flavours tested by taste tests?

plt.rcParams.update({'font.family':'fantasy'})

Top_tastes=Choc_taste.nlargest(5,'count_of_taste')
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice

labels = Top_tastes['taste']
sizes = Top_tastes['count_of_taste']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Top 5 Most Popular Flavours", fontsize="17", pad=20)
plt.show()


