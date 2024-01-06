try:
    my_file = open("index.html", "r", encoding="utf8") 
    html_file = my_file.read()
except FileNotFoundError:
    print("File Not Found Error")
finally:
    my_file.close()

html_file = html_file.split("\n")

for row in html_file:
    title = ""
    if "<title>" and "</title>" in row:
        title = row.strip().replace("<title>","").replace("</title>","")
        print(title)

    h1 = ""
    if "<h1" and "</h1>" in row:
        h1 = row.strip().replace("<h1","").replace("</h1>","")
        if ">" in h1:
            h1 = h1[h1.index(">")+1:]
            print(h1)

    h2 = ""
    if "<h2" and "</h2>" in row:
        h2 = row.strip().replace("<h2","").replace("</h2>","")
        if ">" in h2:
            h2 = h2[h2.index(">")+1:]
            print(h2)

    h3 = ""
    if "<h3" and "</h3>" in row:
        h3 = row.strip().replace("<h3","").replace("</h3>","")
        if ">" in h3:
            h3 = h3[h3.index(">")+1:]
            print(h3)

    h4 = ""
    if "<h4" and "</h4>" in row:
        h4 = row.strip().replace("<h4","").replace("</h4>","")
        if ">" in h4:
            h4 = h4[h4.index(">")+1:]
            print(h4)

    h5 = ""
    if "<h5" and "</h5>" in row:
        h5 = row.strip().replace("<h5","").replace("</h5>","")
        if ">" in h5:
            h5 = h5[h5.index(">")+1:]
            print(h5)

    h6 = ""
    if "<h6" and "</h6>" in row:
        h6 = row.strip().replace("<h6","").replace("</h6>","")
        if ">" in h6:
            h6 = h6[h6.index(">")+1:]
            print(h6)
        
            



