from decimal import Decimal
from application.all_financial_assets import backtestComparisonData

def ReturnZero(input):
    if input == None:
        return 0
    else:
        return input    

def DATECOMPARISON(kupaNum,formatedDate,KupaData,list = list):
    kupaDidNotExist=True
    for index in KupaData:
        if formatedDate == int(index[1]):
            kupaDidNotExist=False
            break

    if kupaDidNotExist:
        return f"קופה {kupaNum} לא היתה קיימת בתאריך זה"        

    for index in KupaData:
        if formatedDate <= int(index[1]):
            list.append(index[0])

    return list        

def COMPARISONCALCULATION(initalInput=0,monthlyInput=0,list=list):
    for index in list:
        if isinstance(index,str):
            initalInput=float(initalInput)*(1+float(index)/100)+float(monthlyInput)
    return initalInput    


    

def compCalculation(myKupaNum,compKupaNum,startDate,initalInput=0,monthlyInput=0):
    initalInput=ReturnZero(initalInput)
    monthlyInput=ReturnZero(monthlyInput)
    if type(startDate)!=type(None):
        MyKupaData=backtestComparisonData(myKupaNum)
        compKupaData=backtestComparisonData(compKupaNum)
        myYear = str(startDate)[0:4]
        myMonth= str(startDate)[5:7]
        formatedDate=int(myYear+myMonth)
        myKupaReturns=[]
        compKupaReturns=[]
        myKupaReturns.append(DATECOMPARISON(myKupaNum,formatedDate,MyKupaData,myKupaReturns))
        compKupaReturns.append(DATECOMPARISON(compKupaNum,formatedDate,compKupaData,compKupaReturns))
        difference = COMPARISONCALCULATION(initalInput,monthlyInput,compKupaReturns)-COMPARISONCALCULATION(initalInput,monthlyInput,myKupaReturns)
        return difference
    return -9999999999999999999
    