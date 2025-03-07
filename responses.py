from datetime import datetime
from random import choice, randint

day_of_year = datetime.now().timetuple().tm_yday
day_of_exam = datetime(2025, 4, 28).timetuple().tm_yday

threattext = f"*Theres only * ***{day_of_exam-day_of_year}*** *days til exams!!*"



single_letter_key: dict = {"m": "math", "p": "physics", "c": "chemistry", "b": "biology", "x": "computer_science", "s": "sports_exercise_and_health_science", "e": "English_A_Language_and_literature", "u": "Spanish_A_Language_and_literature", "y": "business_management", "g": "geography", "n": "global_politics", "h": "history"}

sciences = ["physics", "chemistry", "biology", "computer_science", "sports_exercise_and_health_science"]

languages = ["english_A_Language_and_literature", "spanish_A_Language_and_literature"]

humanities = ["Business_Management", "geography", "global_politics", "history"]

iflag = lambda params: int(params[1:])
stringflag = lambda params: params[1:]

def get_response(user_input:str) -> str:
    final_response = handle_string(user_input[5:])
    print(f'Response:[{final_response}]')
    return final_response

def handle_string(user_input:str) -> str:
    if user_input == "help" or user_input == "h" or user_input == "":
        return help_func()
    if "/" not in user_input:
        return "Please specify levels with a / ! Refer to %bee help!"
    ui_split = user_input.split("-")
    content = ui_split[0]
    content = content.lower()
    ui_split = ui_split[1:]
    maxyear, minyear, papers, name = 0, 0, 0, "";

    for n in ui_split:
        if "N" in n:
            print("namechosen")
            name = " " + stringflag(n)
        elif "x" in n:
            maxyear = iflag(n)
        elif "n" in n:
            minyear = iflag(n)
        elif "p" in n:
            papers = iflag(n)

    subjects, levels = content.split("/")
    levellist = []
    subjectlist = []
    for letter in levels:
        levellist.append("SL" if letter == "s" else "HL")
    for subject in subjects:
        subjectlist.append(single_letter_key.get(subject))

    print("handle string works!!")
    return text_formatter(exam_of_the_day(subjectlist, minyear, maxyear, 0, levellist, papers,name));

def exam_of_the_day(subjectlist: list, minyear: int, maxyear: int, time_o_year: int, level: list[str], papers: int, name:str):
    c_subject = choice(subjectlist)
    c_level = level[subjectlist.index(c_subject)]

    if minyear == 0:
        minyear = 2010
    if maxyear == 0:
        maxyear = 2023

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
    return (c_subject, c_year, toy, c_level, papers, url, name)
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

def text_formatter(params:tuple) -> str:
    print("Start of tf")
    c_subject, c_year, toy, c_level, papers, url, name = params
    print("Params assigned")
    url_paper, url_markscheme = url
    print("Url became")
    hypertext = f'[**{c_subject.capitalize()} {c_year} {toy} {c_level}, paper {papers} **]({url_paper})\n[Markscheme]({url_markscheme})' 
    print("text formatter works!!")
    return f'### Here is your exam{name.capitalize()}! Have a lovely day!\n\n{hypertext}\n\n{threattext}'

# maybe make nicer?? whats the point lowkey
def help_func():
    list_o_subjects = ""
    for e in single_letter_key.values():
        list_o_subjects += "> " + list(single_letter_key.keys())[list(single_letter_key.values()).index(e)] + " || " + e + "\n"

    return f'## Hello! This is the eye bee docks bot!!\n\
The syntax is simple!\nFor a random paper in math HL, physics HL, or chemistry SL, you would write\n```%bee m p c / h h s```\nIt\'s that simple! (spaces are optional, but slash is not)\n\
### Additional flags!!\
\n\
This will specify min and max years!!```%bee m p c / h h s -n2015 -x2022```\
This will specify your paper!!```%bee m p c / h h s -p1```\
This will specify your name!!```%bee m p c / h h s -NSunny```\
\n\
### Supported subjects (PLEASE USE KEY):\n```{list_o_subjects}```\
\nnotes: languages dont work lmao :)\n\
If you find any bugs, or if the links stop working, please message me incessantly until I yell and block you!!! I will fix asap!\n\
This robot\'s code can be found [here!](https://github.com/Milkalotl/ib_study_bot), and yes, you can scream at me there too!\n\n\n{threattext}'

