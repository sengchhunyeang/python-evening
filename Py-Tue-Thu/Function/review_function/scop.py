
# scop : location that declare data

# global variable / global scop
data = "mydata"


def print_year():
    # local scop
    data_s = "mydata_AS this year"
    month = "November"
    print("year",data)
    print("month",month)


def print_month():
    # print(month)
    print(data)

# call function
print_year()
print_month()
