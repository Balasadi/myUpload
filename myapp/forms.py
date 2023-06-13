from django import forms
from .models import Resume

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho', 'Idaho'),
('IllinoisIndiana','IllinoisIndiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('MontanaNebraska','MontanaNebraska'),
('Nevada','Nevada'),
('New Hampshire','New Hampshire'),
('New Jersey','New Jersey'),
('New Mexico','New Mexico'),
('New York','New York'),
('North Carolina','North Carolina'),
('North Dakota','North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('PennsylvaniaRhode Island','PennsylvaniaRhode Island'),
('South Carolina','South Carolina'),
('South Dakota','South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('WestVirginia','WestVirginia'),
('Wisconsin','Wisconsin'),
('Wyoming','Wyoming'),
]

class ResumeForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 #job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
 #job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.Select)                                   
 class Meta:
  model = Resume
  fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'profile_image':'Profile Image', 'my_file':'Document'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }