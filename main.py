# text = open("books/book collections.html", "r").read()
# text = open("books/other books.html", "r").read()
text = open("books/book collections.html", "r").read() + open("books/other books.html", "r").read()
lists = text.split("a href=\"")
books = []
for i in range(0,len(lists)):
    if lists[i].startswith("/wiki/") and i%2==0: 
        books.append(lists[i].split("\"")[0])

for i in books:
    print("https://genshin-impact.fandom.com" + i)