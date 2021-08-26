from app import db, app
from datetime import datetime, timedelta


class AdRequestsByUser(db.Model):
    __tablename__ = "ad_requests_by_user"

    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(), nullable=False)
    ad_requests = db.Column(db.Integer(), nullable=False)

    def __init__(self, user_name):
        self.user_name = user_name
        self.ad_requests = 1

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            return


def findUser(user_name):
    return AdRequestsByUser.query.filter_by(user_name=user_name).first()


def updateUserAdRequests(user_name):
    row = AdRequestsByUser.query.filter_by(user_name=user_name).first()
    row.ad_requests = row.ad_requests + 1
    db.session.commit()
