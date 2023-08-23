import pandas as pd

class FlightData:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        
    def for_city(self, city):
        return self.df[(self.df["From"] == city) | (self.df["To"] == city)]
    
    def from_city(self, city):
        return self.df[self.df["From"] == city]
    
    def between_cities(self, city_from, city_to):
        return self.df[(self.df["From"] == city_from) & (self.df["To"] == city_to)]

data = {
    "Flight ID": ["AI161E90", "BR161F91", "AI161F99", "VS171E20", "AS171G30", "AI131F49"],
    "From": ["BLR", "BOM", "BBI", "JLR", "HYD", "HYD"],
    "To": ["BOM", "BBI", "BLR", "BBI", "JLR", "BOM"],
    "Price": [5600, 6750, 8210, 5500, 4400, 3499]
}

flight_data = FlightData(data)

search_type = input("Search by:\n1. Flights for a particular city\n2. Flights from a city\n3. Flights between two cities\nChoose an option: ")

if search_type == "1":
    city = input("Enter city name: ")
    flights = flight_data.for_city(city)
    print(f"Flights to or from {city}:\n", flights)
elif search_type == "2":
    city = input("Enter city name: ")
    flights = flight_data.from_city(city)
    print(f"Flights from {city}:\n", flights)
elif search_type == "3":
    city_from = input("Enter departure city: ")
    city_to = input("Enter destination city: ")
    flights = flight_data.between_cities(city_from, city_to)
    print(f"Flights from {city_from} to {city_to}:\n", flights)
else:
    print("Invalid option")
