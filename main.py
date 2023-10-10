import json
file = open("data_base.json", "r")
file_content = file.read()
file.close()
if file_content:
    data_list = json.loads(file_content)
else:
    data_list = []

print("-------------Welcome to SIC bank------------")
print("if you already have an account please enter 'login' ")
print("If you don't have an account Enter 'register'")
choice = input().lower()
current_user = None
current_user_idx=None
while True:
    current_user_info=None
    if choice == "register":
        print("----------------Welcome to register page----------------")
        name = input("Please Enter your name : ")
        password = input("Please Enter your password : ")
        phone = input("Please Enter your phone number : ")
        mail = input("Please Enter your E-Mail : ")
        gender = input("Please Enter your gender : ")
        age = input("Please Enter your age : ")
        city = input("Please Enter your city : ")
        Id = len(data_list) + 1

        data_dic = {
            "name": name,
            "password": password,
            "phone": phone,
            "mail": mail,
            "gender": gender,
            "age": age
            , "city": city,
            "Id": Id ,
            "balance": 0
        }
        print("account added successfully " + "Id : ", Id)
        data_list.append(data_dic)
        file = open("data_base.json", "w")
        json.dump(data_list, file, indent=2)
        file.close()
        choice=input("Enter login if you need to login:").lower()

    if choice == "login":
        print("-----------------Welcome to login page------------------- ")
        id = int ( input("Enter your id:"))
        password= input ("Enter your password:")
        i=0
        for person in data_list:
            if person["Id"] == id and person["password"] == password:
                print("Welcome", person["name"])
                current_user=person
                print("here")
                current_user_idx=i

            i+=1
    print("[0] deposit \n [1] withdraw \n [2] transfer \n [3] show your data \n [4] exit \n")
    choice = int(input())
    k=0
    if choice == 0:
        while k == 0:
            list = ["USD", "SAR", "EGP"]
            theamount = int(input("please enter the amount you want to deposit"))
            currency = int(input("please choose the currency(0-USD,1-SAR,2-EGP)"))
            if currency == 0:
                print(f"{theamount}{list[currency]} was deposit successfully!")
                EGP_currency = 30 * theamount
                total_money = EGP_currency + current_user["balance"]
                current_user["balance"]=total_money
                data_list[current_user_idx] = current_user
                print(f"your balance is {total_money}EGP")
                file = open("data_base.json" , "w")
                json.dump(data_list, file)
                file.close()
                break
            elif currency == 1:
                print(f"{theamount}{list[currency]} was deposit successfully!")
                EGP_currency = 9 * theamount
                total_money = EGP_currency + current_user["balance"]
                current_user["balance"] = total_money
                data_list[current_user_idx] = current_user
                print(f"your balance is {total_money}EGP")
                file = open("data_base.json", "w")
                json.dump(data_list, file)
                file.close()
                break
            elif currency == 2:
                print(f"{theamount}{list[currency]} was deposit successfully!")
                total_money = theamount + current_user["balance"]
                current_user["balance"] = total_money
                data_list[current_user_idx] = current_user
                print(f"your balance is {total_money}EGP")
                file = open("data_base.json", "w")
                json.dump(data_list, file)
                file.close()
                break
            else:
                print("please choose in(0,1,2)")
    if choice == 1:
        while k == 0:
            list = ["USD", "SAR", "EGP"]
            theamount = int(input("please enter the amount you want to withdraw"))
            currency = int(input("please choose the currency(0-USD,1-SAR,2-EGP)"))
            if currency == 0:
                EGPcurrency = 30 * theamount
                if current_user["balance"] >= EGPcurrency:
                    total_money = current_user["balance"] - EGPcurrency
                    current_user["balance"] = total_money
                    data_list[current_user_idx] = current_user
                    file = open("data_base.json", "w")
                    json.dump(data_list, file)
                    file.close()
                    print(f"{theamount}{list[currency]} was withdraw successfully!")
                    print(f"your balance is {total_money}EGP")
                    break
                else:
                    print("you don’t have enough money")
                    break
            if currency == 1:
                EGPcurrency = 9 * theamount
                if current_user["balance"] >= EGPcurrency:
                    total_money = current_user["balance"] - EGPcurrency
                    current_user["balance"] = total_money
                    data_list[current_user_idx] = current_user
                    file = open("data_base.json", "w")
                    json.dump(data_list, file)
                    file.close()
                    print(f"{theamount}{list[currency]} was withdraw successfully!")
                    print(f"your balance is {total_money}EGP")
                    break
                else:
                    print("you don’t have enough money")
                    break
            if currency == 2:
                if current_user["balance"] >= currency:
                    total_money = current_user["balance"] - theamount
                    current_user["balance"] = total_money
                    data_list[current_user_idx] = current_user
                    file = open("data_base.json", "w")
                    json.dump(data_list, file)
                    file.close()
                    print(f"{theamount}{list[currency]} was withdraw successfully!")
                    print(f"your balance is {total_money}EGP")
                    break
                else:
                    print("you don’t have enough money")
                    break
            else:
                print("please choose in(0,1,2)")
    if choice == 2:
        while True:
            money_transfer = int(input("Please enter the amount you want to transfer:"))
            person2 = int(input("PLease enter the ID of the account you want to transfer money to:"))
            person1_money = 0
            person2_money = 0
            l = 0
            is_found = False

            transffered_person = None
            transffered_person_idx = -1

            for person in data_list:
                if person["Id"] == person2:
                    transffered_person = person
                    transffered_person_idx = l
                    is_found = True
                    break
                l += 1

            if is_found == True:
                if current_user["balance"]>= money_transfer :
                    current_user["balance"] -= money_transfer


                    transffered_person['balance'] += money_transfer

                    data_list[current_user_idx] = current_user
                    data_list[transffered_person_idx] = transffered_person
                print(f"{money_transfer} EGP was transferred to {person2}")
                print(f"your balance is {current_user['balance']} EGP")
                file = open("data_base.json", "w")
                json.dump(data_list, file, indent=2)
                file.close()
                break
            else :
                print("wrong id")
    if choice == 3:
        print(current_user)


    if choice == 4:
        print("thank you")
        break

