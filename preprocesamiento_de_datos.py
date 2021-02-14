# -*- coding: utf-8 -*-
"""Modelado red social personal

#Codigo de limpieza de lista de datos telefonicos
listT=ListUSR.iloc[:,1]#lista de numeros
listT= [str(x) for x in listT] #transforma la lista de interos en lista de cadenas
listT= [item.replace("-","") for item in listT] #elimina guiones de los numeros
listT= [item.replace(" ","") for item in listT] #elimina espacios de los numeros

for item in listT:
  if len(item)<10:
    listT.remove(item) 
  if len(item)>10:
    listT.remove(item)

for item in listT:
  if item.startswith('+'):
    codigo=item[0:3]
    if codigo != '+57':
      listT.remove(item)
    
      
for item in listT:
  if item[0]!="3" and item[0] != "+":
      listT.remove(item)

listT=set(listT) #elimina los duplicados

