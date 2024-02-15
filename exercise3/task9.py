
class WeatherStation:
    def __init__(self, name):
        self.observations = []
        self.name = name

    def add_observation(self, observation: str):
        self.observations.append(observation)
    # adds an observation as the last entry in a list
    
    def latest_observation(self):
        if self.observations == 0:
            return ''
        else:
            return self.observations[-1]
    # returns the latest observation added to the list. 
    # If there are no observations yet, the method should return an empty string.
    
    def number_of_observations(self):
        if self.observations == 0:
            return None
        else:
            return len(self.observations)
    # returns the total number of observations added
    
    def __str__(self):
        return f"{self.name}, {self.number_of_observations()}"
    # a __str__method which returns the name of the station and the total
    # number of observations added as per the example below.
    
    

station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)