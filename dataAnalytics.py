import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# FIRST HISTOGRAM - Sample data
sample_data = [10, 20, 15, 30, 22, 18, 28, 35, 40, 25, 30, 28, 22, 18, 15]
plt.hist(sample_data, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Data')
plt.show()

# SECOND HISTOGRAM - Using seaborn's iris dataset
df_seaborn = sns.load_dataset('iris')
data = df_seaborn['sepal_length']
plt.hist(data, bins=15, color='skyblue', edgecolor='black', density=True, alpha=0.6)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Density')
plt.title('Histogram of Sepal Length (Seaborn Iris Dataset)')
plt.show()

# KDE Plot - Using sklearn iris dataset
iris = load_iris()
df_sklearn = pd.DataFrame(iris.data, columns=iris.feature_names)
data = df_sklearn[iris.feature_names[2]]  # petal length (cm)
kde = gaussian_kde(data)
x_vals = np.linspace(data.min(), data.max(), 100)

plt.plot(x_vals, kde(x_vals), color='red', label='KDE')
plt.fill_between(x_vals, kde(x_vals), color='orange', alpha=0.3)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.title('KDE of Petal Length (sklearn Iris Dataset)')
plt.legend()
plt.show()

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Compute mean and std for sepal length (feature 0)
means = df.groupby('species')[iris.feature_names[0]].mean()
stds = df.groupby('species')[iris.feature_names[0]].std()

# Plot error bars
plt.errorbar(means.index, means.values, yerr=stds.values, fmt='o', capsize=5)
plt.title("Error Bar Plot - Sepal Length")
plt.ylabel("Length (cm)")
plt.xlabel("Species")
plt.grid(True)
plt.show()

#new

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step plot for first 20 values of sepal length vs sepal width
plt.step(df[iris.feature_names[0]][:20], df[iris.feature_names[1]][:20], where='mid', color='green')
plt.title("Step Plot: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")



# df.pd.DataFrame(iris.data , column=iris.feature_names)
# df['species'] =iris.target_names[iris.target]

# for i , sp in enumerate(iris.target_names):
#   d = df[df['specise'] == sp][iris.feature_names[0]]
#   kde = gaussian_kde(d)
#   x_vals = np.linspace(d.min(), d.max(), 100)
#   y_vals= kde(x_vals)
#   # plt.plot(x_vals, kde(x_vals), label=sp)
#   plt.fill_between(x_vals, i-y_vals , i+y_vals ,   alpha=0.6)
#   plt.xticks(range(3) , iris.target_names)
#   plt.show()


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# KDE plot for each species (stacked vertically)
plt.figure(figsize=(8, 6))
for i, sp in enumerate(iris.target_names):
    d = df[df['species'] == sp][iris.feature_names[0]]  # sepal length
    kde = gaussian_kde(d)
    x_vals = np.linspace(d.min(), d.max(), 100)
    y_vals = kde(x_vals)

    # Fill between for KDE curve vertically offset by species index
    plt.fill_between(x_vals, i - y_vals, i + y_vals, alpha=0.6, label=sp)

# Set y-ticks to species names
plt.yticks(range(3), iris.target_names)
plt.xlabel(iris.feature_names[0].capitalize())
plt.title("KDE Density Plot (Vertically Offset) by Species")
plt.legend()
plt.grid(True)
plt.show()

df= pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[ iris.target]
for i , sp in enumerate(iris.target_names):
  d = df[df['species'] == sp][iris.feature_names[0]]
  jitter = np.random.uniform(-0.1 , 0.1 , size=len(d))
  plt.scatter(np.full_like(d,i)+jitter , d ,alpha=0.6)
plt.xticks(range(3) , iris.target_names)
plt.title("swrm Plot - sepal Length")
plt.show()

  # x_vals = np.linspace(d.min(), d.max(), 100)


df= pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[ iris.target]
for i , sp in enumerate(iris.target_names):
  d = df[df['species'] == sp][iris.feature_names[0]]
  plt.scatter(np.full_like(d,i) ,d ,alpha=0.6)
plt.xticks(range(3) , iris.target_names)
plt.title("swrm Plot - sepal Length")
plt.show()

# Rug plot
df = pd.DataFrame(iris.data, columns=iris.feature_names)
data = df[iris.feature_names[1]]
plt.plot(data, np.zeros_like(data), '|', markersize=10)
plt.title("Rug plot")
plt.yticks([])
plt.show()

import seaborn as sns
print(sns.__version__)

iris = sns.load_dataset('iris')
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.show()

# x=np.arange(1,11)
# y1=2*x
# y2=3*x

# df = pd.DataFrame({
#     'x'  : np.concenrate([y1 ,y2]),
#     'label' : ['y=2x']*len(x) + ['y=3x']*len(x)
# })
# sns.set(style="whitegrid") #dark
# sns.lineplot(data=df, x='x', y='y', hue='label' , style='label' , market=True , linewidth=2.5)

# plt.title("Lne Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.xtick(np.arange(1,11))
# plt.yticks(np.arrange(2,31,2))
# plt.show()

# # plt.show()


x = np.arange(1, 11)
y1 = 2 * x
y2 = 3 * x

# Create DataFrame
df = pd.DataFrame({
    'x': np.concatenate([x, x]),  # Use x twice
    'y': np.concatenate([y1, y2]),
    'label': ['y=2x'] * len(x) + ['y=3x'] * len(x)
})

# Set Seaborn style
sns.set(style="whitegrid")

# Plot lineplot
sns.lineplot(data=df, x='x', y='y', hue='label', style='label', markers=True, linewidth=2.5)

# Add labels and title
plt.title("Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xticks(np.arange(1, 11))
plt.yticks(np.arange(2, 31, 2))
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.lineplot(data=iris , x="sepal_length" , y="sepal_width")
# plt.title("Line Plot:Sepal Length vs Sepal Width")
# plt.xlabel("Sepal Length(cm)")
# plt.ylabel("Sepal Width(cm)")
plt.show()

sns.lineplot(data=iris , x="sepal_length" , y="sepal_width" , sort=False
             )
# plt.title("Line Plot:Sepal Length vs Sepal Width")
# plt.xlabel("Sepal Length(cm)")
# plt.ylabel("Sepal Width(cm)")
plt.show()

sns.lineplot(data=iris , x="sepal_length" , y="sepal_width" , sort=False ,
             hue="species")
# plt.title("Line Plot:Sepal Length vs Sepal Width")
# plt.xlabel("Sepal Length(cm)")
# plt.ylabel("Sepal Width(cm)")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#BAR PLOT H YAHA SE..

df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [12,7,15,9]

})
sns.barplot(x='Category' , y='Value' , data=df)
plt.show

