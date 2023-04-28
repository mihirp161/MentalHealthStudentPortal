from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
import numpy as np
import time
import random
from datetime import datetime
import project3a_BTree as b3

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session


#B-Tree need to store Student ID created by Hash Function

#other global vars (counter for studentID)
df_global_nrows = 0

# Read and store the datasets in a variable to be used by the application below
B = b3.BTree(500)

df_global = pd.DataFrame(columns=["studentName",
                            "studentPhone",
                            "studentEmail",
                            "studentAddress",
                            "studentIds",
                            "studentPassword",
                            "studentVisitDateTime",
                            "studentSexualOrientation",
                            "studentAgeGroup",
                            "studentRace",
                            "studentDOB",
                            "studentAreaOfInterest",
                            "studentInstitutionName",
                            "studentAcademicLevel",
                            "studentGPA",
                            "studentMaritalStatus",
                            "studentHousingCondition",
                            "studentFamilySize",
                            "studentParentalMaritalStatus",
                            "studentEducationOfMother",
                            "studentEducationOfFather",
                            "employeesId",
                            "employeesName",
                            "depressedMood",
                            "depressedHopeless",
                            "lossOfInterestAndEnjoyment",
                            "lossOfPleasureAndEnjoyment",
                            "lessenedEnergy",
                            "lessenedActive",
                            "reducedDecisionMaking",
                            "reducedConcentration",
                            "reducedSelfConfidence",
                            "reducedSelfEsteem",
                            "ideasOfGuilt",
                            "ideasOfUnworthiness",
                            "bleakViewsOfTheFuture",
                            "pessimisticViewsOfTheFuture",
                            "ideasOrActsOfSelfHarmOrSuicide",
                            "disturbedSleep",
                            "diminishedAppetite",
                            "understandingParent",
                            "missedClasses",
                            "smokeDrink",
                            "lostRelative",
                            "relationshipTrouble",
                            "plagrisedHw",
                            "leftJob",
                            "takingMedication",
                            "diagnosedBefore",
                            "urgencyLevel"])



