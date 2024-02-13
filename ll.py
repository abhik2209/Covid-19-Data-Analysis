from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt1
import matplotlib.animation as animation
import pandas as pd
import seaborn as sns

data=pd.read_csv("covid19_data.csv")
data['Region']=data['Region'].astype(str)
data['Confirmed']=data['Confirmed'].astype(str)
data['Deaths']=data['Deaths'].astype(str)
data['Recovered']=data['Recovered'].astype(str)

plt1.style.use('fivethirtyeight')

def animate(i):
    x1  = data['Region']
    y1 = data['Confirmed']
    y2 = data['Deaths']
    y3 = data['Recovered']

    sns.set_style("whitegrid")
    g=sns.FacetGrid(data,hue='Recovered',height=4)
    g.map(plt1.scatter,x=x1,y=y1)
    g.add_legend();


ani = FuncAnimation(plt1.gcf(), animate,frames=200, interval=20, blit=True)
plt1.tight_layout()
plt1.show()
