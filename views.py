from main import app
from flask import render_template, request, jsonify
from models import addLog, getLogs

global new_logs
new_logs = []
@app.route('/')
def index():
    #labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    #values = [100, 90, 80, 70, 60, 40, 70, 80]
    #return render_template('index.html', values=values, labels=labels)
    return render_template('getLog.html')
@app.route('/postLog', methods = ['GET', 'POST'])
def postLog():
    if request.method == 'POST':


        id = request.form['id']
        success = request.form['success']
        log = addLog(id, success)
        new_logs.append(str(log.success) + ',' + str(log.id).strip('\r') + ',' + str(log.time))
        print len(new_logs)

        return 'success'
    elif request.method == 'GET':
        return render_template('addLog.html')


@app.route('/getLog', methods = ['GET', 'POST'])
def getLog():
    if request.method == 'GET':
        logs = getLogs()
        logs_list = [str(log.success) + ',' + str(log.id).strip('\r') + ',' + str(log.time) for log in logs]
        return jsonify(logs_list)

@app.route('/getNewLogs', methods = ['GET', 'POST'])
def get_new():
    if request.method == 'GET':
        logs = list(new_logs)
        del new_logs[:]
        return jsonify(logs)

@app.route('/data')
def data():
    return jsonify({'results':range(10)})


