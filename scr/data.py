"""Module implémentant les données du problème de déploiement de personnel."""

from pydantic import BaseModel, PositiveInt, NonNegativeInt, Field, model_validator
from typing import Annotated, Self

ProportionPositive = Annotated[float, Field(gt=0.0, lt=1.0)]


class Probleme(BaseModel):
    """Encode les paramètres d'un problème de déploiement de personnel.

    Les états initial et final sont fixés.
    Les minima mensuels définissent les contraintes de présence.
    Les coûts unitaires sont exprimés en euros.
    """

    effectif_initial: PositiveInt
    effectif_final: PositiveInt
    minima_mensuels: list[NonNegativeInt]
    cout_mutation: PositiveInt = 160
    cout_ecart: PositiveInt = 200
    max_mutations_absolues: PositiveInt = 3
    max_mutations_relatives: ProportionPositive = 1 / 3
    tolerance_manque: ProportionPositive = 0.25

    @model_validator(mode="after")
    def verifie_coherence(self) -> Self:
        if len(self.minima_mensuels) == 0:
            raise ValueError("Il faut au moins un mois.")
        return self