#-----------------------------------------------------------------------------------

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

        #TO DO:
        #If student, go to the B_Tree
        if userType == "student":
            
            studentIds = studentID
            #Check if the StudentID and password match some stored credentials
            
            if (B.get_keys_value(k = studentID, v = 'studentIds') != None):                
                
                if str(studentPassword)  == str(B.get_keys_value(k = studentID, v = 'studentPassword')):
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
        
        global df_global_nrows
        global df_global
        
        studentIds = "DD" + str(df_global_nrows +1)
        
        df_global_nrows = df_global_nrows + 1
        
        
        #prep to include items in the btree & df
        # randomly assign employees
        temp_eid_list = ['E5', 'E6', 'E3', 'E2', 'E1', 'E4']
        temp_enam_list = ['Kinder, Rachael',  
                        'Schenally, Ashley',
                        'Rivera, Yolotzi',  
                        'Edwards, Cacia',   
                        'Saiz, Antonio',   
                        'Mccarty, Nicolette']
        
        df_temp = pd.DataFrame({'studentName': [studentName],
                                'studentPhone': [studentPhone],
                                'studentEmail': [studentEmail],
                                'studentAddress': [studentAddress],
                                'studentIds': [studentIds],
                                'studentPassword': [studentPassword],
                                'studentInstitutionName': [studentInstitutionName],
                                'studentAcademicLevel': [studentAcademicLevel],
                                'studentSexualOrientation': [studentSexualOrientation],
                                'studentAgeGroup': [studentAgeGroup],
                                'studentRace': [studentRace],
                                'studentAreaOfInterest': [studentAreaOfInterest],
                                'studentGPA': [studentGPA],
                                'studentMaritalStatus': [studentMaritalStatus],
                                'studentHousingCondition': [studentHousingCondition],
                                'studentFamilySize': [studentFamilySize],
                                'studentParentalMaritalStatus': [studentParentalMaritalStatus],
                                'studentEducationOfMother': [studentEducationOfMother],
                                'studentEducationOfFather': [studentEducationOfFather],
                                'studentVisitDateTime': [pd.Timestamp(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))],
                                'studentDOB': [pd.Timestamp(datetime.strptime(studentDOB + " 00:00:00", "%Y-%m-%d %H:%M:%S"))],
                                'employeesId': [random.choice(temp_eid_list)],
                                'employeesName': [random.choice(temp_enam_list)],
                                'depressedMood': [-1], 
                                'depressedHopeless': [-1],
                                'lossOfInterestAndEnjoyment': [-1],
                                'lossOfPleasureAndEnjoyment': [-1],
                                'lessenedEnergy': [-1],
                                'lessenedActive': [-1],
                                'reducedDecisionMaking': [-1],
                                'reducedConcentration': [-1], 
                                'reducedSelfConfidence': [-1], 
                                'reducedSelfEsteem': [-1], 
                                'ideasOfGuilt': [-1], 
                                'ideasOfUnworthiness': [-1], 
                                'bleakViewsOfTheFuture': [-1], 
                                'pessimisticViewsOfTheFuture': [-1], 
                                'ideasOrActsOfSelfHarmOrSuicide': [-1],
                                'disturbedSleep': [-1], 
                                'diminishedAppetite': [-1], 
                                'understandingParent': [-1], 
                                'missedClasses': [-1], 
                                'smokeDrink': [-1], 
                                'lostRelative': [-1],
                                'relationshipTrouble': [-1], 
                                'plagrisedHw': [-1], 
                                'leftJob': [-1], 
                                'takingMedication': [-1], 
                                'diagnosedBefore': [-1], 
                                'urgencyLevel': [0]
                                      })
        
        #update the dataframe
        df_global = pd.concat([df_global, df_temp], axis=0)
        df_global.reset_index(drop=True, inplace=True)
                

        df_temp.set_index("studentIds", drop=False, inplace=True)
        temp_dict = df_temp.to_dict(orient="index")
        
        t0 = time.time()
                
        for p_id, p_info in temp_dict.items():
            B.insert((hash(p_id), p_id, p_info))
            
        t1 = time.time()
         
        print("\nTotal time to insert single datum: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
         
        #---------------------------
        
        df_global.loc[df_global['studentIds'] == studentIds].to_excel("Data/fake_mentalHealth_data_CHANGES.xlsx", index=False)
        #---------------------------
        
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
        

        #store the data in the B Tree

        # Create student obj using the variables above, insert it to your data structure created before @app.route('/')
        # Return its ID to the variable below 
        
        global df_global_nrows
        global df_global
        
        studentIds = "DD" + str(df_global_nrows +1)
        
        df_global_nrows = df_global_nrows + 1
        
        
        #prep to include items in the btree & df
        # randomly assign employees
        temp_eid_list = ['E5', 'E6', 'E3', 'E2', 'E1', 'E4']
        temp_enam_list = ['Kinder, Rachael',  
                        'Schenally, Ashley',
                        'Rivera, Yolotzi',  
                        'Edwards, Cacia',   
                        'Saiz, Antonio',   
                        'Mccarty, Nicolette']
        
        df_temp = pd.DataFrame({'studentName': [studentName],
                                'studentPhone': [studentPhone],
                                'studentEmail': [studentEmail],
                                'studentAddress': [studentAddress],
                                'studentIds': [studentIds],
                                'studentPassword': ['NA'],
                                'studentInstitutionName': [studentInstitutionName],
                                'studentAcademicLevel': [studentAcademicLevel],
                                'studentSexualOrientation': [studentSexualOrientation],
                                'studentAgeGroup': [studentAgeGroup],
                                'studentRace': [studentRace],
                                'studentAreaOfInterest': [studentAreaOfInterest],
                                'studentGPA': [studentGPA],
                                'studentMaritalStatus': [studentMaritalStatus],
                                'studentHousingCondition': [studentHousingCondition],
                                'studentFamilySize': [studentFamilySize],
                                'studentParentalMaritalStatus': [studentParentalMaritalStatus],
                                'studentEducationOfMother': [studentEducationOfMother],
                                'studentEducationOfFather': [studentEducationOfFather],
                                'studentVisitDateTime': [pd.Timestamp(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))],
                                'studentDOB': [pd.Timestamp(datetime.strptime(studentDOB + " 00:00:00", "%Y-%m-%d %H:%M:%S"))],
                                'employeesId': [random.choice(temp_eid_list)],
                                'employeesName': [random.choice(temp_enam_list)],
                                'depressedMood': [-1], 
                                'depressedHopeless': [-1],
                                'lossOfInterestAndEnjoyment': [-1],
                                'lossOfPleasureAndEnjoyment': [-1],
                                'lessenedEnergy': [-1],
                                'lessenedActive': [-1],
                                'reducedDecisionMaking': [-1],
                                'reducedConcentration': [-1], 
                                'reducedSelfConfidence': [-1], 
                                'reducedSelfEsteem': [-1], 
                                'ideasOfGuilt': [-1], 
                                'ideasOfUnworthiness': [-1], 
                                'bleakViewsOfTheFuture': [-1], 
                                'pessimisticViewsOfTheFuture': [-1], 
                                'ideasOrActsOfSelfHarmOrSuicide': [-1],
                                'disturbedSleep': [-1], 
                                'diminishedAppetite': [-1], 
                                'understandingParent': [-1], 
                                'missedClasses': [-1], 
                                'smokeDrink': [-1], 
                                'lostRelative': [-1],
                                'relationshipTrouble': [-1], 
                                'plagrisedHw': [-1], 
                                'leftJob': [-1], 
                                'takingMedication': [-1], 
                                'diagnosedBefore': [-1], 
                                'urgencyLevel': [0]
                            })
        
        #update the dataframe
        df_global = pd.concat([df_global, df_temp], axis=0)
        df_global.reset_index(drop=True, inplace=True)
                

        df_temp.set_index("studentIds", drop=False, inplace=True)
        temp_dict = df_temp.to_dict(orient="index")
        
        t0 = time.time()
                 
        for p_id, p_info in temp_dict.items():
            B.insert((hash(p_id), p_id, p_info))
            
        t1 = time.time()
         
        print("\nTotal time to insert single datum: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")      
        
        #---------------------------
        df_global.loc[df_global['studentIds'] == studentIds].to_excel("Data/fake_mentalHealth_data_CHANGES.xlsx", index=False)
        #---------------------------
        
        
        return render_template('succesfully-registered-obo.html', name = studentName, ID=studentIds)
    return render_template('register-OBO.html')

