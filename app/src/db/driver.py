import time


def init_db(db):
    import app.src.db.models.adRequestsSDKDb
    import app.src.db.models.adRequestsUserDb
    import app.src.db.models.impressionsSDKDb
    import app.src.db.models.impressionsUserDb

    dbRetries = 0

    while dbRetries != 14:
        try:
            # db.drop_all()
            db.create_all()
            break
        except:
            print("Couldn\'t connect to the database, retry in 5 sec")
            time.sleep(5)
            dbRetries += 1
