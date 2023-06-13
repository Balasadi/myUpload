from django.db import models

STATE_CHOICE = (
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
('West Virginia','West Virginia'),
('Wisconsin','Wisconsin'),
('Wyoming','Wyoming'),
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='profileimg', blank=True)
 my_file = models.FileField(upload_to='doc', blank=True)


