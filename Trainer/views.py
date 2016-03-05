from django.views import generic
from django.core.serializers import serialize
import random

from Vokabel.models import Noun, Verb, Adjective, VOCMODELS

class AbstractTrainerView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        vocs=self.choose_vocs()
        return {"vocs": serialize("json", vocs)}

    def choose_vocs(self):
        vocs=[]
        ids=random.sample(self.allIds(), 10)
        for c, model in VOCMODELS.items():
            vocs+=list(model.objects.filter(id__in=[i[1] for i in ids if i[0] == c]))
        random.shuffle(vocs)
        return vocs

    def allIds(self):
        ids=[]
        for c, model in VOCMODELS.items():
            ids+=[(c, i) for i in model.objects.all().values_list("id", flat=True)]
        return ids


class TrainerView(AbstractTrainerView):
    template_name = "quicktrainer.html"
