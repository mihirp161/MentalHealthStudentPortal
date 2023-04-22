options(scipen = 9999)
library(randomNames)
library(openxlsx)
library(data.table)
library(tidyverse)
library(generator)
library(leaflet)

names_many <- randomNames::randomNames(5000000)
name <- sample(names_many[!duplicated(names_many)],size = 100000)   

phone_many <- generator::r_phone_numbers(1000000, use_hyphens = TRUE)

phone <- sample(phone_many[!duplicated(phone_many)],size = 100000) 

email <- paste0(gsub("[[:punct:]]", "", paste0(tolower(gsub("^(.*?),.*", "\\1", name)),
                                               tolower(strtrim(sub('.*,\\s*', '', name), 1)))), "@datadocs.com")


pre_address <- readr::read_csv("FakeNameGenerator.com_c3db0f8e\\FakeNameGenerator.com_c3db0f8e.csv")
cities <- sample(rep(c("Jacksonville",
                       "Tallahassee",
                       "Miami",
                       "Orlando",
                       "St Petersburg",
                       "Tampa",
                       "Fort Lauderdale",
                       "Clearwater",
                       "Hialeah",
                       "Hollywood",
                       "Coral Springs",
                       "Cape Coral",
                       "Daytona Beach"), 5000000), size = 100000)


address <- paste0(pre_address$StreetAddress, ", ", cities,", ", pre_address$ZipCode, "-FL")



userids <- paste0("DD",1:100000)

visitDateTime <- sample(rep(seq(as.POSIXct('2013/01/01'), as.POSIXct('2017/05/01'), by=paste0(sample(1:60, 1), " mins")), 30),
                        size = 100000)

sexualOrientation <- sample(rep(c("Heterosexual", "Bisexual", "Homosexual", "Asexual"), 25000), size = 100000)   
ageGroup <- sample(rep(c("Youth (15-24 years)", "Adults (25-34 years)",
                         "Middle-aged Adults (35-50 years)", "Old-aged Adults (Above 50)"), 25000), size = 100000)

race<- sample(rep(c("Hispanic",
                    "White alone, non-Hispanic",
                    "White alone, Hispanic",
                    "Black or African American alone, non-Hispanic",
                    "Black or African American alone, Hispanic",
                    "American Indian and Alaska Native alone",
                    "Asian alone",
                    "Native Hawaiian and Other Pacific Islander alone",
                    "Some Other Race alone",
                    "Multiracial"), 5000000), size = 100000)

dob <- sample(rep(seq(as.Date('1967/01/01'), as.Date('2008/12/31'), 
                      by=paste0(sample(1:60, 1), " day")), 30000),
              size = 100000)

areaOfInterest <-sample(rep(c("Agriculture, Agriculture Operations, and Related Sciences",
                              "Architecture and Related Services",
                              "Area, Ethnic, Cultural, Gender, and Group Studies",
                              "Aviation",
                              "Biological and Biomedical Sciences",
                              "Business, Management, Marketing, and Related Support Services",
                              "Communication, Journalism, and Related Programs",
                              "Communications Technologies/technicians and Support Services",
                              "Computer and Information Sciences and Support Services",
                              "Construction Trades",
                              "Education",
                              "Engineering Technologies and Engineering-Related Fields",
                              "Engineering",
                              "English Language and Literature/letters",
                              "Family and Consumer Sciences/human Sciences",
                              "Foreign Languages, Literatures, and Linguistics",
                              "Health Professions and Related Programs",
                              "History",
                              "Homeland Security, Law Enforcement, Firefighting",
                              "Human Services",
                              "Legal Professions and Studies",
                              "Liberal Arts and Sciences Studies and Humanities",
                              "Library Science",
                              "Mathematics and Statistics",
                              "Mechanic and Repair Technologies/technicians",
                              "Military Technologies and Applied Sciences",
                              "Multi/interdisciplinary Studies",
                              "Natural Resources and Conservation",
                              "Parks, Recreation, Leisure, and Fitness Studies",
                              "Personal and Culinary Services",
                              "Philosophy and Religious Studies",
                              "Physical Sciences",
                              "Precision Production",
                              "Psychology",
                              "Science Technologies/technicians",
                              "Social Sciences",
                              "Theology and Religious Vocations",
                              "Transportation and Materials Moving",
                              "Visual and Performing Arts"), 5000), size = 100000)

institutionName <-sample(rep(c(paste0("University of ", state.name), 
                               paste0(randomNames::randomNames(568 , name.sep= " "), "High School"),
                               paste0(randomNames::randomNames(568, name.sep= " "), "Elementary School"),
                               paste0(randomNames::randomNames(568, which.names = "First"), "Community College"),
                               paste0(randomNames::randomNames(568, which.names = "Last"), "University")),
                             2000), size = 100000)

