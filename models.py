from main import db
from datetime import datetime

class LOGS(db.Model):
    __tablename__ = 'logs'
    uid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(100))
    success = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self, id, success):
        self.id = id
        self.success = success
        self.time = datetime.utcnow()


def addLog(id, success):
    db.create_all()
    log = LOGS(id, success)
    db.session.add(log)
    db.session.commit()
    return log

def getLogs():
    logs = LOGS.query.all()
    return logs
