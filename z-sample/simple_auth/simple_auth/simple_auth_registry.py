from simple_auth.controller.authentication_controller import auth_controller


class CodeGenTestRegistry:

    def register_model(self, flask_app):
        pass

    def register_controller(self, flask_app):
        flask_app.register_blueprint(auth_controller)


code_gen_test_registry = CodeGenTestRegistry()
