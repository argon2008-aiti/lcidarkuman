from django import forms


class NewMemberForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100,
                                 widget=forms.TextInput({"placeholder": "Richard"}))

    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "Ato"}))

    surname = forms.CharField(label='Surname', max_length=100,
                                 widget=forms.TextInput({"placeholder": "Mensah"}))

    phone_number = forms.CharField(label='Phone Number', max_length=100,
                                 widget=forms.TextInput({"placeholder": "+233241234567"}))

    email_address
