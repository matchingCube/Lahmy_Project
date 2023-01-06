import pyodbc

def getCon():
    server_name = "localhost" 
    database_name = "gemel_tech_db"

    return pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                          f'Server={server_name};'
                          f'Database={database_name};'
                          'Trusted_Connection=yes;')


def backtestSearcher(Polytop_What=1,Polytop_Yatzran1="איילון"):
    
    cursor = getCon().cursor()

    sql = 'exec [GEM_Backtest] ?,?'
    values = (int(Polytop_What),str(Polytop_Yatzran1))

    cursor.execute(sql, values)

    return cursor

def allFinancialAssets(form):

    cursor = getCon().cursor()

    sql = 'exec [test] ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?'
    values = form.getValues()

    cursor.execute(sql, values)

    return cursor


def MYREMOVE(st,r1,r2="",r3=""):
    x = st.replace(r1,"")
    x = x.replace(r2,"")
    x = x.replace(r3,"")
    return x #  מוחק ערכים מטקסט


def FinancialAssetscomparison(Id):

    cursor = getCon().cursor()


    myLen = []
    for i in range(len(Id)):
         myLen.append("?") #  יוצר רשימה שאומרת  לתפקוד  השמור כמה ערכים הוא צריך לקבל

    myStr=str(myLen)
    intermidiant = MYREMOVE(myStr,"[","]","'") # SQL הופך את הרשימה לקריאה ע"י

    sql = 'exec [GEM_Sinun] {}'.format(intermidiant)
    values = (Id)

    cursor.execute(sql, values)

    return cursor.fetchall()

def backtestComparisonData(IdKupa):

    cursor = getCon().cursor()

    
    sql = 'exec [backtestComparisonData] ?'
    
    cursor.execute(sql, IdKupa)

    return cursor
