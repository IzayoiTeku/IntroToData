from flask import Flask, render_template, request
#flask is taking python and putting it in html
from flaskext.mysql import MySQL
import pymysql



app = Flask(__name__)


#Configuration for pymysql
#db = pymysql.connect(host="localhost",user= "root",password= "",database= "ksu") #for local connection
db = pymysql.connect(host="dbdev.cs.kent.edu",user= "bamoako",password="s9Vx8qeW", database= "bamoako") #for connecting to the CS server



@app.route('/')
def index():
    return render_template("home.html")
#html file has to be in render template folder

@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/pet", methods = ["GET", "POST"]) #GET ONLY GETS DATA, POST POSTS IT TO THE SERVER
def displayPet():
    if request.method == 'GET':
        cursor = db.cursor()
        sql = "SELECT * from pet;"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        print(data)
        return render_template('pet.html', data=data)
    if request.method == 'POST':
        data = request.form['pet_id']
        print(data)
        return render_template('pet.html')

@app.route('/search', methods = ['GET','POST'])
def search():   
    if request.method == "GET":
        return render_template("search.html")
    if request.method == "POST":
        petID = request.form["pet_id"]
        ownerID = request.form["owner_id"]
        print("inputs taken")
        print(petID, ownerID)
        if petID != "":
            cursor = db.cursor()
            sql = "SELECT * from pet where pet_id like '%%%s%%';" % petID;
            print(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            print(data)
            print("end of petID")
        print("before ownerID")
        if ownerID != "":
            cursor = db.cursor()
            sql = "SELECT * from pet where owner_id like '%%%s%%';" % ownerID;
            print(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            print(data) 
        if petID == "" and ownerID == "":
            return render_template('search.html')
        return render_template('pet.html', data=data)
            #print("Else Statement")
    return render_template('search.html')

@app.route('/register')
def register():
    return render_template("register.html")

app.run(host = "localhost", port = 8000)


'''
cursor = db.cursor()
sql = "SELECT * from instructor;"
cursor.execute(sql)
data = cursor.fetchall()
cursor.close()
print(data)
'''