sns.barplot(x='species' , y='sepal_length' , data=iris , estimator='mean')
plt.show()

sns.barplot( data=iris , x='species' , y='sepal_length'  , estimator='max')
#upper wali line me kaise
plt.title("Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Sepal Length(cm)")
plt.show()

sns.barplot( data=iris , x='species' , y='sepal_length'  )
#upper wali line me kaise
plt.title("Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Sepal Length(cm)")
plt.show()

fig , axes = plt.subplots(1 , 2 , figsize = (12 , 5))

sns.barplot(x='species' , y='sepal_length' , data=iris , ax=axes[0])
axes[0].set_title("sepal length")

sns.barplot(x='species' , y='sepal_width' , data=iris , ax=axes[1])
axes[1].set_title("sepal width")

# plt.tight_layout()
plt.show()

fig , axes = plt.subplots(2 , 2 , figsize = (12 , 5))
sns.barplot(x='species' , y='sepal_length' , data=iris , ax=axes[0 ,0])
axes[0 ,0].set_title("sepal length")

sns.barplot(x='species' , y='sepal_width' , data=iris , ax=axes[0 ,1])
axes[0 ,1].set_title("sepal Width")

sns.barplot(x='species' , y='petal_length' , data=iris , ax=axes[1,0])
axes[1 ,0].set_title("Petal length")

sns.barplot(x='species' , y='petal_width' , data=iris , ax=axes[1,1])
axes[1 ,1].set_title("Petal width")

# plt.tight_layout() #padding atomatically adjust kr deta h..
plt.show()

data = pd.DataFrame({
    'Category':['A' , 'B' , 'C' , 'D'],
    'Value': np.random.randint(10 , 100 , size=4)
})
# sns.barplot(x='Category' , y='Value' , data=data)
sns.barplot(x='Category' , y='Value' , color='skyblue' , edgecolor='black' , data=data)

