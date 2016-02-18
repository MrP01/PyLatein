from django.shortcuts import render
from django.views import generic
import itertools, random

from Vokabel.models import Noun, Verb, Adjective

def chooseRandom(model, count):
	ids=list(model.objects.all().values_list("id", flat=True))
	return list(model.objects.filter(id__in=random.sample(ids, count)))

class TrainerView(generic.View):
	def get(self, request, **kwargs):
		total=10
		l=random.sample(["n", "v", "a"]*int(total/3+1), total)
		vocs=chooseRandom(Noun, l.count("n"))
		vocs+=chooseRandom(Verb, l.count("v"))
		vocs+=chooseRandom(Adjective, l.count("a"))
		return render(request, "quicktrainer.html", context={
			"vocs":vocs
		})
