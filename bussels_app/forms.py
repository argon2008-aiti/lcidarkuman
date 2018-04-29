from django import forms
from models import Bussel

class BusselReportDetailForm(forms.Form):
    topic = forms.CharField(label="Topic:", max_length=200)
    date  = forms.DateField(widget=forms.TextInput(attrs={'disabled': True}),\
                            label="Report Date:", required=False)
    time  = forms.TimeField(widget=forms.TextInput(attrs={'disabled': True}),\
                            label="Report Time:", required=False)
    time_started    = forms.TimeField(label="Bussel Start Time:")
    time_ended      = forms.TimeField(label="Bussel End Time:")
    bussel_attendance = forms.IntegerField(label="Bussel Attendance:")
    church_attendance = forms.IntegerField(label="Church Attendance:", min_value=0)
    num_souls_won     = forms.IntegerField(label="Souls Won:")
    num_first_timers  = forms.IntegerField(label="First Timers:")
    offertory_given   = forms.DecimalField(label="Offertory(GHS):", decimal_places=2, max_digits=10)


class BussellPerformanceMetricsForm(forms.Form):
    bussell = forms.ModelChoiceField(Bussel.objects.filter(status=1))
    from_date = forms.DateField(input_formats=('%d-%m-%Y',))
    to_date = forms.DateField(input_formats=('%d-%m-%Y',))
