import sqlite3
import pandas as pd

DB_FILEPATH = 'rpg_db.sqlite3'
connection = sqlite3.connect('rpg_db.sqlite3')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)
print()


#Total characters:
query = '''select count(character_id) as char_count
from charactercreator_character_inventory '''
result = cursor.execute(query).fetchone()

print("Total number of characters:")
print(f'{result[0]} \n')

#Total characters per subclass:
query = '''SELECT * FROM
    (SELECT COUNT(DISTINCT character_ptr_id) as clerics FROM charactercreator_cleric)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as fighters FROM charactercreator_fighter)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as mages FROM charactercreator_mage)
    ,(SELECT COUNT(DISTINCT mage_ptr_id) as necromancers FROM charactercreator_necromancer)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as thieves FROM charactercreator_thief)
	'''

result2 = cursor.execute(query).fetchone()
print(f'''Clerics: {result2[0]}  
Fighters: {result2[1]}   
Mages: {result2[2]}  
Necromancers: {result2[3]}
Theives: {result2[4]} \n''')

#Total items:
query = '''
SELECT COUNT(item_id) as item_count
FROM armory_item
'''

result3 = cursor.execute(query).fetchone()
print(f'The total number of items is {result3[0]}. \n')

#How many of the Items are weapons? How many are not?
#Get count of the items table and weapons table and subtract

query = '''
SELECT COUNT(item_id) 
FROM armory_item
'''
result4 = cursor.execute(query).fetchone()

query = '''
SELECT COUNT(item_ptr_id) 
FROM armory_weapon
'''

result5 = cursor.execute(query).fetchone()

result4[0] - result5[0]

print(f'The number of weapons is {result5[0]}')
print(f'The number of non-weapon items is {result4[0] - result5[0]} \n')

#How many Items does each character have? (Return first 20 rows)
query = '''SELECT character_id, count(*) Items
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20;'''

result6 = cursor.execute(query).fetchall()

print('First number in each tuple is character ID, 2nd is item count:')
print(f'{result6} \n')

#How many Weapons does each character have? (Return first 20 rows)

query = '''SELECT character_id, COUNT(*) Weapons 
FROM charactercreator_character_inventory AS cci,
armory_weapon as aw
WHERE cci.item_id = aw.item_ptr_id
GROUP BY character_id LIMIT 20;'''

result7 = cursor.execute(query).fetchall()
print('First number in each tuple is character ID, 2nd is weapon count:')
print(f'{result7} \n')

#On average, how many Items does each Character have?

query = '''SELECT AVG(items.count) FROM (
    SELECT COUNT(*) as count
    FROM charactercreator_character_inventory
    GROUP BY character_id) AS items;'''

result8 = cursor.execute(query).fetchall()

print('Average number of items per character:')
print(f'{result8[0][0]} \n')

#On average, how many Weapons does each character have?

query = '''SELECT AVG(weapons.count) FROM (
    SELECT COUNT(*) as count
    FROM charactercreator_character_inventory AS cci,
    armory_weapon AS aw
    WHERE cci.item_id = aw.item_ptr_id
    GROUP BY character_id) AS weapons;'''
    
result9 = cursor.execute(query).fetchall()

print("Average number of weapons per character:")
print(result9[0][0])





