from tkinter import *   
import tkinter
import joblib
from tkinter import messagebox
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from branca.element import Figure
import webbrowser
import plotly.graph_objects as go
import plotly.express as px
gui = Tk()  
gui.geometry('150x100')  

#set the window color
gui.configure(bg='cyan')

def msgCallBack():
    root = tkinter.Tk()
    root.geometry('800x500')
    root.configure(bg='cyan')
    w = tkinter.Label(root, text="Welcome to Vaccination Prediction Page ")
    w1 = tkinter.Label(root, text="Input Date(do not use any special character) yearmonthday like 20200429 ")
    entry1 = tkinter.Entry (root) 
    w2 = tkinter.Label(root, text="Input State Code(Maharashtra->1 WestBengal->2 Telanganana->3 Bihar->4 Gujrat->5 Telangana->6)")
    entry2 = tkinter.Entry (root) 
    w3 = tkinter.Label(root, text="Input Population")
    w4 = tkinter.Label(root, text="Maharashtra=15495706 , WestBengal=90000896 ,Telanganana = 35200753 ,Bihar=29700639,Gujrat=65700983")
    
    entry3 = tkinter.Entry (root)
    w5 = tkinter.Label(root, text="Total Vaccine Till Date !!")
   
    entry4 = tkinter.Entry (root)
    w6 = tkinter.Label(root, text=" Vaccine Due !!")
   
    entry5 = tkinter.Entry (root)
    entry4.insert(0,0)
    entry5.insert(0,0)
    
    def msgCallBack1():
        x=joblib.load("abc.pkl")
        try:
            xx=float(entry1.get()) #date
            xx1=float(entry2.get()) #state code
            xx2=float(entry3.get()) #population
            
        except:
            print("! valid input");
        y=x.predict([[xx ,xx1 ,xx2]])   
        entry4.delete(0, 'end')
        entry5.delete(0, 'end')
        entry4.insert(0,y) #prediction value
        due=xx2-y
        if(due<0):
            messagebox.showerror("Report", "Vaccine Complete")
            entry5.insert(0,0) #Due Vaccine
        else:
            entry5.insert(0,due) #Due Vaccine

        print(y)
        
    def msgCallBack2():
        data = pd.read_csv("covidv_data.csv")
        f,ax=plt.subplots(figsize=(15,8))
        sns.set_color_codes("pastel")
        sns.barplot(x=data['State'],y=data['Vaccined'],data=data,label="Vaccined",color="r")
        #sns.set_color_codes("muted")
        #sns.barplot(x=data[Choice],y=data['State'],data=data,label=Choice,color="g")
        ax.legend(ncol=2,loc="upper right",frameon=True)
        sns.despine(left=True,bottom=True)
        plt.show()
        
       
        
    bt = tkinter.Button(root, text ="Submit ", command = msgCallBack1)
    bt1 = tkinter.Button(root, text ="State wise Vaccine ", command = msgCallBack2)
    w.pack()
    w1.pack()
    entry1.pack()
    w2.pack()
    entry2.pack()
    w3.pack()
    w4.pack()
    entry3.pack()
    bt.pack()
    w5.pack()
    entry4.pack()
    w6.pack()
    entry5.pack()
    bt1.pack();
def geog():
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

def ras():
    data=pd.read_csv(r"covidv_data.csv")
    fig = go.Figure()
    fig = px.bar(data, x="Date", y="Confirmed", barmode='group', height=400)
    fig.update_layout(title_text='Coronavirus Cases in India on daily basis',plot_bgcolor='rgb(230, 230, 230)')
    fig.show()
    
btn = tkinter.Button(gui, text ="Vaccination Prediction ", command = msgCallBack)
btn1 = tkinter.Button(gui, text ="How many State Effect ", command =geog)
btn2 = tkinter.Button(gui, text ="Date wise covid Case ", command = ras)

btn.pack()
btn1.pack()
btn2.pack()
gui.mainloop()
