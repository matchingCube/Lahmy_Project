import datetime

def MYAPPENDPLOTING(data,kupa1,kupa2,kupa3,kupa4):
    x=0
    for i in data:
        print(i)
        if x==0:
            kupa1.append(i)
            x+=1
        elif x==1:
            kupa2.append(i)
            x+=1
        elif x==2:
            kupa3.append(i)
            x+=1
        elif x==3:
            kupa4.append(i)
            x+=1

def MYMONTHTRACKER(latestdata):
    x = latestdata
    monthList=[]
    for i in range(-11,1):
        m=x.month+i
        y=x.year
        if m<1:
            m=m+12
            y-=1
        tempDate=datetime.datetime(y,m,1)
        tarichim={"01":"ינואר","02":"פברואר","03":"מרץ","04":"אפריל","05":"מאי","06":"יוני","07":"יולי","08":"אוגוסט","09":"ספטמבר","10":"אוקטובר","11":"נובמבר","12":"דצמבר"}
        monthList.append(tempDate.strftime("%Y")+"-"+tarichim[tempDate.strftime("%m")])

    return monthList
