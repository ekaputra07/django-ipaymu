from django import forms
from django.utils.translation import ugettext as _

class IpaymuForm(forms.Form):
    """
    Ipaymu parameters validation.
    """

    FORMAT_CHOICES = (
        ('json', 'JSON'),
        ('xml', 'XML'),
    )

    product = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    comments = forms.CharField(required=False)

    key = forms.CharField()
    action = forms.CharField()

    unotify = forms.URLField()
    ureturn = forms.URLField()
    ucancel = forms.URLField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)

    invoice_number = forms.CharField(required=False)
    paypal_price = forms.DecimalField(required=False, decimal_places=2)
    paypal_email = forms.EmailField(required=False)


    def clean(self):

        cleaned_data = super(IpaymuForm, self).clean()

        if cleaned_data.get('paypal_email'):

            if not cleaned_data.get('invoice_number'):
                self._errors['invoice_number'] = self.error_class([_('Invoice number required for Paypal processing.')])
                del cleaned_data['invoice_number']

            if not cleaned_data.get('paypal_price'):
                self._errors['paypal_price'] = self.error_class([_('Paypal price required for Paypal processing.')])
                del cleaned_data['paypal_price']

        return cleaned_data