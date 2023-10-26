import os


class Cities:
    @staticmethod
    def generateCitiesArray():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'ground_stations_cities_experiment.basic.txt')
        with open(file_path, 'r') as f:
            lines = f.readlines()

        cities = []
        for line in lines:
            city = line.split(',')[1]
            cities.append(city)
        return cities

    @staticmethod
    def generateCitiesDict():
        citiesArray = Cities.generateCitiesArray()
        cities_dict = {}
        i = 0
        for city in citiesArray:
            cities_dict[i] = city
            i += 1
        return cities_dict

    @staticmethod
    def generateCitiesDictCount():
        citiesArray = Cities.generateCitiesArray()
        cities_dict = {}
        for city in citiesArray:
            cities_dict[city] = {"count": 0, "cities":[]}
        return cities_dict

