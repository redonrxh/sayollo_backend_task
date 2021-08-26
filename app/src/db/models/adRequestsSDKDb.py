from app import db, app
from datetime import datetime, timedelta


class AdRequestsBySDK(db.Model):
    __tablename__ = "ad_requests_by_sdk"

    id = db.Column(db.Integer(), primary_key=True)
    sdk_version = db.Column(db.String(), nullable=False)
    ad_requests = db.Column(db.Integer(), nullable=False)

    def __init__(self, sdk_version):
        self.sdk_version = sdk_version
        self.ad_requests = 1

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            return e


def findSDK(sdk_version):
    return AdRequestsBySDK.query.filter_by(sdk_version=sdk_version).first()


def updateSDKAdRequests(sdk_version):
    row = AdRequestsBySDK.query.filter_by(sdk_version=sdk_version).first()
    row.ad_requests = row.ad_requests + 1
    db.session.commit()
