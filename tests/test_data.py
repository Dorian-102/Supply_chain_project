"""Tests du module data."""

import pytest
from pydantic import ValidationError
from scr.data import Probleme, PROBLEME_EXEMPLE


def test_probleme_exemple_valide():
    assert PROBLEME_EXEMPLE.effectif_initial == 3
    assert PROBLEME_EXEMPLE.effectif_final == 3
    assert PROBLEME_EXEMPLE.minima_mensuels == [3, 4, 6, 7, 4, 6, 2]