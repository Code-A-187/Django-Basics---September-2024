from django import forms

from WorldOfSpeedApp.cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'image_url': 'Image URL'
        }


class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True