plt.title("Bar Plot with Custom Colors")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()

data = pd.DataFrame({
    'Category':['A' , 'B' , 'C' , 'D'],
    'Value': np.random.randint(10 , 100 , size=4)
})
# sns.barplot(x='Category' , y='Value' , data=data)
sns.barplot(x='Category' , y='Value' , color='red' , edgecolor='black' , data=data)

plt.title("Bar Plot with Custom Colors")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()

data = pd.DataFrame({
    'Category':['A' , 'B' , 'C' , 'D'],
    'Value': np.random.randint(10 , 100 , size=4)
    #it just take 4 random values in between 10 to 100..
    # than plot a graph for that..
})
# sns.barplot(x='Category' , y='Value' , data=data)
sns.barplot(x='Category' , y='Value' , color='yellow' , edgecolor='black' , data=data)

plt.title("Bar Plot with Custom Colors")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()



categories =['A','B' ,'C']
group1 =np.array([20 , 35 , 30])
group2 =np.array([25 ,32 ,34])
x=np.arange(len(categories))
fig , ax=plt.subplots()
ax.bar(x , group1 , color='skyblue', label='Group1') #width=0.4
ax.bar(x , group2 , color='salmon', label='Group2')

# iske aage ka optional h..jo likha h likho
ax.set_xticks(x )
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Plot')
ax.legend()
plt.show()
# width=0.35

# fig , ax = plt.subplots()

sns.histplot(data=iris , x='sepal_length' , hue='species' , kde=True , bins=10)
plt.show()

sns.histplot(data=iris , x='sepal_length'  , kde=True , bins=10)
plt.show()

sns.histplot(data=iris , x='sepal_length'  , kde=False , bins=10)
plt.show()

sns.histplot(data=iris , x='sepal_length' , bins=10)
plt.show()

