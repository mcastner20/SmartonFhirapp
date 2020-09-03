from django.shortcuts import render
from django.http import HttpResponse
from .models import Conditions, Information, Disaster, Demographics, Hazards, Hazard_probability, Hazard_continued
from .forms import Informations
from bs4 import BeautifulSoup
import requests
import json
#question list this list is used throughout the app
questions = ['Redacted0', 'Redacted1', 'Redacted2', 'Redacted3', 'Redacted4', 'Redacted5', 'Redacted6', 'Redacted7', 'Redacted8', 'Redacted9', 'Redacted10', 'Redacted11', 'Redacted12', 'Redacted13', 'Redacted14', 'Redacted15', 'Redacted16', 'Redacted17', 'Redacted18', 'Redacted19', 'Redacted20', 'Redacted21', 'Redacted22', 'Redacted23', 'Redacted24', 'Redacted25', 'Redacted26', 'Redacted27', 'Redacted28', 'Redacted29', 'Redacted30', 'Redacted31', 'Redacted32', 'Redacted33', 'Redacted34', 'Redacted35', 'Redacted36', 'Redacted37', 'Redacted38', 'Redacted39', 'Redacted40', 'Redacted41', 'Redacted42', 'Redacted43', 'Redacted44', 'Redacted45', 'Redacted46', 'Redacted47', 'Redacted48', 'Redacted49', 'Redacted50', 'Redacted51', 'Redacted52', 'Redacted53', 'Redacted54', 'Redacted55', 'Redacted56', 'Redacted57', 'Redacted58', 'Redacted59']
#takes information for hazard_continued
def takeinformation3(request, questions):
    answers1, answers2, answers3 = [], [], []
    for question in questions:
        try:
            answer1 = request.POST[question]
            if answer1 == '':
                answer1 = None
        except:
            answer1 = None
        try:
            answer2 = request.POST[question +'a']
        except:
            answer2 = None
        try:
            answer3 = request.POST[question + 'b']
        except:
            answer3 = None
        answers1.append(answer1)
        answers2.append(answer2)
        answers3.append(answer3)
    return answers1, answers2, answers3
#takes information from hazard2
def takeinformation2(request, questions):
    values = []
    questionlist = []
    for question in questions:
        try:
            value = request.POST[question]
            if value == 'Yes':
                questionlist.append(question)
                values.append(True)
            elif value == 'No':
                values.append(False)
        except:

            values.append(None)
    return values, questionlist
#takes information from demographic and disaster
def takeinformation(request):
    answers = []
    for _ in range(100):
        try:
            num = 'q' + str(_)
            num = request.POST[str(_)]
            if num == 'True':
                answers.append(True)
            else:
                num = num[-1]
                answers.append(num)
        except:
            answers.append(None)

    return answers

#pull information from the fhir sandbox may need to be changed to access real fhir server in final app
def APIsearch(first_name, last_name, dob):
    conditions, medications, immunizations, allergies, allergy_codes = [], [], [], [], []
    dob = str(dob)
    year = dob[:4]
    day = dob[5:7]
    month = dob[8:]
    dob = year+'-'+month+'-'+day
    url = "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family="+last_name+'&given='+first_name+'&birthdate='+dob
    document = requests.get(url)
    soup = BeautifulSoup(document.content, 'xml')
    id = soup.id['value']
    url = "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition?patient="+id
    document = requests.get(url)
    soup = BeautifulSoup(document.content, 'xml')
    for code in soup.find_all('code'):
        for text in code.find_all('text'):
            conditions.append(text['value'])
    url = "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?patient=" + id
    document = requests.get(url)
    soup = BeautifulSoup(document.content, 'xml')
    for medication in soup.find_all('medicationReference'):
        for display in medication.find_all('display'):
            medications.append(display['value'].title())
    url = "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Immunization?patient=" + id
    document = requests.get(url)
    soup = BeautifulSoup(document.content, 'xml')
    for code in soup.find_all('vaccineCode'):
        for text in code.find_all('text'):
            immunizations.append(text['value'])
    url = "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance?patient=" + id
    document = requests.get(url)
    soup = BeautifulSoup(document.content, 'xml')
    for substance in soup.find_all('substance'):
        for text in substance.find_all('text'):
            allergies.append(text['value'].title())
    for substance in soup.find_all('substance'):
        code = substance.find('code')
        allergy_codes.append(code['value'])

    return conditions, medications, immunizations, allergies, allergy_codes

