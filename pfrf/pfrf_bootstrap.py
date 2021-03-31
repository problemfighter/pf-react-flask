import os

from pfms.common.pfms_exception import PfMsException
from pfms.flask_pf_marshmallow_swagger import PFMarshmallowSwagger

from pfrf.pfrf_app_config import PFRFAppConfigInterface
from pfrf.pfrf_utils import import_from_string

env = os.environ.get('env')


class Bootstrap:

    def _get_app_environment(self):
        if env:
            return env
        return "local"

    def _get_app_config(self) -> PFRFAppConfigInterface:
        app_config = import_from_string("application.app_config.AppConfig", True)
        if app_config:
            if not issubclass(app_config, PFRFAppConfigInterface):
                raise PfMsException("AppConfig Should be Implementation of PFRFAppConfigInterface")
            return app_config()
        return PFRFAppConfigInterface()

    def _register_environment(self, flask_app, app_config: PFRFAppConfigInterface):
        environment = app_config.register_env_config(self._get_app_environment())
        environment_class = "pfrf.pfrf_base_env_config.PFRFBaseEnvConfiguration"
        if environment and isinstance(environment, str):
            environment_class = environment
        flask_app.config.from_object(environment_class)

    def _app_bismillah(self, flask_app):
        app_config = self._get_app_config()
        self._register_environment(flask_app, app_config)
        app_config.register_controller(flask_app)
        with flask_app.app_context():
            app_config.register_model(flask_app)

    def _init_pf_marshmallow_swagger(self, flask_app):
        PFMarshmallowSwagger(flask_app)

    def load_app(self, flask_app):
        self._app_bismillah(flask_app)
        self._init_pf_marshmallow_swagger(flask_app)
