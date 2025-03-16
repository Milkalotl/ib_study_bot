from datetime import datetime
from random import choice, randint
from url import urlhandler
from discord import Embed, Color

version:float = 0.513


day_of_year = datetime.now().timetuple().tm_yday
day_of_exam = datetime(2025, 4, 28).timetuple().tm_yday

threattext = f"*There's only* ***{day_of_exam-day_of_year}*** *days til exams!!*"


single_letter_key: dict = {"m": "Math", "p": "Physics", "c": "Chemistry", "b": "Biology", "x": "Computer_science", "s": "Sports_exercise_and_health_science", "e": "English", "u": "Spanish", "y": "Business", "g": "Geography", "n": "Global_politics", "h": "History"}

sciences = ["Physics", "Chemistry", "Biology", "Computer_science", "Sports_exercise_and_health_science"]

languages = ["English", "Spanish"]
    
humanities = ["Business", "Geography", "Global_politics", "History"]

iflag = lambda params: int(params[1:])
stringflag = lambda params: params[1:]

def get_response(user_input:str, user_name:str, maxyear, minyear, paper, name, repetitions) -> str:
    #print("getresponse")
    final_embed = handle_string(user_input, user_name, maxyear, minyear, paper, name, repetitions)
    final_embed.set_author(name="★sunny★")
    return final_embed

    #final_response = f' Here is your exam{name.capitalize()}! Have a lovely day!\n\n{hypertext}\n\n{threattext}'
    #print(f'Response:[{final_response}]')
    #print(len(final_response))
    #if len(final_response) > 4096:
    #    final_response = finalurl[:4096] 
    #return final_response

def handle_string(user_input:str, user_name:str, maxyear, minyear, paper, name, repetitions) -> tuple:
    #print("handlestring")
    if "/" not in user_input:
         return error_func(1, "Please specify levels with a / ! Refer to /help!")
    user_input = user_input.strip()
    if name == None:
        name = user_name
    subjects, levels = user_input.replace(" ", "").lower().split("/")
    #print("subjects separated")
    levellist = []
    subjectlist = [] 
    for letter in levels:
        levellist.append("SL" if letter == "s" else "HL")
    for subject in subjects:
        psrt = single_letter_key.get(subject)
        if psrt == None:
            return error_func(2, "Something went wrong! One of your subjects is invalid!") 
        #print(psrt, end="/")
        subjectlist.append(psrt)
    #print(subjectlist)
    #print("handle string works!!")

    if repetitions == 1:
        print("rep=1")
        tf_var = exam_of_the_day(subjectlist, minyear, maxyear, 0, levellist, paper)
        if type(tf_var) == Embed:
            return tf_var
        eb_var = text_formatter(tf_var)
        print(eb_var)
        return embed_builder(eb_var,name)
    replist = []
    tf_text, tf_name = "", ""
    print(replist, tf_name, tf_text)
    for n in range(repetitions):
        print(f"#############rep={n}#################")
        tf_var = exam_of_the_day(subjectlist, minyear, maxyear, 0, levellist, paper)
        if type(tf_var) == Embed:
            return tf_var
        tf_text = text_formatter(tf_var)
        replist.append(tf_text)
    repstring = "\n\n".join(replist)
    #print(type(repstring), repstring)
    print(repstring)
    return embed_builder(repstring, name)
        

def exam_of_the_day(subjectlist: list, minyear: int, maxyear: int, time_o_year: int, level: list[str], paper: int):
    c_subject = choice(subjectlist)
    c_level = level[subjectlist.index(c_subject)]
    c_year = randint(minyear, maxyear)

    if paper == 0:
        if (c_subject == "Math" or c_subject == "History" or c_subject == "Business") and c_level == "HL":
            paper = randint(1,3)
        else:
            paper = randint(1,2)
    if time_o_year == 0:
        time_o_year = randint(1,2)


    if c_year == 2020:
        time_o_year = 2
    toy = "November" if time_o_year == 2 else "May"    

    url: str = find_url(c_subject, c_year, toy, c_level, paper)
    #print("exam of the day works!!")
    return (c_subject, c_year, toy, c_level, paper, url)

def find_url(subject, year, toy, level, paper):
    baseurl = f'https://dl.ibdocs.re/IB%20PAST%20PAPERS%20-%20YEAR/{year}%20Examination%20Session/{toy}%20{year}%20Examination%20Session/'
    finalurl = "ERROR"
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

    if("ERROR" in finalurl):
        return error_func(3, "SOMETHING WENT WRONG IN find_url FUNCTION")
    finalurl += urlhandler(subject, paper, level, finalurl) #found in url.py
    return (finalurl + ".pdf", finalurl + "_markscheme.pdf")

def text_formatter(params:tuple) -> tuple:
    #print("Start of tf")
    c_subject, c_year, toy, c_level, paper, url = params
    #print("Params assigned")
    url_paper, url_markscheme = url
    if "url_grab_failed" in url_paper:
        return f"I'm sorry, there was an error!\nInformation:{c_subject} {c_year} {toy} {c_level} {paper} || {url_paper}"
    #print("Url became")
    hypertext = f'[**{c_subject.capitalize()} {c_year} {toy} {c_level} || Paper {paper} **]({url_paper})\n[Markscheme]({url_markscheme})' 
    #print("text formatter works!!")
    return hypertext

 #maybe make nicer?? whats the point lowkey
def embed_builder(hypertext, name):
    built_embed = Embed(
                    title=f"Here you go {name}!",
                    description=f"{hypertext}\n\n{threattext}"
        )
    return built_embed
def help_func():
    list_o_subjects = ""
    for e in single_letter_key.values():
        list_o_subjects += "> " + list(single_letter_key.keys())[list(single_letter_key.values()).index(e)] + " | " + e + "\n"
    f = open("help_text.txt", "r")
    desc = f.read()
    return Embed(title="HELP!", description=desc.format(version,list_o_subjects, threattext))
def error_func(error_code:int, error_text:str)->Embed:
    return Embed(title=f"Error {error_code}", description=error_text, colour=Color.red())

if __name__ == "__main__":
    import sys
    inputstr = sys.argv[1]
    rep = int(sys.argv[2])
    print(get_response(inputstr,"LOCAL", 2010, 2023, 0, None, rep))
