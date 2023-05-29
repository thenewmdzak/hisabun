import mainmenu,fancy

##Personal record keeping that follows Shariah
def welcome():
    print('''
              __    __   __       _______      ___       ______    __    __   __   __  
             |  |  |  | |  |     /       |    /   \     |   _  \  |  |  |  | |  \ |  | 
             |  |__|  | |  |    |   (----`   /  ^  \    |  |_)  | |  |  |  | |   \|  | 
             |   __   | |  |     \   \      /  /_\  \   |   _  <  |  |  |  | |  . `  | 
             |  |  |  | |  | .----)   |    /  _____  \  |  |_)  | |  `--'  | |  |\   | 
             |__|  |__| |__| |_______/    /__/     \__\ |______/   \______/  |__| \__| 
             ====================== The Islamic Accounting App =======================''')

def bye():
    fancy.heading("Thank You for using Hisabun. Have a great day.")

#Program starts executing from here
welcome()
mainmenu.run()
bye()