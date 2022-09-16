# Carga de librerias

#pip install pyodbc
#pip install mkl-service
#pip install tomopy

import pyodbc

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

from scipy.spatial import distance as sci_distance

from sklearn import cluster as sk_cluster

from sklearn.preprocessing import MinMaxScaler
import os 
os.getcwd()
os.chdir('C:/Users/Luis/Desktop/proyecto')

#import tomopy

## Conexion a la base de datos



# Connection string to connect to SQL Server named instance.

#conn_str = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=LENOVO\SQLEXPRESS; DATABASE=tpcxbb_1gb; UID=<username>; PWD=<password>')

conn_str = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-1JMST4E\LUIS_GS;''Database=neptuno;''Trusted_Connection=yes;')

input_query = '''select *
from clientes_91'''









##################

customer_data = pd.read_sql(input_query, conn_str)


customer_data.isnull().sum() #no tengo valores nulos !!
#data['columna'].fillna(value= valor_que_deseamos,inplace=True)
customer_data.venta_total=customer_data.venta_total.fillna(value=0)
customer_data.promedio_ventas=customer_data.promedio_ventas.fillna(value=0)
#######################



print("Data frame:", customer_data.head(n=5))



##########################

# %%

customer_data=pd.DataFrame(customer_data)
(customer_data.reset_index()).columns

customer_data=(customer_data.reset_index())[['idCliente', 'index', 'numero_pedidos', 'venta_total',
       'promedio_ventas']]

d1=customer_data[['idCliente','numero_pedidos', 'venta_total',
       'promedio_ventas']]
customer_data.head(2)
lista=['numero_pedidos', 'venta_total','promedio_ventas']
customer_data=customer_data[lista]

scaler = MinMaxScaler()
customer_data = scaler.fit_transform(customer_data)
customer_data=pd.DataFrame(customer_data)
customer_data.columns=['numero_pedidos', 'venta_total','promedio_ventas']
# =============================================================================

#%%
## numero de clusters usando el Elbow method





cdata = customer_data

K = range(1, 20)

KM = (sk_cluster.KMeans(n_clusters=k).fit(cdata) for k in K)

centroids = (k.cluster_centers_ for k in KM)



D_k = (sci_distance.cdist(cdata, cent, 'euclidean') for cent in centroids)

dist = (np.min(D, axis=1) for D in D_k)

avgWithinSS = [sum(d) / cdata.shape[0] for d in dist]

plt.plot(K, avgWithinSS, 'b*-')

plt.grid(True)

plt.xlabel('Number of clusters')

plt.ylabel('Average within-cluster sum of squares')

plt.title('Elbow for KMeans clustering')

#plt.show()





## clustering usando Kmeans





n_clusters = 3



means_cluster = sk_cluster.KMeans(n_clusters=n_clusters, random_state=111)

columns = ['numero_pedidos', 'venta_total','promedio_ventas']

est = means_cluster.fit(customer_data[columns])

clusters = est.labels_

#-------------------------------#
### este es el producto final ### 
#-------------------------------#

customer_data['cluster'] = clusters





# For each cluster, count the members.

for c in range(n_clusters):

    cluster_members=customer_data[customer_data['cluster'] == c][:]

    print('Cluster{}(n={}):'.format(c, len(cluster_members)))

    print('-'* 17)

print(customer_data.groupby(['cluster']).mean())





#centroides = means_cluster.cluster_centers_

#print(centroides)
customer_data=customer_data.cluster
customer_data=pd.concat([d1,customer_data],axis=1)
cluster=customer_data
#customer_data.columns
cluster.venta_total.sum()
cluster.head()
#print(customer_data)