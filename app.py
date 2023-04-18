from flask import Flask, render_template, request, jsonify, redirect, url_for

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
        userType = request.form['user-type']

        #TO DO:
        #If student, search in the Hash Table
        if userType == "student":
            # Check if the email and password match some stored credentials
            if email == 'user@example.com' and password == 'password123':
                # If the credentials are valid, redirect to the student home page
                return redirect(url_for('student_home'))        
            else:
                # If the credentials are invalid, show an error message
                error_message = 'Invalid email or password'
                return render_template('index.html', error_message=error_message)
        #If student, search in the B_Tree
        elif userType == "employee":
             # Check if the email and password match some stored credentials
            if email == 'user@example.com' and password == 'password1234':
                # If the credentials are valid, redirect to the student home page
                return redirect(url_for('employee_home'))        
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

        #TO DO store the data in a database or file
        print(name, flush=True)
        print("Address:", address)
        print("Phone Number:", phone)
        print("Email:", email)
        print("School:", school)
        print("Year:", year)
        print("Date of Birth:", dob)

        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        ID = "0000001"

        return render_template('succesfully-registered.html', name = name, ID=ID)
    return render_template('register.html')

@app.route('/register-OBO', methods=['GET', 'POST'])
def register_OBO():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        email = request.form.get("email")
        school = request.form.get("school")
        year = request.form.get("year")
        dob = request.form.get("dob")

        #TO DO store the data in a database or file
        print(name, flush=True)
        print("Address:", address)
        print("Phone Number:", phone)
        print("Email:", email)
        print("School:", school)
        print("Year:", year)
        print("Date of Birth:", dob)

        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        ID = "0000001"

        return render_template('succesfully-registered-obo.html', name = name, ID=ID)
    return render_template('register-OBO.html')

@app.route('/student-home', methods=['GET'])
def student_home():
    name = "First Last"
    print(name)
    return render_template('student-home.html', name=name)

@app.route('/employee-home', methods=['GET'])
def employee_home():
    name = "First Last"
    print(name)
    return render_template('employee-home.html', name=name)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == "POST":
        depressedMood = request.form.get("depressed-mood")
        depressedHopeless = request.form.get("depressed-hopeless")
        lossOfInterestAndEnjoyment = request.form.get("loss-interest-and-enjoyment")
        lossOfPleasureAndEnjoyment = request.form.get("loss-pleasure-and-enjoyment")
        lessenedEnergy = request.form.get("fatigued-and-lack-of-energy")
        lessenedActive = request.form.get("less-active-and-productive")
        reducedDecisionMaking = request.form.get("reduced-decision-making")
        reducedConcentration = request.form.get("reduced-concentration")
        reducedSelfConfidence = request.form.get("reduced-self-confidence")
        reducedSelfEsteem = request.form.get("reduced-self-steem")
        ideasOfGuilt = request.form.get("ideas-of-guilt")
        ideasOfUnworthiness = request.form.get("ideas-of-unworthiness")
        bleakViewsOfTheFuture = request.form.get("bleack-views-of-the-future")
        pessimisticViewsOfTheFuture = request.form.get("pessimistic-views-of-the-future")
        ideasOrActsOfSelfHarmOrSuicide = request.form.get("ideas-or-acts-of-self-harm-or-suicide")
        disturbedSleep = request.form.get("disturbed-sleep")
        diminishedAppetite = request.form.get("diminished-apetite")
        understandingParent = request.form.get("understanding-parent")
        missedClasses = request.form.get("missed-classes")
        smokeDrink = request.form.get("smoke-drink")
        lostRelative = request.form.get("lost-relative")
        relationshipTrouble = request.form.get("relationship-trouble")
        plagrisedHw = request.form.get("plagiarized-homework")
        leftJob = request.form.get("left-job")
        takingMedication = request.form.get("taking-medication")
        diagnosedBefore = request.form.get("diagnosed-before")

        #To DO store the data in a database or file
        print("depressedMood: ", depressedMood)
        print("depressedHopeless: ", depressedHopeless)
        print("lossOfInterestAndEnjoyment: ", lossOfInterestAndEnjoyment)
        print("lossOfPleasureAndEnjoyment: ", lossOfPleasureAndEnjoyment)
        print("lessenedEnergy: ", lessenedEnergy)
        print("lessenedActive: ", lessenedActive)
        print("reducedDecisionMaking: ", reducedDecisionMaking)
        print("reducedConcentration: ", reducedConcentration)
        print("reducedSelfConfidence: ", reducedSelfConfidence)
        print("reducedSelfEsteem: ", reducedSelfEsteem)
        print("ideasOfGuilt: ", ideasOfGuilt)
        print("ideasOfUnworthiness: ", ideasOfUnworthiness)
        print("bleakViewsOfTheFuture: ", bleakViewsOfTheFuture)
        print("pessimisticViewsOfTheFuture: ", pessimisticViewsOfTheFuture)
        print("ideasOrActsOfSelfHarmOrSuicide: ", ideasOrActsOfSelfHarmOrSuicide)
        print("disturbedSleep: ", disturbedSleep)
        print("diminishedAppetite: ", diminishedAppetite)
        print("understandingParent: ", understandingParent)
        print("missedClasses: ", missedClasses)
        print("smokeDrink: ", smokeDrink)
        print("lostRelative: ", lostRelative)
        print("relationshipTrouble: ", relationshipTrouble)
        print("plagrisedHw: ", plagrisedHw)
        print("leftJob: ", leftJob)
        print("takingMedication: ", takingMedication)
        print("diagnosedBefore: ", diagnosedBefore)
        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        ID = "0000001"

        name = "student name"

        return render_template('survey-submitted.html', name = name, ID=ID)
    return render_template('survey.html')

@app.route('/deleted', methods=['GET'])
def account_deleted():
    return render_template('account-deleted.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    #TO DO:
    #Query the variable to get the following info
    name = "First Last"
    address = "Gainesville, FL 32611"
    phone = "012-345-6789"
    email = "email@ufl.edu"
    school = "University Of Florida"
    year = "Freshman"
    dob = "2000-01-01" #Must be in this format!!
    ID = "0000001"

    if request.method == 'POST':
        action = request.form['action']
        if action == 'update':
            # handle update action
            print("update")
            address = request.form.get("address")
            phone = request.form.get("phone")
            year = request.form.get("year")

            #TO DO:
            # Update user profile
            return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)    

        elif action == 'delete':
            #TO DO:
            # Delete user profile
            print("delete")
            return render_template('account-deleted.html')
        elif action == 'back':
            return redirect(url_for('student_home'))        
    return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)

if __name__ == '__main__':    
    app.run()