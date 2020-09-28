import datetime
from datetime import datetime as date

def getdate(year, month, day):
    #turns the variables into a date
    date1= datetime.date(year, month, day)
    return date1

def pp(year, month, day):
    #The function tells whether to add or subtract, i.e., it tells us if the date is after the current date or before the current date
    
    now= datetime.datetime.now()
    x= now.year
    y= now.month
    z=now.day
    if(year>x):
        return 0   #when the day is in future (years later)
    else:
        if(year<x):
            return 1   #when the day is in the past(years ago)
        else:
            if(y<month):
                return 2   #when the year is the same but the month is in the future
            else:
                if(y>month):
                    return 3   #when the year is the same but the month is in the past
                else:
                    if(z<day):
                        return 4   #when the year and month are the same but the day is in the future
                    else:
                        if(z>day):
                            return 5  #when the year and month are the same but the day is in the past
                        else:
                            return 6   #when its the same date
                         

def lpf ( year ):
    #tells us whether a certain year is a leap year or not
    
    if(year%100==0 and year%400==0):
        return 0
    elif(year%4==0 and year % 100!=0):
        return 0
    else:
        return 1

def lp2 ( year, month, day):
    #tells us how many days to add
    
    m= pp(year, month, day)
    now= datetime.datetime.now()
    x= now.year
    y=now.month
    z=now.day
    
    if(m==0):
        t=0
        if(lpf(year)==0 and month < 2):
            t=-1
        if(lpf(year)==0 and month==2 and day<=29):
            t=-1
        while( year>=x ):
            if ( lpf(year)==0):
                t=t+1
            year=year-1

    else:
        if(m==1):
            t=0
            if(lpf(year)==0 and month > 2):
                t=-1
            if(month==2 and day==29):
                t=-1
            while( year <= x ):
                if ( lpf(year)==0):
                    t=t+1
                year=year+1

    return t



def dc ( year, month, day):
    #calculate the number of days

    a=pp( year, month, day)
    now= datetime.datetime.now()
    x= now.year
    y=now.month
    z=now.day
    m=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(a==0): #when the day is in future (years later)
        d=lp2(year, month, day)
        w=year
        while(w>x and year>x):
            if(year-1==x and month<=y):
                w=0
            else:
                d=d+365
            year=year-1
        d=d+day
        month=month-1
        while(y>month):
            d=d+m[month-1]
            month=month-1
            if(month<1):
                month=12
        while(y<month):
            d=d+m[month-1]
            month=month-1
        d=d+(m[y-1]-z)
    else:
        if(a==1): #when the day is in the past(years ago)
            d=lp2(year, month, day)
            w=year
            while(w<x and year<x):
                if(year+1==x and month>=y):
                    w=0
                else:
                    d=d+365
                year=year+1
            if(month==2 and day==29):
                d=d+(m[month-1]-day+1)
            else:
                d=d+(m[month-1]-day)
                
            month=month+1
            while(y<month):
                if(month==12):
                    d=d+m[month-1]
                    month=1
                d=d+m[month-1]
                month=month+1
            while(y>month):
                d=d+m[month-1]
                month=month+1
            d=d+z
        else:
            if(a==2):   #when the year is the same but the month is in the future
                d=0
                if(lpf(year)==0 and month>2):
                    d=1
                else:
                    if(lpf(year)==0 and month==2 and day==29):
                        d=1
                d=d+day
                month=month-1
                while (month>y):
                    d=d+m[month-1]
                    month=month-1
                d=d+(m[y-1]-z)
                if (lpf(year)==0 and y==2 and day==29):
                    d=d+1
            else:
                if(a==3):   #when the year is the same but the month is in the past
                    d=0
                    if(lpf(year)==0 and y>2):
                        d=1
                    else:
                        if(lpf(year)==0 and y==2 and y==29):
                            d=1
                    d=m[month-1]-day
                    month=month+1
                    while(month<y):
                        d=d+m[month-1]
                        month=month+1
                    d=d+z
                    if (lpf(year)==0 and month==2 and month==29):
                        d=d-1
                else:
                    if(a==4):   #when the year and month are the same but the day is in the future
                        d=0
                        d=d+(day-z)
                    else:
                        if(a==5):   #when the year and month are the same but the day is in the past
                            d=0
                            d=d+(z-day)
                        else:
                            return " the same date"    #when its the same date
    return d

        
uwu=10
while(uwu>0):   #to run the code a number of times based on user's choice
    owu=list(map(int,input("Enter date in 'yyyy-mm-dd' manner: ").split("-")))
    year=owu[0]
    month=owu[1]
    day=owu[2]
    now= datetime.datetime.now() # now contains current date
    x= now.year
    y=now.month
    z=now.day
    t=getdate(x, y, z)
    g=getdate(year, month, day)
    s=pp(year, month, day)

    print("Today's date is: ", t,", the given date is: ", g )
    print("and the number of days between the following days is: ", dc(year, month, day))

    www=input("Do want to know the day of the date you mentioned? Type Yes or No: ")   #to obtain the day name on date
    if(www=="Yes" or www=="yes" or www=="YES"):
        if(s==0 or s==2 or s==4): 
            print("The day on ", g, " is a ", datetime.date(year, month, day).strftime("%A"), ".")
        else:
            if(s==1 or s==3 or s==5):
                print("The day on ", g, " was a ", datetime.date(year, month, day).strftime("%A"), ".")
            else:
                print("Today is a ", datetime.date(year, month, day).strftime("%A"), ".")
    else:
        if(www=="No" or www=="no" or www=="NO"):
            print("Okay!")
        else:
            print("Invalid Input!")

    owo=input("Would yo like to continue? Type Yes or No: ")   #to continue to run the code or not
    if(owo=="Yes" or owo=="yes" or owo=="YES"):
        uwu=uwu-1
        if(uwu==0):
            print("Sorry the code only runs 10 times at once... Thank you for using this program!")
    else:
        if(owo=="No" or owo=="no" or owo=="NO"):
            print("Thank you for using this program!")
            uwu=0
        else:
            print("Invalid input!")
            uwu=0
