
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import ImageTk,Image


import searoute as sr

class PannedWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("buttons")
        self.paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)

        # Add a label
        #frame1-----
        self.frame1 = tk.Frame(self.paned_window, width=1400, height=750, relief=tk.SUNKEN)
    
        
        self.paned_window.add(self.frame1)
        self.prev_button = tk.Button(self.frame1, text="HOME",font=('Arial',16), width=13,command=self.show_home)
         
        self.prev_button1 = tk.Button(self.frame1, text="SAFETY CHECK", font=('Arial',16),width=13, command=self.show_safety)
        self.prev_button2 = tk.Button(self.frame1, text="ETA",font=('Arial',16), width=13, command=self.show_arrival)
        self.prev_button3 = tk.Button(self.frame1, text="WEATHER",font=('Arial',16), width=13, command=self.show_weather)
        self.paned_window.pack(expand=True, fill=tk.BOTH)
        self.prev_button.pack(pady=30)
        self.prev_button1.pack(pady=40)
        self.prev_button2.pack(pady=50)
        self.prev_button3.pack(pady=50)
        self.current_frame_index = 0

        # self.home_frame_button = tk.Button(self, text="HOME", command=self.add_frame)
        # self.remove_frame_button = tk.Button(self.frame1, text="BACK", command=self.remove_frame)
        # self.add_frame_button.pack(side=tk.LEFT, padx=5)
        # self.remove_frame_button.pack(side=tk.RIGHT, padx=5)

     #frame2----------
        self.frame2 = tk.Frame(self.paned_window,bg='#0F2167', width=1400, height=750, relief="raised")
        self.paned_window.add(self.frame2)
        label1=tk.Label(self.frame2,text="Create Your Account",font=("Arial",28),bg="#0F2167",fg="#FFFFFF").place(x=600,y=50)
        label2=tk.Label(self.frame2,text="Name",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=200)
        label3=tk.Label(self.frame2,text="Email Id",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=340)
        label4=tk.Label(self.frame2,text="Password",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=500) 
        entry1=tk.Entry(self.frame2,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=200)
        entry2=tk.Entry(self.frame2,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=340)
        entry3=tk.Entry(self.frame2,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=500)
        def reg ():
            messagebox.showinfo("safety check", "product key will be sent\nthrough mail in two  to \n  three business day !")
        b1=tk.Button(self.frame2,text="Register",bg="#D9D9D9",font=("Arial",24),borderwidth=5,command=reg,width=15).place(x=640,y=650)

        #frame3----------
        self.frame3= tk.Frame(self.paned_window,bg='#0F2167', width=1400, height=750, relief="raised")
        self.paned_window.add(self.frame3)
        cn=tk.Canvas(self.frame3,bg="#0F2167",height='1400',width='446',borderwidth=0).place(x=0,y=0)
        label=tk.Label(self.frame3,text="Vessel360",font=("Arial",46,"bold"),bg="#0F2167",fg="#FFFFFF").place(x=60,y=82)
        labellog=tk.Label(self.frame3,text="Login",font=("Arial",20,"bold"),bg="#0F2167",fg="#FFFFFF").place(x=155,y=512)
        label1=tk.Label(self.frame3,text="Roll ID",font=("Arial",20),bg="#FFFFFF").place(x=600,y=190)
        label2=tk.Label(self.frame3,text="Password",font=("Arial",20),bg="#FFFFFF").place(x=600,y=370)
        entry1=tk.Entry(self.frame3,font=("Arial",24),bg="#D9D9D9").place(x=600,y=270)
        entry2=tk.Entry(self.frame3,font=("Arial",24),bg="#D9D9D9").place(x=600,y=450)
        label=tk.Label(self.frame3,text="New user?",font=("Arial",24),bg="#FFFFFF").place(x=600,y=600)
        b1=tk.Button(self.frame3,text="Click here...",bg="#FFFFFF",fg="#0F2167",font=("Arial",20),borderwidth=0).place(x=780,y=595)
        b2=tk.Button(self.frame3,text="Login",bg="#0F2167",fg="white",font=("Arial",20),borderwidth=0,width=7).place(x=710,y=510)

