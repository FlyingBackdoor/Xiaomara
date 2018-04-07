import dataset
from colorama import Fore

#This function will add data into database, it required two arguments.
def insrtIntoDB(md5, file_loc):
    try:
        db = dataset.connect(r"sqlite:///E:\Projects\Minor Project\data\database.db")
        table = db['files_history']
        table.insert(dict(md5=md5, location=file_loc))
        print("Entry Added Successfully...")
    except Exception as err:
        print(err)

#This function is useful for retriving all the values available in Database
#md5 color code is green and location color is red
def showData():
    db = dataset.connect(r"sqlite:///E:\Projects\Minor Project\data\database.db")
    print(db['files_history'].columns)
    for item in db['files_history']:
       print(Fore.GREEN +item['md5'] +"\t" +Fore.LIGHTBLUE_EX +item['location'])
    print(Fore.WHITE)

#Use md5 value only as an argument to check whether it is available in
def search(value):
    db = dataset.connect(r"sqlite:///E:\Projects\Minor Project\data\database.db")
    table = db['files_history']
    temp = table.find_one(md5 = value)
    if temp is not None:
        temp.pop('id')
        print("Already available in db \nLocation: "+temp.get('location'))
        return True
    else:
        return False

#print(search('7819bbf0bb6a1abe1f5eb6320fa7309b'))
