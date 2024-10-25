from django import forms
from ExamPrep_II.fruits.models import Fruit
from ExamPrep_II.mixins import PlaceholderMixin, NoLabelMixin, ReadOnlyMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner', )


class FruitCreateForm(PlaceholderMixin, NoLabelMixin, FruitBaseForm):
    placeholders = {
        "name": "Fruit Name",
        "image_url": "Fruit Image URL",
        "description": "Fruit Description",
        "nutrition": "Nutrition Info",
    }


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(ReadOnlyMixin, FruitBaseForm):
    read_only_fields = ['name', 'image_url', 'description', 'nutrition']

