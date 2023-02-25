from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest

class StoreTestSuite(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.amazon.com")

    def tearDown(self):
        self.driver.quit()

#   Search by keyword and then select 3rd item found

    def test_search_and_find_fourth_element_from_list(self):
        self.driver.find_element(By.ID,'twotabsearchtextbox').send_keys("keyboard")
        self.driver.find_element(By.ID,'nav-search-submit-button').click()
        self.driver.find_element(By.XPATH,"//div[@data-index='3']//h2/a").click()
        result = self.driver.find_element(By.ID,"productTitle")
        self.assertTrue(result != "")
 
#   Find element between price range

    def test_search_between_range(self):
        value1 = 10000
        value2 = 30000
        self.driver.find_element(By.ID,'twotabsearchtextbox').send_keys("keyboard")
        self.driver.find_element(By.ID,'nav-search-submit-button').click()
        min_range = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'low-price')))
        max_range = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'high-price')))
        min_range.send_keys(value1)
        max_range.send_keys(value2)
        self.driver.find_element(By.CLASS_NAME,'a-button-input').click()

def main():
    suite = unittest.TestSuite()
    suite.addTest(StoreTestSuite('test_search_and_find_fourth_element_from_list'))
    suite.addTest(StoreTestSuite('test_search_between_range'))
    runner = unittest.TextTestRunner()
    runner.run(suite) 

if __name__ == '__main__':
    main()

