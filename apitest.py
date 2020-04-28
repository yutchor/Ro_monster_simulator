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
# print(_json_map)                                    # Debugging line showing JSON 
monster_Id = _json_map['spawn'][0]['monsterId']  
print(monster_Id)                               # Debugging line showing MonsterID        

# Request monster inforamtion
response = requests.get('https://www.divine-pride.net/api/database/Monster/'
                        + str(monster_Id) +'?apiKey='+ _api)
# Parsiong monster JSON
_json_monster = response.json()
print(_json_monster)