from django.conf.urls import url
import Trainer.views

urlpatterns = [
    url(r"^$", Trainer.views.TrainerView.as_view(), name="trainer"),
]