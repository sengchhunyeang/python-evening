book = ["python","Java","PHP"] #list
# index : 0 1 2
# list is container store data as string int
# String datatype store data as text
# int datatype store data as number (Example : 1 2 3 45 55)
# How to call list print list
print(book)
#
print("print index of Python :",book[2])

# How to remove list item 
bookRemove=book.remove("PHP")
print(book)

book.insert(2,"HTML")
print("book added HTML",book)
book.append("JavaScript")
print(book)

