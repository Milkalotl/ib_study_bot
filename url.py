import requests
from bs4 import BeautifulSoup
urllist = ["https://google.com"]
for n in urllist:
    r = requests.get(n)
    soup = BeautifulSoup(r.text, "html.parser")
    tbparsed = soup.text
    inputstr = tbparsed[124:]
    inputlist = inputstr.split("KB")
    newlist = []
    for n in inputlist:
        num = n.find(".pdf")
        newlist.append(n[:(num+4)])
    for e in newlist:
        print(e)
    print()

