import requests
import re

# get book list
text = open("books/book collections.html", "r").read() + open("books/other books.html", "r").read()
lists = text.split("a href=\"")
books = []
for i in range(0,len(lists)):
    if lists[i].startswith("/wiki/") and i%2==0: 
        books.append(lists[i].split("\"")[0])


# miscellenous functino
def remove_between(text, str1, str2): 
    while str1 in text or str2 in text: 
            text = text.split(str2, 1)
            text[0] = text[0].split(str1, 1)[0]
            text = f"{text[0]} {text[1]}"
    text = " ".join(text.split())
    return text

# get book content
def book_collection(link, location): 
    response = requests.get(link)
    name = str(link).split("/")[-1]
    with open(f"{location}/{name}.txt", "w", encoding="utf8") as f:
        text = (str(response.content)[2:-1].replace("\\n", "").replace("\\t", ""))
        try: 
            text = text.split("<span class=\"mw-headline\" id=\"Vol._1\">Vol. 1</span>")[1].split("<span class=\"mw-headline\" id=\"Trivia\">Trivia</span>")[0]
        except Exception as e: 
            print("FAILED")
            # text = text.split("<span id=\"Vol_1\" class=\"mw-headline\">Vol 1</span>")[1].split("<span class=\"mw-headline\" id=\"Trivia\">Trivia</span>")[0]
            text = ""
            return ""
        
        try: 
            text = text.split("Other Languages")[0]
        except: 
            pass

        text = text.replace("[", "").replace("]", "").replace("\\", "").replace("&#8212;", "—")

        text = remove_between(text, "<", ">")
        # text = remove_between(text, "{", "}")
        print(text)
        f.write(text)
        return text

def other_book(link, location): 
    response = requests.get(link)
    name = str(link).split("/")[-1]
    with open(f"{location}/{name}.txt", "w", encoding="utf8") as f:
        text = (str(response.content)[2:-1].replace("\\n", "").replace("\\t", ""))
        try:
            text = text.split("<span class=\"mw-headline\" id=\"Text\">Text</span>")[1].split("<span class=\"mw-headline\" id=\"Trivia\">Trivia</span>")[0]
        except: 
            print("FAILED")
            '''
            try: 
                text = text.split("<span id=\"Lore\" class=\"mw-headline\">Lore</span>")[1].split("<span id=\"Other_Languages\" class=\"mw-headline\">Other Languages</span>")[0]
            except: 
                text = text.split("<span id=\"Description\" class=\"mw-headline\">Description</span>")[1].split("<span id=\"Other_Languages\" class=\"mw-headline\">Other Languages</span>")[0]
            '''
            text = ""
            return ""
        text = text.replace("[", "").replace("]", "").replace("\\", "").replace("&#8212;", "—")

        text = remove_between(text, "<", ">")

        try: 
            text = text.split("Other Languages")[0]
        except: 
            pass

        # text = remove_between(text, "{", "}")
        print(text)
        f.write(text)
        return text

with open("book content.txt", "w") as f:
    f.write("")

with open("books/book collections list.txt", "r", encoding="utf8") as f: 
    lists = f.read().split("\n")
    for i in range(0, len(lists)): 
        try:
            with open("book content.txt", "a", encoding="utf8") as content: 
                content.write(book_collection(lists[i], "books/book collections contents"))
                print(f"Book Collection Done ({i+1}/{len(lists)}): {lists[i]}")
        except Exception as e: 
            print(f"----------\nFailed ({i+1}/{len(lists)}) | Book Collection: {lists[i]}\n{e}\n----------")

print("===========================\nBook Collections Completed!!!\n===========================")

with open("books/other books list.txt", "r", encoding="utf8") as f: 
    lists = f.read().split("\n")
    for i in range(0, len(lists)): 
        try: 
            with open("book content.txt", "a", encoding="utf8") as content: 
                content.write(other_book(lists[i], "books/other books contents"))
                print(f"Other Book Done ({i+1}/{len(lists)}): {lists[i]}")
        except Exception as e: 
            print(f"----------\nFailed ({i+1}/{len(lists)}) | Other Book: {lists[i]}\n{e}\n----------")

print("===========================\n Other Books Completed!!!\n===========================")

