"""Tests du module data."""

import pytest
from pydantic import ValidationError
from scr.data import Probleme, PROBLEME_EXEMPLE


def test_probleme_exemple_valide():
    assert PROBLEME_EXEMPLE.effectif_initial == 3
    assert PROBLEME_EXEMPLE.effectif_final == 3
    assert PROBLEME_EXEMPLE.minima_mensuels == [3, 4, 6, 7, 4, 6, 2]


def test_effectif_initial_negatif_interdit():
    with pytest.raises(ValidationError):
        Probleme(effectif_initial=-1, effectif_final=3, minima_mensuels=[3, 4])


def test_effectif_initial_zero_interdit():
    with pytest.raises(ValidationError):
        Probleme(effectif_initial=0, effectif_final=3, minima_mensuels=[3, 4])


def test_minima_negatif_interdit():
    with pytest.raises(ValidationError):
        Probleme(effectif_initial=3, effectif_final=3, minima_mensuels=[-1, 4])


def test_minima_vides_interdits():
    with pytest.raises(ValidationError):
        Probleme(effectif_initial=3, effectif_final=3, minima_mensuels=[])