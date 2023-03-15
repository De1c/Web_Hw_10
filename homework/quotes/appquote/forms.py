from django.forms import ModelForm, CharField, TextInput, ModelChoiceField

from .models import Tag, Author, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=250, widget=TextInput())
    born_date = CharField(widget=TextInput())
    born_location = CharField(widget=TextInput())
    description = CharField(widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    text = CharField(max_length=500, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ['text', 'author']
        exclude = ['tags']