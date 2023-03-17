"""Locust test package"""
from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """Test class for Locust"""

    @task
    def home(self):
        """Tests the home page"""
        self.client.get("/fr/")

    # : implémenter 3 tests de plus
    #       Chaque test doit tester une route différente
    #       Chaque test doit être executé 2 fois plus de fois que le précédent.
    @task(2)
    def ag(self):
        """Test the subcription page"""
        self.client.get("/fr/abonnements-et-billets/abonnements/ag.html")

    @task(4)
    def night(self):
        """Test nidht train page"""
        self.client.get("/fr/loisirs-et-vacances/trains-excursions/train-de-nuit.html")

    @task(8)
    def bern(self):
        """Test bern station page"""
        self.client.get("/fr/gare-services/a-la-gare/gares/gare-de-berne.html")
