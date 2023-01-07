import os
import datetime

from application import appy, db
from application.pdfs import myPdfs
from application.forms import ResultFilter, RegistrationForm, LoginForm, backTestingForm, agentInfo, riskProfile
from application.plotting import MYAPPENDPLOTING,MYMONTHTRACKER
from application.identities.formData import formData
from application.user_model import user,load_user
from flask_login import login_user,login_required,logout_user,LoginManager
from flask import render_template, session, url_for, redirect, request, Flask,flash
from application.all_financial_assets import allFinancialAssets, FinancialAssetscomparison,backtestSearcher
from application.backTestingCalc import compCalculation

# אפליקציה #
@appy.route('/', methods=["GET", "POST"])
def index():
    Polytop_What = "10"
    kupotData = ""
    form = ResultFilter()
    data = formData()
    results = allFinancialAssets(data)
    max_menayot=1
    max_matach=1
    min_menayot=0
    min_matach=0

    excelLimitor=10
    User=None
    try:
        if session["User"] is not None:
            User = user.query.filter_by(email=session["User"]).first()
            excelLimitor=1000000
    except:
        session["User"]=None

    if form.validate_on_submit():
        reloder=0
        # print(form.expr_sel.data)

        data.set(form)
        results = allFinancialAssets(data)
        trimdList=[x for x in form.id_list.data.split(",") if x != ""]
        kupotData = FinancialAssetscomparison(trimdList)

    else:
        reloder=1
        print(form.errors)

    return render_template('gemelTeck.html', form=form, results=results, Polytop_What=data.Polytop_What, kupotData=kupotData,
    max_menayot=data.AdChassifaMenayot, max_matach=data.AdChassifaMatach, min_menayot=data.MiChassifaMenayot,
     min_matach=data.MiChassifaMatach,User=User,excelLimitor=excelLimitor,reloder=reloder)

@appy.route('/kupotComp', methods=["GET"])
def comparison():
    User=None
    try:
        if session["User"] is not None:
            User = user.query.filter_by(email=session["User"]).first()
            excelLimitor=1000000
    except:
        session["User"]=None
    myData={}
    myData["myList"] = request.args.get("idList")
    myData["type"] = request.args.get("kupaType")
    myData["date"] = datetime.datetime.now().strftime("%d/%m/%Y")
    myData["menayot"] = request.args.get("maxMenayot")
    myData["matach"] = request.args.get("maxMatach")
    myData["search"] = request.args.get("searchWord")

    trimdList=[x for x in myData["myList"].split(",") if x != ""]

    kupotData = FinancialAssetscomparison(trimdList)
    dictOfSugim = {"1":"ביטוח","2":"קופות גמל","3":"קרנות פנסיה","8":"קרנות השתלמות"}
    kupaType = dictOfSugim[str(myData['type'])]

    kupotNameList = []
    for i in kupotData:
        kupotNameList.append(i.shemKupa)

    myDates = MYMONTHTRACKER(kupotData[0].AD_TKUFAT_DIVUACH)

    selectedkupot = kupotData

    kupotHeaderIndex = []
    myIndex = 0
    for index in kupotData:
        myIndex+=1
        kupotHeaderIndex.append(myIndex)

    return render_template('kupotComp.html', trimdList=trimdList, kupotData=kupotData, myData=myData,
     kupaType=kupaType,kupotNameList=kupotNameList,myDates=myDates,selectedkupot=selectedkupot,
     kupotHeaderIndex=kupotHeaderIndex,User=User)

@appy.route('/printPDF', methods=["GET"])
def printPDF():
    User=None
    try:
        if session["User"] is not None:
            User = user.query.filter_by(email=session["User"]).first()
            excelLimitor=1000000
    except:
        session["User"]=None
    myData={}
    myData["myList"] = request.args.get("idList")
    myData["type"] = request.args.get("kupaType")
    myData["date"] = datetime.datetime.now().strftime("%d/%m/%Y")
    myData["menayot"] = request.args.get("maxMenayot")
    myData["matach"] = request.args.get("maxMatach")
    myData["search"] = request.args.get("searchWord")

    trimdList=[x for x in myData["myList"].split(",") if x != ""]

    kupotData = FinancialAssetscomparison(trimdList)
    dictOfSugim = {"1":"ביטוח","2":"קופות גמל","3":"קרנות פנסיה","8":"קרנות השתלמות"}
    kupaType = dictOfSugim[str(myData['type'])]

    kupotNameList = []
    for i in kupotData:
        kupotNameList.append(i.shemKupa)

    myDates = MYMONTHTRACKER(kupotData[0].AD_TKUFAT_DIVUACH)

    selectedkupot = kupotData

    kupotHeaderIndex = []
    myIndex = 0
    for index in kupotData:
        myIndex+=1
        kupotHeaderIndex.append(myIndex)

    return render_template('printPDF.html', trimdList=trimdList, kupotData=kupotData, myData=myData,
     kupaType=kupaType,kupotNameList=kupotNameList,myDates=myDates,selectedkupot=selectedkupot,
     kupotHeaderIndex=kupotHeaderIndex,User=User,myPdfs=myPdfs)

@appy.route('/logout')
@login_required
def logout():
    logout_user()
    flash("התנתקת בהצלחה")
    session["User"]=None
    return redirect(url_for("index"))

