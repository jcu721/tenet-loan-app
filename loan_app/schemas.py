"""
Marshmallow schema definitions.
"""
from marshmallow import Schema, fields, post_load

from loan_app.models import Application, LoanOffer, User


class UserSchema(Schema):
    """
    User Marshmallow Schema.
    """

    id = fields.Integer(allow_none=False)
    first_name = fields.String(allow_none=False)
    last_name = fields.String(allow_none=False)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class ApplicationSchema(Schema):
    """
    Application Marshmallow Schema.
    """

    id = fields.Integer(allow_none=False)
    user_id = fields.Integer(allow_none=False)

    credit_score = fields.Integer()
    bankruptcies = fields.Integer()
    delinquincies = fields.Integer()
    monthly_debt = fields.Number()
    monthly_income = fields.Number()
    vehicle_value = fields.Number()
    loan_amount = fields.Number()

    @post_load
    def make_application(self, data, **kwargs):
        return Application(**data)


class LoanOfferSchema(Schema):
    """
    LoanOffer Marshmallow Schema.
    """

    id = fields.Integer(allow_none=False)
    user_id = fields.Integer(allow_none=False)
    application_id = fields.Integer(allow_none=False)

    apr = fields.Number()
    monthly_payment = fields.Number()
    term_length_months = fields.Integer()

    accepted = fields.Boolean()
    rejection_reason = fields.String()

    @post_load
    def make_loan_offer(self, data, **kwargs):
        return LoanOffer(**data)
