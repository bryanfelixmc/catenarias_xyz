import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
data1=pd.read_excel(r'D:\python_bryan\python_programs\catenaria\libro1.xlsx', sheet_name='Hoja1')
df=pd.DataFrame(data1)

df_Poste=np.array(df['Poste'])

fig = plt.figure(figsize=plt.figaspect(0.4))

#Para grafico 3d
ax1 = fig.add_subplot(1,2,1,projection='3d')
aux_boolean=True
for elem in df_Poste:
    df=df[df['Poste']==elem]
    #Dibujar postes 3D
    x = [df['x'],df['x']]
    y = [df['y'],df['y']]
    z = [df['z'],df['z']+df['Altura']]
    ax1.plot(x, y, z, label='Poste '+str(elem), color='brown')
    ax1.text(float(df['x'].values),float(df['y'].values),float(df['z'].values), elem, color='black')
    #ax1.legend()
    #Dibujar catenaria 3D
    if aux_boolean:
        x1=df['x'].values
        y1=df['y'].values
        z1=df['z'].values+df['Altura'].values
    else:
        x2=df['x'].values
        y2=df['y'].values
        z2=df['z'].values+df['Altura'].values
        ax1.plot([x1,x2], [y1,y2], [z1,z2], color='green') #esto debe convertirse en catenaria 3d
        x1=x2
        y1=y2
        z1=z2
    aux_boolean=False
    df=pd.DataFrame(data1)

plt.title('Distribución 3D')

#Para grafico 2d
ax2=fig.add_subplot(1,2,2)
aux_boolean=True
for elem in df_Poste:
    df=df[df['Poste']==elem]
    if aux_boolean:
        x1=df['x'].values
        y1=df['y'].values
        z1=df['z']+df['Altura']
        x0=0
    else:
        x2=df['x'].values
        y2=df['y'].values
        z2=df['z']+df['Altura']
        d=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        ax2.plot([x0,x0+d],[z1,z2], color='green') #esto debe convertirse en catenaria 2d
        x0=x0+d
        x1=x2
        y1=y2
        z1=z2
    xx=[x0,x0]     
    z = [df['z'],df['z']+df['Altura']]
    ax2.plot(xx,z, label='Poste '+str(elem), color='brown')
    
    ax2.text(float(x0),float(df['z'].values), elem, color='black')
    #ax2.legend()
    df=pd.DataFrame(data1)
    aux_boolean=False
del aux_boolean

plt.title('Distribución 2D')
plt.show()