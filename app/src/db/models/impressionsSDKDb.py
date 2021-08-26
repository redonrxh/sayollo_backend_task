from app import db, app
from datetime import datetime, timedelta


class ImpressionsBySDK(db.Model):
    __tablename__ = "impressions_by_sdk"

    id = db.Column(db.Integer(), primary_key=True)
    sdk_version = db.Column(db.String(), nullable=False)
    impressions = db.Column(db.Integer(), nullable=False)

    def __init__(self, sdk_version):
        self.sdk_version = sdk_version
        self.impressions = 1

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            return e


def findSDK(sdk_version):
    return ImpressionsBySDK.query.filter_by(sdk_version=sdk_version).first()


def updateSDKImpressions(sdk_version):
    row = ImpressionsBySDK.query.filter_by(sdk_version=sdk_version).first()
    row.impressions = row.impressions + 1
    db.session.commit()
