from django import forms
import random
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from thessia.models import PruebaTres



class PalabraForm(forms.Form):
    """
    Clase para crear el formulario de palabras
    """

    # Creamos los campos de tipo texto cuyo requisito es que sea rellenado. En caso de no hacerlo, se muestra un mensaje de error
    palabra1 = forms.CharField(required=True)
    palabra2 = forms.CharField(required=True)
    palabra3 = forms.CharField(required=True)
    palabra4 = forms.CharField(required=True)
    palabra5 = forms.CharField(required=True)

    def clean(self):
        """
        Metodo que se encarga de realizar la validación de los elementos del formulario
        :return:
        """

        # Almacenamos en una variable el contenido de lo que introduce el usuario y lo que se envía en la petición POST
        cleaned_data = super().clean()  # ensures that any validation logic in parent classes is maintained

        # Almacenamos en una variable de tipo queryset el resultado de la consulta que recoge los primeros 5 conceptos
        cinco_registros = PruebaUno.objects.all()[:5]

        # Almacenamos en una variable lo que introduce el usuario en las casillas de texto para
        concept1 = self.cleaned_data.get("palabra1")
        concept2 = self.cleaned_data.get("palabra2")
        concept3 = self.cleaned_data.get("palabra3")
        concept4 = self.cleaned_data.get("palabra4")
        concept5 = self.cleaned_data.get("palabra5")

        # Creamos la condición que debe cumplirse para que el formulario sea validad correctamente
        if concept1 != "Transgenero" or concept2 != "Sexo" or concept3 != "Homosexual" or concept4 != "Genero" or \
                concept5 != "Bisexual":

            # En caso de que no se cumpla la condición, almacenamos un mensaje de error
            error_msg = "Ups... Parece que esa no es la palabra"
            # self.add_error('name', error_msg)  # field error
            # Lanzamos la excepción con el mensaje que hemos almacenado anteriormente
            raise ValidationError(error_msg)  # form error

        # Retornamos el contenido del formulario rellenado por el usuario
        return cleaned_data

class PalabraDefForm(forms.Form):

    # Indicamos a través de una tupla el contenido de los desplegables
    WORD_CHOICES = (
        ('1', 'Homosexual'),
        ('2', 'Orientación sexual'),
        ('3', 'Estereotipo de género'),
        ('4', 'Intersexualidad'),
        ('5', 'Identidad de género'),
    )

    # Creamos los elementos del formulario y les damos valor
    inscripcion1 = forms.ChoiceField(choices=WORD_CHOICES, initial="2")
    inscripcion2 = forms.ChoiceField(choices=WORD_CHOICES)
    inscripcion3 = forms.ChoiceField(choices=WORD_CHOICES)
    inscripcion4 = forms.ChoiceField(choices=WORD_CHOICES)
    inscripcion5 = forms.ChoiceField(choices=WORD_CHOICES)

    def clean(self):
        """
        Metodo que se encarga de realizar la validación de los elementos del formulario
        :return:
        """

        # Almacenamos en una variable el contenido de lo que introduce el usuario y lo que se envía en la petición POST
        cleaned_data = super().clean()  # ensures that any validation logic in parent classes is maintained

        # Almacenamos en una variable la elección que ha marcado el usuario en cada uno de los desplegables creados
        palabra1 = self.cleaned_data.get("inscripcion1")
        palabra2 = self.cleaned_data.get("inscripcion2")
        palabra3 = self.cleaned_data.get("inscripcion3")
        palabra4 = self.cleaned_data.get("inscripcion4")
        palabra5 = self.cleaned_data.get("inscripcion5")

        # Creamos una condición que se encarga de validar el contenido de los desplegables
        if palabra1 != "2" or palabra2 != "4" or palabra3 != "5" or palabra4 != "1" or palabra5 != "3":

            # Almacenamos un mensaje de error en caso de que no se cumpla la condición anterior
            error_msg = "Ups... Parece que esa no es la combinación"
            # self.add_error('palabra1', error_msg)  # field error

            # Lanzamos la excepción en caso de que no se cumpla la condición anterior
            raise ValidationError(error_msg)  # form error

        # Retornamos el contenido del formulario rellenado por el usuario
        return cleaned_data

class Diferencias(forms.ModelForm):
    class Meta:
        model = PruebaTres
        fields = ('def1', 'def2','def3')


class Acciones(forms.Form):
    Diferencia1 = forms.CharField(required=True, widget=forms.Textarea)
    Diferencia2 = forms.CharField(required=True, widget=forms.Textarea)
    Diferencia3 = forms.CharField(required=True, widget=forms.Textarea)