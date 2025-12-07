with (open("testing.txt","w") as file) :
    # print index
    for index, text in enumerate(file) :
        print(index,text)


