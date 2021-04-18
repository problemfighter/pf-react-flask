from marshmallow import fields, Schema
from pfms.pfapi.base.pfms_base_schema import PfBaseSchema


class LoginDto(PfBaseSchema):
    identifier = fields.String(required=True, error_messages={"required": "Please enter identifier."})
    password = fields.String(required=True, error_messages={"required": "Please enter password."})


class Login(Schema):
    accessToken = fields.String()
    refreshToken = fields.String()


class User(Schema):
    firstName = fields.String()
    lastName = fields.String()
    id = fields.Integer()


class Navigation(Schema):
    icon = fields.String()
    name = fields.String()
    url = fields.String()
    displayName = fields.String()
    groupDisplayName = fields.String()
    groupName = fields.String()
    groupUrl = fields.String()


class LoginResponseDto(PfBaseSchema):
    login = fields.Nested(Login)
    user = fields.Nested(User)
    navList = fields.Nested(Navigation, many=True)
