from django import forms
from ExamPrep_II.fruits.models import Fruit
from ExamPrep_II.mixins import PlaceholderMixin, NoLabelMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(PlaceholderMixin, NoLabelMixin, FruitBaseForm):
    placeholders = {
        "name": "Fruit Name",
        "image_url": "Fruit Image URL",
        "description": "Fruit Description",
        "nutrition": "Nutrition Info",
    }

    class Meta(FruitBaseForm.Meta):
        exclude = ['owner', ]


class FruitEditForm(PlaceholderMixin, NoLabelMixin, FruitBaseForm):
    pass
