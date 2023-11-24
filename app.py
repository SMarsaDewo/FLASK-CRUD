from flask_migrate import Migrate

migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

import resources.user

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
