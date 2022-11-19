from stockfight import db, models


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
