from django import forms

class MetodoPagoForm(forms.Form):
    METODOS_PAGO = [
        ('transferencia', 'Transferencia bancaria'),
        # Mas metodos de pago pueden ser añadidos aquí
    ]
    metodo = forms.ChoiceField(choices=METODOS_PAGO, label="Método de pago", widget=forms.RadioSelect)
