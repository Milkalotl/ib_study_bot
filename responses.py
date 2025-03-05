from random import choice, randint

def help_func():
    return f'## Hello! This is the eye bee docks bot!!\nPlease use **%bee** for a random subject, and **%bee [subject]** for a random paper in that subject!\nNothing else is supported at the moment, and its just math and phys, but its alright!! You got this for sure !!\n\nIf you find any bugs, or if the links stop working, please message me incessantly until I yell and block you!!! I will fix asap!'

def handle_string(user_input:str) -> str:
    subjects = ["math", "physics"]
    print(f'[{user_input}]')
    if user_input == "help" or user_input == "h":
        return help_func()
    if user_input != "":
        subjects = [user_input]
    return exam_of_the_day(subjects, 2010, 2023, 0, 0, 0);

def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()
    return handle_string(lowered[5:])
    #return handle_string(user_input[4:])

def exam_of_the_day(subjects: list, minyear: int, maxyear: int, time_o_year: int, level: int, papers: int):
    c_subject = choice(subjects)
    c_year = randint(minyear, maxyear)
    c_level = "HL" if level == 0 else "SL"
    if papers == 0:
        papers = randint(1,2)
    if time_o_year == 0:
        time_o_year = randint(1,2)


    if c_year == 2020:
        time_o_year = 2

    url: str = find_url(c_subject, c_year, time_o_year, c_level, papers)
    return url;

def find_url(subject, year, time_o_year, level, paper):
    toy = "November" if time_o_year == 2 else "May"
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
    if subject == "physics":
        if year == 2024:
            return f'{baseurl}PDF/Experimental%20Sciences/Physics_paper_{paper}_{tz}{level}.pdf' 
        if year == 2023:
            return f'{baseurl}PDFs/Experimental%20Sciences/Physics_paper_{paper}_{tz}{level}.pdf' 
        if year > 2015:
            return f'{baseurl}Experimental%20sciences/Physics_paper_{paper}__{tz}{level}.pdf'
        if year <= 2015:
            return f'{baseurl}Group%204%20-%20Sciences/Physics_paper_{paper}_{tz}{level}.pdf'

    return "ERROR: SOMETHING WENT WRONG IN find_url FUNCTION"
