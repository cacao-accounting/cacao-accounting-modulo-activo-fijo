from cacao_accounting import create_app
from cacao_accounting.conf import configuracion

app = create_app(configuracion)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost:3306/cacaodb"


def test_mysql():
    with app.app_context():
        from cacao_accounting.database import db
        from cacao_accounting_modulo_activofijo import db as afdb

        db.create_all()
        afdb.create_all()
