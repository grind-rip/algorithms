"""
Manacher's Algorithm
--------------------
"""

from src.manachers_algorithm import (
    augmentation_with_separator,
    expansion_around_centers,
    manachers_algorithm,
    palindromic_radii_array,
)


def test_expansion_around_centers():
    assert expansion_around_centers("noon") == "noon"
    assert expansion_around_centers("racecar") == "racecar"
    assert expansion_around_centers("abc") == "a"
    assert expansion_around_centers("") == ""


def test_augmentation_with_separator():
    assert augmentation_with_separator("noon") == "noon"
    assert augmentation_with_separator("racecar") == "racecar"
    assert augmentation_with_separator("abc") == "a"
    assert augmentation_with_separator("") == ""


def test_palindromic_radii_array():
    assert palindromic_radii_array("noon") == "noon"
    assert palindromic_radii_array("racecar") == "racecar"
    assert palindromic_radii_array("abc") == "a"
    assert palindromic_radii_array("") == ""


def test_manachers_algorithm():
    assert manachers_algorithm("noon") == "noon"
    assert manachers_algorithm("racecar") == "racecar"
    assert manachers_algorithm("abc") == "a"
    assert manachers_algorithm("") == ""
