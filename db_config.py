from flask_sqlalchemy import SQLAlchemy


def sql(app, mydb = ' '):
    app.config['SQLALCHEMY_DATABASE_URI'] = mydb
    db = SQLAlchemy(app)

    return db
