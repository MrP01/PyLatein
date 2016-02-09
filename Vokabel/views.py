from django.views import generic
from django.core import serializers

from .forms import *

class MultipleModelsListView(generic.View, generic.base.TemplateResponseMixin, generic.base.ContextMixin):
	querysets={}    #context_object_name:getter method
	def get(self, request, *args, **kwargs):
		ctx=self.get_context_data(**kwargs)
		return self.render_to_response(ctx)

	def get_context_data(self, **kwargs):
		ctx=super(MultipleModelsListView, self).get_context_data(**kwargs)
		for name, getter in self.querysets.items():
			ctx[name]=getter()
		return ctx

class AllVoc(MultipleModelsListView):
	template_name="index.html"
	querysets = {
		"nouns": Noun.objects.all,
		"verbs": Verb.objects.all,
		"adjectives": Adjective.objects.all
	}

class CreateNoun(generic.CreateView):
	template_name = "noun_form.html"
	form_class = NounForm
	success_url = "/"

class NounDetail(generic.DetailView):
	template_name = "noun_detail.html"
	model = Noun

class CreateVerb(generic.CreateView):
	template_name = "verb_form.html"
	form_class = VerbForm
	success_url = "/"

class VerbDetail(generic.DetailView):
	template_name = "verb_detail.html"
	model = Verb

class CreateAdjective(generic.CreateView):
	template_name = "adjective_form.html"
	form_class = AdjectiveForm
	success_url = "/"

class AdjectiveDetail(generic.DetailView):
	template_name = "adjective_detail.html"
	model = Adjective
