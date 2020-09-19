from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField


class Formulario(Form):
    usuario = StringField("usuario")
    correo = EmailField("mail")
    comentario = TextField("texto")