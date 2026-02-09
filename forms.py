from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField, SelectField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese nombre valido")
    ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField("Amaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])

class CinepolisForm(Form):
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido")
    ])
    compradores=IntegerField('Compradores',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingresa al menos 1")
    ])
    boletos = IntegerField("Boletos", [
        validators.DataRequired(), 
        validators.NumberRange(min=1)])
    tarjeta=SelectField("Paga con tarjeta CINECO?",
                        choices=[("no"),("si")],
                        default="no"
                        )