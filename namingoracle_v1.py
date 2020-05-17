#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python Documentation
# https://docs.python.org/3.8/
# https://docs.python.org/3.8/library/index.html

# basic examples
# https://www.programiz.com/python-programming/examples

# reading an input string in interactive mode and store it in variable firstname
firstname = input('Bitte Vorname eingeben: ')

# reading an input string in interactive mode and store it in variable lastname
lastname = input('Bitte Nachname eingeben: ')

# Ausgabe:
# len(String) gibt die Länge des Strings als integer Zahl (Ganzzahl) zurück
# siehe https://docs.python.org/3.8/library/functions.html?highlight=len#len

# str(integer) macht aus einer integer Zahl einen String
# siehe https://docs.python.org/3.8/library/stdtypes.html?highlight=str#str

# print(String) gibt einen String auf der Kommandozeile aus
# https://docs.python.org/3.8/library/functions.html#print
print("der Vorname ist " + str(len(firstname)) + " Zeichen lang.")
print("der Nachname ist " + str(len(lastname)) + " Zeichen lang.")

# varianten für die Längenbestimmung eines Strings:
# https://www.geeksforgeeks.org/find-length-of-a-string-in-python-4-ways/

print("erstes Zeichen des Vornames: " + firstname[0])

# https://www.w3schools.com/python/python_for_loops.asp
for i in range(0, len(firstname)):
    print("Zeichen " + i)
    #
    # weitere Verarbeitungschritte kommen hier
    #
    #
