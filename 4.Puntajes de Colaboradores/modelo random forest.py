import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# Sklearn
from sklearn.model_selection import train_test_split
# Modulos de arbol de decision
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
#regresion logistica 
from sklearn.linear_model import LogisticRegression
# modelo de regresion 
from sklearn.linear_model import LinearRegression
# random forest
from sklearn.ensemble import RandomForestRegressor
# Metricas
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import os
os.chdir('C:/Users/Luis/Desktop/proyecto_DataScienceHR/')
help(pd.read_excel)
df=pd.read_excel("Base de Datos.xlsx",sheet_name="BD")
df.columns
df.isna().sum()
df1=df.copy()
df1=df1.drop(columns=['Cod'],axis=1)
df1.columns
y1=df1['Puntaje Final']
x1=df1.drop('Puntaje Final',axis=1)

x1.columns

# Particionamos
x1_train, x1_test, y1_train, y1_test= train_test_split(x1,
                                                   y1,
                                                   test_size=0.25,
                                                   random_state=1
                                                   )

# %%

#------------------------
#  arbol regresion !!!
#------------------------

# INstanciamos la clase para el modelado 
arbol_regre=DecisionTreeRegressor(random_state=2022)


# Siguiente paso : Ajustar el modelo 
arbol_regre.fit(x1_train, y1_train)

# Score del modelo para los datos de testeo
arbol_regre.score(x1_test, y1_test)

# R Coeficiente de determinacion:0.8695775711422259
#--------------------------------------------------

yPronostico = arbol_regre.predict(x1_test)

MAPE_arbol= metrics.mean_absolute_percentage_error(y1_test, yPronostico)
print("Mape arbol de regresion",MAPE_arbol)
# MAPE es: 0.08240824546063434


# %%

#-------------------
#  random forest !!!
#-------------------

# INstanciamos la clase para el modelado 
rdn=RandomForestRegressor(random_state=2022)


# Siguiente paso : Ajustar el modelo 
rdn.fit(x1_train, y1_train)

# Score del modelo para los datos de testeo
rdn.score(x1_test, y1_test)

# R Coeficiente de determinacion:0.8625603458715031
#--------------------------------------------------

yPronostico = rdn.predict(x1_test)

MAPE_rdn= metrics.mean_absolute_percentage_error(y1_test, yPronostico)
print("Mape random forest",MAPE_rdn)
# MAPE es: 0.043881773942967876

# %%

#~~~~~~~~~~~#
# longitud  #
#~~~~~~~~~~~#
print("x_test",len(x1_test))
print("x1_train",len(x1_train))
print("x1",len(x1))

# x_test 100
# x1_train 299
# x1 399


#%%

#---------------------------#
# Variables mas importantes #
#---------------------------#

# paso 1 rdn : random forest !!!
#-------

importancia=list(rdn.feature_importances_)   #>>>>>>>>>>>> lista 
x1_test.columns                              #>>>>>>>>>>>> lista

len(importancia)
len(x1_test.columns)

tablita = pd.DataFrame({'Model': x1_test.columns, 'importancia': importancia})
                                #lista                       #lista


tablita.sort_values('importancia')

# paso 2 ordenando por importancia
#-------

tablita.sort_values('importancia',ascending=False)
tablita_importancia=tablita.sort_values('importancia',ascending=False)
# %% 

#----------------------------------------------------------#
# comparacion "Puntaje Final" con "Puntaje Final predicho" #
#----------------------------------------------------------#


print("x1",len(x1))
#~~~~~~~~~~~~~#
# prediciendo #
#~~~~~~~~~~~~~#
df1["Puntaje Final predicho"]=rdn.predict(x1)
df1.columns
lista=['Puntaje Final', 'Puntaje Final predicho']
df1[lista].head(8)
# x_test 100
# x1_train 299
# x1 399


#%% 

#--------------------#
# Exportando la data # lo que me interesa !!
#--------------------#

df1.columns
df.Cod.head(2)
# unimos el indice ! 

df2=pd.concat([df.Cod,df1],axis=1)
df2.columns

df2.to_excel("data_final.xlsx")
tablita_importancia.dtypes
# Model           object
# importancia    float64
# dtype: object
tablita_importancia=pd.DataFrame(tablita_importancia)
tablita_importancia.to_excel("data_final_variables_importante.xlsx")


#%% 

#---------------------------------#
# Pronosticando Nuevas Instancias # 
#---------------------------------#
os.chdir('C:/Users/Luis/Desktop/proyecto_DataScienceHR/')
help(pd.read_excel)
nuevos=pd.read_excel("data_final.xlsx",sheet_name="pronosticando_nuevas_instancias")
nuevos.head(2)
predicho=rdn.predict(nuevos)
predicho
