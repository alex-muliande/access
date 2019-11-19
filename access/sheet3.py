import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from .models import scoreModel

# use creds to create a client to interact with the Google Drive API

def assesment_responses():
    '''
    returns the json response from the api
    '''
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('assesment_secret.json', scope)
    #authorize
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.

    sheet = client.open("Assesment").sheet1
    pp = pprint.PrettyPrinter()

    # Extract and print all of the values
    # pp.pprint(sheet.get_all_records())
    processed_data=sheet.get_all_records()
    json_results=None

    if sheet:
        '''
        checking if there is a response from the form api
        then you now call process response
        '''
        json_results=processed_data

    return json_results



def score_response():
    '''
    this function creates the instances and saves to db
    and returns the data
    '''
    json_response= assesment_responses()
    json_data=[]
    print('**************************************************')
    for res in json_response:
        '''
        looping the json response array
        '''
        timestamp=res['Timestamp']
        email =res['Email Address']
        score=res['Score']
        name=res['Full Names. Please write ALL of your names.']
        number=res["Mobile Number"]
        device=res["What medium are you using to complete this assessment?"]
        key_command=res['Which keyboard commands will copy a highlighted section of a document?']
        key_command2=res["Which keyboard commands is used to paste?"]
        key_command3=res['What is the function of "ctrl + z" ?']
        highlight_passage=res["How would you highlight a part of a passage?"]
        mouse_select=res["Which button on the mouse selects?"]
        mouse_select1=res["Which button on the mouse opens contextual menus?"]
        laptop_charge=res["Which of the following components can a fully charged laptop survive without for a couple of hours?"]
        web_page=res["Which of the following is used to refresh the web page?"]
        web_page1=res["Which of the following is used to go to the previous page?"]
        web_page2=res["Which of the following is used to go to the next page?"]
        web_page3=res["Which of the following is used to add a tab in the window?"]
        web_page4=res["Which of the following is used to close the tab?"]
        web_page5=res["Identify the chrome web browser"]
        email_page=res["Which icon is used to refresh the email account?"]
        email_page1=res["Which icon is used to go to the next page ?"]
        email_page2=res['Which icon will show you an extensive menu for the email account?']
        email_page3=res["How would you change the color of the text in the email?"]
        email_page4=res['What happens when you click on "x"?']
        assesment_time=res["About how much time did it take you to complete this assessment? You will not be evaluated based on your answer."]

        
        # print('name*************************************')

        if name:
            '''
            making sure each response has a name attached to it
            '''
            application_object = scoreModel.objects.create(
                            name=name,email=email,number=number,
                            score=score,assesment_time=assesment_time,
                            )
            #application_object.save()
            json_data.append(application_object)

    return json_data
assesment_responses()      