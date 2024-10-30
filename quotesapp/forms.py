from django.forms import CheckboxSelectMultiple, DateInput, ModelChoiceField, ModelForm, CharField, ModelMultipleChoiceField, Select, SelectMultiple, TextInput, DateField, Textarea
from .models import Quote, Author, Tag

class QuoteForm(ModelForm):
    quote = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('full_name'), widget=Select(attrs={'class': 'form-select'}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'),widget=SelectMultiple, required=False)
    
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


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