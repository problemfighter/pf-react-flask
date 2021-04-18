from flask import Blueprint
from pfms.swagger.pfms_swagger_decorator import pfms_post_request
from simple_auth.dto.authentication_dto import LoginResponseDto, LoginDto
from simple_auth.service.authentication_service import AuthenticationService


auth_controller = Blueprint("auth_controller", __name__, url_prefix="/api/v1/authentication")
auth_service = AuthenticationService()


@auth_controller.route("/login", methods=["POST"])
@pfms_post_request(request_body=LoginDto, response_obj=LoginResponseDto)
def login():
    return auth_service.login()
