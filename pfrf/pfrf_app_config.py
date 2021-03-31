
class PFRFAppConfigInterface:

    def register_controller(self, flask_app):
        pass

    def register_model(self, flask_app):
        pass

    def register_env_config(self, env) -> str:
        pass


class PFRFModuleConfigInterface:

    def register_controller(self, flask_app):
        pass

    def register_model(self, flask_app):
        pass