# #frame4----------------
#         self.frame4= tk.Frame(self.paned_window,bg='#0F2167', width=1400, height=750, relief="raised")
#         self.paned_window.add(self.frame4)
#         cn=tk.Canvas(self.frame4,bg='#FFFFFF',height='450',width='700').place(x=70,y=150)
#         label1=tk.Label(self.frame4,text="Departure port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=150)
#         label2=tk.Label(self.frame4,text="Arrival port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=260)
#         entry1=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=150)
#         entry2=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=260)
#         btn1=tk.Button(self.frame4,text='Submit',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=10).place(x=1000,y=370)
#         label2=tk.Label(self.frame4,text="ETA",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=500)
#         entry1=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=500)
#         label1=tk.LabelFrame(root).place(x=70,y=150)
                

        
    def get_sea(self):
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

        # Show the plot
        plt.show()
        plt.savefig('image.jpg')


    def show_home(self):
        self.paned_window.remove(self.frame2)
        self.paned_window.remove(self.frame3)
        self.paned_window.remove(self.frame4)
        self.paned_window.remove(self.frame5)

        b6=tk.Button(cn_side,text="Optimized route",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white',command=get_sea).place(x=760,y=570)
        label1=tk.LabelFrame(root).place(x=300,y=125)

        newpic1=ImageTk.PhotoImage(Image.open('image.jpg'))
        piclab1=tk.Label(label1,image=newpic1,borderwidth=0,bg="#A9B8E1").place(x=300,y=125)

        '''mapwig=tkintermapview.TkinterMapView(label1,width=700,height=400,corner_radius=0)
        mapwig.pack()'''
        #ri8 
        cn_right=tk.Canvas(self.frame6,bg="#818FB4",height='515',width='250',borderwidth=0).place(x=1050,y=125)
        dts_lb=tk.Label(cn_right,text="Details",font=("Arial" ,18, "bold"),bg="#818FB4").place(x=1125,y=175)
        long_lb=tk.Label(cn_right,text="Longitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=225)
        longt_lb=tk.Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=275)
        lat_lb=tk.Label(cn_right,text="Latitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=325)
        latt_lb=tk.Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=375)
        spd_lb=tk.Label(cn_right,text="Speed:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=425)
        spdt_lb=tk.Label(cn_right,text="21km/h",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=475)

        #home
        dep=tk.Label(self.frame6,text=("Depature   ---> "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=475,y=600)
        arr=tk.Label(self.frame6,text=(" Arrival "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=650,y=600)
        dep_lb=tk.Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=475,y=650)
        arr_lb=tk.Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=655,y=650)

        
        
    def show_safety(self):
        self.paned_window.remove(self.frame2)
        self.paned_window.remove(self.frame3) 
    def show_arrival(self):
        self.paned_window.remove(self.frame2)
        self.paned_window.remove(self.frame3)
        # self.paned_window.remove(self.frame1)
        self.frame4= tk.Frame(self.paned_window,bg='#0F2167', width=1400, height=750, relief="raised")
        self.paned_window.add(self.frame4)
        cn=tk.Canvas(self.frame4,bg='#FFFFFF',height='450',width='700').place(x=70,y=150)
        label1=tk.Label(self.frame4,text="Departure port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=150)
        label2=tk.Label(self.frame4,text="Arrival port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=260)
        entry1=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=150)
        entry2=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=260)
        btn1=tk.Button(self.frame4,text='Submit',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=10).place(x=1000,y=370)
        label2=tk.Label(self.frame4,text="ETA",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=500)
        entry1=tk.Entry(self.frame4,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=500)
        label1=tk.LabelFrame(root).place(x=70,y=150)
       
        # Add the new frame to the paned window
        self.paned_window.add(self.frame4)
       
        # Add the new frame to the list
        self.frames.append(self.frame4)


        '''if self.current_frame_index > 2:
            self.current_frame_index -= 1
            self.paned_window.sash_place(self.current_frame_index, 2)  '''
    def show_weather(self):
        if self.current_frame_index > 3:
            self.current_frame_index += 1
            self.paned_window.sash_place(self.current_frame_index, 3)  
    def show_next(self):
        if self.current_frame_index < 1:
            self.current_frame_index += 1
            self.paned_window.sash_place(self.current_frame_index, self.paned_window.winfo_width() - 4)  

if __name__ == "__main__":
 root = tk.Tk()   
 app = PannedWindowApp(root)
 root.mainloop()