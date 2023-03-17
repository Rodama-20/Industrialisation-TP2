from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class TestSeleniumFunctional:
    """Functional tests class using selenium"""

    # Implémenter la méthode test_get_research_assistants qui réalise les actions suivantes:
    # - Ouvrir Firefox
    # - Se rendre sur la page www.he-arc.ch
    # - Accepter les cookies
    # - Cliquer sur le bouton "Ra&D"
    # - Cliquer sur le bouton "Domaines de compétences"
    # - Ouvrir la liste "Ingénierie"
    # - Cliquer sur le groupe de compétence "Analyse de données"
    # - Ecrire le nom de chaque professeurs (section "Professeur-e-s" de la page) dans la console

    # Les 3 premières étapes sont déjà implémentées pour vous, il suffit de décommenter les lignes.

    def test_get_teachers(self):
        """Opens the He-Arc website and prints the list of teachers from the 'Analyse de données' competence group."""

        # Loads Geckodriver
        browser = webdriver.Firefox(
            service=Service(executable_path=GeckoDriverManager().install())
        )

        # Opens HE-Arc website.
        browser.get("https://www.he-arc.ch")

        # Accept cookies
        cookies_button = browser.find_element(By.ID, "axeptio_btn_acceptAll")
        cookies_button.click()

        ##### YOUR CODE HERE #####

        ra_d_button = browser.find_element(By.ID, "w-dropdown-toggle-3")
        ra_d_button.click()

        competence_button = browser.find_element(
            By.LINK_TEXT, "Domaines de compétences"
        )
        competence_button.click()

        engineering_button = browser.find_element(
            By.ID, "accordion-block_619259e970051"
        )
        engineering_button.click()

        data_analysis_button = browser.find_element(
            By.PARTIAL_LINK_TEXT, "Analyse de données"
        )
        data_analysis_button.click()

        professors = browser.find_elements(
            By.XPATH,
            "/html/body/main/article/section[1]/div[2]/div[1]/div/div[3]/ul[*]/li[*]/a/div[*]/h3",
        )
        for prof in professors:
            print(prof.text)

        ##########################

        # Close Geckodriver
        browser.quit()
