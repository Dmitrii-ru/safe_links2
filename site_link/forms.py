from django import forms
from django.core.exceptions import ValidationError

from .models import Links


class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['slug', 'link']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        for l in Links.objects.all():
            if str(slug) == str(l.slug):
                raise ValidationError('Поле не уникально')
        return slug

    def clean_link(self):
        link = self.cleaned_data['link']
        if len(link) > 250:
            raise ValidationError(
                f'Длина превышает на {int(len(link)) - 250} , ссылка не должна превышать 250 символов ')
        else:
            return link
