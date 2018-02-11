# -*- coding: utf-8 -*-

import json


def parse_sensors_current(text_json):
    parsed = json.loads(text_json)
    # print(type(parsed))
    for sensor_data in parsed:
        sensor_id = sensor_data['id']

        # tworzymy pełny adres sensora w formacie: route, streetNumber, locality

        address = sensor_data['address']['route']

        # if 'streetNumber' in sensor_data['address'] and len(sensor_data['address']['streetNumber'])>0:
        #     address += " " + sensor_data['address']['streetNumber']
        # else:
        #     print("Brak streetNumber dla sensora: " + str(sensor_id))

        if 'streetNumber' in sensor_data['address']:
            if len(sensor_data['address']['streetNumber'])>0:
                address += " " + sensor_data['address']['streetNumber']
            else:
                print("Pusta wartość streetNumber dla sensora: " + str(sensor_id))
        else:
            print("Brak indeksu streetNumber dla sensora: " + str(sensor_id))

        address += ", " + sensor_data['address']['locality']

        # print("sensor_id streetNumber= " + str(sensor_id))
        # print("address = " + address)
        # print("-"*30)
        # print(str(sensor_data))
        # break


with open('sensors_current.json', 'r') as myfile: # otwiera plik do odczytu
    sensors_current = myfile.read()  # zmiennej text przypisujemy wartosc odczytu pliku


# parsed = json.loads(sensors_current)
#
# print(parsed)

parse_sensors_current(sensors_current)
