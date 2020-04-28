#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# Create a monster list


# In[3]:


monster_list = ['Familar', 'Spore', 'Thief Bug Egg', 'Thief Bug', 'Thief Bug Female', 'Plankton', 'Tarou']
monster_weights = [10, 20, 20, 70, 10, 30, 60]


# In[4]:


# Create loot tables for each monster


# In[5]:


loots_Familar = ['Red Herb', 'Grape', 'Fly Wing', 'Concentration Potion', 'Tooth of Bat', 'Falchion', 'Ribbon', 'Familiar Card']
weights_Familar = [100, 30, 15, 15, 100, 6, 4.5, 0.3]


# In[6]:


loots_Spore = ['Red Herb', 'Blue Herb', 'Strawberry', 'Spore Doll', 'Mushroom Spore', 'Hat', 'Spore Card', 'Poison Spore']
weights_Spore = [100, 15, 100, 30, 100, 12, 0.3, 15]


# In[7]:


loots_Thief_Bug_Egg = ['Red Gemstone', 'Black Ladle', 'Chrysalis', 'Sticky Mucus', 'Iron Ore', 'Pharacon', 'Guard [1]', 'Thief Bug Egg Card']
weights_Thief_Bug_Egg = [30, 3, 100, 100, 75, 90, 0.6, 0.3]


# In[8]:


loots_Thief_Bug = ['Red Herb', 'Jellopy', 'Worm Peeling', 'Iron Ore', 'Jacket', 'Jacket [1]', 'Thief Bug Card']
weights_Thief_Bug = [100, 100, 100, 75, 36, 24, 0.3]


# In[9]:


loots_Thief_Bug_Female = ['Red Herb', 'Red Gemstone', 'Garlet', 'Insect Feeler', 'Worm Peeling', 'Iron Ore', 'Blade [4]', 'Female Theif Bug Card']
weights_Thief_Bug_Female = [100, 15, 75, 60, 100, 90, 4.5, 0.3]


# In[10]:


loots_Plankton = ['Dew Laden Moss', 'Concentration Potion', 'Empty Bottle', 'Garlet', 'Sticy Mucus', 'Alcohol', 'Single Cell', 'Plankton Card']
weights_Plankton = [6, 15, 100, 90, 100, 1.2, 100, 0.3]


# In[11]:


loots_Tarou = ['Monster\'s Feed', 'Ora Ora', 'Animal Skin', 'Feather', 'Rat Tail', 'Tarou Card']
weights_Tarou = [100, 0.6, 100, 100, 100, 0.3]


# In[12]:


# Create a dictionary for loot table


# In[13]:


loot_dict = {
    'Familar': loots_Familar,
    'Spore': loots_Spore,
    'Thief Bug Egg': loots_Thief_Bug_Egg,
    'Thief Bug': loots_Thief_Bug,
    'Thief Bug Female': loots_Thief_Bug_Female,
    'Plankton': loots_Plankton,
}


# In[14]:


# Create an inventory table


# In[15]:


inventory_table = []


# In[16]:


# Create a found monster table


# In[17]:


found_monster_table = []


# In[18]:


# Pick a random monsters


# In[19]:


total_hunting_numbers = input('How many monsters do you want to hunt :')
for x in range(int(total_hunting_numbers)):
    picked_monster = random.choices(monster_list, monster_weights, k =1)

    found_monster_table.append(picked_monster[0])
    #print('Monster found: ', picked_monster[0])                           # Debugging line to tell which monster is picked.
    
    # Pick a matched loot table
    
    if picked_monster[0] in loot_dict:
        loot_table = loot_dict.get(picked_monster[0])
        #print(loot_table)                                                          # Debugging line to tell which loots table is picked.
    
    # Simulate drop chance

        pos = 0
        for i in range(len(loot_table)):
            probability = random.uniform(0, 100)
            #print('Prob = ', probability)                                       # Debugging line to tell the probability.
            #print('Drop rate = ', weights_Spore[pos], '%')             # Debugging line to tell the drop rate.
            #print('Table position = ', pos + 1)                            # Degugging line to tell the position in loot table.
            if probability <= weights_Spore[pos]:
                inventory_table.append(loot_table[pos])
                #print('\x1b[31mGet\x1b[0m :', loot_table[pos],)     #
            print('\n')    
            pos += 1


# In[20]:


# Show all loots and monsters found
found_monster_table.sort()
counted_monster = [len(list(group)) for key, group in groupby(found_monster_table)]
found_monster_table = list(dict.fromkeys(found_monster_table))
inventory_table.sort()
counted_inventory = [len(list(group)) for key, group in groupby(inventory_table)]
inventory_table = list(dict.fromkeys(inventory_table))
print(found_monster_table)
print(counted_monster)
print(inventory_table)
print(counted_inventory)


# In[21]:


# Increase figure size
from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

# Make a dataset:
height_monster = counted_monster
bars_monster = found_monster_table
y_pos_monster = np.arange(len(bars_monster))

# Create labels
plt.xlabel('Kills')
plt.ylabel('Monsters')
plt.title('Map: prt_sewb2')

# Create bars
plt.barh(y_pos_monster, height_monster)
 
# Create names on the x-axis
plt.yticks(y_pos_monster, bars_monster)

# Create value on top of each bar
for index, value in enumerate(counted_monster):
    plt.text(value, index, str(value))
 
# Show graphic
plt.show()


# In[22]:


# Increase figure size
from matplotlib.pyplot import figure
figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')

# Make a dataset:
height_inventory = counted_inventory
bars_inventory = inventory_table
y_pos_inventory = np.arange(len(bars_inventory))

# Create labels
plt.xlabel('Drops')
plt.ylabel('Items')
plt.title('Map: prt_sewb2')
 
# Create bars
plt.barh(y_pos_inventory, height_inventory)
 
# Create names on the x-axis
plt.yticks(y_pos_inventory, bars_inventory)

# Create value on top of each bar
for index, value in enumerate(counted_inventory):
    plt.text(value, index, str(value))
 
# Show graphic
plt.show()

