class DisableFormFields:
    def disable_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
