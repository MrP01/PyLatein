from django.http import Http404
from django.shortcuts import redirect
from django.views import generic
from django.core.serializers import serialize
import random

from Vokabel.models import Noun, Verb, Adjective, VOCMODELS
from .forms import *

class AbstractTrainerMixin:
    def __init__(self):
        super(AbstractTrainerMixin, self).__init__()
        self.query=None

    def get_context_data(self, **kwargs):
        vocs=self.choose_vocs()
        return {"vocs": serialize("json", vocs)}

    def choose_vocs(self):
        vocs=[]
        for group in self.query["vocgroups"]:
            vocs+=group.nounmembers.all()
            vocs+=group.verbmembers.all()
            vocs+=group.adjectivemembers.all()
        # random.shuffle(vocs)
        return vocs

    @staticmethod
    def allIds():
        ids=[]
        for c, model in VOCMODELS.items():
            ids+=[(c, i) for i in model.objects.all().values_list("id", flat=True)]
        return ids

class TrainerView(AbstractTrainerMixin, generic.TemplateView):
    template_name = "quicktrainer.html"
    def get(self, request, *args, **kwargs):
        form=VocSelectForm(request.GET)
        if form.is_valid():
            self.query=form.cleaned_data
            print(self.query)
            return super(TrainerView, self).get(request, *args, **kwargs)
        raise Http404("Invalid Request :(")


class VocSelectionView(generic.FormView):
    template_name = "vocselection.html"
    form_class = VocSelectForm

    def form_valid(self, form):
        print(form.cleaned_data)
        # self.request.session["train_vocs"]=form.cleaned_data["vocgroups"]
        return redirect("trainer")
