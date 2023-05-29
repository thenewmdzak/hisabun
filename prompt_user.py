import check,fancy

def action(limit=50):
    while True:
        user_input=input("|Choice - ")
        if check.is_int(user_input) and int(user_input) in range(limit):
            return int(user_input)
        else:
            fancy.invalid()
            continue
def filename():
    user_input=input("|File Name: ")
    # Future checks on user_input will be done here
    return user_input
def entry():
    amt=None
    inout=None
    date=None
    typeof_entry=None
    detail=None
    full_detail=str()
    while True:
        fancy.line("Note: add a +/- before the number")
        amt=input("|Enter Amount: ")
        if (amt[0]=="+" or amt[0]=="-") and (check.is_int(amt[1:]) and int(amt[1:])!=0):
            if amt[0]=="+":
                inout="In"
            elif amt[0]=="-":
                inout="Out"
            amt=int(amt[1:])
            break
        elif (check.is_int(amt[1:]) and int(amt[1:])==0) or amt=="0":
            return False
        else:
            fancy.invalid()
            continue
    while True:
        fancy.line("Note: Date should be in DD/MM/YYYY format")
        date=input("|Enter Date: ")
        if date=="0":
            return False
        else:
            date_elements=date.strip().split("/")
            if check.is_int(date_elements[0]) and check.is_int(date_elements[1]) and check.is_int(date_elements[2]):
                day=int(date_elements[0])
                month=int(date_elements[1])
                year=int(date_elements[2])
                if month in range(13) and year in range(2024):
                    if month == 1|3|5|7|8|10|12:
                        if day in range(32):
                            date=str(day)
                        else:
                            fancy.invalid()
                            continue
                    elif month == 4|6|9|11:
                        if day in range(31):
                            date=str(day)
                        else:
                            fancy.invalid()
                            continue
                    else:
                        if year%4==0:
                            if day in range(29):
                                date=str(day)
                            else:
                                fancy.invalid()
                                continue
                        else:
                            if day in range(30):
                                date=str(day)
                            else:
                                fancy.invalid()
                                continue
                else:
                    fancy.invalid()
                    continue
                date=f"{date}/{month}/{year}"
                break
            else:
                fancy.invalid()
                continue
    
    fancy.line("What type of entry is it?")
    fancy.line("1 - Person")
    fancy.line("2 - Non-Person")
    user_input=action(limit=3)
    if user_input == 0:
        return False
    else:
        if user_input==1:
            typeof_entry="Person"
        elif user_input==2:
            typeof_entry="Non-Person"
    
    if inout == "In":
        fancy.line("Is this a Loan?")
        fancy.line("1 - Yes")
        fancy.line("2 - No")
        user_input=action(limit=3)
        if user_input == 0:
            return False
        else:
            if user_input==1:
                detail="Loan"
            elif user_input==2:
                detail="Normal"
    elif inout=="Out":
        fancy.line("Did you buy Wealth?")
        fancy.line("1 - Yes")
        fancy.line("2 - No")
        user_input=action(limit=3)
        if user_input == 0:
            return False
        else:
            if user_input==1:
                detail="Wealth"
            elif user_input==2:
                detail="Normal"
    
    amt=str(amt)
    full_detail=f"\n{amt} {date} {inout} {typeof_entry} {detail}"
    return full_detail