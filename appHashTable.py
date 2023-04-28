from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from hash_table import HashTable
from datetime import datetime
import pandas as pd
import numpy as np
import time
import random
import csv
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session

#Hash Table

hash_table = HashTable()

with open('Data/fake_mentalHealth_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for idx, row in enumerate(csv_reader):
        hash_table.put(row[4], row)
        hash_table.ID = idx + 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
       
    if 'studentID' in session:
        session.pop('studentID', None)  # Clear studentID from session if it exists
    if 'employeeID' in session:
        session.pop('employeeID', None)  # Clear studentID from session if it exists
    if request.method == 'POST':
        # Gets the user's input StudentID and password
        studentID = request.form['studentID']
        studentPassword  = request.form['password']
        userType = request.form['user-type']

        if userType == "student":
            student_information = hash_table.get(studentID)
            
            studentIds = studentID
            print(student_information)
            #Check if the StudentID and password match some stored credentials

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
        #If employee, go to the Hash Table
        elif userType == "employee":
            
            temp_eid_list = ['E5', 'E6', 'E3', 'E2', 'E1', 'E4']

            employeesId = studentID
            #Check if Employee ID exist, if it does, check if the HARDCODED password matches(line 40)
            # currently employee can't create an account. By design decision.
            if (employeesId  in temp_eid_list) and studentPassword  == 'e1234':
                # If the credentials are valid, redirect to the student home page
                session['employeeID'] = employeesId
                return redirect(url_for('employee_home', employeesId=employeesId))        
            else:
                # If the credentials are invalid, show an error message
                error_message = 'Invalid EmployeeID or password'
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
        
        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below
        hash_table.ID += 1
        studentIds = "DD" + str(hash_table.ID)

        #prep to include items in the btree & df
        # randomly assign employees
        temp_eid_list = ['E5', 'E6', 'E3', 'E2', 'E1', 'E4']
        temp_enam_list = ['Kinder, Rachael',
                        'Schenally, Ashley',
                        'Rivera, Yolotzi',
                        'Edwards, Cacia',
                        'Saiz, Antonio',
                        'Mccarty, Nicolette']

        employeeId = random.choice(temp_eid_list)
        employeeName = random.choice(temp_enam_list)

        #----James Code--------
        student_list = [studentName, studentPhone, studentEmail, studentAddress, studentIds,
                        studentPassword, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), studentSexualOrientation,
                        studentAgeGroup, studentRace, studentDOB, studentAreaOfInterest,
                        studentInstitutionName, studentAcademicLevel, studentGPA, studentMaritalStatus,
                        studentHousingCondition, studentFamilySize, studentParentalMaritalStatus,
                        studentEducationOfMother,
                        studentEducationOfFather, employeeId, employeeName]
        t0 = time.time()
        hash_table.put(studentIds, student_list)
        t1 = time.time()
        print("\nTotal time to insert single datum: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")
        
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
        
        # studentIds = "DD" + str(df_global_nrows +1)
        hash_table.ID += 1
        studentIds = "DD" + str(hash_table.ID)               
        
        #prep to include items in the btree & df
        # randomly assign employees
        temp_eid_list = ['E5', 'E6', 'E3', 'E2', 'E1', 'E4']
        temp_enam_list = ['Kinder, Rachael',  
                        'Schenally, Ashley',
                        'Rivera, Yolotzi',  
                        'Edwards, Cacia',   
                        'Saiz, Antonio',   
                        'Mccarty, Nicolette']

        employeeId = random.choice(temp_eid_list)
        employeeName = random.choice(temp_enam_list)        
        
        #------James' Code-------------
        student_list = [studentName, studentPhone, studentEmail, studentAddress, studentIds,
                        "NA", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), studentSexualOrientation,
                        studentAgeGroup, studentRace, studentDOB, studentAreaOfInterest,
                        studentInstitutionName, studentAcademicLevel, studentGPA, studentMaritalStatus,
                        studentHousingCondition, studentFamilySize, studentParentalMaritalStatus,
                        studentEducationOfMother,
                        studentEducationOfFather, employeeId, employeeName]
        t0 = time.time()
        hash_table.put(studentIds, student_list)
        t1 = time.time()
        print("\nTotal time to insert single datum: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")


        return render_template('succesfully-registered-obo.html', name = studentName, ID=studentIds)
    return render_template('register-OBO.html')

@app.route('/student-home', methods=['GET'])
def student_home():
    studentIds = session.get('studentID')

    student_information = hash_table.get(studentIds)
    name = student_information[0]    
    
    return render_template('student-home.html', name=name, studentID=studentIds)

@app.route('/employee-home', methods=['GET'])
def employee_home():
    #Get employee name from the B Tree according to the employeesId
    employeesId = session.get('employeeID')
    name = "First Last"
    
    temp_enam_list = {'E5': 'Kinder, Rachael',  
                      'E6': 'Schenally, Ashley',
                      'E3': 'Rivera, Yolotzi',  
                      'E2': 'Edwards, Cacia',   
                      'E1': 'Saiz, Antonio',   
                      'E4': 'Mccarty, Nicolette'}
    
    for eid, ename in temp_enam_list.items():
      if str(eid) == str(employeesId):
          name = ename
          break
        
    return render_template('employee-home.html', name=name)


