from django import forms
from info_system.models import GENDER, MARITAL_STATUS, NATIONALITY, YES_NO, ROLES, MEMBERSHIP_STATUS 
from info_system.models import EDUCATION_LEVEL, LANGUAGES
from info_system.models import Ministry, Language


class NewMemberForm(forms.Form):

    # personal info ----------------------------------------------
    first_name = forms.CharField(label='First Name', max_length=100,
                                 widget=forms.TextInput({"placeholder": "e.g Richard"}))

    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Ato"}))

    last_name = forms.CharField(label='Surname', max_length=100,
                                 widget=forms.TextInput({"placeholder": "e.g Mensah"}))

    phone = forms.CharField(label='Phone Number', max_length=100,
                                 widget=forms.TextInput({"placeholder": "e.g +233241234567"}))

    email_address = forms.EmailField(label="Email", max_length=50, required=False,
                                     widget=forms.EmailInput({"placeholder": "e.g example@gmail.com"}))

    gender = forms.ChoiceField(label="Gender",  choices=GENDER)

    marital_status = forms.ChoiceField(choices=MARITAL_STATUS)

    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.TextInput({'placeholder': 'choose date'}))

    place_of_birth  = forms.CharField(label='Place of Birth', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Accra"}))

    hometown  = forms.CharField(label='Hometown (Town or City, Region or State or Province, Country)', max_length=200, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Chorkor, Greater Accra, Ghana"}))

    tribal_origin  = forms.CharField(label='Tribal Origin (Tribe, Region or State or Province, Country)', max_length=200, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Asante, Asante Region, Ghana"}))

    nationality_at_birth = forms.ChoiceField(choices=NATIONALITY)
    nationality  = forms.ChoiceField(choices=NATIONALITY)
    level_of_education = forms.ChoiceField(choices=EDUCATION_LEVEL)
    lingual_competency = forms.ModelMultipleChoiceField(Language.objects.all(), label="Lingual Comptence", required=False)
    occupation = forms.CharField(label="Current Occupation", max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder":"e.g Police"}))

    # residence ------------------------------------------------------
    house_number  = forms.CharField(label='House Number', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g B1043/15"}))

    street_name  = forms.CharField(label='Street Name', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Antruma St."}))

    suburb  = forms.CharField(label='Suburb', max_length=100, required=False,
                                 widget=forms.TextInput({"placeholder": "e.g Alafia"}))

    description_of_house  = forms.CharField(label='Description of Residence', max_length=1024, required=False,
                                 widget=forms.Textarea({"placeholder": "e.g. green storey building with blue gates adjacent to Azia Preparatory School"}))

    # church info ----------------------------------------------------
    date_joined = forms.DateField(label="Date Joined", widget=forms.TextInput({'placeholder': 'choose date'}))
    baptized_by_immersion  = forms.ChoiceField(label="Water Baptism By Immersion", choices=YES_NO)
    holy_ghost_baptism  = forms.ChoiceField(label="Holy Ghost Baptism", choices=YES_NO)
    leadership_role = forms.ChoiceField(label="Leadership Role", choices=ROLES)
    membership_status = forms.ChoiceField(label="Membership Status", choices=MEMBERSHIP_STATUS)
    ministries = forms.ModelMultipleChoiceField(Ministry.objects.all(), label="Ministries")
