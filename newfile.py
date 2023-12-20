from tkinter import *
from PIL import ImageTk,Image
import tkintermapview
import time

root=Tk()
root.geometry('1400x750')
root.configure(bg="#FFFFFF")
root.title("Main page")
    #side
cn_side=Canvas(root,bg="#818FB4",height='1400',width='230',borderwidth=0).place(x=0,y=0)
    #up
cn_up=Canvas(root,bg="#A9B8E1",height='100',width='1400',borderwidth=0).place(x=0,y=0)
label=Label(cn_up,text="Vessel Name :",font=("Arial",30),bg="#A9B8E1").place(x=300,y=25)
    #logo
pic=Image.open('pillayare2.jpeg')
resized=pic.resize((80,80))
newpic=ImageTk.PhotoImage(resized)
piclab=Label(cn_up,image=newpic,borderwidth=0,bg="#A9B8E1").place(x=15,y=15)


#################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


import searoute as sr

def get_sea():
    origin = [0.3515625, 50.064191736659104]

    destination = [117.42187500000001, 39.36827914916014]

    route = sr.searoute(origin, destination)

    print("{:.1f} {}".format(route.properties['length'], route.properties['units']))

    print(route)



    route_length = route.properties['length']

    route_duration_hours = route.properties['duration_hours']

    route_duration_hours

    route_duration_days = route_duration_hours/24

    route_duration_days

    # Optionally, define the units for the length calculation included in the properties object.
    # Defaults to km, can be can be 'm' = meters 'mi = miles 'ft' = feet 'in' = inches 'deg' = degrees
    # 'cen' = centimeters 'rad' = radians 'naut' = nautical 'yd' = yards
    routeMiles = sr.searoute(origin, destination, units="mi")

    route_length_miles = routeMiles.properties['length']

    route_length_miles

    route

    route_coordinates = route.geometry['coordinates']

    route_coordinates

    # Extract longitudes and latitudes into separate lists
    lons = [coord[0] for coord in route_coordinates]
    lats = [coord[1] for coord in route_coordinates]

    # Print the resulting lists
    print("Longitudes (lons):", lons)
    print("Latitudes (lats):", lats)

    import geopandas as gpd
    import matplotlib.pyplot as plt

    # Create a GeoDataFrame with your coordinates
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy(lons, lats))

    # Create a world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Plot the world map
    world.plot()

    # Plot your coordinates on top
    gdf.plot(marker='o', color='red', markersize=2, ax=plt.gca())

    # Customize the plot, add labels, etc.
    plt.title('Shortest Searoute')
    
    # piclab2=Label(cn_right,image=newpic1,borderwidth=0)
    # piclab2.place(x=300,y=125)
    # Show the plot
    plt.savefig('image1.jpg')
    new_image_path = 'image1.jpg'
    new_image_pil = Image.open(new_image_path)
    #resized=new_image_pil.resize(300,275)
    new_image = ImageTk.PhotoImage(new_image_pil)

    piclab1.config(image=new_image)
    piclab1.image = new_image
    time.sleep(1)



    #left buttons
b1=Button(cn_side,text="Weather",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=225)
b2=Button(cn_side,text="ETA",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=300)
b4=Button(cn_side,text="Home",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=150)
b5=Button(cn_side,text="Safety check",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=375)
b6=Button(root,text="Optimized route",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white',command=get_sea).place(x=760,y=600)


'''mapwig=tkintermapview.TkinterMapView(label1,width=700,height=400,corner_radius=0)
mapwig.pack()'''
#ri8 
cn_right=Canvas(root,bg="#818FB4",height='515',width='250',borderwidth=0).place(x=1050,y=125)
dts_lb=Label(cn_right,text="Details",font=("Arial" ,18, "bold"),bg="#818FB4").place(x=1125,y=175)
long_lb=Label(cn_right,text="Longitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=225)
longt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=275)
lat_lb=Label(cn_right,text="Latitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=325)
latt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=375)
spd_lb=Label(cn_right,text="Speed11:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=425)
spdt_lb=Label(cn_right,text="21km/h",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=475)

label1=LabelFrame(cn_right)
label1.place(x=300,y=70)
mapPath = r'image.jpg'
img = Image.open(mapPath)
newpic1=ImageTk.PhotoImage(img)
#resized2=newpic1.resize((200,125))
piclab1=Label(cn_right,image=newpic1,borderwidth=0)
piclab1.place(x=300,y=100)

#home
dep=Label(root,text=("Depature   ---> "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=475,y=600)
arr=Label(root,text=(" Arrival "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=650,y=600)
dep_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=475,y=650)
arr_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=655,y=650)



root.mainloop()