def to_bool(s):
    return 1 if s == 'true' else 0


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    
    studentID = session.get('studentID')

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

        index = [0] # you can change the value in the list to set a different index value

        df_survey = pd.DataFrame({
        'depressedMood': to_bool(depressedMood),
        'depressedHopeless': to_bool(depressedHopeless),
        'lossOfInterestAndEnjoyment': to_bool(lossOfInterestAndEnjoyment),
        'lossOfPleasureAndEnjoyment': to_bool(lossOfPleasureAndEnjoyment),
        'lessenedEnergy': to_bool(lessenedEnergy),
        'lessenedActive': to_bool(lessenedActive),
        'reducedDecisionMaking': to_bool(reducedDecisionMaking),
        'reducedConcentration': to_bool(reducedConcentration),
        'reducedSelfConfidence': to_bool(reducedSelfConfidence),
        'reducedSelfEsteem': to_bool(reducedSelfConfidence),
        'ideasOfGuilt': to_bool(ideasOfGuilt),
        'ideasOfUnworthiness': to_bool(ideasOfUnworthiness),
        'bleakViewsOfTheFuture': to_bool(bleakViewsOfTheFuture),
        'pessimisticViewsOfTheFuture': to_bool(pessimisticViewsOfTheFuture),
        'ideasOrActsOfSelfHarmOrSuicide': to_bool(ideasOrActsOfSelfHarmOrSuicide),
        'disturbedSleep': to_bool(disturbedSleep),
        'diminishedAppetite': to_bool(diminishedAppetite),
        'understandingParent': to_bool(understandingParent),
        'missedClasses': to_bool(missedClasses),
        'smokeDrink': to_bool(smokeDrink),
        'lostRelative': to_bool(lostRelative),
        'relationshipTrouble': to_bool(relationshipTrouble),
        'plagrisedHw': to_bool(plagrisedHw),
        'leftJob': to_bool(leftJob),
        'takingMedication': to_bool(takingMedication),
        'diagnosedBefore': to_bool(diagnosedBefore),
        'urgencyLevel': 0.0}, index=[0])

        # Loop through rows in df_temp.
        #Suggestion, depending on the average range, we could assign qualitative values instead of quantitative: High (>=0.7), Medium (0.7 > x > 0.4, Average (0.4 > x >= 0.25, Low (<0.25)
        # See line 20 for another suggestion
        for index, row in df_survey.iterrows():
            # Extract values for 'b', 'c', 'd', and 'e' in current row
            ideasOrActsOfSelfHarmOrSuicide = row["ideasOrActsOfSelfHarmOrSuicide"]       
            if ideasOrActsOfSelfHarmOrSuicide >= 1:
                df_survey.at[index, 'urgencyLevel'] = 1.0
                normalized_avg = 1.0
            else:
                symptoms = row.tolist()[:-1]  # exclude 'urgencyLevel' column
                # Calculate average of symptom values in df_temp
                avg = sum(symptoms) / len(symptoms)        
                # Check if denominator is not zero
                if max(symptoms) - min(symptoms) > 0:
                    # Normalize average value to be between 0.00 and 1.00
                    normalized_avg = (avg - min(symptoms)) / (max(symptoms) - min(symptoms))
                else:
                    # Set normalized average value to NaN if denominator is zero
                    normalized_avg = np.nan
                df_survey.at[index, 'urgencyLevel'] = normalized_avg

        #------ James' Code--------
        student_information = hash_table.get(studentID)
        # print("----Hash Map-----")
        # print(student_information[0])
        survey_information = [depressedMood, depressedHopeless, lossOfInterestAndEnjoyment, lossOfPleasureAndEnjoyment,
                              lessenedEnergy, lessenedActive, reducedDecisionMaking, reducedConcentration,
                              reducedSelfConfidence,
                              reducedSelfEsteem, ideasOfGuilt, ideasOfUnworthiness, bleakViewsOfTheFuture,
                              pessimisticViewsOfTheFuture,
                              ideasOrActsOfSelfHarmOrSuicide, disturbedSleep, diminishedAppetite, understandingParent,
                              missedClasses,
                              smokeDrink, lostRelative, relationshipTrouble, plagrisedHw, leftJob, takingMedication,
                              diagnosedBefore, normalized_avg]
        t0 = time.time()
        student_information.extend(survey_information)
        t1 = time.time()

        print("\nTotal time to update data: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")
        
        return redirect(url_for('survey_submitted', studentID=studentID))      
    return render_template('survey.html', studentID=studentID)

@app.route('/survey-submitted', methods=['GET', 'POST'])
def survey_submitted():
    studentID = session.get('studentID')

    student_information = hash_table.get(studentID)
    name = student_information[0]
    #Return student name from ID
    return render_template('survey-submitted.html', name = name, studentID=studentID)

