class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():  # ('first_name': field_obj)
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class NoLabelMixin:
    def remove_labels(self):
        for field in self.fields.values():
            field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_labels()