academicLevel <- sample(rep(c("Freshman", "Sophomore", "Junior", "Senior"), 25000), size = 100000)
gradePointRange <-  sample(rep(c("0.0-1.5", "1.6-2.5", "2.6-3.5", "3.6-4.0"), 25000), size = 100000)
studentMaritalStatus <- sample(rep(c("Married", "Divorced", "Separated", "Widowed", "Single"), 20000), size = 100000)   
housingCondition <- sample(rep(c("Homeless", "Orphanage", "Live with the family",
                                 "Live alone", "Live with a partner", "Live in a shelter home"), 16667), size = 100000)
familySize <- sample(rep(c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Greater than 10"), 8334), size = 100000)
parentMaritalStatus <- sample(rep(c("Not Applicable","Married", "Divorced", "Separated", "Widowed", "Single"), 20000), size = 100000) 
educationOfMother <- sample(rep(c("Not Applicable",
                                  "No education",
                                  "Some primary Education",
                                  "Primary Education",
                                  "Some upper secondary education",
                                  "Diploma",
                                  "Some college",
                                  "Associates degree",
                                  "Bachelors degree",
                                  "Masters degree",
                                  "Doctoral degree or above"), 10000), size = 100000) 

educationOfFather <- sample(rep(c("Not Applicable",
                                  "No education",
                                  "Some primary Education",
                                  "Primary Education",
                                  "Some upper secondary education",
                                  "Diploma",
                                  "Some college",
                                  "Associates degree",
                                  "Bachelors degree",
                                  "Masters degree",
                                  "Doctoral degree or above"), 10000), size = 100000) 

questions_colnames <- c("depressedMood", # Are you feeling depressed?
                        "depressedHopeless", # Are you feeling hopeless?
                        "lossOfInterestAndEnjoyment", # Do you feel like you are not interested in anything right now?
                        "lossOfPleasureAndEnjoyment", # Do you have less pleasure in doing things you usually enjoy?
                        "lessenedEnergy", # Do you currently have considerably less energy? 
                        "lessenedActive", # Are your everyday tasks making you very tired currently?
                        "reducedDecisionMaking", # Is it hard for you to make decisions currently?
                        "reducedConcentration", # Is it hard for you to concentrate currently?
                        "reducedSelfConfidence", # Is your self-confidence clearly lower than usual?
                        "reducedSelfEsteem", # Are you feeling up to your tasks?
                        "ideasOfGuilt", # Are you blaming yourself currently? 
                        "ideasOfUnworthiness", # Do you think you are worth less than others right now?
                        "bleakViewsOfTheFuture", # Are you thinking that you will be doing well in the future? 
                        "pessimisticViewsOfTheFuture", # Are you looking hopefully into the future?
                        "ideasOrActsOfSelfHarmOrSuicide", #Are you thinking about death more often than usual? 
                        "disturbedSleep", # Did you sleep badly last night? 
                        "diminishedAppetite", # Do you have less or no appetite today?
                        "understandingParent", # Do you have understanding parents?
                        "missedClasses", # Have you stopped going to classes or infrequently attending lectures?
                        "smokeDrink", # Do you smoke or drink?
                        "lostRelative", # Have you lost a close friend or family member recently?
                        "relationshipTrouble", # Did you go through a breakup recently or having relationship trouble?
                        "plagrisedHw", # Do you often copy assignments due to not being able to focus on your work?
                        "leftJob", #Were you let go from or did you resign your job recently?
                        "takingMedication", # Are you currently taking any presecribed medication?
                        "diagonsedBefore" # Have you ever been diagonsed with depression or anxity before?
)

employeesId <- sample(rep(c("E1",
                            "E2",
                            "E3",
                            "E4",
                            "E5",
                            "E6"), 100000), size = 100000)

employeesName <- sample(rep(randomNames::randomNames(6), 500000), size = 100000)

studentPassword <- "12345"

fake_dataframe <- data.frame(studentName = name, studentPhone = phone, studentEmail = email,
                             studentAddress = address, studentIds = userids,
                             studentPassword = studentPassword,
                             studentVisitDateTime = visitDateTime, 
                             studentSexualOrientation = sexualOrientation,
                             studentAgeGroup = ageGroup, studentRace = race,
                             studentDOB = dob, studentAreaOfInterest = areaOfInterest,
                             studentInstitutionName = institutionName, 
                             studentAcademicLevel = academicLevel, studentGPA = gradePointRange,
                             studentMaritalStatus = studentMaritalStatus,
                             studentHousingCondition = housingCondition, studentFamilySize = familySize,
                             studentParentalMaritalStatus = parentMaritalStatus,
                             studentEducationOfMother = educationOfMother,
                             studentEducationOfFather = educationOfFather,
                             employeesId = employeesId,
                             employeesName = employeesName
)

for(x in 1:26){
  fake_dataframe[questions_colnames[x]] <- sample(rep(c(1,0), 500000), size = 100000)
}

range01 <- function(x){(x-min(x))/(max(x)-min(x))}

fake_dataframe$urgencyLevel <- range01(rowSums(fake_dataframe[ ,24:49])/26)

openxlsx::write.xlsx(fake_dataframe, "fake_mentalHealth_data.xlsx")

