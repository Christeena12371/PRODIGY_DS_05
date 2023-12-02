#!/usr/bin/env python
# coding: utf-8

# # PRODIGY INFOTECH 

# ## TASK-5

# ### Analyze traffic accident data to identify patterns related to road conditions,weather, and time of day. Visualize accident hotspots and contributing factors. 

# In[32]:


#Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[5]:


#Load the data 
Data=pd.read_csv("C:/Users/steph/Downloads/uk.csv")
Data


# In[6]:


#Create a dataframe
df=pd.DataFrame(Data)
df


# In[8]:


#First 5 rows of the dataset
df.head()


# In[10]:


#Last 5 rows of the dataset
df.tail()


# In[11]:


#Check for all the columns of the dataset
df.columns


# In[12]:


#Check for the number of rows and columns of the dataset
df.shape


# In[13]:


#Check for the information ,i.e, dtype and null value for each column
df.info


# In[14]:


#Check for Statistical Analysis
df.describe


# In[15]:


#Datatype of each column
df.dtypes


# ##  DATA CLEANING

# In[16]:


#Check for the null values
print(df.isnull().sum())


# In[17]:


#Remove unnecesary columns
df1=df.drop(['Location_Easting_OSGR','Longitude',
            'LSOA_of_Accident_Location','Pedestrian_Crossing-Human_Control',
            'Pedestrian_Crossing-Physical_Facilities'],axis=1)
df1


# In[18]:


#New dataframe without unnecesary columns
print(df1.isnull().sum())


# ## DATA VISUALIZATION

# In[22]:


#Accident rates by year

year=df1["Year"]
years=df1["Year"].unique()
num=year.values

sns.barplot(x=year, y= num,color='blue')
plt.title("Number of Traffic Accidents per year")
plt.xlabel("Years")
plt.ylabel("Number of Accidents")


# In[23]:


#Accident rates by week
week = df1["Day_of_Week"].value_counts()
week
weeks = df1["Day_of_Week"].unique()
num_weeks = week.values
sns.barplot(x=weeks,y=num_weeks,color='green')
plt.title("Number of Traffic Acciddetns By Weekdays")
plt.xlabel("Number of Accidents")
plt.ylabel("Weekdays")


# In[28]:


#Accident rates due to road conditions
road_conditions = df1["Road_Surface_Conditions"].value_counts()
road_conditions_values = df1["Road_Surface_Conditions"].unique()

figure(figsize=(10, 10), dpi=80)
plt.pie(road_conditions,labels = road_conditions_values,autopct="%1.1f%%",wedgeprops={'edgecolor':'black'},
        startangle=90)
plt.tight_layout()
plt.legend()
plt.title("How Do Weather Events Impact Roads")
plt.show()


# In[30]:


#Accident rates due to weather conditions
weather_cond = df1["Weather_Conditions"].value_counts() 
weather_cond_values= df1["Weather_Conditions"].unique()
weather_num_acc_arr = weather_cond.values

figure(figsize=(10, 10), dpi=80)
plt.pie(weather_cond, labels = weather_cond_values,startangle = 30,textprops={'size': 'large'},explode=(0.01,0.01,0.01,0.01,0.01,0.20,0.3,0.50,0.7),autopct="%1.1f%%")
plt.legend(loc ="lower left")
plt.title("Accident Rate by Weather Condition")


# In[31]:


#Accidents rates in urban and rural areas
plt.style.use('fivethirtyeight')
df1["Urban_or_Rural_Area"].value_counts().plot(kind='bar')
plt.ylabel("Number of Accidents")
plt.xlabel("Urban(1) or Rural(2) Area")
plt.title("Urban Area vs Rural Area")


# In[9]:


#Number of injured in accidents and the severity of accidents
sns.barplot(x="Year",y="Number_of_Casualties",data=df1,hue="Accident_Severity")
plt.title("Accident_Severity")
plt.ylabel("Number of Casualties")
plt.legend(loc="upper right")
plt.show()

