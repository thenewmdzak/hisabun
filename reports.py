def get_summable_list():
    types=[
        ["Money In"    ,0],
        ["Money Out"   ,0],
        ["Total Debt"  ,0],
        ["Physical Wealth",0],
        ["Balance"     ,0]
    ]
    return types
def totals(file_data):
    file_data=file_data[1:] 
    summed_data=get_summable_list()
    for i in range(len(file_data)):
        if file_data[i][2].lower() == "in":
            summed_data[0][1] += int(file_data[i][0])
            if file_data[i][4].lower() == "loan":
                summed_data[2][1] += int(file_data[i][0])
        elif file_data[i][2].lower() == "out":
            summed_data[1][1] += int(file_data[i][0])
            if file_data[i][4].lower() == "wealth":
                summed_data[3][1] += int(file_data[i][0])
    if file_data:
        summed_data[4][1]=summed_data[0][1]-summed_data[1][1]
    return summed_data

def get_data_from_file(fhand):
    file_data=list()
    first_line=True
    i=1
    for each_line in fhand:
        entry_details=each_line.strip().split(" ")
        file_data.append(entry_details)
        if first_line:
            first_line=False
        else:
            file_data[i][0]=int(file_data[i][0])
            i += 1
    return file_data