from django import forms
from django.utils.timezone import now

from cartapp.models import DaysOfWeek, Service, WindowWashing
from common.const import CLEANING_TIME_CHOICES


class AddToCartForm(forms.Form):

    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(),
                                              widget=forms.CheckboxSelectMultiple,
                                              required=False)

    comment = forms.CharField(max_length=1024, widget=forms.Textarea, required=False)

    cleaning_days = forms.ModelMultipleChoiceField(queryset=DaysOfWeek.objects.all(),
                                                   widget=forms.CheckboxSelectMultiple(),
                                                   required=False
                                                   )

    cleaning_time = forms.ChoiceField(choices=CLEANING_TIME_CHOICES,
                                      widget=forms.RadioSelect,
                                      required=False
                                      )

    number_stuff = forms.IntegerField(min_value=1,
                                      widget=forms.NumberInput(attrs={'id': 'amount',
                                                                      'value': '1'}),
                                      required=False
                                      )
    is_windows = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        services_d = kwargs.pop('services_dict')
        super().__init__(*args, **kwargs)
        self.fields['services'].queryset = services_d


class AddToCartWindowsForm(forms.ModelForm):
    class Meta:
        model = WindowWashing
        fields = '__all__'


class AddDateToCartForm(forms.Form):
    date_order = forms.DateField(widget=forms.RadioSelect)
    is_other_date = forms.BooleanField(required=False)

    def clean_date_order(self):
        date_order = self.cleaned_data['date_order']
        now_date = now().date()
        if date_order < now_date:
            raise forms.ValidationError('???????????? ?????????????? ???????????? ???????????? ????????')
        return date_order


