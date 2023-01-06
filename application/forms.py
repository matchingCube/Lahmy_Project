from tkinter import N
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, IntegerRangeField, SearchField, BooleanField, HiddenField, StringField,EmailField,TelField,PasswordField,DateField,DecimalField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError, InputRequired
from application.user_model import user

class riskProfile(FlaskForm):
    riskProfile=SelectField("פרופיל הסיכון שלי",choices=["1.ללא סיכון/סיכוי לתשואה מינימאלי","2.מעט מאוד סיכון/סיכוי לתשואה נמוך מאוד","3.מעט סיכון/סיכוי לתשואה נמוך",
    "4.סיכון בינוני נמוך/סיכוי לתשואה בינוני נמוך","5.סיכון בינוני/סיכוי לתשואה בינוני","6.סיכון בינוני פלוס/סיכוי לתשואה בינוני פלוס",
    "7.סיכון מעט גבוהה/סיכוי לתשואה מעט גבוהה","8.סיכון יחסית גבוהה/סיכוי לתשואה יחסית גבוהה","9.סיכון גבוהה/סיכוי לתשואה גבוהה","10.סיכון מירבי/סיכוי לתשואה מירבי"])

    question1=SelectField("1.איך הייתם מדרגים את נכונותכם לקחת סיכונים",choices=["נכונות נמוכה","נכונות בינונית נמוכה","נכונות בינונית","נכונות בינונית גבוהה","נכונות גבוהה"])
    question2=SelectField("2.האם אי-פעם לוויתם כסף לצורך מינוף בתיק שלכם",choices=["לא","כן"])
    question3=SelectField("3.כאשר אתם חושבים על המילה סיכון בהקשר הפיננסי מהי המילה הראשונה שעולך במחשבתכם",choices=["פחד","חוסר וודאות","הזדמנות","הימור"])
    question4=SelectField("4.השקעות בשוק ההון הינן תנודתיות,מה יגרום לכם לחוש שלא בנוח במידה והשקעתכם תרד כתוצא מתנודתיות בשוק",choices=["כל ירידה","ירידה מעל 10%","ירידה מעל20%",
    "ירידה מעל30%"])
    question5=SelectField("5.מה השינוי שחל  הרמת הסיכון של השקעותייך במהלך השנים האחרונות",choices=["מעבר של כל ההשקעות לסיכון נמוך","מעבר מרבית ההשקעות לסיכון נמוך",
    "ללא שינוי","מעבר מרבית ההשקעות לסיכון גבוהה","מעבר כל ההשקעות לסיכון גבוהה יותר"])
    question6=SelectField("6.איזה שיעור מהכסף שלכם הייתם מוכנים להשקיע בנכסים המניבים תשואה מעל הממוצע ,אך לרוב הינם  גם מסוכנים יותר מהממוצע",choices=["כלום","עד 10%","עד 20%",
    "עד 50%","עד 70%","עד 100%"])
    question7=SelectField("7.איזה משפט מתאר בצורה הטובה ביותר את התיחסותך להשקעות",choices=["ארגיש טוב אם נכסי יושקעו באפיקים סולידים בעלי סיכון נמוך",
    "ארגיש טוב אם רוב נכסי יושקעו באפיקים סולידים וחלק קטעם יושקע באפיקים בעלי סיכון גבוהה יותר",
    "ארגיש טוב עם השקעה מאוזנת בין נכסים מסוכנים יותר  לפמסוכנים פחות ,בידיעה שיתכנו תקופות של תשואות שליליות בתיק",
    "ארגיש טוב אם חלק קטן יחסית מנכסי ההשקעה שלי יושקעו באפיקים סולידים ומרבית הנכסים באפיקים מסוכנים יותר",
    "אני מעדיף השקעה רק במניות המציעות תשואה גבוהה לצד סיכון גבוהה"])

    submit = SubmitField("שמרו בחירת פרופיל", validators=[InputRequired()])

class agentInfo(FlaskForm):
    name = StringField("שם מלא", validators=[DataRequired(message='נא למלא שדה זה')])
    phone = TelField("טלפון", validators=[DataRequired(message='נא למלא שדה זה')])
    email = EmailField('אימייל', validators=[DataRequired(),Email()])
    submit = SubmitField('שלחו')

