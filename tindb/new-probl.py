from tinydb import TinyDB, Query
from tinydb import where
import time
import random

db = TinyDB('db.db')
timestamp = time.time()
rID = random.randrange(0, 9999)

jmeno = input("Zadejte jmeno pacienta, ke kteemu chcete vytvorit problem: ")

query = db.search(where('jmeno') == jmeno)

if query:
    anamneza = input("Jak se ma pacient? ")
    tbricho = input("Má pacient tvrdé břicho? ")
    
    ##Vlozime data do db
    db.insert({'rID': rID, 'anamneza': anamneza, 'tbricho': tbricho, 'timestamp': timestamp})
    print("Uspesne jsme pacienta pridali do databaze.")
else:
    print("Nenasel jsem zadneho pacienta s timto jmenem. :(")