from django.forms import CheckboxSelectMultiple, DateInput, ModelChoiceField, ModelForm, CharField, ModelMultipleChoiceField, Select, TextInput, DateField, Textarea
from .models import Quote, Author, Tag

class QuoteForm(ModelForm):
    quote = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all(), widget=Select(attrs={'class': 'form-select'}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=CheckboxSelectMultiple, required=False)
    
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        # exclude = ['author', 'tags'] # For what?


class AuthorForm(ModelForm):
    full_name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    born_date = DateField(widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    born_location = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = Author
        fields = ['full_name', 'born_date', 'born_location', 'description']
        

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name'}),
        }