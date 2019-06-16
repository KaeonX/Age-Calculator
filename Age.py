print("In the following field, key in the",
	     "current year in which you are running",
	     "this script, in the format <YYYY>.\n")
cy = input("CURRENT YEAR: ")
currentyear = int(cy[-2:])

def convert99(year):
    if year > currentyear: #both years must be in <YY> format.
        year -= 100
    return year


print("\nIn the following field, key in the",
	     "date on which the person's age will be",
	     "calculated, in the format <DDMMYY>.\n")
rd = input("REFERENCE DATE (Age On): ")
if rd=="":
    rd = "0104" + cy
ny = [31, 28, 31, 30, 31, 30,
      31, 31, 30, 31, 30, 31] #normalyear
ly = [31, 29, 31, 30, 31, 30,
      31, 31, 30, 31, 30, 31] #leapyear
ry, rm, rd = int(rd[-2:]), int(rd[2:4]), int(rd[:2]) #referenceyearmonthday
ry = convert99(ry)
if ry%4==0:
    year = ly
else:
    year = ny
    
    
while True:
        
    print("\nIn the following field, key in the",
    	     "person's date of birth, in the format",
             "<DDMMYY>.\n")
    dob = input("DATE OF BIRTH: ")
    by, bm, bd = int(dob[-2:]), int(dob[2:4]), int(dob[:2]) #birthyearmonthday
    by = convert99(by)
        
    if (rd-bd)<0:
        monthoffset = -1
        agedays = year[rm - 2] - bd + rd
    else:
        monthoffset = 0
        agedays = rd - bd
        
    if (rm-bm)<0:
        yearoffset = -1
        agemonths = 12 - bm + rm + monthoffset
    else:
        yearoffset = 0
        agemonths = rm - bm + monthoffset
        
    ageyears = ry - by + yearoffset
        
    print("\nThe person's age is {} years, {} months and {} days.".format(ageyears, agemonths, agedays))
    
    print("\nContinue with next person?\n")
    cont = input("Y/N: ")
    if cont=="N" or cont=="n":
        break
