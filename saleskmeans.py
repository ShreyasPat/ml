import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
----------------------
df = pd.read_csv("sales_data_sample.csv", sep=",", encoding='Latin-1')
df
----------------
df.info()
----------------
df.isnull().sum()
--------------
df.describe()
----------------
X = df.iloc[:, [3,4]].values
----------------
wcss = []   #within cluster sum of square

for i in range(1,11):
    #init argument is the method for initializing the centroid
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    #we calculate wcss value for each k value
    wcss.append(kmeans.inertia_)
    
ks = [1,2,3,4,5,6,7,8,9,10]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow method")
plt.xticks(ks)
plt.xlabel("K value")
plt.ylabel("WCSS")
--------------------
# mean is far from std this indicates high variance 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
scaled = ss.fit_transform(X)
------------------------
wcss =[]

for i in range(1,11):
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42)
    clustering.fit(scaled)
    wcss.append(clustering.inertia_)
    
ks = [1,2,3,4,5,6,7,8,9,10]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow method")
plt.xticks(ks)
plt.xlabel("K value")
plt.ylabel("WCSS")
-----------------------
