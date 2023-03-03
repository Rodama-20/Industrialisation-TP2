"""
Unit tests for matrix_calculation.py package
"""
from tests.fixtures.matrix_calculation_fixtures import identity_matrix_3x3, ones_3x3
from src.matrix_calulation import mat_mul, identity, add


# NOTE
# pytest peut représenter les tests de 2 manières. Sous forme
# de fonction comme montré dans les autres fichiers ou sous
# forme de classe, comme montré ci-dessous. Les classes de tests
# permettent de mieux organiser son code et possèdent un set de
# méthodes (setup et teardown) qui s'executent avant, entre ou
# après les tests. C'est notamment très utilse pour configurer
# l'environnement de test.


def setup_module(module):
    """Called when this module is imported"""
    print("\n--> Setup module")


def teardown_module(module):
    """Called after all tests of this module are tested"""
    print("--> TearDown module")


class TestMatrixCalculation:
    """Test class for matrix_calculation.py"""

    @classmethod
    def setup_class(cls):
        """Called when this class is created"""
        print("--> Setup class")

    @classmethod
    def teardown_class(cls):
        """Called when this class is destroyed"""
        print("--> Teardown class")

    def setup_method(self, method):
        """Called before each unit test of this class"""
        print("--> Setup method")

    def teardown_method(self, method):
        """Called after each unit test of this class"""
        print("\n--> Teardown method")

    # TODO: implémenter les 3 tests ci-dessous

    def test_add(self, identity_matrix_3x3, ones_3x3):
        """Tests add function"""

        for i in range(len(identity_matrix_3x3)):
            for j in range(len(identity_matrix_3x3[i])):
                assert (
                    identity_matrix_3x3[i][j] + ones_3x3[i][j]
                    == add(identity_matrix_3x3, ones_3x3)[i][j]
                )

    def test_matmul(self, identity_matrix_3x3):
        """Tests  matmul function"""
        for i in range(len(identity_matrix_3x3)):
            for j in range(len(identity_matrix_3x3[i])):
                assert (
                    identity_matrix_3x3[i][j] * identity_matrix_3x3[i][j]
                    == mat_mul(identity_matrix_3x3, identity_matrix_3x3)[i][j]
                )

    def test_identity(self, identity_matrix_3x3):
        """Tests identity function"""
        for i in range(len(identity_matrix_3x3)):
            for j in range(len(identity_matrix_3x3[i])):
                assert identity_matrix_3x3[i][j] == identity(3)[i][j]
