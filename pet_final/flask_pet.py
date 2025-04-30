from flask import Flask, render_template, request
#flask is taking python and putting it in html
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

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html') 
    if request.method == 'POST':
        petId = request.form["pet_id"]
        pName = request.form["name"]
        pSpecies = request.form["species"]
        pBreed = request.form["breed"]
        pColor = request.form["color"]
        pHealth = request.form["health_id"]
        pBehav = request.form["b_stat"]
        ownerId = request.form["owner_id"]
        pLost = request.form["lost"]
        vetId = request.form["vet_id"]
        pdob = request.form["dob"]
        #request.from rest of attributes in order of db
        cursor = db.cursor()
        sql = "INSERT INTO pet VALUES (\"" + petId + "\",\"" + pName + "\",\"" + pSpecies + "\",\"" + pBreed + "\",\"" + pColor + "\",\"" + pHealth + "\",\"" + pBehav + "\",\"" + ownerId + "\",\"" + pLost + "\",\"" + vetId + "\", \"" + pdob + "\");"
        print(sql)
        cursor.execute(sql)
        cursor.close()

        cursor = db.cursor()
        sql = "SELECT * from pet"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        edited = []
        print(data)
        for i in data:
            edited.append(i[0])
        print('')
        return render_template('pet.html', data=data)
    


    #its just for the test but it didnt work. 
    @app.route('/lost', methods = ['GET', 'POST'])
    def lost():
        if request.method == 'GET':
            return render_template('lost.html') 
        if request.method == 'POST':
            petId = request.form["pet_id"]
            pSpecies = request.form["species"]
            pBreed = request.form["breed"]
            pColor = request.form["color"]
           

    



app.run(host = "localhost", port = 8000)


'''
cursor = db.cursor()
sql = "SELECT * from instructor;"
cursor.execute(sql)
data = cursor.fetchall()
cursor.close()
print(data)
'''