from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox 
#Submodules for tkinter, need to import additionally.
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from keys import API

# Initializing the Tk module
root = Tk()
root.title("Weather App") 
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = textfield.get().lower()
        if city == "ankara":
            messagebox.showinfo("You found the secret!", "Atatürk's home. ")
        geolocator = Nominatim(user_agent="weatherApp")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API


        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition,"|", "FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")

# Search Box
search_image = PhotoImage(file="search.png") # Load image from search.png
my_image = Label(image=search_image) # Label widget for containing the img
my_image.place(x=20, y=20) # Placement

textfield = tk.Entry(root,bg="#404040",justify = "center",relief="ridge", width=17, font=("poppis",25,"bold"), border=0,fg="white")
textfield.place(x=50, y=40)
textfield.focus() #Automatically focus on this widget when window opens

# Search Button
Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon,
                    borderwidth=0,
                    cursor="hand2",
                    bg="#404040",
                    command=getWeather,
                    activebackground="#303030",
                    relief="solid",
                    padx=10,
                    pady=10,
                    )
myimage_icon.place(x=400,y=34)

root.bind("<Return>", lambda event: getWeather())

# Logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150,y = 115) 

# Bottom Box
frame_image = PhotoImage(file="box.png")
frame = Label(image=frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)

# Time

name = Label(root, font=("arial",15,"bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica",20) )
clock.place(x=30,y=130)
# Label
class Labels:
    def __init__(self, root, font=("Helvetica",15,"bold"), fg="white",bg="#1ab5ef"):
        self.root = root
        self.font = font
        self.fg = fg
        self.bg = bg

    def labeler(self, text, x, y):
        label = Label(self.root, text= text, font=self.font, fg=self.fg, bg=self.bg)
        label.place(x=x,y=y)
        return label
    
label_data = [
    ("WIND", 120, 400),
    ("HUMIDITY", 235, 400),
    ("DESCRIPTION", 430, 400),
    ("PRESSURE", 650, 400)
]

label_creator = Labels(root)

for label_text,x_pos,y_pos in label_data:
    label_creator.labeler(label_text, x_pos, y_pos)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400,y=250)

class Label_Items:
    def __init__(self, root, font=("arial",20,"bold"), bg="#1ab5ef"):
        self.root = root
        self.font = font
        self.bg = bg

    def itemer(self,text, x,y):
        item =Label(self.root, text= text, font=self.font, bg=self.bg)
        item.place(x=x, y=y)
        return item
    
item_data = [
    ("...",120,430),
    ("...",280,430),
    ("...",450,430),
    ("...",670,430)
]
item_creator = Label_Items(root)

w, h, d, p = [item_creator.itemer(item_text, item_x, item_y) for item_text, item_x, item_y in item_data]


w = Label(text= "...", font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=120, y= 430)
root.mainloop()