from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from hash_table import HashTable
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session
# TO DO
# Read and store the datasets in a variable to be used by the application below

#Hash Table

hash_table = HashTable();


#B-Tree need to store Student ID created by Hash Function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    print("home")
    if 'studentID' in session:
        session.pop('studentID', None)  # Clear studentID from session if it exists
    if 'employeeID' in session:
        session.pop('employeeID', None)  # Clear studentID from session if it exists
    if request.method == 'POST':
        # Gets the user's input StudentID and password
        studentID = request.form['studentID']
        studentPassword  = request.form['password']
        userType = request.form['user-type']
        print(studentID)
        print(studentPassword)
        #TO DO:
        #If student, go to the Hash Table
        if userType == "student":
            student_information = hash_table.get(studentID)

            studentIds = studentID
            print(student_information)
            #Check if the StudentID and password match some stored credentials
            #Check if Student ID exist, if it does, check if the password matches (line 30)
            if student_information is not None:
                print(student_information[5])
                print(student_information[4])
                if studentIds == student_information[4] and studentPassword == student_information[5]:
                    # If the credentials are valid, redirect to the student home page
                    session['studentID'] = studentIds
                    return redirect(url_for('student_home', studentID=studentIds))     
                else:
                    # If the credentials are invalid, show an error message
                    error_message = 'Invalid StudentID or password'
                    return render_template('index.html', error_message=error_message)   
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
                session['employeeID'] = employeesId
                return redirect(url_for('employee_home', employeesId=employeesId))        
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
        hash_table.ID += 1
        studentIds = "DD" + str(hash_table.ID)
        student_list = [studentName, studentPhone, studentEmail, studentAddress, studentIds,
                        studentPassword, datetime.date.today(), studentSexualOrientation,
                        studentAgeGroup, studentRace, studentDOB, studentAreaOfInterest,
                        studentInstitutionName, studentAcademicLevel, studentGPA, studentMaritalStatus,
                        studentHousingCondition, studentFamilySize, studentParentalMaritalStatus, studentEducationOfMother,
                        studentEducationOfFather]

        hash_table.put(studentIds, student_list)

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
        # Hash Table
        hash_table.ID += 1
        studentIds = "DD" + str(hash_table.ID)
        student_list = [studentName, studentPhone, studentEmail, studentAddress, studentIds,
                        "N/A", datetime.date.today(), studentSexualOrientation,
                        studentAgeGroup, studentRace, studentDOB, studentAreaOfInterest,
                        studentInstitutionName, studentAcademicLevel, studentGPA, studentMaritalStatus,
                        studentHousingCondition, studentFamilySize, studentParentalMaritalStatus,
                        studentEducationOfMother,
                        studentEducationOfFather, 0.0]
        hash_table.put(studentIds, student_list)

        # TO DO: 
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below


    return render_template('succesfully-registered-obo.html', name = studentName, ID=studentIds)

@app.route('/student-home', methods=['GET'])
def student_home():
    #TO DO GET FIRST AND LAST NAME from the Hash Table according to the student ID
    studentIds = session.get('studentID')
    print(studentIds)
    student_information = hash_table.get(studentIds)
    name = student_information[0]

    return render_template('student-home.html', name=name, studentID=studentIds)

@app.route('/employee-home', methods=['GET'])
def employee_home():    
    #TO DO GET FIRST AND LAST NAME from the B Tree according to the employeesId
    employeesId = session.get('employeeID')

    name = "First Last"
    return render_template('employee-home.html', name=name)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    studentID = session.get('studentID')
    print(studentID)
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
        #Hash Map
        student_information = hash_table.get(studentID)
        survey_information = [depressedMood, depressedHopeless, lossOfInterestAndEnjoyment, lossOfPleasureAndEnjoyment,
                              lessenedEnergy, lessenedActive, reducedDecisionMaking, reducedConcentration, reducedSelfConfidence,
                              reducedSelfEsteem, ideasOfGuilt, ideasOfUnworthiness, bleakViewsOfTheFuture, pessimisticViewsOfTheFuture,
                              ideasOrActsOfSelfHarmOrSuicide, disturbedSleep, diminishedAppetite, understandingParent, missedClasses,
                              smokeDrink, lostRelative, relationshipTrouble, plagrisedHw, leftJob, takingMedication, diagnosedBefore]
        student_information.extend(survey_information)



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

        return redirect(url_for('survey_submitted', studentID=studentID))      
    return render_template('survey.html', studentID=studentID)

@app.route('/survey-submitted', methods=['GET', 'POST'])
def survey_submitted():
    studentID = session.get('studentID')
    print(studentID)
    # TO DO: 
    #Return student name from ID
    student_information = hash_table.get(studentID)
    name = student_information[0]
    return render_template('survey-submitted.html', name = name, studentID=studentID)

@app.route('/deleted', methods=['GET'])
def account_deleted():
    return render_template('account-deleted.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    #TO DO:
    studentID = session.get('studentID')
    # studentID = request.args.get('studentID')

    #Hash Table
    student_information = hash_table.get(studentID)


    ID = studentID
    #Query the variable based on the ID to get the following info
    #name = search student ID get their name
    name = student_information[0]
    address = student_information[3]
    phone = student_information[1]
    email = student_information[2]
    school = student_information[12]
    year = student_information[13]
    dob = student_information[10] #Must be in this format!!
    if studentID == None:
        studentID = ID
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
            #Hash Table
            student_information[3] = address
            student_information[1] = phone
            student_information[13] = year
            return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)    

        elif action == 'delete':
            #TO DO:
            # Delete user profile
            #Hash Table
            hash_table.remove(studentID)
            print("delete")
            if 'studentID' in session:
                session.pop('studentID', None)  # Clear studentID from session if it exists
            return render_template('account-deleted.html')
        elif action == 'back':
            return redirect(url_for('student_home'))        
    return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)

@app.route('/update-student-profile', methods=['GET', 'POST'])
def update_student_profile():
    #TO DO:
    #Query the variable to get the following info
    #name = search student ID get their name
    studentID = session.get('studentID')

    #Hash Table
    student_information = hash_table.get(studentID)

    # studentID = session.get('studentID')

    employeesId = session.get('employeeID')
    print(studentID)
    print(employeesId)
    ID = studentID
    name = student_information[0]
    address = student_information[3]
    phone = student_information[1]
    email = student_information[2]
    school = student_information[12]
    year = student_information[13]
    dob = student_information[10] #Must be in this format!!
    ID = student_information[4]
    urgencyLevel = student_information[-1]
    if request.method == 'POST':
        student_id = request.args.get('student_info')
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
            #Hash Table
            student_information[3] = address
            student_information[1] = phone
            student_information[13] = year

            return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)    

        elif action == 'delete':
            #TO DO:
            # Delete user profile

            #Hash Table
            hash_table.remove(studentID)
            print("delete")
            return render_template('account-deleted-OBO.html')
        elif action == 'back':
            return redirect(url_for('employee_home'))        
    return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)

@app.route('/search-student', methods=['GET', 'POST'])
def search_student():
    # Get the student ID from the form
    if request.method == 'POST':
        
        studentID = request.form['student-id']
        print(studentID)

        #TO DO Search Student
        #Hash Table
        student_information = hash_table.get(studentID)

        #If found:
        if studentID == student_information[4]:
            session['studentID'] = studentID
            return redirect(url_for('update_student_profile', studentID=studentID))
        #If not found
        else:
            error_message = 'Invalid StudentID: ' + studentID
            return render_template('search-student.html', error_message=error_message)
    return render_template('search-student.html')

if __name__ == '__main__':    
    app.run()