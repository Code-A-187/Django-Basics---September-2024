class PlaceholderMixin:
    placeholders = {}

    def set_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder_text = self.placeholders.get(field_name)
            if placeholder_text:
                field.widget.attrs['placeholder'] = placeholder_text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_placeholders()


class ReadOnlyMixin:
    read_only_fields = ()

    def make_fields_readonly(self):
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()