from app import db, app
from datetime import datetime, timedelta


class ImpressionsByUser(db.Model):
    __tablename__ = "impressions_by_user"

    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(), nullable=False)
    impressions = db.Column(db.Integer(), nullable=False)

    def __init__(self, user_name):
        self.user_name = user_name
        self.impressions = 1

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            return e


def findUser(user_name):
    return ImpressionsByUser.query.filter_by(user_name=user_name).first()


def updateUserImpressions(user_name):
    row = ImpressionsByUser.query.filter_by(user_name=user_name).first()
    row.impressions = row.impressions + 1
    db.session.commit()
