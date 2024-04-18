#!/usr/bin/python3

from xml.dom import minidom

facx = minidom.parse('characters.facx')

characters = facx.getElementsByTagName('character')


print(characters[0].childNodes[0].data)
