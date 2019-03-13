from django import forms


from mycommunity.models import Events


# class MyModelForm(forms.ModelForm):
#     boolfield = forms.TypedChoiceField(
#                     coerce=lambda x: bool(int(x)),
#                    choices=((0, 'False'), (1, 'True')),
#                    widget=forms.RadioSelect
#                 )
#     class Meta:
#          model = Events

# class EventForm(forms.ModelForm):
#     YESNO_CHOICES = ((0, 'No'), (1, 'Yes'))
#     Allergies = forms.TypedChoiceField(
#         choices=YESNO_CHOICES, widget=forms.RadioSelect, coerce=int
#     )
#     class Meta:
#         model = Events
#         fields = '__all__'
