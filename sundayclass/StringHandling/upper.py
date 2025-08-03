text = "welcome to ict and this to study " # Declare string (Text)
# upper()
print(text.upper()) # method upper for convert anything to text uppercase 

text1 = "Welcome to ICT for Convert to lowercase " # index : 0-10000
print(text1.lower())
print(text1.find("t"))

print(text1.replace("Welcome","Hello"))
text2= "Hello world something and somthing "
# print(text2.split())


list = ["Apple","book","Movie","Language"] # 3index : 0 1 2
# sentence = "I like \b".join(list)
# print("I like :",sentence)
for index, item in enumerate(list) :
    # print("I like : ",item)
    print(f"Index :{index} item :{item}")

