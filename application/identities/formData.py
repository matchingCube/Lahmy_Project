class formData:
    def __init__(self):
        self.Polytop_What=0
        self.Polytop_WhatTatKupaBit=1
        self.Polytop_WhatTatKupaKg=1
        self.Polytop_WhatTatKupaKp=1
        self.MilatChipus=""
        self.hitmahut="ללא"
        self.AdChassifaMenayot=100
        self.AdChassifaMatach=100
        self.MiChassifaMenayot=0
        self.MiChassifaMatach=0
        self.Miun=1
        self.YatzranChoice=0
        self.Yatzran1=""
        self.Yatzran2=""
        self.Yatzran3=""
        self.Yatzran4=""

    def set(self, form):

        self.Polytop_What=form.kupa_type.data

        if form.kupa_type.data == {'kupa_type': ['Not a valid choice.']}:
            self.Polytop_What=2

        self.Polytop_WhatTatKupaBit=form.saving_policies.data
        self.Polytop_WhatTatKupaKg=form.kupot_gemel.data
        self.Polytop_WhatTatKupaKp=form.pension_funds.data

        self.Yatzran1 = form.Yatzran1.data
        self.Yatzran2 = form.Yatzran2.data
        self.Yatzran3 = form.Yatzran3.data
        self.Yatzran4 = form.Yatzran4.data
        self.MilatChipus = form.search.data

        self.hitmahut = form.expr_sel.data
        self.AdChassifaMenayot = float(form.hidden_menayot_max.data)/100
        self.AdChassifaMatach = float(form.hidden_forex_max.data)/100
        self.MiChassifaMenayot = float(form.hidden_menayot_min.data)/100
        self.MiChassifaMatach = float(form.hidden_forex_min.data)/100
        self.Miun = form.filter.data

        if form.all_manufacturers.data:
            self.YatzranChoice = 0
        else:
            self.YatzranChoice = 1

    def getValues(self):
        return (self.Polytop_What,
        self.Polytop_WhatTatKupaBit,self.Polytop_WhatTatKupaKg,self.Polytop_WhatTatKupaKp,self.MilatChipus, self.hitmahut, self.AdChassifaMenayot, self.AdChassifaMatach, self.MiChassifaMenayot, self.MiChassifaMatach, self.Miun,
                  self.YatzranChoice, self.Yatzran1, self.Yatzran2, self.Yatzran3, self.Yatzran4)
