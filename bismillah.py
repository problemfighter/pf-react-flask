import os

from flask import Flask
from flask_cors import CORS
from pf_sqlalchemy.db.orm import database
from pfms.flask_pf_marshmallow_swagger import PFMarshmallowSwagger
from pfms.swagger.pfms_swagger_decorator import simple_get
from sso.sso_registry import SSORegistry
from region.module_registry import regionRegistry
from supplier.module_registry import supplierRegistry


env = os.environ.get('env')
app = Flask(__name__)

if env and str(env) == 'prod':
    app.config.from_object('config.prod_config.ProdConfiguration')
else:
    app.config.from_object('config.dev_config.DevConfiguration')


database.init_app(app)
sso_registry = SSORegistry()

with app.app_context():
    regionRegistry.register_model()
    supplierRegistry.register_model()

pfms_ins = PFMarshmallowSwagger(app)
app.register_blueprint(user_blueprint)

sso_registry.register_controller(app)
supplierRegistry.register_controller(app)

CORS(app, resources={r"/api/*": {"origins": "*", "Access-Control-Allow-Origin": "*"}})


@app.route('/')
@simple_get(response_obj=None)
def bismiallah():
    return 'Bismillah'


if __name__ == '__main__':
    app.run()
