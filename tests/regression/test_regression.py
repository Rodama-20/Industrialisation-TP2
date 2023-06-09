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
