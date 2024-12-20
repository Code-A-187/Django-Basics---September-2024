class PlaceholderMixin:
    placeholders = {}

    def set_placeholders(self):
        for field_name, field in self.fields.items():
            # Fetch placeholder text from the dictionary if it exists
            placeholder_text = self.placeholders.get(field_name)
            if placeholder_text:
                field.widget.attrs['placeholder'] = placeholder_text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_placeholders()


class NoLabelMixin:
    def remove_labels(self):
        for field in self.fields.values():
            field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_labels()


class ReadOnlyMixin:
    read_only_fields = ()

    def make_fields_readonly(self):
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()