@appy.route("/login",methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        User = user.query.filter_by(email=form.email.data).first()
        if  User is not None and User.check_password(form.password.data):

            login_user(User)
            session["User"]=User.email
            flash('התחברת בהצלחה')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                return redirect(url_for("index"))
            return redirect(url_for(next))
        else:
            flash("שם המשתמש או הסיסמא אינם נכונים")

    return render_template("logIn.html",form=form)


@appy.route("/register",methods=['GET',"POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        User = user(Email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        if form.check_email(form.email)=="email":
            flash("אימייל זה נמצא כבר בשימוש")
            return redirect(url_for('register'))

        if form.check_email(form.email)=="length":
            flash("אימייל זה ארוך מדי")
            return redirect(url_for('register'))

        if form.check_username(form.username):
            flash("שם משתמש זה כבר נמצא בשימוש")
            return redirect(url_for('register'))

        db.session.add(User)
        db.session.commit()
        flash("משתמש נרשם בהצלחה")
        login_user(User)
        return redirect(url_for('index'))
    else:
        for error in form.errors:
            flash(form.errors[error][0])
    return render_template('register.html',form=form)

@appy.route("/Backtest",methods=['GET',"POST"])
def Backtest():
    sugKupa=1
    menahelKupa="איילון"
    def mystring(char):
        return str(char)

    form=backTestingForm()
    User=None
    try:
        if session["User"] is not None:
            User = user.query.filter_by(email=session["User"]).first()
    except:
        session["User"]=None

    myResults={}
    myResults["myRow0"]=[(x[0],x[1]) for x in list(backtestSearcher(form.backKupaType0.data,form.backKupaManufacturers0.data))]
    myResults["testingRow0"]=[(x[0],x[1]) for x in list(backtestSearcher(form.frontKupaType0.data,form.frontKupaManufacturers0.data))]
    
    myResults["myRow1"]=[(x[0],x[1]) for x in list(backtestSearcher(form.backKupaType1.data,form.backKupaManufacturers1.data))]
    myResults["testingRow1"]=[(x[0],x[1]) for x in list(backtestSearcher(form.frontKupaType1.data,form.frontKupaManufacturers1.data))]

    myResults["myRow2"]=[(x[0],x[1]) for x in list(backtestSearcher(form.backKupaType2.data,form.backKupaManufacturers2.data))]
    myResults["testingRow2"]=[(x[0],x[1]) for x in list(backtestSearcher(form.frontKupaType2.data,form.frontKupaManufacturers2.data))]

    myResults["myRow3"]=[(x[0],x[1]) for x in list(backtestSearcher(form.backKupaType3.data,form.backKupaManufacturers3.data))]
    myResults["testingRow3"]=[(x[0],x[1]) for x in list(backtestSearcher(form.frontKupaType3.data,form.frontKupaManufacturers3.data))]

    myResults["myRow4"]=[(x[0],x[1]) for x in list(backtestSearcher(form.backKupaType4.data,form.backKupaManufacturers4.data))]
    myResults["testingRow4"]=[(x[0],x[1]) for x in list(backtestSearcher(form.frontKupaType4.data,form.frontKupaManufacturers4.data))]

    if form.validate_on_submit:
        reloder=0
        selectedResults={}
        selectedResults["0"]=form.backKupaName0.data
        selectedResults["1"]=form.frontKupaName0.data

        selectedResults["2"]=form.backKupaName1.data
        selectedResults["3"]=form.frontKupaName1.data

        selectedResults["4"]=form.backKupaName2.data
        selectedResults["5"]=form.frontKupaName2.data

        selectedResults["6"]=form.backKupaName3.data
        selectedResults["7"]=form.frontKupaName3.data

        selectedResults["8"]=form.backKupaName4.data
        selectedResults["9"]=form.frontKupaName4.data

        compResults={}
        compResults["0"]=int(compCalculation(int(form.backKupaName0.data),int(form.frontKupaName0.data),form.testStartDate0.data,form.initialInput0.data,form.repeatingInput0.data))
    else:
        reloder=1
    return render_template('Backtesting.html', form=form, User=User,mystring=mystring,backtestSearcher=backtestSearcher,sugKupa=sugKupa,menahelKupa=menahelKupa,
    myResults=myResults,selectedResults=selectedResults,reloder=reloder,compResults=compResults)

@appy.route("/myProfile",methods=['GET',"POST"])
def myProfile():
    form=riskProfile()
    try:
        if session["User"] is not None:
            User = user.query.filter_by(email=session["User"]).first()
    except:
        session["User"]=None

    if form.validate_on_submit:
         if form.submit.data:
            User.riskeProfile = form.riskProfile.data
            db.session.add(User)
            db.session.commit()

    return render_template('myProfile.html',User=User,form=form)

@appy.route("/calculators",methods=['GET',"POST"])
def calculators():
   return render_template('calculators.html')

@appy.route("/optimizer",methods=['GET',"POST"])
def optimizer():
   return render_template('optimizer.html')

@appy.route("/dictionary",methods=['GET',"POST"])
def dictionary():
   return render_template('dictionary.html')

@appy.route("/agentRedirect",methods=['GET',"POST"])
def agentRedirect():
   form =agentInfo()
   return render_template('agentRedirect.html',form=form)

if __name__ == '__main__':
    appy.run(debug=True, host='0.0.0.0', port=80)