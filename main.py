import json
from time import sleep
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


class RobotAuto:
    def proceed_to_unsafe(self):
        self.driver.find_element(By.XPATH, "//*[@id='details-button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#proceed-link").click()

    def acessa(self, url):
        self.driver.get(url)

    def autentica(self):

        with open("credentials.json", "r") as f:
            credentials = json.load(f)

            username = self.driver.find_element(By.CSS_SELECTOR, "#username")
            username.send_keys(credentials['username'])
            passwd = self.driver.find_element(By.CSS_SELECTOR, "#password")
            passwd.send_keys(credentials['passwd'])

            sleep(10)

            self.driver.find_element(By.CSS_SELECTOR, "#btn-submit").click()

    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()

        self.options.add_argument(
            r"user-data-dir=C:\Users\domje\PycharmProjects\robot_get\robot-get\Perfil")
        # self.options.add_argument("--profile-directory=Profile 1")

        self.driver = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )


if __name__ == '__main__':
    # ABRE O ARQUIVO CREDENTIALS E RECUPERA AS CREDENCIAIS DO GET

    print("Acessing get...")
    robot = RobotAuto()
    robot.acessa("https://somesitethatrequiresauthentication.com")
    # robot.proceed_to_unsafe()

    robot.autentica()
    #
    sleep(10)
    # CODIGO DE AUTENTICADOR 2FA
    robot.driver.find_element(By.NAME, "_eventId_submit").click()

    robot.proceed_to_unsafe()

    select = Select(robot.driver.find_element(By.ID, 'domains'))
    select.select_by_value("UO:01.500.1.CGRD")

    robot.driver.find_element(
        By.CSS_SELECTOR, "#formTarefas\:btCriarTarefa").click()
    robot.driver.find_element(
        By.CSS_SELECTOR, "#formNovaTarefa\:servicoBusca_input").send_keys("admissi")
    robot.driver.find_element(By.XPATH,
                              "//*[@id='formNovaTarefa:servicoBusca_panel']/table/tbody/tr[2]/td/text()").click()

    robot.driver.quit()
