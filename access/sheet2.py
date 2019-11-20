import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from .models import interestModel

# use creds to create a client to interact with the Google Drive API

def interest_responses():
    '''
    returns the json response from the api
    '''
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('access_secret.json', scope)
    #authorize
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.

    sheet = client.open("Access Outcomes Project Responses").sheet1
    pp = pprint.PrettyPrinter()

    # Extract and print all of the values
    #pp.pprint(sheet.get_all_records())
    processed_data=sheet.get_all_records()
    json_results=None

    if sheet:
        '''
        checking if there is a response from the form api
        then you now call process response
        '''
        json_results=processed_data

    return json_results



def firstapplication_response():
    '''
    this function creates the instances and saves to db
    and returns the data
    '''
    json_response= interest_responses()
    json_data=[]
    print('**************************************************')
    for res in json_response:
        '''
        looping the json response array
        '''
        timestamp=res['Timestamp']
        email =res['Email Address']
        name=res['Full names']
        phone_number=res['Phone number']
        guardians_number=res["Guardian's phone number"]
        age=res["Age"]
        date_of_birth=res['Date of birth']
        gender=res["Gender"]
        prior_acceptance=res['Have you been considered for the Access Program before?']
        highest_education_level=res["Highest level of education"]
        bachelors_degree=res["Have you been to university in pursuit of a bachelor's degree?"]
        completion_date=res["If you have completed the coursework for your bachelor's degree, what was the date and year you finished?"]
        applied_to_uni=res["Have you applied to university within the last 6 months?"]
        start_date=res["If you have applied for university within the last 6 months, when is your most probable start date?"]
        moringa_student=res["Have you ever been a Moringa School student?"]
        class_name=res["If you have attended Moringa School before, please write the name of your class."]
        commitment=res["The Access Program is full-time, Monday-Friday from 8:30am-6:00pm, for six months. This class starts January 6, 2020 and ends July 4, 2020. Can you commit to this?"]
        refered_by=res["If you heard about the Access Program from an Access Program student, what is their name?"]
        computer_literacy=res["Have you used a computer before?"]
        fluency=res["Are you fully fluent in both written and spoken English?"]
        residence=res["Do you currently reside in Nairobi or within daily traveling distance of Nairobi?"]
        residence_other=res['If you answered "no" above, do you have a place to live in Nairobi for 6 months while you are enrolled in the program?']
        residence_clarification=res["If you do not currently live in or near Nairobi, please describe where you will stay while you are attending Moringa School."]
        
        
        # print('name*************************************')

        if name:
            '''
            making sure each response has a name attached to it
            '''
            application_object = interestModel.objects.create(
                            email=email,name=name,
                            phone_number=phone_number, guardians_number=guardians_number,
                            age=age, date_of_birth=date_of_birth,
                            gender=gender,prior_acceptance=prior_acceptance,
                            highest_education_level=highest_education_level,bachelors_degree=bachelors_degree,
                            completion_date=completion_date,applied_to_uni=applied_to_uni,
                            start_date=start_date,moringa_student=moringa_student,
                            class_name=class_name,commitment=commitment,
                            refered_by=refered_by,computer_literacy=computer_literacy,
                            fluency=fluency,residence=residence,
                            residence_other=residence_other,residence_clarification=residence_clarification
                            )
            #application_object.save()
            json_data.append(application_object)

    return json_data
interest_responses()      