@app.route('/deleted', methods=['GET'])
def account_deleted():
    return render_template('account-deleted.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    studentID = session.get('studentID')

    ID = studentID
   
    # ----- James' Code --------
    # Hash Table
    student_information = hash_table.get(studentID)
    name = student_information[0]
    address = student_information[3]
    phone = student_information[1]
    email = student_information[2]
    school = student_information[12]
    year = student_information[13]
    date_string = student_information[10]
    date_format = "%Y-%m-%d"
    dt = datetime.strptime(date_string.split()[0], "%Y-%m-%d")
    dob = dt.strftime(date_format)  # Must be in this format!!

    if studentID == None:
        studentID = ID
    print(studentID)
    if request.method == 'POST':
        action = request.form['action']
        if action == 'update':
            # handle update action

            #name = search student ID get their name
            #update value on dataset
            address = request.form.get("address")
            phone = request.form.get("phone")
            year = request.form.get("year")            

            t0 = time.time()
            # Hash Table Update user profile
            student_information[3] = address
            student_information[1] = phone
            student_information[13] = year
            t1 = time.time()

            print("\nTotal time to update data: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")
            
            return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school, year=year, dob=dob, ID = ID)    

        elif action == 'delete':
            
            # Delete user profile
            if 'studentID' in session:                         
                session.pop('studentID', None)  # Clear studentID from session if it exists

                # Hash Table Delete user profile
                t0 = time.time()
                hash_table.remove(studentID)
                t1 = time.time()

                print("\nTotal time to delete single datum: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")

            return render_template('account-deleted.html')
        elif action == 'back':
            return redirect(url_for('student_home'))        
    return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)

@app.route('/update-student-profile', methods=['GET', 'POST'])
def update_student_profile():    
    studentID = session.get('studentID')
    # Hash Table
    student_information = hash_table.get(studentID)

    employeesId = session.get('employeeID')

    ID = studentID
    #Jamse Code
    name = student_information[0]
    address = student_information[3]
    phone = student_information[1]
    email = student_information[2]
    school = student_information[12]
    year = student_information[13]
    date_string = student_information[10]
    date_format = "%Y-%m-%d"
    dt = datetime.strptime(date_string.split()[0], "%Y-%m-%d")
    dob = dt.strftime(date_format)  # Must be in this format!!
    ID = student_information[4]
    urgencyLevel = student_information[-1]
    
    temp_enam_list = ['Kinder, Rachael',  
                      'Schenally, Ashley',
                      'Rivera, Yolotzi',  
                      'Edwards, Cacia',   
                      'Saiz, Antonio',   
                      'Mccarty, Nicolette']
    if urgencyLevel in temp_enam_list:
            tempUrgencyLevel = "Survey not Submitted"   
            urgencyLevel  = tempUrgencyLevel       
    else:      
        tempUrgencyLevel = float(urgencyLevel)
        if type(tempUrgencyLevel) == str: 
            urgencyLevel = "Survey not Submitted"
        elif tempUrgencyLevel >=0.85: 
            urgencyLevel = "Extreme"
        elif tempUrgencyLevel >=0.7: 
            urgencyLevel = "High"
        elif tempUrgencyLevel >=0.3: 
            urgencyLevel = "Medium"
        else: urgencyLevel = "Low"

    student_information = hash_table.get(studentID)

    if request.method == 'POST':
        action = request.form['action']
        if action == 'update':
          
            address = request.form.get("address")
            phone = request.form.get("phone")
            year = request.form.get("year")

            t0 = time.time()
            # Hash Table
            student_information[3] = address
            student_information[1] = phone
            student_information[13] = year
            t1 = time.time()
            print("\nTotal time to update data: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")
            
            return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)    

        elif action == 'delete':     
            t0 = time.time()
            # Hash Table
            hash_table.remove(studentID)
            t1 = time.time()
            print("\nTotal time to delete single data: {:.05f} seconds for Hash Map: ".format(t1 - t0), "\n\n")
            
            return render_template('account-deleted-OBO.html')
        elif action == 'back':
            return redirect(url_for('employee_home'))        
    return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)

@app.route('/search-student', methods=['GET', 'POST'])
def search_student():
    # Get the student ID from the form
    if request.method == 'POST':
        
        studentID = request.form['student-id']
        # Hash Table
        student_information = hash_table.get(studentID)
        if student_information is not None:
            if studentID == student_information[4]:
                session['studentID'] = studentID
                return redirect(url_for('update_student_profile', studentID=studentID))
            else:
                error_message = 'Invalid StudentID: ' + studentID
                return render_template('search-student.html', error_message=error_message)
        #If not found
        else:
            error_message = 'Invalid StudentID: ' + studentID
            return render_template('search-student.html', error_message=error_message)
        
    return render_template('search-student.html')

@app.route('/backup', methods=['GET'])
def backup():
    
    return redirect(url_for('employee_home'))    


if __name__ == '__main__':   
       
    app.run()
