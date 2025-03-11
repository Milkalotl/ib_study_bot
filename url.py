import requests
from random import choice
from bs4 import BeautifulSoup

keywords = []
def initkeys():
    f = open("subjectkeys", "r")
    filelist = f.read().split("-")
    for e in filelist:
        keywords.append(e.strip("\n").strip().split("/"))
    if __name__ == "__main__":
        print(keywords)

def urlhandler(subject, paper, level, furl:str) -> str:
    initkeys()
    r = requests.get(furl)
    soup = BeautifulSoup(r.text, "html.parser")
    tbparsed = soup.text
    inputstr = tbparsed[124:]
    inputlist = inputstr.split("KB")
    newlist = []
    for n in inputlist:
        num = n.find(".pdf")
        newlist.append(n[:(num+4)])
    return urlpicker(subject, paper, level, newlist)

def urlpicker(subject, paper, level, urllist:list)-> str:
    for e in keywords:
        if subject in e[0]:
            print("SUBJECT WAS " + subject)
            subject = subjectmod(subject, urllist, e)
            print("SUBJECT NOW IS" + subject)
    valid_urllist = []
    for g in urllist:
        #print(g,end="**")
        print("> " + g)
        #if subject in g and str(paper) in g and level in g:
                #valid_urllist.append(g.strip(".pdf"))
        if subject in g:
            print("Subject FOUND", end="/")
            if str(paper) in g:
                print("Paper FOUND", end="/")
                if level in g:
                    print("Level FOUND")
                    valid_urllist.append(g.strip(".pdf"))
    print()
    print(valid_urllist)
    if len(valid_urllist) != 0:
        return choice(valid_urllist)
    return "url_grab_failed"
def subjectmod(subject, urllist:list, keylist:list)-> str:
    for f in keylist:
        for g in urllist:
            if f in g:
                return f

if __name__ == "__main__":
    initkeys()
