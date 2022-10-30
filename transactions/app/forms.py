from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators, ValidationError


class TransactionsForm(FlaskForm):
    value = IntegerField(label='Сумма транзакций', validators=[validators.DataRequired()])
    status = StringField(label='Статус', validators=[validators.DataRequired()])
    unit = StringField(label='валюта', validators=[validators.DataRequired()])
    comment = StringField(label='комментарии (не обязательно)')
    submit = SubmitField(label='Совершить транзакцию')

    def validate_value(self, value):
        if value.data <= 0:
            raise ValidationError('значение не может быть меньше или равно 0')
