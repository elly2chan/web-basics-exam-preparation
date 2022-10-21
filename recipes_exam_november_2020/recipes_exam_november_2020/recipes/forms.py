from django import forms

from recipes_exam_november_2020.recipes.mixins import DisableFormFields
from recipes_exam_november_2020.recipes.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(BaseRecipeForm):
    pass


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(DisableFormFields, BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        self.disable_fields()