sns.boxplot(data=iris , x='species' , y='sepal_length')
plt.title("Box Plot - Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()

maths =['jan' , 'feb' , 'mar' , 'Apr' , 'may' , 'jun']
temperature= [5 , 7 ,12 , 18 , 24 , 29]
rainfall = [78 , 60 ,45, 20 ,25 , 35]

x=np.arange(len(months))
fig,ax1 =plt.subplots()
ax1.plot(x , temperature , color='red' ,marker='o' , label='temperature(*C)')
ax1.set_xlabel('Months')
ax1.set_ylabel('Temperature(*C)' , color='red')
ax1.tick_params(axis='y' , labelcolor='red')
ax1.set_xticks(x)
ax1.set_xticklabels(months)  # rotation=45

ax2=ax1.twinx()

ax2.bar(x , rainfall , color='skyblue' , label='Rainfall(mm)')
ax2.set_ylabel('Rainfall(mm)' , color='skyblue')
ax2.tick_params(axis='y' , labelcolor='skyblue')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset("iris")

x = iris.index[:20]
y = iris["sepal_length"][:20]

# create stemp like plot
plt.figure(figsize=(8,5))
plt.vline(x ,ymin=0 , color='teal' , linewidth=2)
sns.scatterplot(x=x , y=y , color='crimson' , s=60 , marker = 'o')

plt.title("Step Plot - Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset("iris")

x = iris.index[:20]
y = iris["sepal_length"][:20]

# create stem-like plot
plt.figure(figsize=(8, 5))
plt.vlines(x, ymin=0, ymax=y, color='teal', linewidth=2)  # corrected: plt.vlines
sns.scatterplot(x=x, y=y, color='crimson', s=60, marker='o')

plt.title("Stem Plot - Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

# data_Analytics
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tip = sns.load_dataset('tips')
tip

# iske baad sbse pehle info check krte h..
# caterogical feature pta kro
# numerical feature kaise filture kroge
# data kis baare me h
# data smjho pehle
# column smjho pehle

tip.info()

tip.select_dtypes(include='object').columns

tip.describe()

tip.select_dtypes(include=['object', 'category']).columns

# day , time  , sex , smoker => catogorical features

# Shows only object or category columns (categorical features)
categorical_columns = tip.select_dtypes(include=['object', 'category']).columns
print("Categorical Features:\n", categorical_columns)

categorical_columns = tip.select_dtypes(include=['object' , 'category']).columns
for i in categorical_columns:
  print(tip[i].value_counts())

#koi bhi missing values h ki ni h
# outliers dekhnege..

sns.catplot(x="day" , y="total_bill" , hue="sex" , kind="swarm" , data=tip)
#it  is to analyse categorical features
#hue and kind change krkr saare plot bna skte h

sns.pairplot(tip , hue="sex")
plt.show()
# piar plot is for analysing numerical features
# total bill ka male or females ke liye
# numerical me bhi discreate , continues values

sns.pairplot(tip , hue="day")
plt.show()

sns.pairplot(tip , hue="smoker")
plt.show()

# facet plots - multiple subplots based on categories
facet =sns.FacetGrid(tip , col='sex')
# facet.map(sns.histplot , 'total_bill')
facet.map(plt.hist , 'total_bill')
plt.show()


# multiple cheezo ko apne aap compare

facet =sns.FacetGrid(tip , col='sex')
# facet.map(sns.histplot , 'total_bill')
facet.map(plt.kde , 'total_bill')
plt.show()

facet =sns.FacetGrid(tip , col='day')
# facet.map(sns.histplot , 'total_bill')
facet.map(plt.hist , 'total_bill')
plt.show()

facet =sns.FacetGrid(tip , col='sex')
facet.map(plt.hist , 'tip')
plt.show()

facet =sns.FacetGrid(tip , col='smoker')
facet.map(plt.hist , 'total_bill')
plt.show()

# regression plot

sns.regplot(x="total_bill" , y="tip" , data=tip )
plt.show()

iris_dataset=sns.load_dataset("iris")
sns.regplot(x="sepal_length" , y="sepal_width" , data=iris_dataset)
plt.show()

# -ve slope ki  line h
# -ve regression / correlation

#QUE: how tip data amount relateds to total_bill.

# soln: scatter plot , line  , regression plot

sns.regplot(x="total_bill" , y="tip" , data=tip)
plt.show()

# prompt: scatter plot for total bill vs tip

import matplotlib.pyplot as plt
sns.scatterplot(x='total_bill', y='tip', data=tip)
plt.title('Scatter Plot of Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

# whetehr sex or smoker status infuences tiping behaviour

# compare krne ke liye kon sa plot -- box and bar plot

# box plot
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.boxplot(x='sex' ,y='tip' , data=tip)

plt.subplot(1,2,2)
sns.boxplot(x='smoker' , y='tip' , data=tip)
plt.show()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.boxplot(x='sex' ,y='tip' , data=tip)

plt.subplot(1,2,2)
sns.boxplot(x='smoker' , y='tip' , data=tip)
plt.tight_layout()
plt.show()

sns.barplot(data=tip , x="sex" , y="tip" , estimator='mean' , errorbar="sd")
plt.ylabel("Tip Amount")
plt.show()

sns.barplot(data=tip , x="smoker" , y="tip" , estimator='mean' , errorbar="sd")
plt.ylabel("Tip Amount")
plt.show()

#3 cheezo ko ek saath bhi  compare kr skte h

sns.boxplot(data=tip , x="smoker" , y="tip" ,hue="sex")

plt.show()

# bar box scatter heat histogram kde
# pandas ki analysis
# merge info describe
# head tail indexing
# python:loop , list
sns.lmplot(data=tip , x="total_bill" , y="tip" , aspect=1.5 , height=5)
# regression plot ka more inhanced version..
plt.show()

sns.lmplot(x='total_bill' , y='tip' , data=tip , hue='sex')
plt.show()

sns.lmplot(x='total_bill' , y='tip' , data=tip , hue='smoker' , col='time')
plt.show()

# all 7 feature nikalene
# nimerical ka box plot se ya reg. plot se histogram se  lmplot
# categorical ka countplot

sns.countplot(x='sex' , data=tip)
plt.show()

numeric_data = tip.select_dtypes(include='number')
corr_matrix = numeric_data.corr()

sns.set(style="whitegrid")
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix , annot=True , cmap='coolwarm' , center=0 , linewidths=0.5 , square=True)
plt.title("Correlation Heatmap")
plt.show()
