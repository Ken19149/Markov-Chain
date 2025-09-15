import requests
import re

text = open("books/book collections.html", "r").read() + open("books/other books.html", "r").read()
lists = text.split("a href=\"")
books = []
for i in range(0,len(lists)):
    if lists[i].startswith("/wiki/") and i%2==0: 
        books.append(lists[i].split("\"")[0])

for i in books:
    print("https://genshin-impact.fandom.com" + i)


response = requests.get("https://genshin-impact.fandom.com" + books[1])
# book collections
with open("test.html", "w", encoding="utf8") as f:
    text = (str(response.content)[2:-1].replace("\\n", "").replace("\\t", ""))
    text = text.split("<span class=\"mw-headline\" id=\"Vol._1\">Vol. 1</span>")[1].split("<span class=\"mw-headline\" id=\"Trivia\">Trivia</span>")[0]
    text = text.replace("[", "").replace("]", "").replace("\\", "").replace("&#8212;", "—")

    while "<" in text or ">" in text: 
        text = text.split(">", 1)
        text[0] = text[0].split("<", 1)[0]
        text = f"{text[0]} {text[1]}"

    text = " ".join(text.split())

    f.write(text)