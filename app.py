from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        school = request.form.get("school")
        year = request.form.get("year")
        dob = request.form.get("dob")

        #To-DO store the data in a database or file
        print(name, flush=True)
        print("Address:", address)
        print("Phone Number:", phone)
        print("School:", school)
        print("Year:", year)
        print("Date of Birth:", dob)
        
        # TO DO: 
        # Insert student and return its ID
        ID = "0000001"
        return render_template('succesfully-registered.html', name = name, ID=ID)
    return render_template('register.html')

if __name__ == '__main__':
    app.run()