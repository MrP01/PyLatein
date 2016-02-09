from django.db import models
import enum

#################################
#Constants

class Genus(enum.Enum):
	masculine, feminine, neuter = "m", "f", "n"

class Case(enum.Enum):
	(sg1, sg2, sg3, sg4, sg5, sg6,
	pl1, pl2, pl3, pl4, pl5, pl6) = range(1, 13)

class Person(enum.Enum):
	(sg1, sg2, sg3,
	pl1, pl2, pl3) = range(1, 7)

class Tense(enum.Enum):
	present, perfect, imperfect, pluqperfect, future=range(5)


class Vocable(models.Model):
	translation=models.CharField(max_length=100)
	class Meta:
		abstract=True

#################################
#Noun

class Noun(Vocable):
	genus=models.CharField(max_length=1,
		choices=[(g.value, g.name) for g in Genus],
        blank=False, default="m")

	#stem and ending
	sg1=models.CharField(max_length=100)
	sg2=models.CharField(max_length=100)
	sg3=models.CharField(max_length=100)
	sg4=models.CharField(max_length=100)
	sg5=models.CharField(max_length=100)
	sg6=models.CharField(max_length=100)

	pl1=models.CharField(max_length=100)
	pl2=models.CharField(max_length=100)
	pl3=models.CharField(max_length=100)
	pl4=models.CharField(max_length=100)
	pl5=models.CharField(max_length=100)
	pl6=models.CharField(max_length=100)


#################################
#Verb

class Verb(Vocable):
	infinitive=models.CharField(max_length=100)
	imperative_sg=models.CharField(max_length=100)
	imperative_pl=models.CharField(max_length=100)

	present_sg1=models.CharField(max_length=100)
	present_sg2=models.CharField(max_length=100)
	present_sg3=models.CharField(max_length=100)
	present_pl1=models.CharField(max_length=100)
	present_pl2=models.CharField(max_length=100)
	present_pl3=models.CharField(max_length=100)

	perfect_sg1=models.CharField(max_length=100)
	perfect_sg2=models.CharField(max_length=100)
	perfect_sg3=models.CharField(max_length=100)
	perfect_pl1=models.CharField(max_length=100)
	perfect_pl2=models.CharField(max_length=100)
	perfect_pl3=models.CharField(max_length=100)

	imperfect_sg1=models.CharField(max_length=100)
	imperfect_sg2=models.CharField(max_length=100)
	imperfect_sg3=models.CharField(max_length=100)
	imperfect_pl1=models.CharField(max_length=100)
	imperfect_pl2=models.CharField(max_length=100)
	imperfect_pl3=models.CharField(max_length=100)

	pluqperfect_sg1=models.CharField(max_length=100)
	pluqperfect_sg2=models.CharField(max_length=100)
	pluqperfect_sg3=models.CharField(max_length=100)
	pluqperfect_pl1=models.CharField(max_length=100)
	pluqperfect_pl2=models.CharField(max_length=100)
	pluqperfect_pl3=models.CharField(max_length=100)

	future_sg1=models.CharField(max_length=100)
	future_sg2=models.CharField(max_length=100)
	future_sg3=models.CharField(max_length=100)
	future_pl1=models.CharField(max_length=100)
	future_pl2=models.CharField(max_length=100)
	future_pl3=models.CharField(max_length=100)

	future2_sg1=models.CharField(max_length=100)
	future2_sg2=models.CharField(max_length=100)
	future2_sg3=models.CharField(max_length=100)
	future2_pl1=models.CharField(max_length=100)
	future2_pl2=models.CharField(max_length=100)
	future2_pl3=models.CharField(max_length=100)

class Conjugation(models.Model):
	id=models.CharField(max_length=5, primary_key=True)
	description=models.CharField(max_length=100)
	vocal=models.CharField(max_length=1)

class VerbEndings(models.Model):
	"""Contains 3 singular and 3 plural endings for a verb"""
	id=models.CharField(max_length=5, primary_key=True)
	description=models.CharField(max_length=100)

	sg1=models.CharField(max_length=12)
	sg2=models.CharField(max_length=12)
	sg3=models.CharField(max_length=12)
	pl1=models.CharField(max_length=12)
	pl2=models.CharField(max_length=12)
	pl3=models.CharField(max_length=12)


#################################
#Adjective

