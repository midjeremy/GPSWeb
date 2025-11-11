from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Correo o RUT',
        widget=forms.TextInput(attrs={
            'id': 'username',   # 👈 Aquí va el id que usas en tu CSS
            'placeholder': 'Correo o RUT'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'placeholder': 'Contraseña'
        })
    )
