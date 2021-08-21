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
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = weather_condition + "\n" + str(temperature) + "°C"
    final_data = "\nMax Temperature:\t" + str(maximum_temperature) + "°C\nMin Temperature:\t" + str(
        minimum_temperature) + "°C\nPressure:\t\t" + str(pressure) + " mb\nHumidity:\t\t" + str(
        humidity) + " %\nWindspeed: \t" + str(windspeed) + " km/h\nSunrise:\t\t" + sunrise + "\nSunset:\t\t" + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("Weather")
canvas.iconbitmap('images/icon.ico')
canvas.configure(bg='black')

f = ("verdana", 15, "bold")
t = ("verdana", 35, "bold")

textfield = tk.Entry(canvas, justify='center', font=t, fg="black")
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', GetWeather)

label1 = tk.Label(canvas, font=t, fg="white", bg="black", bd=2, relief="flat")
label1.pack(ipady=5, ipadx=5)

label2 = tk.Label(canvas, font=f, fg="white", bg="black", bd=2, relief="flat", justify="left")
label2.pack(pady=5, ipady=5, ipadx=5)

canvas.mainloop()
