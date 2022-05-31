from tinydb import TinyDB, Query
db = TinyDB('db.db')

jmeno = input("Zadejte jmeno pacienta: ")
datnar = input("Zadejte datum narozeni pacienta: ")

##Pridani pacienta do db
db.insert({'jmeno': jmeno, 'datnar': datnar})

print("Pacient ", jmeno, " byl uspesne pridan do databaze.")