from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# TO DO
# Read and store the datasets in a variable to be used by the application below

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user's input email and password
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password match some stored credentials
        if email == 'user@example.com' and password == 'password123':
            # If the credentials are valid, redirect to the student home page
            return render_template('student-home.html')
        else:
            # If the credentials are invalid, show an error message
            error_message = 'Invalid email or password'
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        email = request.form.get("email")
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
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        ID = "0000001"

        return render_template('succesfully-registered.html', name = name, ID=ID)
    return render_template('register.html')

@app.route('/student-home', methods=['GET'])
def student_home():
    return render_template('student-home.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == "POST":
        isDepressed = request.form.get("is-feeling-depressed")
        hasPreviousDiagnostic = request.form.get("previous-diagnostic")

        #To-DO store the data in a database or file

        print(isDepressed, flush=True)
        print("Has Previous Diagnostic?", hasPreviousDiagnostic)
        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        ID = "0000001"

        return render_template('succesfully-registered.html', name = isDepressed, ID=ID)
    return render_template('survey.html')

if __name__ == '__main__':    
    app.run()