Book = ["English","Khmer","Korean"]
# print("book before using append() :",Book)
# Book.append("Vietnam")
# print("book after using append() :",Book)

Book1 = ["Vn","Myanmar","Laos"]
Book1[0]="Vietnamese"
Book1.extend(Book)
print(Book1)