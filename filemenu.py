import fancy,prompt_user,reports

def display_menu():
    fancy.subheading("Actions Menu")
    fancy.line("1 - New Entry")
    fancy.line("2 - Show all Entries")
    fancy.line("3 - Balance")
    fancy.line("0 - Exit")

def display_entry(file_name,file_directory,mode):
    fhand=open(file_directory+file_name+".txt")
    file_data=reports.get_data_from_file(fhand)
    fhand.close()
    if mode=="entries":
        fancy.table(file_data)
    elif mode=="balance":
        totals=reports.totals(file_data)
        fancy.table(totals)

def new_entry(file_name,file_directory):
    fancy.subheading("New Entry")
    # fhand=open(file_directory+file_name+".txt")
    # file_data=reports.get_data_from_file(fhand)
    # fhand.close()
    # totals=reports.totals(file_data)
    # available_balance=totals[4][1]
    entry=prompt_user.entry()
    if not entry:
        return
    else:
        fhand=open(file_directory+file_name+".txt","a")
        fhand.write(entry)
        fhand.close()
        fancy.line("Entry made Successfully",align="center")

def run(file_name,file_directory="./userfiles/"):
    fancy.heading(file_name)
    while True:
        display_menu()
        action=prompt_user.action(limit=4)
        if   action==0:
            break
        elif action==1:
            new_entry(file_name,file_directory)
            continue
        elif action==2:
            display_entry(file_name,file_directory,mode="entries")
            continue
        elif action==3:
            display_entry(file_name,file_directory,mode="balance")
            continue