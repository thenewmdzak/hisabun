def is_int(string,check_pve=True):#is input an integer with added +ve -ve check
    try   :    int(string)
    except:    return False
    if check_pve==True:
        if int(string) > -1:    return True
        else               :    return False
    else:
        return True

def app_size(size):#is input a valid size
    if is_int(size):    return True
    else           :   return False