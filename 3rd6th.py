class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    # Subscribe an observer
    def subscribe(self, observer):
        self.observers.append(observer)

    # Unsubscribe an observer
    def unsubscribe(self, observer):
        self.observers.remove(observer)

    # Notify all observers
    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)

    # Change temperature
    def set_temperature(self, temperature):
        self.temperature = temperature
        print("\nTemperature changed to:", temperature, "°C")

        self.notify()


class Display:
    def __init__(self, name):
        self.name = name

    # Update method called by WeatherStation
    def update(self, temperature):
        print(self.name, "Display updated:", temperature, "°C")


# Creating Weather Station
weather_station = WeatherStation()

# Creating Displays
display1 = Display("Mobile")
display2 = Display("TV")
display3 = Display("Computer")

# Subscribing displays
weather_station.subscribe(display1)
weather_station.subscribe(display2)
weather_station.subscribe(display3)

# Changing temperature
weather_station.set_temperature(30)

# Unsubscribe one display
weather_station.unsubscribe(display2)

# Change temperature again
weather_station.set_temperature(35)