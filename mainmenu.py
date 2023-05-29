import fancy,os,filemenu,prompt_user

def display_menu():
    fancy.heading("Main Menu")
    fancy.line("1 - New File")
    fancy.line("2 - Open File")
    fancy.line("0 - Exit")

def file_creation(file_name,file_directory="./userfiles/"):
    fhand=open(file_directory+file_name+".txt","a")
    fhand.write("Amount Date In/Out Type Detail")
    fhand.close()
    fancy.line(f"{file_name} created",align="center")
    filemenu.run(file_name)

def does_file_exist(file_name,file_directory="./userfiles/"):
    available_files=os.listdir(file_directory)
    if file_name+".txt" in available_files:
        return True
    else:
        return False

def file_precheck(file_name,mode):
    if mode=="new_file":
        if does_file_exist(file_name):
            fancy.line("File already there.",align="center")
            return False
        else:
            return True
    elif mode=="open_file":
        if not does_file_exist(file_name):
            fancy.line("File not found.",align="center")
            return False
        else:
            return True

def new_file():
    fancy.subheading("New File")
    file_name=prompt_user.filename()
    if file_precheck(file_name,mode="new_file"):
        file_creation(file_name)
    else:
        fancy.line(f"Do you want to open {file_name}?")
        fancy.line("1 - Yes")
        fancy.line("0 - No")
        action=prompt_user.action(limit=2)
        if action==1:
            filemenu.run(file_name)

def open_file():
    fancy.subheading("Open File")
    file_name=prompt_user.filename()
    if file_precheck(file_name,mode="open_file"):
        filemenu.run(file_name)
    else:
        fancy.line(f"Do you want to create file {file_name}?")
        fancy.line("1 - Yes")
        fancy.line("0 - No")
        action=prompt_user.action(limit=2)
        if action==1:
            file_creation(file_name)

def run():
    while True:
        display_menu()
        action=prompt_user.action(limit=3)
        if   action==0:
            break
        elif action==1:
            new_file()
        elif action==2:    
            open_file()