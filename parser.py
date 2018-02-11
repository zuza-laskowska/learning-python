import json

with open('example.json', 'r') as myfile: #otwiera plik do odczytu
    text = myfile.read()  #zmiennej text przypisujemy wartosc odczytu pliku


parsed = json.loads(text)
# print(type(text))
# print (type(parsed))


for parametr in parsed:
    # text = parametr + ";" + str(parsed[parametr])
    # print(text)

    print(parametr, parsed[parametr])

# print(parsed['description'])

