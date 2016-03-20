from django.conf.urls import url
import Trainer.views

app_name = "trainer"
urlpatterns = [
    url(r"^$", Trainer.views.TrainerView.as_view(), name="trainer"),
    url(r"^select$", Trainer.views.VocSelectionView.as_view(), name="select"),
]