from django.db import models
import enum

#################################
#Constants

class Genus(enum.Enum):
	maskulin, feminin, neutrum = "m", "f", "n"

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
	imperativeSg=models.CharField(max_length=100)
	imperativePl=models.CharField(max_length=100)

	presentSg1=models.CharField(max_length=100)
	presentSg2=models.CharField(max_length=100)
	presentSg3=models.CharField(max_length=100)
	presentPl1=models.CharField(max_length=100)
	presentPl2=models.CharField(max_length=100)
	presentPl3=models.CharField(max_length=100)

	perfectSg1=models.CharField(max_length=100)
	perfectSg2=models.CharField(max_length=100)
	perfectSg3=models.CharField(max_length=100)
	perfectPl1=models.CharField(max_length=100)
	perfectPl2=models.CharField(max_length=100)
	perfectPl3=models.CharField(max_length=100)

	imperfectSg1=models.CharField(max_length=100)
	imperfectSg2=models.CharField(max_length=100)
	imperfectSg3=models.CharField(max_length=100)
	imperfectPl1=models.CharField(max_length=100)
	imperfectPl2=models.CharField(max_length=100)
	imperfectPl3=models.CharField(max_length=100)

	pluqperfectSg1=models.CharField(max_length=100)
	pluqperfectSg2=models.CharField(max_length=100)
	pluqperfectSg3=models.CharField(max_length=100)
	pluqperfectPl1=models.CharField(max_length=100)
	pluqperfectPl2=models.CharField(max_length=100)
	pluqperfectPl3=models.CharField(max_length=100)

	futureSg1=models.CharField(max_length=100)
	futureSg2=models.CharField(max_length=100)
	futureSg3=models.CharField(max_length=100)
	futurePl1=models.CharField(max_length=100)
	futurePl2=models.CharField(max_length=100)
	futurePl3=models.CharField(max_length=100)

	future2Sg1=models.CharField(max_length=100)
	future2Sg2=models.CharField(max_length=100)
	future2Sg3=models.CharField(max_length=100)
	future2Pl1=models.CharField(max_length=100)
	future2Pl2=models.CharField(max_length=100)
	future2Pl3=models.CharField(max_length=100)

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
	posSg1m=models.CharField(max_length=100)
	posSg2m=models.CharField(max_length=100)
	posSg3m=models.CharField(max_length=100)
	posSg4m=models.CharField(max_length=100)
	posSg5m=models.CharField(max_length=100)
	posSg6m=models.CharField(max_length=100)
	posPl1m=models.CharField(max_length=100)
	posPl2m=models.CharField(max_length=100)
	posPl3m=models.CharField(max_length=100)
	posPl4m=models.CharField(max_length=100)
	posPl5m=models.CharField(max_length=100)
	posPl6m=models.CharField(max_length=100)
	posSg1f=models.CharField(max_length=100)
	posSg2f=models.CharField(max_length=100)
	posSg3f=models.CharField(max_length=100)
	posSg4f=models.CharField(max_length=100)
	posSg5f=models.CharField(max_length=100)
	posSg6f=models.CharField(max_length=100)
	posPl1f=models.CharField(max_length=100)
	posPl2f=models.CharField(max_length=100)
	posPl3f=models.CharField(max_length=100)
	posPl4f=models.CharField(max_length=100)
	posPl5f=models.CharField(max_length=100)
	posPl6f=models.CharField(max_length=100)
	posSg1n=models.CharField(max_length=100)
	posSg2n=models.CharField(max_length=100)
	posSg3n=models.CharField(max_length=100)
	posSg4n=models.CharField(max_length=100)
	posSg5n=models.CharField(max_length=100)
	posSg6n=models.CharField(max_length=100)
	posPl1n=models.CharField(max_length=100)
	posPl2n=models.CharField(max_length=100)
	posPl3n=models.CharField(max_length=100)
	posPl4n=models.CharField(max_length=100)
	posPl5n=models.CharField(max_length=100)
	posPl6n=models.CharField(max_length=100)

	compSg1m=models.CharField(max_length=100)
	compSg2m=models.CharField(max_length=100)
	compSg3m=models.CharField(max_length=100)
	compSg4m=models.CharField(max_length=100)
	compSg5m=models.CharField(max_length=100)
	compSg6m=models.CharField(max_length=100)
	compPl1m=models.CharField(max_length=100)
	compPl2m=models.CharField(max_length=100)
	compPl3m=models.CharField(max_length=100)
	compPl4m=models.CharField(max_length=100)
	compPl5m=models.CharField(max_length=100)
	compPl6m=models.CharField(max_length=100)
	compSg1f=models.CharField(max_length=100)
	compSg2f=models.CharField(max_length=100)
	compSg3f=models.CharField(max_length=100)
	compSg4f=models.CharField(max_length=100)
	compSg5f=models.CharField(max_length=100)
	compSg6f=models.CharField(max_length=100)
	compPl1f=models.CharField(max_length=100)
	compPl2f=models.CharField(max_length=100)
	compPl3f=models.CharField(max_length=100)
	compPl4f=models.CharField(max_length=100)
	compPl5f=models.CharField(max_length=100)
	compPl6f=models.CharField(max_length=100)
	compSg1n=models.CharField(max_length=100)
	compSg2n=models.CharField(max_length=100)
	compSg3n=models.CharField(max_length=100)
	compSg4n=models.CharField(max_length=100)
	compSg5n=models.CharField(max_length=100)
	compSg6n=models.CharField(max_length=100)
	compPl1n=models.CharField(max_length=100)
	compPl2n=models.CharField(max_length=100)
	compPl3n=models.CharField(max_length=100)
	compPl4n=models.CharField(max_length=100)
	compPl5n=models.CharField(max_length=100)
	compPl6n=models.CharField(max_length=100)

	supSg1m=models.CharField(max_length=100)
	supSg2m=models.CharField(max_length=100)
	supSg3m=models.CharField(max_length=100)
	supSg4m=models.CharField(max_length=100)
	supSg5m=models.CharField(max_length=100)
	supSg6m=models.CharField(max_length=100)
	supPl1m=models.CharField(max_length=100)
	supPl2m=models.CharField(max_length=100)
	supPl3m=models.CharField(max_length=100)
	supPl4m=models.CharField(max_length=100)
	supPl5m=models.CharField(max_length=100)
	supPl6m=models.CharField(max_length=100)
	supSg1f=models.CharField(max_length=100)
	supSg2f=models.CharField(max_length=100)
	supSg3f=models.CharField(max_length=100)
	supSg4f=models.CharField(max_length=100)
	supSg5f=models.CharField(max_length=100)
	supSg6f=models.CharField(max_length=100)
	supPl1f=models.CharField(max_length=100)
	supPl2f=models.CharField(max_length=100)
	supPl3f=models.CharField(max_length=100)
	supPl4f=models.CharField(max_length=100)
	supPl5f=models.CharField(max_length=100)
	supPl6f=models.CharField(max_length=100)
	supSg1n=models.CharField(max_length=100)
	supSg2n=models.CharField(max_length=100)
	supSg3n=models.CharField(max_length=100)
	supSg4n=models.CharField(max_length=100)
	supSg5n=models.CharField(max_length=100)
	supSg6n=models.CharField(max_length=100)
	supPl1n=models.CharField(max_length=100)
	supPl2n=models.CharField(max_length=100)
	supPl3n=models.CharField(max_length=100)
	supPl4n=models.CharField(max_length=100)
	supPl5n=models.CharField(max_length=100)
	supPl6n=models.CharField(max_length=100)
