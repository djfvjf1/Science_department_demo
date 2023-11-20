# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import (KPI_1, KPI_2, KPI_3, KPI_4, KPI_5, KPI_6, KPI_7, KPI_8,
                     KPI_9)


# create a ModelForm
class KPI_1_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_1
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_2_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_2
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class KPI_3_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_3
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_4_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_4
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_5_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_5
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_6_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_6
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_7_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_7
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_8_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_8
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class KPI_9_Form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = KPI_9
        fields = "__all__"

    widgets = {
            'points': forms.TextInput(attrs={'readonly': 'readonly'}),
        }