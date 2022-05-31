from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from flask_cors import CORS
query = Query()
db = TinyDB('db.json')
patients = db.table('patients')

app = Flask(__name__)
CORS(app)


@app.route("/")
def view_home():
    return "Tady bude appka."


@app.route("/api/patient/", methods=['POST', 'GET'])
def patient():
    if request.method == 'POST':
        data = request.json
        p = {
            'id': len(patients),
            'name': data['name'],
            'dob': data['dob'],
            'problems': []
        }
        patients.insert(p)
        return jsonify(p)
    else:
        return jsonify(patients.all())


@app.route("/api/patient/<int:pid>/", methods=['POST', 'GET'])
def one_patient(pid):
    if request.method == 'POST':
        return jsonify("Wait till the end.") # TODO: update patient with this post
    else:
        if patients.search(query.id == pid):
            return jsonify(patients.search(query.id == pid))
        else:
            return jsonify("Not found.")


@app.route("/api/problem/<int:pid>/", methods=['POST', 'GET'])
def problem(pid):
    if request.method == 'POST':
        if patients.search(query.id == pid):
            problems = patients.search(query.id == pid)[0]['problems']
            data = request.json
            p = {
                'id': len(problems),
                'problem': data['problem'],
                'appointments': []
            }
            problems.append(p)
            patients.update({'problems': problems}, query.id == pid)
            return jsonify(p)
        else:
            return jsonify("Not found.")
    else:
        if patients.search(query.id == pid):
            return jsonify(patients.search(query.id == pid)[0]['problems'])
        else:
            return jsonify("Not found.")


@app.route("/api/problem/<int:pid>/<int:PrId>/", methods=['POST', 'GET'])
def one_problem(pid, PrId):
    if request.method == 'POST':
        return jsonify("Wait till the end.")  # TODO: do something with it
    else:
        problems = patients.search(query.id == pid)[0]['problems']
        for i in problems:
            if PrId == i['id']:
                p = i
        if p:
            return jsonify(p)
        else:
            return jsonify("Not found.")


@app.route("/api/appointment/<int:pid>/<int:PrId>/", methods=['POST', 'GET'])
def appointments(pid, PrId):
    if request.method == 'POST':
        if patients.search(query.id == pid):
            appm = {
                'date': request.form['date'],
                'data': request.form['data']
            }
            problems = patients.search(query.id == pid)[0]['problems']
            for i in problems:
                if PrId == i['id']:
                    p = i
            if p:
                problems.remove(p)
                p['appointments'].append(appm)
                problems.append(p)
                patients.update({'problems': problems}, query.id == pid)
                return jsonify(p)
            else:
                jsonify("Not found.")
        else:
            return jsonify("Not found.")
    else:
        problems = patients.search(query.id == pid)[0]['problems']
        for i in problems:
            if PrId == i['id']:
                p = i['appointments']
        if p:
            return jsonify(p)
        else:
            jsonify("Not found.")
