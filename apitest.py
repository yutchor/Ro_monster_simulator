# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:57:32 2020

@author: k4noob2
"""


import requests

# Definding an apikey
_api = 'cc9bfa83e5e1605c8e2c292ba8bc9a56'

# Get map id
_map = input('Map: ')

# Request map information
response = requests.get('https://www.divine-pride.net/api/database/Map/'
                        + _map +'?apiKey='+ _api)
# Parsing map JSON 
_json_map = response.json()
# print(_json_map)                                      # Debugging line showing JSON 
monster_Id = _json_map['spawn']         
# print(monster_Id)                                     # Debugging line showing MonsterID        
monster_Id_table = []
for i in range(len(_json_map['spawn'])):
    monster_Id_table.append(_json_map['spawn'][i]['monsterId'])
print(monster_Id_table)                               # Debugging line show MonsterID's table

# Create monster's name table
monster_Name_table = []
monster_Drops_table = []

# Request monster inforamtion
for i in range(len(monster_Id_table)):
    response = requests.get('https://www.divine-pride.net/api/database/Monster/'
                            + str(monster_Id_table[i]) +'?apiKey='+ _api)
    # Parsiong monster JSON
    _json_monster = response.json()
    # print(_json_monster)                              # Debugging line showing JSON
    monster_Name = _json_monster['name']
    monster_Drops = _json_monster['drops']
    monster_Name_table.append(monster_Name)
    monster_Drops_table.append(monster_Drops)

# Zipping name and drops table
monster_Zipped_table = list(zip(monster_Name_table, monster_Drops_table))
print(monster_Zipped_table[0][1][2]['itemId'])
print(monster_Zipped_table[0][1][2]['chance'])
