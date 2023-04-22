from flask import Flask, render_template, request, jsonify, redirect, url_for

import time

app = Flask(__name__)

# TO DO
# Read and store the datasets in a variable to be used by the application below

#Hash Table

#B-Tree need to store Student ID created by Hash Function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Gets the user's input StudentID and password
        studentID = request.form['studentID']
        studentPassword  = request.form['password']
        userType = request.form['user-type']

        #TO DO:
        #If student, go to the Hash Table
        if userType == "student":
            studentIds = studentID
            #Check if the StudentID and password match some stored credentials
            #Check if Student ID exist, if it does, check if the password matches (line 30)
            if studentIds == 'user@example.com' and studentPassword  == 'password123':
                # If the credentials are valid, redirect to the student home page
                return redirect(url_for('student_home', studentID=studentID))        
            else:
                # If the credentials are invalid, show an error message
                error_message = 'Invalid StudentID or password'
                return render_template('index.html', error_message=error_message)
        #If employee, go to the B_Tree
        elif userType == "employee":
            employeesId = studentID
            #Check if Student ID exist, if it does, check if the password matches(line 40)
            if employeesId == 'user@example.com' and studentPassword  == 'password1234':
                # If the credentials are valid, redirect to the student home page
                return redirect(url_for('employee_home', studentID=studentID))        
            else:
                # If the credentials are invalid, show an error message
                error_message = 'Invalid StudentID or password'
                return render_template('index.html', error_message=error_message)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        studentName = request.form.get("name")
        studentPhone = request.form.get("phone")
        studentEmail = request.form.get("email")
        studentAddress = request.form.get("address")
        studentInstitutionName = request.form.get("school")
        studentAcademicLevel = request.form.get("year")
        studentDOB = request.form.get("dob")
        studentSexualOrientation = request.form.get("sexual-orientation")
        studentAgeGroup = request.form.get("age-group")
        studentRace = request.form.get("race")
        studentAreaOfInterest = request.form.get("area-of-interest")
        studentGPA = request.form.get("gpa")
        studentMaritalStatus = request.form.get("marital-status")
        studentHousingCondition = request.form.get("housing-condition")
        studentFamilySize = request.form.get("family-size")
        studentParentalMaritalStatus = request.form.get("parental-marital-status")
        studentEducationOfMother = request.form.get("education-mother")
        studentEducationOfFather = request.form.get("education-father")
        studentPassword = request.form.get("password")

        #TO DO store the data in the B Tree and Hash Table

        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        studentIds = "0000001"

        return render_template('succesfully-registered.html', name = studentName, ID=studentIds)
    return render_template('register.html')

@app.route('/register-OBO', methods=['GET', 'POST'])
def register_OBO():
    if request.method == "POST":
        studentName = request.form.get("name")
        studentPhone = request.form.get("phone")
        studentEmail = request.form.get("email")
        studentAddress = request.form.get("address")
        studentInstitutionName = request.form.get("school")
        studentAcademicLevel = request.form.get("year")
        studentDOB = request.form.get("dob")
        studentSexualOrientation = request.form.get("sexual-orientation")
        studentAgeGroup = request.form.get("age-group")
        studentRace = request.form.get("race")
        studentAreaOfInterest = request.form.get("area-of-interest")
        studentGPA = request.form.get("gpa")
        studentMaritalStatus = request.form.get("marital-status")
        studentHousingCondition = request.form.get("housing-condition")
        studentFamilySize = request.form.get("family-size")
        studentParentalMaritalStatus = request.form.get("parental-marital-status")
        studentEducationOfMother = request.form.get("education-mother")
        studentEducationOfFather = request.form.get("education-father")

        #TO DO store the data in the B Tree and Hash Table

        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        studentIds = "0000001"

        return render_template('succesfully-registered-obo.html', name = studentName, ID=studentIds)
    return render_template('register-OBO.html')

@app.route('/student-home', methods=['GET'])
def student_home():
    #TO DO GET FIRST AND LAST NAME from the Hash Table according to the student ID
    studentID = request.args.get('studentID') # Get the studentID from the URL parameter
    name = "First Last"
    print(name)
    print(studentID)
    return render_template('student-home.html', name=name, studentID=studentID)

@app.route('/employee-home', methods=['GET'])
def employee_home():
    
    #TO DO GET FIRST AND LAST NAME from the B Tree according to the student ID
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

        #To DO store the data in the B Tree and Hash Table
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
        #Return student name and ID
        name = "student name"

        return render_template('survey-submitted.html', name = name, ID=ID)
    return render_template('survey.html')

@app.route('/deleted', methods=['GET'])
def account_deleted():
    return render_template('account-deleted.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    #TO DO:
    studentID = request.args.get('studentID')

    ID = studentID
    #Query the variable based on the ID to get the following info
    #name = search student ID get their name
    name = "First Last"
    address = "Gainesville, FL 32611"
    phone = "012-345-6789"
    email = "email@ufl.edu"
    school = "University Of Florida"
    year = "Freshman"
    dob = "2000-01-01" #Must be in this format!!
    print(studentID)

    if request.method == 'POST':
        action = request.form['action']
        if action == 'update':
            # handle update action
            print("update")
            #name = search student ID get their name
            #update value on dataset
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

@app.route('/update-student-profile', methods=['GET', 'POST'])
def update_student_profile():
    #TO DO:
    #Query the variable to get the following info
    #name = search student ID get their name
    student_id = request.args.get('student_info')
    ID = student_id
    name = "First Last"
    address = "Gainesville, FL 32611"
    phone = "012-345-6789"
    email = "email@ufl.edu"
    school = "University Of Florida"
    year = "Freshman"
    dob = "2000-01-01" #Must be in this format!!
    ID = "0000001"
    urgencyLevel = 0.01
    if request.method == 'POST':
        action = request.form['action']
        if action == 'update':
            # handle update action
            print("update")
            #name = search student ID get their name
            #update value on dataset

            address = request.form.get("address")
            phone = request.form.get("phone")
            year = request.form.get("year")
            
            #TO DO:
            # Update user profile
            return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)    

        elif action == 'delete':
            #TO DO:
            # Delete user profile
            print("delete")
            return render_template('account-deleted.html')
        elif action == 'back':
            return redirect(url_for('employee_home'))        
    return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)

@app.route('/search-student', methods=['GET', 'POST'])
def search_student():
    # Get the student ID from the form
    if request.method == 'POST':
        
        student_id = request.form['student-id']
        #TO DO Search Student    
        #If found:
        if student_id == "0000001":
            return redirect(url_for('update_student_profile', student_id=student_id))
        #If not found
        else:
            error_message = 'Invalid StudentID: ' + student_id
            return render_template('search-student.html', error_message=error_message)
    return render_template('search-student.html')

if __name__ == '__main__':    
    app.run()