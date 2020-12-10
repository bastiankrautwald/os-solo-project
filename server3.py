import os
import main as logic

from flask import Flask, request, jsonify

# starting web server
app = Flask(__name__, instance_relative_config=True)

# route
@app.route('/')
@app.route('/index')
def default():
    return "<h1>defaultwebsite</h1>"

@app.route('/postdata', methods=["POST","GET"])
def postdata():
    semester = request.form['semester']
    totalSemester = request.form['totalSemester']
    financialNeed = request.form['financialNeed']
    studyField = request.form['studyField']
    calculationFinancingAmount = logic.financingAmountCalculation(totalSemester,semester,financialNeed)
    calculationRepayment = logic.averageRepayment(studyField)
    return jsonify({"Financing Amount":calculationFinancingAmount,"Repayment":calculationRepayment})

if __name__ == '__main__':
    app.run()