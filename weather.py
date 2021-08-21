import tkinter as tk
import requests
import time


def GetWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=a9ed01edf4ffa172945f75128236f0d0"
    json_data = requests.get(api).json()
    weather_condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    minimum_temperature = int(json_data['main']['temp_min'] - 273.15)
    maximum_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    windspeed = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = weather_condition + "\n" + str(temperature) + "°C"
    final_data = "\n" + "Maximum Temperature: " + str(maximum_temperature) + "\n" + "Minimum Temperature: " + str(
        minimum_temperature) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Windspeed: " + str(windspeed) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather")
canvas.iconbitmap('images/icon.ico')

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', GetWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
