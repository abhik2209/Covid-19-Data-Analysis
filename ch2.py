from tkinter import *
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from branca.element import Figure
import webbrowser

#Create an instance of Tkinter frame
#win= Tk()

#Set the geometry of tkinter frame
#win.geometry("750x250")

#fig=Figure(width=550,height=350)
#m1=folium.Map(width=550,height=350,location=[28.644800, 77.216721],zoom_start=11,min_zoom=8,max_zoom=14)
#fig.add_child(m1)

# Creating Basemap
fig3=Figure(width=500,height=600)
m3=folium.Map(location=[21.7679, 78.8718],tiles='cartodbpositron',zoom_start=5)

data1=pd.read_csv(r"latlong.csv")
df=pd.DataFrame(data1)
df['Lat']=df['Lat'].astype('object')
df['Lat']=df['Lat'].astype('float')
df['Long']=df['Long'].astype('object')
df['Long']=df['Long'].astype('float')
for lat,long,state in zip(data1['Lat'],data1['Long'],data1['State']):
    folium.Marker(location=[lat, long],radious=0.8,popup=('<strong>State</strong>:'+str(state).capitalize()),tooltip='Click here to State Name',icon=folium.Icon(color="red",icon="envelope")).add_to(m3)
m3.save('ab.html')

new = 1 # open in a new tab, if possible


url = "ab.html"
webbrowser.open(url,new=new)

url = "file://d/testdata.html"
webbrowser.open(url,new=new)
