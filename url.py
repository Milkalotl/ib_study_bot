import requests
from random import choice
from bs4 import BeautifulSoup

keywords = []
def initkeys() -> None:
    f = open("subjectkeys", "r")
    filelist = f.read().split("-")
    for e in filelist:
        keywords.append(e.strip("\n").strip().split("/"))
        #print(keywords)

def urlhandler(subject, paper, level, furl:str) -> str:
    initkeys()
    print("furl", furl)
    r = requests.get(furl)
    soup = BeautifulSoup(r.text, "html.parser")
    tbparsed = soup.text
    #print(tbparsed)
    inputstr = tbparsed[124:]
    inputlist = inputstr.split("KB")
    newlist = []
    for n in inputlist:
        num = n.find(".pdf")
        newlist.append(n[:(num)])
    #print("newlist", newlist)
    return urlpicker(subject, paper, level, newlist)

def urlpicker(subject, paper, level, urllist:list)-> str:
    #print(f"Original Subject: {subject}")
    for e in keywords:
        #print(e, end = " / ")
        #print(e[0])
        if subject == e[0]:
            subject = subjectmod(subject, urllist, e[1:])
            break
    #print(f"Current Subject: {subject}")
    valid_urllist = []
    for g in urllist:
        if (subject in g) and ("paper_"+str(paper) in g) and (level in g):
            if ("markscheme" not in g) and ("French" not in g) and ("Spanish" not in g) and ("German" not in g):
                valid_urllist.append(g)
            #print(valid_urllist.index(g))
    for e in valid_urllist:
        print("<",e,">")
    #print(valid_urllist)
    if len(valid_urllist) != 0:
        return choice(valid_urllist)
    return "url_grab_failed"
def subjectmod(subject, urllist:list, keylist:list)-> str:
    for f in keylist:
        #print("f>",f)
        for g in urllist:
            #print("g>",g)
            if f in g:
                return str(f)

if __name__ == "__main__":
    initkeys()
