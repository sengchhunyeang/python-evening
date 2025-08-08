road = "============Do you to go ?============"
option1 = "1-Phnom Penh => Battambong"
option2 = "2-Phnom Penh => PreyVeng"
option3 = "3-Phnom Penh => Kampong Chhnang "
print(road)
print(f"{option1}\n{option2}\n{option3}")
while True:
    inputOption = input("pls input one option :")
    if inputOption == "1":
        print("=" * 40)
        print("Battambong 284km")
        print("4.5h ")
        print("Ticket Price 10$")
        print("thank you ")
    elif inputOption == "2":
        print("=" * 40)
        print("PreyVeng 90km")
        print("2.5h ")
        print("Ticket Price 8$")
        print("thank you ")
    elif inputOption == "3":
        print("=" * 40)
        print("Kampong Chhnang 91km")
        print("2.5h ")
        print("Ticket Price 7$")
        print("thank you")
    else:
        exit  # exit is keyword for stop execute code
