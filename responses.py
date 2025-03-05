from random import choice, randint


sciences = ["physics", "chemistry", "biology", "computer_science", "sports_exercise_and_health_science"]
languages = ["english", "spanish"]
humanities = ["business_management", "geography", "global_politics", "history"]


def help_func():
    list_o_subjects = ""
    for e in sciences:
        list_o_subjects += "- " + e + "\n"
    for e in languages:
        list_o_subjects += "- " + e + "\n"
    for e in humanities:
        list_o_subjects += "- " + e + "\n"

    return f'## Hello! This is the eye bee docks bot!!\n\
Please use **%bee** for a random subject, and **%bee [subject]** for a random paper in that subject!\n\
Nothing else is supported at the moment, and its just math and phys, but its alright!! You got this for sure !!\n\
### Supported subjects (WRITE AS STATED):\n{list_o_subjects}\
\n\n\
If you find any bugs, or if the links stop working, please message me incessantly until I yell and block you!!! I will fix asap!'

def text_formatter(params:tuple) -> str:
    c_subject, c_year, toy, c_level, papers, url = params
    hypertext = f'[{c_subject.capitalize()} {c_year} {toy} {c_level}, paper {papers}]({url})' 

    return f'Here is your exam! Have a lovely day -> {hypertext}'


def handle_string(user_input:str) -> str:
    subjects = ["math", "physics"]
    print(f'[{user_input}]')
    if user_input == "help" or user_input == "h":
        return help_func()
    if user_input != "":
        subjects = [user_input]
    return text_formatter(exam_of_the_day(subjects, 2010, 2023, 0, 0, 0));


def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()
    final_response = handle_string(lowered[5:])
    print(f'Response:[{final_response}]')
    return final_response
    #return handle_string(user_input[4:])

def exam_of_the_day(subjects: list, minyear: int, maxyear: int, time_o_year: int, level: int, papers: int):
    c_subject = choice(subjects)
    c_year = randint(minyear, maxyear)
    c_level = "HL" if level == 0 else "SL"
    if papers == 0:
        papers = randint(1,2)
    if time_o_year == 0:
        time_o_year = randint(1,2)

    toy = "November" if time_o_year == 2 else "May"    
    if c_year == 2020:
        time_o_year = 2

    url: str = find_url(c_subject, c_year, toy, c_level, papers)
    return (c_subject, c_year, toy, c_level, papers, url)

def find_url(subject, year, toy, level, paper):
    
    baseurl = f'https://dl.ibdocs.re/IB%20PAST%20PAPERS%20-%20YEAR/{year}%20Examination%20Session/{toy}%20{year}%20Examination%20Session/'
    tz = "" if toy == "November" else "TZ1_"
    if subject == "math":
        if year == 2024:
            return f'{baseurl}PDF/Mathematics/Mathematics_analysis_and_approaches_paper_{paper}__{tz}{level}.pdf'
        if year == 2023:
            return f'{baseurl}PDFs/Mathematics/Mathematics_analysis_and_approaches_paper_{paper}__{tz}{level}.pdf'
        if year > 2020:
            return f'{baseurl}Mathematics/Mathematics_analysis_and_approaches_paper_{paper}__{tz}{level}.pdf'
        if year > 2015:
            return f'{baseurl}Mathematics/Mathematics_paper_{paper}__{tz}{level}.pdf'
        if year <= 2015:
            return f'{baseurl}Group%205%20-%20Mathematics/Mathematics_paper_{paper}_{tz}{level}.pdf'
    if subject in sciences:
        if year == 2024:
            return f'{baseurl}PDF/Experimental%20Sciences/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year == 2023:
            return f'{baseurl}PDFs/Experimental%20Sciences/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year > 2015:
            return f'{baseurl}Experimental%20sciences/{subject.capitalize()}_paper_{paper}__{tz}{level}.pdf'
        if year <= 2015:
            return f'{baseurl}Group%204%20-%20Sciences/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf'
    if subject in languages:
        if year == 2024:
            return f'{baseurl}PDF/Language%20acquisition/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year == 2023:
            return f'{baseurl}PDFs/Language%20acquisition/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year > 2015:
            return f'{baseurl}Language%20acquisition/{subject.capitalize()}_paper_{paper}__{tz}{level}.pdf'
        if year <= 2015:
            return f'{baseurl}Group%202%20-%20Language%20acquisition/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf'
    if subject in humanities:
        if year == 2024:
            return f'{baseurl}PDF/Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year == 2023:
            return f'{baseurl}PDFs/Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf' 
        if year > 2015:
            return f'{baseurl}Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}__{tz}{level}.pdf'
        if year <= 2015:
            return f'{baseurl}Group%203%20-%20Individuals%20and%20Societies/{subject.capitalize()}_paper_{paper}_{tz}{level}.pdf'

    return "ERROR: SOMETHING WENT WRONG IN find_url FUNCTION"
