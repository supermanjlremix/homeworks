try:
    my_file = open("index.txt", "r") 
    html_file = my_file.readlines()
except FileNotFoundError:
    print("File Not Found Error")
finally:
    my_file.close()

print(html_file)
# for row in html_file:
#     if "<title>" in row:
#         for symbol in row:
#             if symbol == ">":
#                 row = row[row.index(symbol):]
#                 print(row)



