import requests
from random import choice
from bs4 import BeautifulSoup

keywords = []
def initkeys() -> None:
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
        newlist.append(n[:(num)])
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
        #print(g,end="**")
        print("> " + g)
        if subject in g:
            print("Subject FOUND", end="/")
            if "paper_"+str(paper) in g:
                print("Paper FOUND", end="/")
                if level in g:
                    print("Level FOUND")
                    valid_urllist.append(g)
    #print()
    #print(valid_urllist)
    for e in valid_urllist:
        if "markscheme" in e:
            valid_urllist.remove(e)
    if subject != "Spanish" and subject != "French":
        for e in valid_urllist:
            if "French" in e or "Spanish" in e:
                valid_urllist.remove(e)
    #print(valid_urllist)
    if len(valid_urllist) != 0:
        return choice(valid_urllist)
    return "url_grab_failed"
def subjectmod(subject, urllist:list, keylist:list)-> str:
    for f in keylist:
        for g in urllist:
            if f in g:
                return str(f)

if __name__ == "__main__":
    initkeys()
