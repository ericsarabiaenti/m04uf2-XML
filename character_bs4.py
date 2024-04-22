#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

print("BIENVENIDO A FARY ADVENTURES JEFE")

for character in characters:
	print(f"{character['id']}\t {character.find('name').text}")

encontrado = False
while not encontrado:
	choose = input('PORFAVOR ESCOGE UN PERSONAJE, PONIENDO SU ID: ')

	character = soup.find('character', {'id': choose})

	if not character:
		print('ERROR: ID NO ENCONTRADO')
		exit()
	else:
		encontrado = True
print(f"{character['id']}\t {character.find('name').text}\t\t{character.find('age').text}\t{character.find('level')['value']}")
