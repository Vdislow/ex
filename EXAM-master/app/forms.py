from flask_wtf import FlaskForm
from wtforms import validators
import wtforms as wf





class EmployeeForm (FlaskForm):
    fullname = wf.StringField('ФИО', validators=[wf.validators.DataRequired()])
    phone = wf.StringField('Телефон', validators=[wf.validators.DataRequired()])
    short_info = wf.TextAreaField('Краткая информация', validators=[wf.validators.DataRequired()])
    experience = wf.StringField('Опыт', validators=[wf.validators.DataRequired()])
    preferred_position = wf.StringField('Предполагаемая позиция')
    submit = wf.SubmitField('Ok')

    def validate(self):
        if not super().validate():
            return False
        if " " not in self.fullname.data:
            self.fullname.errors.append("ФИО нужно писать раздельно")
            return False
        return True


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')



    def validate_password(self, field):
        if len(field.data) < 8:
            raise validators.ValidationError('Password не должен быть короче 8 символов')