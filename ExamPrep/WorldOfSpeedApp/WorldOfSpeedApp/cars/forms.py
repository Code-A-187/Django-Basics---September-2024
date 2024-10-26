from django import forms

from WorldOfSpeedApp.cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'image_url': 'Image URL'
        }


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    pass
