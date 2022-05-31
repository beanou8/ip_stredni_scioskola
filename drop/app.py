from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query, where
from datetime import datetime

app = Flask(__name__)

db = TinyDB("db.json")
t_links = db.table("links")

query = Query()

@app.route("/")
def home():
    links = t_links.search(query.visibility == "visible")
    return render_template("home.html", links = links)

@app.route("/add/",methods = ['POST'])
def add():
    link = request.form['link']
    date = datetime.today().strftime('%d. %m. %Y')
    key_id = str(len(t_links) + 1)
    visibility = "visible"
    
    t_links.insert({"key_id":key_id, "date":date, "content":link, "visibility":visibility})
    return redirect(url_for('home'))


##NOT WORKING
@app.route("/disable/")
def disable():
    id = "1"
    t_links.update(set('visible', 'hidden'), t_links.key_id == id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="localhost",port="8080",debug=True)