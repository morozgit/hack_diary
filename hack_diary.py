import django
from django.conf import settings
import random
settings.configure()
django.setup()
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Teacher


schoolkid = input()
subject = input()
praise = ['Молодец!', 'Это как раз то, что нужно!', 'Ты на верном пути!', 'Ты многое сделал, я это вижу!']

def fix_marks(schoolkid):
	child = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
	for point in child:
		point.points = 5 
		point.save()


def remove_chastisements(schoolkid):
	chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
	chastisement.delete()


def create_commendation(schoolkid, subject):
	schoolchild = Schoolkid.objects.get(full_name__contains=schoolkid)
	subject_6A = Lesson.objects.filter(subject__title__contains=subject, year_of_study__contains=6, group_letter__contains="А").first()
	Commendation.objects.create(text=random.choice(praise), created=subject_6A.date, schoolkid=schoolchild, subject=subject_6A.subject, teacher=subject_6A.teacher)
	remove_chastisements(schoolkid)