class LoginForm(FlaskForm):
    email = EmailField('אימייל', validators=[DataRequired(),Email()])
    password= PasswordField("סיסמא", validators=[DataRequired()])
    submit = SubmitField('התחברו')

class RegistrationForm(FlaskForm):
    email = EmailField('אימייל', validators=[DataRequired("test")])
    username = StringField("שם משתמש", validators=[DataRequired(message='נא למלא שדה זה')])
    password= PasswordField("סיסמה", validators=[DataRequired(message='נא למלא שדה זה'), EqualTo("pass_confirm",message='אימות הסיסמא חייב להתאים לסיסמא')])
    pass_confirm= PasswordField("אימות סיסמא", validators=[DataRequired(message='נא למלא שדה זה')])
    submit = SubmitField('הרשמה')

    def check_email(self,field):
        if len(field.data) > 63:
            return "length"
        if user.query.filter_by(email = field.data).first():
            return "email"

    def check_username(self,field):
        if user.query.filter_by(username = field.data).first():
            return True

class ResultFilter(FlaskForm):

                # אזור היצרנים
    all_manufacturers = BooleanField("כל החברות",default=True)

    Yatzran1 = SelectField("יצרן 1", coerce=str, validate_choice=False)

    Yatzran2 = SelectField("יצרן 2", coerce=str, validate_choice=False)

    Yatzran3 = SelectField("יצרן 3", coerce=str, validate_choice=False)

    Yatzran4 = SelectField("יצרן 4", coerce=str, validate_choice=False)

    def __init__(self, *args, **kwargs):
        Yatzranim_options = ["אי.די.אי","איילון","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                    "הלמן-אלדובי","הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה","פסגות"]
        user = kwargs.pop('user', None)
        super(ResultFilter, self).__init__(*args, **kwargs)
        self.Yatzran1.choices = ["בחרו חברה"] + [x for x in Yatzranim_options]
        self.Yatzran2.choices = ["בחרו חברה"] + [x for x in Yatzranim_options]
        self.Yatzran3.choices = ["בחרו חברה"] + [x for x in Yatzranim_options]
        self.Yatzran4.choices = ["בחרו חברה"] + [x for x in Yatzranim_options]

                # אזור סוג קופה
    kupa_type = RadioField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)

                # אזור הסינון
    kupot_gemel = RadioField("קופות גמל", choices=[("תגמולים ואישית לפיצויים","תגמולים ואישית לפיצויים"),
                                                    ("קופת גמל להשקעה - חסכון לילד","קופת גמל-חסכון לילד"),
                                                    ("קופת גמל להשקעה","קופת גמל להשקעה"),
                                                    ("מרכזית לפיצויים","קופה מרכזית לפיצויים"),
                                                    ("מטרה אחרת","מטרה אחרת"),], coerce=str, validate_choice=False,default="תגמולים ואישית לפיצויים")

    saving_policies = RadioField("פוליסות חיסכון", choices=[("מ-2004","פוליסות מ-2004 והילך"),
                                                                ("מ1992 עד 2003","פוליסות מ-1992 עד 2003"),
                                                                ("מ1990 עד 1991","פוליסות מ-1990 עד 1991")], coerce=str, validate_choice=False,default="מ-2004")

    pension_funds = RadioField("קרנות פנסיה", choices=[("קרנות חדשות","קרנות חדשות"),
                                                                ("קרנות כלליות","קרנות כלליות")], coerce=str, validate_choice=False,default="קרנות חדשות")

    pension_receivers = BooleanField("כולל מקבלי קצבה")
    market_average = BooleanField("כולל ממוצע שוק")

    Submit = SubmitField('חפש')
    # Submit2 = SubmitField('השוואת קופות')

                # אזור התמחויות
    expr_sel = RadioField("מיון תוצאות לפי", choices=[("ללא", "כל ההתמחויות"),  #עובד
                                                            ("אגח", 'אג"חים'),  # עובד
                                                            ("מניות", "מניות"),
                                                            ("הלכה","הלכה"),
                                                            ("חול","חול"),
                                                            ("כללי","כללי"),
                                                            ("מדרגות","בני 50-60"),
                                                            ("פנסיונר","פנסיונרים"),
                                                            ("שיקלי","שיקלי"),
                                                            ("IRA","IRA")], validate_choice=False,default="ללא")  # עובד

                # אזור מילת חיפוש
    search = SearchField()  # עובד
    stock_lim = IntegerRangeField("מגבלת מניות")
    hidden_menayot_max = HiddenField()
    hidden_menayot_min = HiddenField()

    forex_lim = IntegerRangeField('מגבלת מט"ח')
    hidden_forex_max = HiddenField()
    hidden_forex_min = HiddenField()

    risk_level_lim = IntegerRangeField("מגבלת דרגות סיכון")
    hidden_risk_level_max = HiddenField()
    hidden_risk_level_min = HiddenField()

                # אזור מיון
    filter = RadioField("מיון תוצאות לפי", choices=[(1, "תשואות שנה אחורה"),
                                                    (2, "תשואות 3 שנים אחורה"),
                                                    (3, "תשואות 1 ו-3 שנים "),
                                                    (4, "שארפ")], validate_choice=False,default=1)  # עובד
                                                    # ,(5, "דירוג סיכון")
                    # אזור קופות שנבחרו לצורך ההשוואה
    id_list = StringField()

