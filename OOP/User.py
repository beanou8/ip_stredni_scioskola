from tinydb import TinyDB, Query
db = TinyDB('db.json')
query = Query()

import shortuuid
import bcrypt


class User:

    uuid = shortuuid.uuid()

    # Constructor
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        password = self.password.encode('utf-8')

        db.insert({
            'uuid': self.uuid,
            'name': self.name,
            'email': self.email,
            'password': bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
        })

    def getinfo(self, email):
        return db.search(query.email == email)[0]

    def login(self):
        if self.getinfo(self.email):
            pwd = self.getinfo(self.email)['password'].encode('utf-8')

            if bcrypt.checkpw(self.password.encode('utf-8'), pwd):
                return 'true'
            else:
                return 'false'

        else:
            return 'false'
