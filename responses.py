from datetime import datetime
from random import choice, randint
from url import urlhandler
from discord import embed

version:float = 0.103


day_of_year = datetime.now().timetuple().tm_yday
day_of_exam = datetime(2025, 4, 28).timetuple().tm_yday

threattext = f"*There's only* ***{day_of_exam-day_of_year}*** *days til exams!!*"



single_letter_key: dict = {"m": "Math", "p": "Physics", "c": "Chemistry", "b": "Biology", "x": "Computer_science", "s": "Sports_exercise_and_health_science", "e": "English", "u": "Spanish", "y": "Business", "g": "Geography", "n": "Global_politics", "h": "History"}

sciences = ["Physics", "Chemistry", "Biology", "Computer_science", "Sports_exercise_and_health_science"]

languages = ["English", "Spanish"]

humanities = ["Business", "Geography", "Global_politics", "History"]

iflag = lambda params: int(params[1:])
stringflag = lambda params: params[1:]

def get_response(user_input:str) -> str:
    handletuple = handle_string(user_input[5:])
    if len(handletuple) == 1:
        return str(handletuple)
    hypertext, name = handletuple
    final_response = f' Here is your exam{name.capitalize()}! Have a lovely day!\n\n{hypertext}\n\n{threattext}'
    #print(f'Response:[{final_response}]')
    if len(final_response) > 4096:
        final_response = finalurl[:4096] 
    return final_response

def handle_string(user_input:str) -> tuple:
    if user_input == "help" or user_input == "h" or user_input == "":
        return help_func()
    if "/" not in user_input:
        return "Please specify levels with a / ! Refer to %bee help!"
    user_input = user_input.strip()
    
    repetitions: int = (int(x) if (x := user_input[:1]).isnumeric() else 1)
    if repetitions > 1:
        user_input = user_input[1:]
    
    print(repetitions)


    ui_split = user_input.split("-")
    content = ui_split[0]
    content = content.lower()
    ui_split = ui_split[1:]
    maxyear, minyear, papers, name = 0, 0, 0, "";

    for n in ui_split:
        match n[:1]:
            case "N":
                #print("namechosen")
                name = " " + stringflag(n)
            case "x":
                maxyear = iflag(n)
            case "n":
                minyear = iflag(n)
            case "p":
                papers = iflag(n)
            case "y":
                maxyear = iflag(n)
                minyear = iflag(n)

    subjects, levels = content.replace(" ", "").split("/")
    levellist = []
    subjectlist = [] 
    for letter in levels:
        levellist.append("SL" if letter == "s" else "HL")
    for subject in subjects:
        psrt = single_letter_key.get(subject)
        if psrt == None:
            return "Something went wrong! One of your subjects is invalid!"
        #print(psrt, end="/")
        subjectlist.append(psrt)
    #print()
    print("handle string works!!")

    if repetitions == 1:
        return text_formatter(exam_of_the_day(subjectlist, minyear, maxyear, 0, levellist, papers,name))


    replist = []
    tf_text, tf_name = "", ""
    print(replist, tf_name, tf_text)
    for n in range(repetitions):
        tf_text, tf_name  = text_formatter(exam_of_the_day(subjectlist, minyear, maxyear, 0, levellist, papers,name))
        print(f"{tf_text} ! {tf_name}")
        replist.append(tf_text)
    repstring = "\n\n".join(replist)
    #print(type(repstring), repstring)
    return (repstring, tf_name)
        

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
    #print("exam of the day works!!")
    return (c_subject, c_year, toy, c_level, papers, url, name)

def find_url(subject, year, toy, level, paper):
    baseurl = f'https://dl.ibdocs.re/IB%20PAST%20PAPERS%20-%20YEAR/{year}%20Examination%20Session/{toy}%20{year}%20Examination%20Session/'
    finalurl = "ERROR: SOMETHING WENT WRONG IN find_url FUNCTION"
    tz = "" if toy == "November" else "TZ1_"

    if year == 2023 and toy == "November":
            baseurl += 'PDFs/'
    elif year > 2022:
            baseurl += 'PDF/'

    if subject == "Math":
        #print("MATH")
        if year > 2020:
            finalurl = f'{baseurl}Mathematics/'
        elif year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Mathematics/'
        else:
            finalurl = f'{baseurl}Group%205%20-%20Mathematics/'

    elif subject in sciences:
        #print("SCI")
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Experimental%20sciences/'
        else:
            finalurl = f'{baseurl}Group%204%20-%20Sciences/'

    elif subject in languages:
        #print("LANG")
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Studies%20in%20language%20and%20literature/'
        else:
            finalurl = f'{baseurl}Group%201%20-%20Studies%20in%20Language%20and%20Literature/'
    elif subject in humanities:
        #print("HUMA")
        if year > 2015 and not (year == 2016 and toy == "May"):
            finalurl = f'{baseurl}Individuals%20and%20societies/'
        else:
            finalurl = f'{baseurl}Group%203%20-%20Individuals%20and%20Societies/'
-+

    finalurl += urlhandler(subject, paper, level, finalurl) #found in url.py
    return (finalurl + ".pdf", finalurl + "_markscheme.pdf")

def text_formatter(params:tuple) -> tuple:
    #print("Start of tf")
    c_subject, c_year, toy, c_level, papers, url, name = params
    #print("Params assigned")
    url_paper, url_markscheme = url
    if "url_grab_failed" in url_paper:
        return f"I'm sorry, there was an error!\nInformation:{c_subject} {c_year} {toy} {c_level} {papers} || {url_paper}"
    #print("Url became")
    hypertext = f'[**{c_subject.capitalize()} {c_year} {toy} {c_level} || Paper {papers} **]({url_paper})\n[Markscheme]({url_markscheme})' 
    #print("text formatter works!!")
    return (hypertext, name)

 #maybe make nicer?? whats the point lowkey
def help_func():
    list_o_subjects = ""
    for e in single_letter_key.values():
        list_o_subjects += "> " + list(single_letter_key.keys())[list(single_letter_key.values()).index(e)] + " | " + e + "\n"

    return f' Hello! This is the eye bee docks bot!!\n\
Current Version: {version}\n\
The syntax is simple!\nFor a random paper in Math HL, Physics HL, or chemistry SL, you would write\n```%bee m p c / h h s```\nIt\'s that simple! (spaces are optional, but slash is not)\n\
 Additional flags!!\
\n\
This will specify min and max years!!```%bee m p c / h h s -n2015 -x2022```\
This will specify a specific year!!```%bee m p c / h h s -y2018```\
This will specify your paper!!```%bee m p c / h h s -p1```\
This will specify your name!!```%bee m p c / h h s -NSunny```\
\n\
 Supported subjects (PLEASE USE KEY):\n```{list_o_subjects}```\
\nnotes: if your link doesnt work for one of the subjects, please try a different subject level! Especially sports science!\n\
If you find any bugs, or if the links stop working, please message me incessantly until I yell and block you!!! I will fix asap!\n\
This robot\'s code can be found [here!](https://github.com/Milkalotl/ib_study_bot), and yes, you can scream at me there too!\n\n\n{threattext}'



if __name__ == "__main__":
    import sys
    inputstr = sys.argv[1]
    print(get_response("%bee " + inputstr))
