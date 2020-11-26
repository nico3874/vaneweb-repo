from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
#Los widget extienden la configuración y le podemos poner los atributos del frontend original
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    #Aquí hay una diferencia con los modelos ya que para texto largo utlizamos charfield en lugar textfield
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':5, 'placeholder':'Escribe tu mensaje'}
        ), min_length=10, max_length=1000)