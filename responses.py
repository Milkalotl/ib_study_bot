from random import choice, randint
from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
day_of_exam = datetime(2025, 4, 28).timetuple().tm_yday

threattext = f"*Theres only * ***{day_of_exam-day_of_year}*** *days til exams!!*"


single_letter_key: dict = {"m": "math", "p": "physics", "c": "chemistry", "b": "biology", "x": "computer_science", "s": "sports_exercise_and_health_science", "e": "English_A_Language_and_literature", "u": "Spanish_A_Language_and_literature", "y": "business_management", "g": "geography", "n": "global_politics", "h": "history"}

sciences = ["physics", "chemistry", "biology", "computer_science", "sports_exercise_and_health_science"]

languages = ["english_A_Language_and_literature", "spanish_A_Language_and_literature"]

humanities = ["Business_Management", "geography", "global_politics", "history"]

# maybe make nicer?? whats the point lowkey
def help_func():
    list_o_subjects = ""
    for e in single_letter_key.values():
        list_o_subjects += "> " + list(single_letter_key.keys())[list(single_letter_key.values()).index(e)] + " || " + e + "\n"

    return f'## Hello! This is the eye bee docks bot!!\n\
The syntax is simple!\nFor a random paper in math HL, physics HL, or chemistry SL, you would write\n```%bee m p c - h h s```\nIt\'s that simple! (spaces are optional, but dash is not)\n\
Additional flag!!\n```%bee m p c - h h s / 2015 2022```\n This will specify min and max years!!\n\
### Supported subjects (WRITE AS STATED OR USE KEY):\n```{list_o_subjects}```\
\nnotes: languages dont work lmao :)\n\
If you find any bugs, or if the links stop working, please message me incessantly until I yell and block you!!! I will fix asap!\n\
This robot\'s code can be found [here!](https://github.com/Milkalotl/ib_study_bot), and yes, you can scream at me there too!\n\n\n{threattext}'

def text_formatter(params:tuple) -> str:
    print("Start of tf")
    c_subject, c_year, toy, c_level, papers, url = params
    print("Params assigned")
    url_paper, url_markscheme = url
    print("Url became")
    hypertext = f'[**{c_subject.capitalize()} {c_year} {toy} {c_level}, paper {papers} **]({url_paper})\n[Markscheme]({url_markscheme})' 
    print("text formatter works!!")
    return f'### Here is your exam! Have a lovely day!\n\n{hypertext}\n\n{threattext}'

def year_reader(ui:str) -> str:
    ui_list = ui.split("/")
    returnparams = []
    returnparams.append(ui_list[0])
    yearpart = ui_list[1].split(" ")
    for e in yearpart:
        if e.isnumeric():
            returnparams.append(int(e))
    return tuple(returnparams)



def handle_string(user_input:str) -> str:
    if user_input == "help" or user_input == "h" or user_input == "":
        return help_func()
    if "-" not in user_input:
        return "Please specify levels with a - ! Refer to %bee help!"
    u_i_list = user_input.split("-")
    subjects = []
    print(f'{u_i_list}')

    minyear = 2010
    maxyear = 2023
    
    if "/" in u_i_list[1]:
        u_i_list[1], minyear, maxyear = year_reader(u_i_list[1])

    for word in u_i_list[0]:
        if word in single_letter_key:
            subjects.append(single_letter_key.get(word))
    levels = str(u_i_list[1]).replace(" ", "")
    levellist = []
    for letter in levels:
        levellist.append("SL" if letter == "s" else "HL")
    
    print("handle string works!!")
    return text_formatter(exam_of_the_day(subjects, minyear, maxyear, 0, levellist, 0));


def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()
    final_response = handle_string(lowered[5:])
    print(f'Response:[{final_response}]')
    return final_response
    #return handle_string(user_input[4:])

def exam_of_the_day(subjects: list, minyear: int, maxyear: int, time_o_year: int, level: list[str], papers: int):
    c_subject = choice(subjects)
    c_level = level[subjects.index(c_subject)]
    c_year = randint(minyear, maxyear)
    if papers == 0:
        papers = randint(1,2)
    if time_o_year == 0:
        time_o_year = randint(1,2)
    if c_year == 2020:
        time_o_year = 2
    toy = "November" if time_o_year == 2 else "May"    

    url: str = find_url(c_subject, c_year, toy, c_level, papers)
    print("exam of the day works!!")
    return (c_subject, c_year, toy, c_level, papers, url)

#building
def find_url_experimental(subject, year, toy, level, paper):
    
    baseurl = f'https://dl.ibdocs.re/IB%20PAST%20PAPERS%20-%20YEAR/{year}%20Examination%20Session/{toy}%20{year}%20Examination%20Session/'
    finalurl = ""
    tz = "" if toy == "November" else "TZ1_"
    
    if year == 2023 and toy == "November":
            baseurl += 'PDFs/'
    elif year > 2022:
            baseurl += 'PDF/'


def find_url(subject, year, toy, level, paper):
    
    baseurl = f'https://dl.ibdocs.re/IB%20PAST%20PAPERS%20-%20YEAR/{year}%20Examination%20Session/{toy}%20{year}%20Examination%20Session/'
    finalurl = "ERROR: SOMETHING WENT WRONG IN find_url FUNCTION"
    tz = "" if toy == "November" else "TZ1_"

    if year == 2023 and toy == "November":
            baseurl += 'PDFs/'
    elif year > 2022:
            baseurl += 'PDF/'

    if subject == "math":
        if year > 2020:
            finalurl = f'{baseurl}Mathematics/Mathematics_analysis_and_approaches_paper_{paper}__{tz}{level}'
        elif year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Mathematics/Mathematics_paper_{paper}__{tz}{level}'
        else:
            finalurl = f'{baseurl}Group%205%20-%20Mathematics/Mathematics_paper_{paper}_{tz}{level}'

    elif subject in sciences:
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Experimental%20sciences/{subject.capitalize()}_paper_{paper}__{tz}{level}'
        else:
            finalurl = f'{baseurl}Group%204%20-%20Sciences/{subject.capitalize()}_paper_{paper}_{tz}{level}'

    elif subject in languages:
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Studies%20in%20language%20and%20literature/{subject}_paper_{paper}__{tz}{level}'
        else:
            finalurl = f'{baseurl}Group%201%20-%20Studies%20in%20Language%20and%20Literature/{subject}_paper_{paper}_{tz}{level}'
    elif subject == "Business_Management":
        print("#BM") 
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Individuals%20and%20Societies/{subject}_paper_{paper}__{level}'
        else:
            finalurl = f'{baseurl}Group%203%20-%20Individuals%20and%20Societies/Business_and_Management__paper_{paper}_{level}'
    elif subject in humanities:
        print("#HUMA") 
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}__{level}'
        else:
            finalurl = f'{baseurl}Group%203%20-%20Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}_{level}'
    return (finalurl + ".pdf", finalurl + "_markscheme.pdf")
