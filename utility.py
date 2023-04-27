import pandas as pd
import numpy as np

def getUrgencyLevel(depressedMood, depressedHopeless, lossOfInterestAndEnjoyment, lossOfPleasureAndEnjoyment, lessenedEnergy, lessenedActive, reducedDecisionMaking,
                    reducedConcentration,reducedSelfConfidence, reducedSelfEsteem, ideasOfGuilt, ideasOfUnworthiness, bleakViewsOfTheFuture, pessimisticViewsOfTheFuture,
                    ideasOrActsOfSelfHarmOrSuicide,disturbedSleep, diminishedAppetite, understandingParent, missedClasses, smokeDrink, lostRelative, relationshipTrouble,
                    plagrisedHw, leftJob, takingMedication, diagnosedBefore):
    
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

    # df_temp = pd.DataFrame({
    #     'depressedMood': depressedMood,
    #     'depressedHopeless': depressedHopeless,
    #     'lossOfInterestAndEnjoyment': lossOfInterestAndEnjoyment,
    #     'lossOfPleasureAndEnjoyment': lossOfPleasureAndEnjoyment,
    #     'lessenedEnergy': lessenedEnergy,
    #     'lessenedActive': lessenedActive,
    #     'reducedDecisionMaking': reducedDecisionMaking,
    #     'reducedConcentration': reducedConcentration,
    #     'reducedSelfConfidence': reducedSelfConfidence,
    #     'reducedSelfEsteem': reducedSelfEsteem,
    #     'ideasOfGuilt': ideasOfGuilt,
    #     'ideasOfUnworthiness': ideasOfUnworthiness,
    #     'bleakViewsOfTheFuture': bleakViewsOfTheFuture,
    #     'pessimisticViewsOfTheFuture': pessimisticViewsOfTheFuture,
    #     'ideasOrActsOfSelfHarmOrSuicide': ideasOrActsOfSelfHarmOrSuicide,
    #     'disturbedSleep': disturbedSleep,
    #     'diminishedAppetite': diminishedAppetite,
    #     'understandingParent': understandingParent,
    #     'missedClasses': missedClasses,
    #     'smokeDrink': smokeDrink,
    #     'lostRelative': lostRelative,
    #     'relationshipTrouble': relationshipTrouble,
    #     'plagrisedHw': plagrisedHw,
    #     'leftJob': leftJob,
    #     'takingMedication': takingMedication,
    #     'diagnosedBefore': diagnosedBefore})
    
    # df_global = pd.DataFrame({
    # 'depressedMood': [0, 1],
    # 'depressedHopeless': [0, 0],
    # 'lossOfInterestAndEnjoyment': [0, 1],
    # 'lossOfPleasureAndEnjoyment': [1, 0],
    # 'lessenedEnergy': [0, 0],
    # 'lessenedActive': [0, 0],
    # 'reducedDecisionMaking': [1,0],
    # 'reducedConcentration': [1, 0],
    # 'reducedSelfConfidence': [1, 0],
    # 'reducedSelfEsteem': [1, 0],
    # 'ideasOfGuilt': [0, 0],
    # 'ideasOfUnworthiness': [0, 1],
    # 'bleakViewsOfTheFuture': [0, 1],
    # 'pessimisticViewsOfTheFuture': [0, 1],
    # 'ideasOrActsOfSelfHarmOrSuicide': [1, 0],
    # 'disturbedSleep': [0, 0],
    # 'diminishedAppetite': [1, 0],
    # 'understandingParent': [0, 1],
    # 'missedClasses': [1, 0],
    # 'smokeDrink': [0, 1],
    # 'lostRelative': [0, 1],
    # 'relationshipTrouble': [1, 1],
    # 'plagrisedHw': [1, 0],
    # 'leftJob': [1, 1],
    # 'takingMedication': [1, 0],
    # 'diagonsedBefore': [1, 0], 
    # 'urgencyLevel': [1, 0]})

    # Convert 'urgencyLevel' column to float
    # df_temp['urgencyLevel'] = df_temp['urgencyLevel'].astype(float)

    # Loop through rows in df_temp.
    #Suggestion, depending on the average range, we could assign qualitative values instead of quantitative: High (>=0.7), Medium (0.7 > x > 0.4, Average (0.4 > x >= 0.25, Low (<0.25)
    # See line 20 for another suggestion
    # for index, row in df_temp.iterrows():
    #     # Extract values for 'b', 'c', 'd', and 'e' in current row
    #     ideasOrActsOfSelfHarmOrSuicide = row["ideasOrActsOfSelfHarmOrSuicide"]
        
    #     if ideasOrActsOfSelfHarmOrSuicide >= 1:
    #         urgencyLevel = 1.0
    #     else:
    #         symptoms = row.tolist()[:-1]  # exclude 'urgencyLevel' column
            
    #         # Calculate average of symptom values in df_temp
    #         avg = sum(symptoms) / len(symptoms)
            
    #         # Check if denominator is not zero
    #         if max(symptoms) - min(symptoms) > 0:
    #             # Normalize average value to be between 0.00 and 1.00
    #             normalized_avg = (avg - min(symptoms)) / (max(symptoms) - min(symptoms))
    #         else:
    #             # Set normalized average value to NaN if denominator is zero
    #             normalized_avg = np.nan
            
    #         # Assign normalized average value to 'urgencyLevel' in df_global
    #         df_temp = normalized_avg
    urgencyLevel = 1.0
    # Replace NaN values with 0.00
    if type(urgencyLevel) != float and urgencyLevel.isnan():
        urgencyLevel = 0.00
    # df_temp['urgencyLevel'].fillna(0.00, inplace=True)
    return urgencyLevel
