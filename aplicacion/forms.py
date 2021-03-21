from flask_wtf import FlaskForm
from wtforms import Form, TextField,PasswordField,SubmitField
from wtforms.fields.html5 import DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required , DataRequired

class singupForm(FlaskForm):
    name = TextField("Name", validators=[Required("Debes ingresar tu nombre")])
    username = TextField("Username", validators=[Required("Debes ingresar tu usuario y/o correo")])
    password = PasswordField("Password", validators=[DataRequired("Debes ingresar tu contraseña")])
    submit = SubmitField('SingUp')
    
    
class loginForm(FlaskForm):
    usernameLg = TextField("Username", validators=[Required("Debes ingresar tu usuario y/o correo")])
    passwordLg = PasswordField("Password", validators=[Required("Debes ingresar tu contraseña")])
    submitLg = SubmitField('Login')
    
class regIncomes(FlaskForm):
    dateIncome = DateField("Day",format='%Y-%m-%d',validators=[Required("Proporciona la fecha")])
    descrip = TextField("Description",validators=[Required("Debes ingresar la descripción del Ingreso")])
    amount = DecimalField("Amount",validators=[Required("Debes ingresar la cantidad de dinero ganada")])
    submitRg = SubmitField('Save')
    
class regExpenses(FlaskForm):
    dateEx = DateField("Day",format='%Y-%m-%d',validators=[Required("Proporciona la fecha")])
    descripEx = TextField("Description",validators=[Required("Debes ingresar la descripción del gasto")])
    amountEx = DecimalField("Amount",validators=[Required("Debes ingresar la cantidad de dinero gastada")])
    submitRgEx = SubmitField('Save')
    
class verFechas(FlaskForm):
    dateNow = DateField("Day",format='%Y-%m-%d')
    seeButton = SubmitField('See')