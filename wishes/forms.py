from django import forms

from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ["name", "price", "link"]
        help_texts = {
            'price': ('optional'),
            'link': ('optional'),
        }
        labels = {
         "name": "",
         "price": "",
         "link": "",
        }
    def __init__(self, *args, **kwargs):
        super(WishForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = ('Item Name')
        self.fields['price'].widget.attrs['placeholder'] = ('Price Estimate')
        self.fields['link'].widget.attrs['placeholder'] = ('Link to Item')