#only page that requires all questions to be filled out. Patients should be able to skip fututre personal questions. Therefore this page requires a form
def home(request):

    form = Informations()

    return render(request, 'home/homev2.html', {'form':form})

#medical questions autofilled by fhir sandbox. allows user to edit
def questions(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        information = Information(first_name=first, last_name=last, dob=dob)
        information.save()


        conditions, medications, immunizations, allergies, allergy_codes = APIsearch(first, last, dob)
        conditions = Conditions(condition=conditions, immunizations=immunizations, allergies=allergies,
                            medications=medications)
        conditions.save()
        #since the API search pulls a list the following code makes the list visual
        conditions.condition = ', '.join(conditions.condition)
        conditions.medications = ', '.join(conditions.medications)
        conditions.immunizations = ', '.join(conditions.immunizations)
        conditions.allergies = ', '.join(conditions.allergies)


    else:
        #This is used throughout the app to pull the last post to the database when going back on the survey
        conditions = Conditions.objects.all().order_by('-id')[0]
        information = Information.objects.all().order_by('-id')[0]
    return render(request, 'home/questions.html', {'conditions':conditions, 'information':information})
#First set of survey questions
def disaster(request):
    if request.method == 'POST':
        condition = request.POST['condition']
        immunizations = request.POST['immunizations']
        allergies = request.POST['allergies']
        medications = request.POST['medications']
        conditions = Conditions(condition=condition, immunizations=immunizations, allergies=allergies, medications=medications)
        conditions.save()
        disasters = None
    else:
        disasters = Disaster.objects.all().order_by('-id')[0]


    return render(request, 'home/disaster.html', {'disasters':disasters})
#Demographic questions
def demographic(request):
    if request.method == 'POST':

        answers = takeinformation(request)
        disasters = Disaster(q0=answers[0], q1=answers[1], q2=answers[2], q3=answers[3], q4=answers[4], q5=answers[5], q6=answers[6], q7=answers[7], q8=answers[8], q9=answers[9],
                             q10=answers[10], q11=answers[11], q12=answers[12], q13=answers[13], q14=answers[14], q15=answers[15], q16=answers[16],
                             q17=answers[17], q18=answers[18], q19=answers[19], q20=answers[20], q21=answers[21], q22=answers[22], q23=answers[23], q24=answers[24],
                             q25=answers[25], q26=answers[26])
        disasters.save()
        demographics = None

    else:
        demographics = Demographics.objects.all().order_by('-id')[0]
    return render(request, 'home/demographic.html', {'demographics': demographics})
#yes or no hazard page
def hazard2(request):
    questions = ['Redacted0', 'Redacted1', 'Redacted2', 'Redacted3', 'Redacted4', 'Redacted5', 'Redacted6', 'Redacted7', 'Redacted8', 'Redacted9', 'Redacted10', 'Redacted11', 'Redacted12', 'Redacted13', 'Redacted14', 'Redacted15', 'Redacted16', 'Redacted17', 'Redacted18', 'Redacted19', 'Redacted20', 'Redacted21', 'Redacted22', 'Redacted23', 'Redacted24', 'Redacted25', 'Redacted26', 'Redacted27', 'Redacted28', 'Redacted29', 'Redacted30', 'Redacted31', 'Redacted32', 'Redacted33', 'Redacted34', 'Redacted35', 'Redacted36', 'Redacted37', 'Redacted38', 'Redacted39', 'Redacted40', 'Redacted41', 'Redacted42', 'Redacted43', 'Redacted44', 'Redacted45', 'Redacted46', 'Redacted47', 'Redacted48', 'Redacted49', 'Redacted50', 'Redacted51', 'Redacted52', 'Redacted53', 'Redacted54', 'Redacted55', 'Redacted56', 'Redacted57', 'Redacted58', 'Redacted59']
    if request.method == 'POST':
        answers = takeinformation(request)
        demographics = Demographics(q26=answers[26], q27=answers[27], q28a=answers[28], q28b=answers[29], q28c=answers[30], q28d=answers[31], q28e=answers[32], q28f=answers[33],
                                   q29a=answers[34], q29b=answers[35], q29c=answers[36], q29d=answers[37], q29e=answers[38], q29f=answers[39], q30=answers[40], q31=answers[41],
                                   q32=answers[42],q33a=answers[43], q33b=answers[44], q33c=answers[45], q33d=answers[46], q33e=answers[47], q33f=answers[48],q34=answers[50])


        demographics.save()
        hazards = questions
    else:
        hazard = Hazards.objects.all().order_by('-id')[0]
        hazards = [hazard.q0,hazard.q1,hazard.q2,hazard.q3,hazard.q4,hazard.q5,hazard.q6,hazard.q7,hazard.q8,hazard.q9,hazard.q10,hazard.q11,hazard.q12,hazard.q13,
                   hazard.q14,hazard.q15,hazard.q16,hazard.q17,hazard.q18,hazard.q19,hazard.q20,hazard.q21,hazard.q22,hazard.q23,hazard.q24,hazard.q25,hazard.q26,
                   hazard.q27,hazard.q28,hazard.q29,hazard.q30,hazard.q31,hazard.q32,hazard.q33,hazard.q34,hazard.q35,hazard.q36,hazard.q37,hazard.q38,hazard.q39,
                   hazard.q40,hazard.q41,hazard.q42,hazard.q43,hazard.q44,hazard.q45,hazard.q46,hazard.q47,hazard.q48,hazard.q49,hazard.q50,hazard.q51,hazard.q52,
                   hazard.q53,hazard.q54,hazard.q55,hazard.q56,hazard.q57,hazard.q58,hazard.q59,]

    return render(request, 'home/hazard2.html', {'mylist':zip(questions, hazards)})
def hazard_continued(request):
    questions = ['Redacted0', 'Redacted1', 'Redacted2', 'Redacted3', 'Redacted4', 'Redacted5', 'Redacted6', 'Redacted7', 'Redacted8', 'Redacted9', 'Redacted10', 'Redacted11', 'Redacted12', 'Redacted13', 'Redacted14', 'Redacted15', 'Redacted16', 'Redacted17', 'Redacted18', 'Redacted19', 'Redacted20', 'Redacted21', 'Redacted22', 'Redacted23', 'Redacted24', 'Redacted25', 'Redacted26', 'Redacted27', 'Redacted28', 'Redacted29', 'Redacted30', 'Redacted31', 'Redacted32', 'Redacted33', 'Redacted34', 'Redacted35', 'Redacted36', 'Redacted37', 'Redacted38', 'Redacted39', 'Redacted40', 'Redacted41', 'Redacted42', 'Redacted43', 'Redacted44', 'Redacted45', 'Redacted46', 'Redacted47', 'Redacted48', 'Redacted49', 'Redacted50', 'Redacted51', 'Redacted52', 'Redacted53', 'Redacted54', 'Redacted55', 'Redacted56', 'Redacted57', 'Redacted58', 'Redacted59']
    if request.method == 'POST':
        #questionlist is a list of questions the user said yes to
        values, questionslist = takeinformation2(request, questions)

        hazards = Hazards(q0=values[0],q1=values[1],q2=values[2],q3=values[3],q4=values[4],q5=values[5],q6=values[6],q7=values[7],q8=values[8],q9=values[9],q10=values[10],
                          q11=values[11],q12=values[12],q13=values[13],q14=values[14],q15=values[15],q16=values[16],q17=values[17],q18=values[18],q19=values[19],q20=values[20],
                          q21=values[21],q22=values[22],q23=values[23],q24=values[24],q25=values[25],q26=values[26],q27=values[27],q28=values[28],q29=values[29],q30=values[30],
                          q31=values[31],q32=values[32],q33=values[33],q34=values[34],q35=values[35],q36=values[36],q37=values[37],q38=values[38],q39=values[39],q40=values[40],
                          q41=values[41],q42=values[42],q43=values[43],q44=values[44],q45=values[45],q46=values[46],q47=values[47],q48=values[48],q49=values[49],q50=values[50],
                          q51=values[51],q52=values[52],q53=values[53],q54=values[54],q55=values[55],q56=values[56],q57=values[57],q58=values[58],q59=values[59],)
        hazards.save()
        answer1 = questionslist
        answer2 = questionslist
        answer3 = questionslist
    else:
        hazard_cont = Hazard_continued.objects.all().order_by('-id')[0]
        #pulls list of individual answers
        answers1 = [hazard_cont.q0,hazard_cont.q1,hazard_cont.q2,hazard_cont.q3,hazard_cont.q4,hazard_cont.q5,hazard_cont.q6,hazard_cont.q7,hazard_cont.q8,hazard_cont.q9,hazard_cont.q10,hazard_cont.q11,hazard_cont.q12,hazard_cont.q13,
                   hazard_cont.q14,hazard_cont.q15,hazard_cont.q16,hazard_cont.q17,hazard_cont.q18,hazard_cont.q19,hazard_cont.q20,hazard_cont.q21,hazard_cont.q22,hazard_cont.q23,hazard_cont.q24,hazard_cont.q25,hazard_cont.q26,
                   hazard_cont.q27,hazard_cont.q28,hazard_cont.q29,hazard_cont.q30,hazard_cont.q31,hazard_cont.q32,hazard_cont.q33,hazard_cont.q34,hazard_cont.q35,hazard_cont.q36,hazard_cont.q37,hazard_cont.q38,hazard_cont.q39,
                   hazard_cont.q40,hazard_cont.q41,hazard_cont.q42,hazard_cont.q43,hazard_cont.q44,hazard_cont.q45,hazard_cont.q46,hazard_cont.q47,hazard_cont.q48,hazard_cont.q49,hazard_cont.q50,hazard_cont.q51,hazard_cont.q52,
                   hazard_cont.q53,hazard_cont.q54,hazard_cont.q55,hazard_cont.q56,hazard_cont.q57,hazard_cont.q58,hazard_cont.q59,]
        answers2 = [hazard_cont.q0a,hazard_cont.q1a,hazard_cont.q2a,hazard_cont.q3a,hazard_cont.q4a,hazard_cont.q5a,hazard_cont.q6a,hazard_cont.q7a,hazard_cont.q8a,hazard_cont.q9a,hazard_cont.q10a,hazard_cont.q11a,hazard_cont.q12a,hazard_cont.q13a,
                   hazard_cont.q14a,hazard_cont.q15a,hazard_cont.q16a,hazard_cont.q17a,hazard_cont.q18a,hazard_cont.q19a,hazard_cont.q20a,hazard_cont.q21a,hazard_cont.q22a,hazard_cont.q23a,hazard_cont.q24a,hazard_cont.q25a,hazard_cont.q26a,
                   hazard_cont.q27a,hazard_cont.q28a,hazard_cont.q29a,hazard_cont.q30a,hazard_cont.q31a,hazard_cont.q32a,hazard_cont.q33a,hazard_cont.q34a,hazard_cont.q35a,hazard_cont.q36a,hazard_cont.q37a,hazard_cont.q38a,hazard_cont.q39a,
                   hazard_cont.q40a,hazard_cont.q41a,hazard_cont.q42a,hazard_cont.q43a,hazard_cont.q44a,hazard_cont.q45a,hazard_cont.q46a,hazard_cont.q47a,hazard_cont.q48a,hazard_cont.q49a,hazard_cont.q50a,hazard_cont.q51a,hazard_cont.q52a,
                   hazard_cont.q53a,hazard_cont.q54a,hazard_cont.q55a,hazard_cont.q56a,hazard_cont.q57a,hazard_cont.q58a,hazard_cont.q59a,]
        answers3 = [hazard_cont.q0b,hazard_cont.q1b,hazard_cont.q2b,hazard_cont.q3b,hazard_cont.q4b,hazard_cont.q5b, hazard_cont.q6b,hazard_cont.q7b,hazard_cont.q8b,hazard_cont.q9b,hazard_cont.q10b,hazard_cont.q11b,hazard_cont.q12b,hazard_cont.q13b,
                   hazard_cont.q14b,hazard_cont.q15b,hazard_cont.q16b,hazard_cont.q17b,hazard_cont.q18b,hazard_cont.q19b,hazard_cont.q20b,hazard_cont.q21b,hazard_cont.q22b,hazard_cont.q23b,hazard_cont.q24b,hazard_cont.q25b,hazard_cont.q26b,
                   hazard_cont.q27b,hazard_cont.q28b,hazard_cont.q29b,hazard_cont.q30b,hazard_cont.q31b,hazard_cont.q32b,hazard_cont.q33b,hazard_cont.q34b,hazard_cont.q35b,hazard_cont.q36b,hazard_cont.q37b,hazard_cont.q38b,hazard_cont.q39b,
                   hazard_cont.q40b,hazard_cont.q41b,hazard_cont.q42b,hazard_cont.q43b,hazard_cont.q44b,hazard_cont.q45b,hazard_cont.q46b,hazard_cont.q47b,hazard_cont.q48b,hazard_cont.q49b,hazard_cont.q50b,hazard_cont.q51b,hazard_cont.q52b,
                   hazard_cont.q53b,hazard_cont.q54b,hazard_cont.q55b,hazard_cont.q56b,hazard_cont.q57b,hazard_cont.q58b,hazard_cont.q59b,]
        questionslist, answer1, answer2, answer3 = [], [], [], []
        hazard = Hazards.objects.all().order_by('-id')[0]
        hazards = [hazard.q0, hazard.q1, hazard.q2, hazard.q3, hazard.q4, hazard.q5, hazard.q6, hazard.q7, hazard.q8,
                   hazard.q9, hazard.q10, hazard.q11, hazard.q12, hazard.q13,
                   hazard.q14, hazard.q15, hazard.q16, hazard.q17, hazard.q18, hazard.q19, hazard.q20, hazard.q21,
                   hazard.q22, hazard.q23, hazard.q24, hazard.q25, hazard.q26,
                   hazard.q27, hazard.q28, hazard.q29, hazard.q30, hazard.q31, hazard.q32, hazard.q33, hazard.q34,
                   hazard.q35, hazard.q36, hazard.q37, hazard.q38, hazard.q39,
                   hazard.q40, hazard.q41, hazard.q42, hazard.q43, hazard.q44, hazard.q45, hazard.q46, hazard.q47,
                   hazard.q48, hazard.q49, hazard.q50, hazard.q51, hazard.q52,
                   hazard.q53, hazard.q54, hazard.q55, hazard.q56, hazard.q57, hazard.q58, hazard.q59, ]

        for hazard, question, answer01, answer02, answer03 in zip(hazards, questions, answers1, answers2, answers3):
            if hazard == True:
                answer1.append(answer01)
                answer2.append(answer02)
                answer3.append(answer03)
                questionslist.append(question)


    return render(request, 'home/hazard_continued.html', {'mylist': zip(questionslist, answer1, answer2, answer3)})
def hazard_probability(request):
    questions = ['Redacted0', 'Redacted1', 'Redacted2', 'Redacted3', 'Redacted4', 'Redacted5', 'Redacted6', 'Redacted7', 'Redacted8', 'Redacted9', 'Redacted10', 'Redacted11', 'Redacted12', 'Redacted13', 'Redacted14', 'Redacted15', 'Redacted16', 'Redacted17', 'Redacted18', 'Redacted19', 'Redacted20', 'Redacted21', 'Redacted22', 'Redacted23', 'Redacted24', 'Redacted25', 'Redacted26', 'Redacted27', 'Redacted28', 'Redacted29', 'Redacted30', 'Redacted31', 'Redacted32', 'Redacted33', 'Redacted34', 'Redacted35', 'Redacted36', 'Redacted37', 'Redacted38', 'Redacted39', 'Redacted40', 'Redacted41', 'Redacted42', 'Redacted43', 'Redacted44', 'Redacted45', 'Redacted46', 'Redacted47', 'Redacted48', 'Redacted49', 'Redacted50', 'Redacted51', 'Redacted52', 'Redacted53', 'Redacted54', 'Redacted55', 'Redacted56', 'Redacted57', 'Redacted58', 'Redacted59']
    if request.method == 'POST':
        answer1, answer2, answer3 = takeinformation3(request, questions)
        hazard_cont = Hazard_continued(q0=answer1[0],q1=answer1[1],q2=answer1[2],q3=answer1[3],q4=answer1[4],q5=answer1[5],q6=answer1[6],q7=answer1[7],q8=answer1[8],q9=answer1[9],q10=answer1[10],
                          q11=answer1[11],q12=answer1[12],q13=answer1[13],q14=answer1[14],q15=answer1[15],q16=answer1[16],q17=answer1[17],q18=answer1[18],q19=answer1[19],q20=answer1[20],
                          q21=answer1[21],q22=answer1[22],q23=answer1[23],q24=answer1[24],q25=answer1[25],q26=answer1[26],q27=answer1[27],q28=answer1[28],q29=answer1[29],q30=answer1[30],
                          q31=answer1[31],q32=answer1[32],q33=answer1[33],q34=answer1[34],q35=answer1[35],q36=answer1[36],q37=answer1[37],q38=answer1[38],q39=answer1[39],q40=answer1[40],
                          q41=answer1[41],q42=answer1[42],q43=answer1[43],q44=answer1[44],q45=answer1[45],q46=answer1[46],q47=answer1[47],q48=answer1[48],q49=answer1[49],q50=answer1[50],
                          q51=answer1[51],q52=answer1[52],q53=answer1[53],q54=answer1[54],q55=answer1[55],q56=answer1[56],q57=answer1[57],q58=answer1[58],q59=answer1[59],
                          q0a=answer2[0],q1a=answer2[1],q2a=answer2[2],q3a=answer2[3],q4a=answer2[4],q5a=answer2[5],q6a=answer2[6],q7a=answer2[7],q8a=answer2[8],q9a=answer2[9],q10a=answer2[10],
                          q11a=answer2[11],q12a=answer2[12],q13a=answer2[13],q14a=answer2[14],q15a=answer2[15],q16a=answer2[16],q17a=answer2[17],q18a=answer2[18],q19a=answer2[19],q20a=answer2[20],
                          q21a=answer2[21],q22a=answer2[22],q23a=answer2[23],q24a=answer2[24],q25a=answer2[25],q26a=answer2[26],q27a=answer2[27],q28a=answer2[28],q29a=answer2[29],q30a=answer2[30],
                          q31a=answer2[31],q32a=answer2[32],q33a=answer2[33],q34a=answer2[34],q35a=answer2[35],q36a=answer2[36],q37a=answer2[37],q38a=answer2[38],q39a=answer2[39],q40a=answer2[40],
                          q41a=answer2[41],q42a=answer2[42],q43a=answer2[43],q44a=answer2[44],q45a=answer2[45],q46a=answer2[46],q47a=answer2[47],q48a=answer2[48],q49a=answer2[49],q50a=answer2[50],
                          q51a=answer2[51],q52a=answer2[52],q53a=answer2[53],q54a=answer2[54],q55a=answer2[55],q56a=answer2[56],q57a=answer2[57],q58a=answer2[58],q59a=answer2[59],
                          q0b=answer3[0],q1b=answer3[1],q2b=answer3[2],q3b=answer3[3],q4b=answer3[4],q5b=answer3[5],q6b=answer3[6],q7b=answer3[7],q8b=answer3[8],q9b=answer3[9],q10b=answer3[10],
                          q11b=answer3[11],q12b=answer3[12],q13b=answer3[13],q14b=answer3[14],q15b=answer3[15],q16b=answer3[16],q17b=answer3[17],q18b=answer3[18],q19b=answer3[19],q20b=answer3[20],
                          q21b=answer3[21],q22b=answer3[22],q23b=answer3[23],q24b=answer3[24],q25b=answer3[25],q26b=answer3[26],q27b=answer3[27],q28b=answer3[28],q29b=answer3[29],q30b=answer3[30],
                          q31b=answer3[31],q32b=answer3[32],q33b=answer3[33],q34b=answer3[34],q35b=answer3[35],q36b=answer3[36],q37b=answer3[37],q38b=answer3[38],q39b=answer3[39],q40b=answer3[40],
                          q41b=answer3[41],q42b=answer3[42],q43b=answer3[43],q44b=answer3[44],q45b=answer3[45],q46b=answer3[46],q47b=answer3[47],q48b=answer3[48],q49b=answer3[49],q50b=answer3[50],
                          q51b=answer3[51],q52b=answer3[52],q53b=answer3[53],q54b=answer3[54],q55b=answer3[55],q56b=answer3[56],q57b=answer3[57],q58b=answer3[58],q59b=answer3[59],)
        hazard_cont.save()
    return render(request, 'home/hazard_probability.html', {'questions':questions})

def results(request):
    questions = ['Redacted0', 'Redacted1', 'Redacted2', 'Redacted3', 'Redacted4', 'Redacted5', 'Redacted6', 'Redacted7', 'Redacted8', 'Redacted9', 'Redacted10', 'Redacted11', 'Redacted12', 'Redacted13', 'Redacted14', 'Redacted15', 'Redacted16', 'Redacted17', 'Redacted18', 'Redacted19', 'Redacted20', 'Redacted21', 'Redacted22', 'Redacted23', 'Redacted24', 'Redacted25', 'Redacted26', 'Redacted27', 'Redacted28', 'Redacted29', 'Redacted30', 'Redacted31', 'Redacted32', 'Redacted33', 'Redacted34', 'Redacted35', 'Redacted36', 'Redacted37', 'Redacted38', 'Redacted39', 'Redacted40', 'Redacted41', 'Redacted42', 'Redacted43', 'Redacted44', 'Redacted45', 'Redacted46', 'Redacted47', 'Redacted48', 'Redacted49', 'Redacted50', 'Redacted51', 'Redacted52', 'Redacted53', 'Redacted54', 'Redacted55', 'Redacted56', 'Redacted57', 'Redacted58', 'Redacted59']

    if request.method == 'POST':

        values = []
        for question in questions:
            try:
                value = request.POST[question]
            except:
                value = None
            values.append(value)
        hazard_prop = Hazard_probability(q0=values[0], q1=values[1], q2=values[2], q3=values[3], q4=values[4], q5=values[5],
                          q6=values[6], q7=values[7], q8=values[8], q9=values[9], q10=values[10],
                          q11=values[11], q12=values[12], q13=values[13], q14=values[14], q15=values[15],
                          q16=values[16], q17=values[17], q18=values[18], q19=values[19], q20=values[20],
                          q21=values[21], q22=values[22], q23=values[23], q24=values[24], q25=values[25],
                          q26=values[26], q27=values[27], q28=values[28], q29=values[29], q30=values[30],
                          q31=values[31], q32=values[32], q33=values[33], q34=values[34], q35=values[35],
                          q36=values[36], q37=values[37], q38=values[38], q39=values[39], q40=values[40],
                          q41=values[41], q42=values[42], q43=values[43], q44=values[44], q45=values[45],
                          q46=values[46], q47=values[47], q48=values[48], q49=values[49], q50=values[50],
                          q51=values[51], q52=values[52], q53=values[53], q54=values[54], q55=values[55],
                          q56=values[56], q57=values[57], q58=values[58], q59=values[59],)
        hazard_prop.save()

    return render(request, 'home/results.html')