@app.route('/student-home', methods=['GET'])
def student_home():

    studentIds = session.get('studentID')
    name =  B.get_keys_value(k = studentIds, v = 'studentName')
    
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
          break;
        
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
    
        
        global df_global
    
        #To DO store the data in the B Tree
        df_temp = pd.DataFrame({
                                'studentIds': [B.get_keys_value(k = studentID, v = 'studentIds')],
                                'studentVisitDateTime': [pd.Timestamp(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))],
                                'depressedMood': [to_bool(depressedMood)], 
                                'depressedHopeless': [to_bool(depressedHopeless)],
                                'lossOfInterestAndEnjoyment': [to_bool(lossOfInterestAndEnjoyment)],
                                'lossOfPleasureAndEnjoyment': [to_bool(lossOfPleasureAndEnjoyment)],
                                'lessenedEnergy': [to_bool(lessenedEnergy)],
                                'lessenedActive': [to_bool(lessenedActive)],
                                'reducedDecisionMaking': [to_bool(reducedDecisionMaking)],
                                'reducedConcentration': [to_bool(reducedConcentration)], 
                                'reducedSelfConfidence': [to_bool(reducedSelfConfidence)], 
                                'reducedSelfEsteem': [to_bool(reducedSelfEsteem)], 
                                'ideasOfGuilt': [to_bool(ideasOfGuilt)], 
                                'ideasOfUnworthiness': [to_bool(ideasOfUnworthiness)], 
                                'bleakViewsOfTheFuture': [to_bool(bleakViewsOfTheFuture)], 
                                'pessimisticViewsOfTheFuture': [to_bool(pessimisticViewsOfTheFuture)], 
                                'ideasOrActsOfSelfHarmOrSuicide': [to_bool(ideasOrActsOfSelfHarmOrSuicide)],
                                'disturbedSleep': [to_bool(disturbedSleep)], 
                                'diminishedAppetite': [to_bool(diminishedAppetite)], 
                                'understandingParent': [to_bool(understandingParent)], 
                                'missedClasses': [to_bool(missedClasses)], 
                                'smokeDrink': [to_bool(smokeDrink)], 
                                'lostRelative': [to_bool(lostRelative)],
                                'relationshipTrouble': [to_bool(relationshipTrouble)], 
                                'plagrisedHw': [to_bool(plagrisedHw)], 
                                'leftJob': [to_bool(leftJob)], 
                                'takingMedication': [to_bool(takingMedication)], 
                                'diagnosedBefore': [to_bool(diagnosedBefore)], 
                                'urgencyLevel': [-1.0]
                                })
        
        #update the dataframe
        df_temp = df_temp.astype(df_global[df_global.columns[df_global.columns.isin(df_temp.columns)]].dtypes)
        
        
        df_temp.reset_index(drop=True, inplace=True)
        df_global.reset_index(drop=True, inplace=True)
        
        df_temp.set_index("studentIds", drop=False, inplace=True)
        df_global.set_index("studentIds", drop=False, inplace=True)
        
        df_global.update(df_temp)
        df_global.set_index("studentIds", drop=False, inplace=True)
        
        

        # Convert 'urgencyLevel' column to float
        df_global['urgencyLevel'] = df_global['urgencyLevel'].astype(float)
        
        # Loop through rows in df.
        for index, row in df_global.loc[:, 'depressedMood':'urgencyLevel'].iterrows():
            ideasOrActsOfSelfHarmOrSuicide = row["ideasOrActsOfSelfHarmOrSuicide"]
            
            if ideasOrActsOfSelfHarmOrSuicide >= 1:
                df_global.at[index, 'urgencyLevel'] = 1.0
            else:
                symptoms = row.tolist()[:-1]  # exclude 'urgencyLevel' column
                
                # Calculate average of symptom values in df_global
                avg = sum(symptoms) / len(symptoms)
                
                # Check if denominator is not zero
                if max(symptoms) - min(symptoms) > 0:
                    # Normalize average value to be between 0.00 and 1.00
                    normalized_avg = (avg - min(symptoms)) / (max(symptoms) - min(symptoms))
                else:
                    # Set normalized average value to NaN if denominator is zero
                    normalized_avg = np.nan
                
                # Assign normalized average value to 'urgencyLevel' in df_global
                df_global.at[index, 'urgencyLevel'] = normalized_avg
        
        # Replace NaN values with 0.00
        df_global['urgencyLevel'].fillna(0.00, inplace=True)
        
        
        df_temp.loc[df_temp['studentIds'] == studentID, 'urgencyLevel'] =  df_global['urgencyLevel'].iloc[-1]

         
        t0 = time.time()
         
        for (col_name, col_value) in df_temp.iteritems():
            B.update_keys(studentID, col_name, col_value.values[0])
        
        t1 = time.time()
         
        print("\nTotal time to update data: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
        
        #B.pull_node_info(studentID)
        
        #---------------------------
        
        df_global.loc[df_global['studentIds'] == studentID].to_excel("Data/fake_mentalHealth_data_CHANGES.xlsx", index=False)
        #---------------------------
        
        return redirect(url_for('survey_submitted', studentID=studentID))      
    return render_template('survey.html', studentID=studentID)

@app.route('/survey-submitted', methods=['GET', 'POST'])
def survey_submitted():
    studentID = session.get('studentID')
    #Return student name from ID
    name = B.get_keys_value(k = studentID, v = 'studentName')
    return render_template('survey-submitted.html', name = name, studentID=studentID)

@app.route('/deleted', methods=['GET'])
def account_deleted():
    return render_template('account-deleted.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    studentID = session.get('studentID')

    ID = studentID
    #Query the variable based on the ID to get the following info
    #name = search student ID get their name
    name = B.get_keys_value(k = studentID, v = 'studentName')
    address =  B.get_keys_value(k = studentID, v = 'studentAddress')
    phone = B.get_keys_value(k = studentID, v = 'studentPhone')
    email = B.get_keys_value(k = studentID, v = 'studentEmail')
    school = B.get_keys_value(k = studentID, v = 'studentInstitutionName')
    year = B.get_keys_value(k = studentID, v = 'studentAcademicLevel') 
    dob = str(datetime.strptime(str(B.get_keys_value(k = studentID, v = 'studentDOB')), "%Y-%m-%d %H:%M:%S").date()) #"YYYY-dd-mm" Must be in this format!!

    if studentID == None:
        studentID = ID
    
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
                         
            # Update user profile
            B.update_keys(studentID, 'studentAddress', address)
            B.update_keys(studentID, 'studentPhone', phone)
            B.update_keys(studentID, 'studentAcademicLevel', year)
            
            t1 = time.time()
             
            print("\nTotal time to update data: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
            
             
            df_global.loc[df_global['studentIds'] == studentID, 'studentAddress'] =  address
            df_global.loc[df_global['studentIds'] == studentID, 'studentPhone'] =  phone
            df_global.loc[df_global['studentIds'] == studentID, 'studentAcademicLevel'] =  year
            
            #---------------------------
            df_global.loc[df_global['studentIds'] == studentID].to_excel("Data/fake_mentalHealth_data_CHANGES.xlsx", index=False)
            #---------------------------
            
            return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school, year=year, dob=dob, ID = ID)    

        elif action == 'delete':
            
            # Delete user profile
            if 'studentID' in session:
                
                
                df_global.drop(df_global.loc[df_global['studentIds']==studentID].index, inplace=True)
                
                
                t0 = time.time()
                 
                B.delete(B.root, hash(studentID))
                
                t1 = time.time()
                 
                print("\nTotal time to delete single datum: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
                
                #---------------------------
                                
                #df_global.to_excel("Data/fake_mentalHealth_data.xlsx", index=False)
                
                #---------------------------                
                
                session.pop('studentID', None)  # Clear studentID from session if it exists
            return render_template('account-deleted.html')
        elif action == 'back':
            return redirect(url_for('student_home'))        
    return render_template('profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID)

@app.route('/update-student-profile', methods=['GET', 'POST'])
def update_student_profile():

    
    studentID = session.get('studentID')


    employeesId = session.get('employeeID')
    print(studentID)
    print(employeesId)
    ID = studentID
    name = B.get_keys_value(k = studentID, v = 'studentName')
    address =  B.get_keys_value(k = studentID, v = 'studentAddress')
    phone = B.get_keys_value(k = studentID, v = 'studentPhone')
    email = B.get_keys_value(k = studentID, v = 'studentEmail')
    school = B.get_keys_value(k = studentID, v = 'studentInstitutionName')
    year = B.get_keys_value(k = studentID, v = 'studentAcademicLevel') 
    dob = str(datetime.strptime(str(B.get_keys_value(k = studentID, v = 'studentDOB')), "%Y-%m-%d %H:%M:%S").date()) #"YYYY-dd-mm" Must be in this format!!
    urgencyLevel = B.get_keys_value(k = studentID, v = 'urgencyLevel') 
    
    
    tempUrgencyLevel = urgencyLevel
    if type(tempUrgencyLevel) == str: urgencyLevel = "Survey not Submitted"
    elif tempUrgencyLevel >=0.85: urgencyLevel = "Extreme"
    elif tempUrgencyLevel >=0.7: urgencyLevel = "High"
    elif tempUrgencyLevel >=0.3: urgencyLevel = "Medium"
    else: urgencyLevel = "Low"
    
    
    
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
            
            
            t0 = time.time()
             
            # Update user profile
            B.update_keys(studentID, 'studentAddress', address)
            B.update_keys(studentID, 'studentPhone', phone)
            B.update_keys(studentID, 'studentAcademicLevel', year)
            
            t1 = time.time()
             
            print("\nTotal time to update data: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
            
            #B.pull_node_info(studentID)
            
            
            df_global.loc[df_global['studentIds'] == studentID, 'studentAddress'] =  address
            df_global.loc[df_global['studentIds'] == studentID, 'studentPhone'] =  phone
            df_global.loc[df_global['studentIds'] == studentID, 'studentAcademicLevel'] =  year
            
            #---------------------------
            
            df_global.loc[df_global['studentIds'] == studentID].to_excel("Data/fake_mentalHealth_data_CHANGES.xlsx", index=False)
            
            #---------------------------
            
            return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)    

        elif action == 'delete':
          
            df_global.drop(df_global.loc[df_global['studentIds']==studentID].index, inplace=True)

            
            t0 = time.time()

            B.delete(B.root, hash(studentID))
            
            t1 = time.time()
             
            print("\nTotal time to delete single data: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
            
            #---------------------------
            
            #df_global.to_excel("Data/fake_mentalHealth_data.xlsx", index=False)
            
            #---------------------------
            
            return render_template('account-deleted-OBO.html')
        elif action == 'back':
            return redirect(url_for('employee_home'))        
    return render_template('update-student-profile.html', name=name, address=address, phone=phone,email=email, school=school,year=year, dob=dob, ID = ID, urgencyLevel=urgencyLevel)

@app.route('/search-student', methods=['GET', 'POST'])
def search_student():
    # Get the student ID from the form
    if request.method == 'POST':
        
        studentID = request.form['student-id']

        #earch Student    
        #If found:
        if B.get_keys_value(k = studentID, v = 'studentIds') != None:
            session['studentID'] = studentID
            return redirect(url_for('update_student_profile', studentID=studentID))
        #If not found
        else:
            error_message = 'Invalid StudentID: ' + studentID
            return render_template('search-student.html', error_message=error_message)
        
    return render_template('search-student.html')

@app.route('/backup', methods=['GET'])
def backup():
    
    # Python function to print "backup"
    #df_global.to_excel("Data/fake_mentalHealth_data.xlsx", index=False)
    
    # You can also return a response to the client if needed
    return redirect(url_for('employee_home'))    


if __name__ == '__main__':
    
    #----------- btree
    df_global = pd.read_excel('Data/fake_mentalHealth_data.xlsx')
    
    df_global.index = range(len(df_global.index))
    
    
    df_global_nrows = int(''.join(filter(str.isdigit, df_global['studentIds'].iloc[-1]) ))   #initial id of the dataframe

    
    df_global.set_index("studentIds", drop=False, inplace=True)
    dict = df_global.to_dict(orient="index")
       
    
    t0 = time.time()
    for p_id, p_info in dict.items():
        B.insert((hash(p_id), p_id, p_info))
    t1 = time.time()
    
    print("\nTotal time to insert data:: {:.05f} seconds for BTREE: ".format(t1-t0), "\n\n")
    #-----------------
    
    app.run()