import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from .models import FormtwoResponses

# use creds to create a client to interact with the Google Drive API
def form_responses():
    '''
    returns the json response from the api
    '''
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('access_secret.json', scope)
    #authorize
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Access Sheet2").sheet1
    pp = pprint.PrettyPrinter()
    print('******************************************************')
    # Extract and print all of the values
    pp.pprint(sheet.get_all_records())
    processed_data=sheet.get_all_records()


    json_results=None

    if sheet:
        '''
        checking if there is a response from the form api
        then you now call process response
        '''
        json_results=processed_data

    return json_results



def process_response():
    '''
    this function creates the instances and saves to db
    and returns the data
    '''
    json_response= form_responses()
    json_data=[]
   
    for res in json_response:
        '''
        looping the json response array
        '''
        
        timestamp=res['Timestamp']
        email=res['Email Address']
        all_names=res['Please write ALL of your names.']
        currently_doing=res['What are you doing with your life right now?']
        work_experience=res["Do you have any work, internship, and/or volunteer experience? What did you do? Which organization and/or person did you do it for?"]
        participated_job_project=res['Have you previously participated in ONE OR MORE of the following? 1) A white collar job with a company, 2) An internship with a company, 3) A project-based contract with a company, 4) Freelancing.']
        run_a_business=res["Have you run your own business before? If so, explain what the business sold and/or what service it performed."]
        career_goals=res['What are your career goals?']
        experience_in_tech=res["Do you have any experience in tech? This could be work, education, volunteering, extracurricular activities in school, personal projects, etc. If so, please describe."]
        previous_experience=res['What is your previous programming experience? You may choose more than one answer.']
        why_program=res['Why do you want to learn how to program? How is programming related to your career goals?']
        where_grow_up=res['Where did you grow up?']
        live_most_year=res['Where do you live most of the year?']
        currently_live=res['Where do you CURRENTLY live? If you live in Nairobi, name the estate.']
        classify_neigbourhood=res['How would you classify your neighborhood?']
        live_with=res['Who do you live with?']
        guardians=res['Who are your guardians? "Guardian" means the person who is primarily responsible for your care. Write their names and their relations to you.']
        relationship_status=res['Are you married or in a domestic partnership, or single?']
        children=res['Do you have children?']
        earnings_per_month=res['How much money do you earn each month? Include only money you earn yourself through working. Do not include money you receive from other people.']
        primary_financier=res['Who is the primary person who supports you financially right now? "Primary person" means the person who provides you the greatest amount of financial support.']
        monthly_expenses=res['Please list your personal monthly expenses.']
        monthly_expenses_cost=res['How much do your personal monthly expenses  cost in total, per month?']
        support_others_financially=res['Do you support anyone financially? How many people? What is their relation to you?']
        made_money_before=res['Have you made money before in any way? If so, what did you do?']
        taken_bank_loan=res['Have you or your guardian ever taken out a loan from a bank?']
        who_took_loan=res['Who took out the loan?']
        loan_value=res['How much was the loan for?']
        loan_use=res['What was the loan used to pay for?']
        loan_collateral=res['What was used as collateral to pay the loan?']
        gurdians_make_money=res['How do your guardians make money? Please explain further. For example, if they sell goods, which kinds of goods do they sell and where?']
        gurdians_employment=res['Are your guardians employed by a company? If so, what is their job title and the company name?']
        gurdians_earning=res['List the names of your guardians and write how much money they make per month. If it depends on the month, write the average.']
        gurdians_support=res['How many people do your guardians support financially? ']
        names_age_supported=res['List the names and ages of EACH of the people your guardians support financially.']
        shool_and_schoolfees=res['If the people you listed above are currently in school, write which year they are in and how much their school fees cost. How are their fees being paid for?']
        spouse_make_money=res['If you are in a relationship, how does your spouse or domestic partner make money? Please explain further. For example, if they sell goods, which kinds of goods do they sell and where?']
        spouse_employment_detail=res['If your spouse or domestic partner is employed, what is their job title and the company name?']
        spouse_earnings=res['How much money does your spouse or domestic partner make per month? If it depends on the month, write the average.']
        smartphone_details=res['Do you own a smartphone? What kind of smartphone is it? What year was it made?']
        afford_smartphone=res['How did you afford your smartphone?']
        laptop_details=res['Do you own a laptop? What kind of laptop is it? What year was it made?']
        afford_laptop=res['How did you afford your laptop?']
        guardians_car=res['Do you or your guardians own a car? What kind of car? What year was it made?']
        form_of_transport=res['What form of transport do you use most often?']
        own_house=res['Do you or your guardians own the house you currently live in?']
        how_acquire_house=res['If you or your guardians own the house you currently live in, how was it financially possible to purchase the house?']
        rent_cost=res["If your household pays rent, what is the cost of your household's monthly rent?"]
        home_description=res['Please describe your home: number of rooms, construction materials (thatched roof, concrete walls, wood, mud walls, metal roof, etc.), plumbing (piped water, no piped water, flush toilet, etc), and electricity.']
        sent_home_schoolfees=res['Were you ever sent home from high school to collect school fees? If so, how many times were you sent home?']
        time_out_of_school=res['If you were sent home to collect school fees, how much time did you spend out of school in total?']
        schoolfees_per_term=res['How much did your school fees cost per term?']
        high_school_financial_support=res['Did you receive financial support to pay for your school fees? If so, how much did you receive in total? Who or which organization provided this support?']
        why_financial_support=res['Why did you need financial support to pay for your school fees?']
        why_dropout=res["If you have been to university in pursuit of a bachelor's degree but did not finish, why didn't you finish?"]
        university_name=res['If you have been to university, what did you study?']
        university_fees=res['If you attended university, how much did your fees cost per term?']
        how_afford_fees=res['If you attended university for any length of time, how did you afford the fees?']
        financial_support_university=res['Did you receive financial support to pay for your university fees?']
        who_howmuch_support_university=res['If you received financial support for your university fees, how much did you receive in total? Who or which organization provided this support?']
        story_of_your_life=res['Please tell us the story of your life. You may tell us where you grew up, what your family, friends, and community are like, what difficulties you have had to overcome, and what your hopes are for your future. If you have had challenges in your life, please explain these and how you faced them.']
        medium_complete_application=res['What medium did you use to complete this application?']
        timetaken_complete_application=res['How long did it take you to complete this application?']
   
        
        if timestamp:
            '''
            making sure each response has a name attached to it
            '''
            application_object = FormtwoResponses.objects.create(
                            timestamp=timestamp,all_names=all_names,
                            email=email,currently_doing=currently_doing,
                            work_experience=work_experience,  #work_experience_other=work_experience_other,
                            participated_job_project=participated_job_project,run_a_business=run_a_business,
                            career_goals=career_goals,experience_in_tech=experience_in_tech,
                            previous_experience=previous_experience,why_program=why_program,
                            where_grow_up=where_grow_up,live_most_year=live_most_year,
                            currently_live=currently_live,classify_neigbourhood=classify_neigbourhood,
                            live_with=live_with,guardians=guardians,
                            relationship_status=relationship_status,children=children,
                            earnings_per_month=earnings_per_month,primary_financier=primary_financier,
                            monthly_expenses=monthly_expenses,monthly_expenses_cost=monthly_expenses_cost,
                            support_others_financially=support_others_financially,made_money_before=made_money_before,
                            taken_bank_loan=taken_bank_loan,who_took_loan=who_took_loan,
                            loan_value=loan_value,loan_use=loan_use,                        
                            loan_collateral=loan_collateral,gurdians_make_money=gurdians_make_money,
                            gurdians_employment=gurdians_employment,gurdians_earning=gurdians_earning,
                            gurdians_support=gurdians_support,names_age_supported=names_age_supported,
                            shool_and_schoolfees=shool_and_schoolfees,spouse_make_money=spouse_make_money,
                            spouse_employment_detail=spouse_employment_detail,spouse_earnings=spouse_earnings,
                            smartphone_details=smartphone_details,afford_smartphone=afford_smartphone,
                            laptop_details=laptop_details,afford_laptop=afford_laptop,
                            guardians_car=guardians_car,form_of_transport=form_of_transport,                          
                            own_house=own_house,how_acquire_house=how_acquire_house,
                            rent_cost=rent_cost,home_description=home_description,
                            sent_home_schoolfees=sent_home_schoolfees,time_out_of_school=time_out_of_school,
                            schoolfees_per_term=schoolfees_per_term,high_school_financial_support=high_school_financial_support,
                            why_financial_support=why_financial_support,why_dropout=why_dropout,
                            university_name=university_name,university_fees=university_fees,
                            how_afford_fees=how_afford_fees,financial_support_university=financial_support_university,
                            who_howmuch_support_university=who_howmuch_support_university,story_of_your_life=story_of_your_life,
                            medium_complete_application=medium_complete_application,
                            timetaken_complete_application=timetaken_complete_application
                            
                            
                                                     
                            
                            )
            application_object.save()
            json_data.append(application_object)

    return json_data      