import pytest
import pytest_regressions


def get_student():
    """Returns an object repesenting a student"""
    return {
        "Id": 0,
        "firstName": "John",
        "lastName": "Johnson",
        "address": {
            "street": "Espa. de l'Europe 11",
            "postalCode": 2000,
            "city": "Neuchâtel",
            "country": "Switzerland",
        },
        "grades": [
            {"courseId": 0, "courseName": "Math", "mark": 6.0},
            {"courseId": 0, "courseName": "Math", "mark": 3.8},
            {"courseId": 1, "courseName": "Physics", "mark": 5.1},
            {
                "courseId": 1,
                "courseName": "Physics",
                "mark": 5.5,
            },  # update by using pytest --force-regen
        ],
    }


def test_regression_student(data_regression):
    """Checks that get_student methods returns the same object structure"""
    data_regression.check(get_student())

    """
    La première execution n'a pas de référence, elle échoue mais crée la référence. Le test suivant réussi.
    Le test opéré est donc la comparaison entre une référence et l'object obtenu depuis la méthode testée

    La valeur de retour de la fonction est différente après le changement.
    Si cette valeur doit être la nouvelle référence il faut lancer pytest comme suit:
    pytest --force-regen
    le teste échoue à nouveau mais la référence est mise à jour et l'execution suivant réussira
    """
