def personal_user(name="No name",age=0,gender="No Set"): # Parameter can be set by default
    print("Information of User:",name)
    print("="*20)
    return f"{name} + {name} + {name}"
personal_user(name="tola",age=20,gender="Male")

UserRith = personal_user("Rith",9,"Male")
UserLeang = personal_user("Leang",21,"Male")
UserViset = personal_user("Viset",18,"Female")

