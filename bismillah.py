import os

from flask import Flask, render_template
from flask_cors import CORS
from pf_sqlalchemy.db.orm import database
from pfms.flask_pf_marshmallow_swagger import PFMarshmallowSwagger


env = os.environ.get('env')
app = Flask(__name__)

if env and str(env) == 'prod':
    app.config.from_object('config.prod_config.ProdConfiguration')
else:
    app.config.from_object('config.dev_config.DevConfiguration')


database.init_app(app)

with app.app_context():
    pass

pfms_ins = PFMarshmallowSwagger(app)


CORS(app, resources={r"/api/*": {"origins": "*", "Access-Control-Allow-Origin": "*"}})


@app.route('/')
def bismiallah():
    return render_template('bismillah.html')


if __name__ == '__main__':
    app.run()
