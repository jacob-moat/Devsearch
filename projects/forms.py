from django.forms import ModelForm, widgets
from django import forms
from .models import project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwards):
        super(ProjectForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwards):
        super(ReviewForm, self).__init__(*args, **kwards)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