class Adjective(Vocable):
	pos_sg1m=models.CharField(max_length=100)
	pos_sg2m=models.CharField(max_length=100)
	pos_sg3m=models.CharField(max_length=100)
	pos_sg4m=models.CharField(max_length=100)
	pos_sg5m=models.CharField(max_length=100)
	pos_sg6m=models.CharField(max_length=100)
	pos_pl1m=models.CharField(max_length=100)
	pos_pl2m=models.CharField(max_length=100)
	pos_pl3m=models.CharField(max_length=100)
	pos_pl4m=models.CharField(max_length=100)
	pos_pl5m=models.CharField(max_length=100)
	pos_pl6m=models.CharField(max_length=100)
	pos_sg1f=models.CharField(max_length=100)
	pos_sg2f=models.CharField(max_length=100)
	pos_sg3f=models.CharField(max_length=100)
	pos_sg4f=models.CharField(max_length=100)
	pos_sg5f=models.CharField(max_length=100)
	pos_sg6f=models.CharField(max_length=100)
	pos_pl1f=models.CharField(max_length=100)
	pos_pl2f=models.CharField(max_length=100)
	pos_pl3f=models.CharField(max_length=100)
	pos_pl4f=models.CharField(max_length=100)
	pos_pl5f=models.CharField(max_length=100)
	pos_pl6f=models.CharField(max_length=100)
	pos_sg1n=models.CharField(max_length=100)
	pos_sg2n=models.CharField(max_length=100)
	pos_sg3n=models.CharField(max_length=100)
	pos_sg4n=models.CharField(max_length=100)
	pos_sg5n=models.CharField(max_length=100)
	pos_sg6n=models.CharField(max_length=100)
	pos_pl1n=models.CharField(max_length=100)
	pos_pl2n=models.CharField(max_length=100)
	pos_pl3n=models.CharField(max_length=100)
	pos_pl4n=models.CharField(max_length=100)
	pos_pl5n=models.CharField(max_length=100)
	pos_pl6n=models.CharField(max_length=100)
	
	comp_sg1m=models.CharField(max_length=100)
	comp_sg2m=models.CharField(max_length=100)
	comp_sg3m=models.CharField(max_length=100)
	comp_sg4m=models.CharField(max_length=100)
	comp_sg5m=models.CharField(max_length=100)
	comp_sg6m=models.CharField(max_length=100)
	comp_pl1m=models.CharField(max_length=100)
	comp_pl2m=models.CharField(max_length=100)
	comp_pl3m=models.CharField(max_length=100)
	comp_pl4m=models.CharField(max_length=100)
	comp_pl5m=models.CharField(max_length=100)
	comp_pl6m=models.CharField(max_length=100)
	comp_sg1f=models.CharField(max_length=100)
	comp_sg2f=models.CharField(max_length=100)
	comp_sg3f=models.CharField(max_length=100)
	comp_sg4f=models.CharField(max_length=100)
	comp_sg5f=models.CharField(max_length=100)
	comp_sg6f=models.CharField(max_length=100)
	comp_pl1f=models.CharField(max_length=100)
	comp_pl2f=models.CharField(max_length=100)
	comp_pl3f=models.CharField(max_length=100)
	comp_pl4f=models.CharField(max_length=100)
	comp_pl5f=models.CharField(max_length=100)
	comp_pl6f=models.CharField(max_length=100)
	comp_sg1n=models.CharField(max_length=100)
	comp_sg2n=models.CharField(max_length=100)
	comp_sg3n=models.CharField(max_length=100)
	comp_sg4n=models.CharField(max_length=100)
	comp_sg5n=models.CharField(max_length=100)
	comp_sg6n=models.CharField(max_length=100)
	comp_pl1n=models.CharField(max_length=100)
	comp_pl2n=models.CharField(max_length=100)
	comp_pl3n=models.CharField(max_length=100)
	comp_pl4n=models.CharField(max_length=100)
	comp_pl5n=models.CharField(max_length=100)
	comp_pl6n=models.CharField(max_length=100)
	
	sup_sg1m=models.CharField(max_length=100)
	sup_sg2m=models.CharField(max_length=100)
	sup_sg3m=models.CharField(max_length=100)
	sup_sg4m=models.CharField(max_length=100)
	sup_sg5m=models.CharField(max_length=100)
	sup_sg6m=models.CharField(max_length=100)
	sup_pl1m=models.CharField(max_length=100)
	sup_pl2m=models.CharField(max_length=100)
	sup_pl3m=models.CharField(max_length=100)
	sup_pl4m=models.CharField(max_length=100)
	sup_pl5m=models.CharField(max_length=100)
	sup_pl6m=models.CharField(max_length=100)
	sup_sg1f=models.CharField(max_length=100)
	sup_sg2f=models.CharField(max_length=100)
	sup_sg3f=models.CharField(max_length=100)
	sup_sg4f=models.CharField(max_length=100)
	sup_sg5f=models.CharField(max_length=100)
	sup_sg6f=models.CharField(max_length=100)
	sup_pl1f=models.CharField(max_length=100)
	sup_pl2f=models.CharField(max_length=100)
	sup_pl3f=models.CharField(max_length=100)
	sup_pl4f=models.CharField(max_length=100)
	sup_pl5f=models.CharField(max_length=100)
	sup_pl6f=models.CharField(max_length=100)
	sup_sg1n=models.CharField(max_length=100)
	sup_sg2n=models.CharField(max_length=100)
	sup_sg3n=models.CharField(max_length=100)
	sup_sg4n=models.CharField(max_length=100)
	sup_sg5n=models.CharField(max_length=100)
	sup_sg6n=models.CharField(max_length=100)
	sup_pl1n=models.CharField(max_length=100)
	sup_pl2n=models.CharField(max_length=100)
	sup_pl3n=models.CharField(max_length=100)
	sup_pl4n=models.CharField(max_length=100)
	sup_pl5n=models.CharField(max_length=100)
	sup_pl6n=models.CharField(max_length=100)
