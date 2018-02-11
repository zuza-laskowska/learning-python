# number_1 = 2.0
# number_2 = 5.0
# number_3 = number_1 ** number_2  # 3 to the fourth power
# print (number_3)
# print (number_1) + (number_2)

import json

lista_1= ['a', 'b', {'jeden': 1, 'dwa': 'hello'}]

cytryna = {'aa': 11,
           'bb': lista_1}

owoce = {'ananas': "2",
         'jablko': [3, 2, 1],
         'cytryna': cytryna}

json_string = json.dumps(owoce, indent=4, sort_keys=True)
#
with open('struktury.json', 'w') as f:
    f.write(json_string)

print(json_string)

# for nazwa_owoca in owoce:
#     print(nazwa_owoca)
#     print(owoce[nazwa_owoca])
#     print(type(owoce[nazwa_owoca]))
#     print('')

# print(cytryna.get('aa'))

bb_2 = owoce['cytryna']['bb'][2]
wynik = bb_2.get('dwa')
print(wynik)