class backTestingForm(FlaskForm):        
    backKupaType0=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    backKupaType1=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    backKupaType2=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    backKupaType3=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    backKupaType4=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)

    frontKupaType0=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    frontKupaType1=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    frontKupaType2=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    frontKupaType3=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)
    frontKupaType4=SelectField("סוג קופה", choices=[(1,"ביטוח"),(3,"קרנות פנסיה"),(8,"קרנות השתלמות"),(2,"קופות גמל")],default=1)

    backKupaManufacturers0=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    backKupaManufacturers1=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    backKupaManufacturers2=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    backKupaManufacturers3=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    backKupaManufacturers4=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])

    frontKupaManufacturers0=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    frontKupaManufacturers1=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    frontKupaManufacturers2=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    frontKupaManufacturers3=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])
    frontKupaManufacturers4=SelectField("מנהל קופה",choices=["איילון","אי.די.אי","אינפיניטי","אלטשולר שחם","אנליסט","הכשרה",
                                                "הפניקס","הראל","כלל","מגדל","מור","מיטב דש","מנורה"])

    backKupaName0=SelectField("שם הקופה (מספר הקופה)")
    backKupaName1=SelectField("שם הקופה")
    backKupaName2=SelectField("שם הקופה")
    backKupaName3=SelectField("שם הקופה")
    backKupaName4=SelectField("שם הקופה")

    frontKupaName0=SelectField("שם הקופה")
    frontKupaName1=SelectField("שם הקופה")
    frontKupaName2=SelectField("שם הקופה")
    frontKupaName3=SelectField("שם הקופה")
    frontKupaName4=SelectField("שם הקופה")

    testStartDate0=DateField("תאריך הפקדה ראשוני", format='%Y-%m-%d')
    testStartDate1=DateField("תאריך הפקדה ראשוני", format='%Y-%m-%d')
    testStartDate2=DateField("תאריך הפקדה ראשוני", format='%Y-%m-%d')
    testStartDate3=DateField("תאריך הפקדה ראשוני", format='%Y-%m-%d')
    testStartDate4=DateField("תאריך הפקדה ראשוני", format='%Y-%m-%d')

    initialInput0=DecimalField("הפקדה ראשונית לקופה")
    initialInput1=DecimalField("הפקדה ראשונית לקופה")
    initialInput2=DecimalField("הפקדה ראשונית לקופה")
    initialInput3=DecimalField("הפקדה ראשונית לקופה")
    initialInput4=DecimalField("הפקדה ראשונית לקופה")

    repeatingInput0=DecimalField("הפקדות חודשיות")
    repeatingInput1=DecimalField("הפקדות חודשיות")
    repeatingInput2=DecimalField("הפקדות חודשיות")
    repeatingInput3=DecimalField("הפקדות חודשיות")
    repeatingInput4=DecimalField("הפקדות חודשיות")

    difference0=DecimalField("הפרש")
    difference1=DecimalField("הפרש")
    difference2=DecimalField("הפרש")
    difference3=DecimalField("הפרש")
    difference4=DecimalField("הפרש")

    submit = SubmitField("חפשו")