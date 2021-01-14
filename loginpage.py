def linearsearch(list, maxindex):  # creating a linearserch program
    useridfound = False
    loginok = False
    myuserid = str(input("enter user id"))
    mypass = (input("enter tha pass"))
    while loginok == False:
        for index in range(len(list)):
            if list[index] == myuserid:
                useridfound = True
                if useridfound == True:
                    for index in range(len(list)):
                        if list[index] == mypass:
                            loginok = True
    if loginok == True:
        print("login succesfull")
    else:
        print("login not valid")


# example recods on a dtatbase
useridlist = ["faisal", "ahmed", "bronxe", "jhon"]
userpasslist = ["Alphanumer", "ABCD1234", "GHJNMB",
                "FGGGD"]  # example recods on a dtatbase
linearsearch(useridlist, 4)
