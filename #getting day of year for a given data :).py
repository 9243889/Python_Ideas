#getting day of year for a given data :)
#yyyy-mm-dd
cal=input('DATE(yyyy-mm-dd):')
date=cal.split('-')#split the date

year=int(date[0])
month=int(date[1])
day=int(date[2])

arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
num=0

if((year%4==0)and(year%100!=0)) or (year%400==0):
    arr[2]=29

for i in range(1,len(arr)):
    if month>i:
        num+=arr[i]
    else:
        num+=day
        break
print('DAY OF THIS YEAR:',num)