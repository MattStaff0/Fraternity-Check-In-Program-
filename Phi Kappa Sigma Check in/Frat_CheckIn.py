'''
Matthew Stafford
Fraternity Check In Program 
'''
# imports 
import gspread
import datetime

# list intialization 
def make_master_list():
    names = ['Henry Smith', 'Miles Henry', 'Will Reed', 'Andrew Giuliani', 'Austin Spieles',
            'Avner Mangeot', 'Ben Bryant', 'Brad Parsons', 'Bradin Haynie',
            'Chris Wohl', 'Cole Rosenthal', 'Jack Decicco', 'Ethan Bayerlein',
            'Greg Willmering', 'Jack Carrigan', 'Jack Eggers', 'Jack Gustafson',
            'Jackson Brooks', 'James Gullet', 'Kale Pittman', 'Landon Provost',
            'Liam Runyon', 'Luc Covella', 'Lucas Levenberg', 'Mason Gallarneau',
            'Matthew Stafford', 'Micheal Kotchian', 'Nick Gimbel', 'Nico Rodreiguez',
            'Oliver Mandel', 'Phillip Himmelreich', "Ryan O'Niel", 'Ryan Palmer',
            'Sam Walton', 'Thomas Dunn', 'Trent Varga', 'Vincent Castano', 'Will Elrod',
            'Will Heekin', 'Will McMilan', 'Will Stokes', 'Grayson Jukuc']
    return names

def get_is_here_list():
    is_here = []
    return is_here

def get_not_here_list():
    not_here = []
    return not_here

def connect_open_google_file(service_file_name, googleform_name, worksheet_name):
    # Opening Files 
    sa = gspread.service_account(service_file_name)
    sh = sa.open(googleform_name)

    # worksheet
    wks = sh.worksheet(worksheet_name)
    return wks

# getting all values in the google sheet form
def get_vals(wks):
    all_vals = []

    values = wks.get_all_values()
    #print(values)
    for val in values:
        #print(f'This is {val[0]}')
        if val[0].lower() != 'timestamp':
            if val[0] != '':
                all_vals.append(val)

    return all_vals

# only getting names for the right date
def get_current_date():
    current_datetime = datetime.datetime.now()

    current_date = current_datetime.date()
    current_date = current_date.strftime("%Y-%m-%d")

    return current_date

#chaning the date time values in all vals list
def change_to_datetime(all_vals):
    data = all_vals
    for item in data:
        item[0] = datetime.datetime.strptime(item[0],'%m/%d/%Y %H:%M:%S') 
    for item in data:
        item[0] = item[0].strftime('%Y-%m-%d')
    return data

def make_is_here_list(all_vals, here_list, names_list):
    for list in all_vals:
        if list[0] == current_date:
            if list[1] in names_list:
                here_list.append(list[1])
    return here_list

def make_not_here_list(not_here_list, here_list, names):
     for name in names:
        if name not in here_list:
            not_here_list.append(name)
     return not_here_list


def compare_dates(current_date, all_vals):
    names = make_master_list()
    here_list = get_is_here_list()
    not_here_list = get_not_here_list()
    current_date = current_date
    data = all_vals

    here_attendance = make_is_here_list(all_vals, here_list, names)
    not_here_attendance = make_not_here_list(not_here_list, here_list, names)

    return here_attendance, not_here_attendance

# Fucntion Calls

# gets current date 
current_date = get_current_date()

# getting the worksheet obj 
get_wks = connect_open_google_file('phi-kappa-sigma-check-in-fe9de7c84420.json', "Phi Kappa Sigma Check-in  (Responses)", "CheckIn" )

#getting all values 
all_vals = get_vals(get_wks)

#changing all dates to datetime form to comapre to current date
print(change_to_datetime(all_vals))

#compares the dates 

#if date matches will put in list that they were there // if not then put in not there list

here_attendance, not_here_attendance = compare_dates(get_current_date(), all_vals)
    
print("Here: ", here_attendance)
print("Not here: ", not_here_attendance)



        





    




