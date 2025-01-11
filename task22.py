import csv
import collections

def max_crime(crimes):
    max = -1
    type = ''
    for key in crimes:
        crime = key
        count = crimes[key]
        if count > max:
            max = count
            type = crime
            
    return type

def get_date(crime): # crime – dictionary
    date = crime['Date'][6:10]
    return date
    

crimes = {}
with open('Crimes.csv') as f:
    file = csv.DictReader(f)
    for row in file:
        crime = row['Primary Type']
        date = get_date(row)
        
        if date == "2015":
            if crime in crimes:
                crimes[crime] += 1
            else: # new type of crime
                crimes[crime] = 1
    
    
    answer = max_crime(crimes)
    print(answer)
    
    
#     for i, row in enumerate(file):
#         print(row)
#         if i >= 10:
#             break