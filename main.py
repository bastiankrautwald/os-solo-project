studyfieldincomeafter = {
    "science": 80000,
    "culture": 40000,
    "sport": 50000,
    "medicine": 140000,
    "engineering": 100000,
    "art": 40000,
    "social science": 40000,
    "economics": 45000,
}

#income share agreement return
targetirr = .06
repaymentTime = 6
incomeShare = .04

def financingAmountCalculation(numberOfTotalSemesters, semester, financialNeed):
    differenzsemester = int(numberOfTotalSemesters) - int(semester)
    numfinancingsemester = differenzsemester * 6
    financingamount = numfinancingsemester * int(financialNeed)
    return financingamount

def averageRepayment(studyField):
    totalRepayment = studyfieldincomeafter[studyField] * incomeShare * repaymentTime
    return totalRepayment