import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestElements(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def a_redirect_banner(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//a[@href='https://www.toolsqa.com/selenium-training/']/img[@alt='Selenium Online Training']").click() # isi email
        time.sleep(3)
        
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        get_url = browser.current_url
        print("The current url is:",get_url)
        self.assertEqual((get_url), 'https://www.toolsqa.com/selenium-training/')

    def b_submit_textbox(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/text-box") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='userName']").send_keys("Arini") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='userEmail']").send_keys("pqa@gmail.com") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//textarea[@id='currentAddress']").send_keys("Jl. rumah no 1") 
        time.sleep(1)
        
        browser.find_element(By.ID,"submit").click() # 
        time.sleep(1)

        output_box = browser.find_element(By.ID,"output")

        # validasi
        response_data_name = output_box.find_element(By.ID,"name").text
        response_data_email = output_box.find_element(By.ID,"email").text
        response_data_currentAddress = output_box.find_element(By.ID,"currentAddress").text

        self.assertEqual(response_data_name, 'Name:Arini')
        self.assertEqual(response_data_email, 'Email:pqa@gmail.com')
        self.assertEqual(response_data_currentAddress, 'Current Address :Jl. rumah no 1')

    
    def c_add_webTable(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/webtables") # buka situs
        time.sleep(1)

        # rowSizeBefore = len(bodyTable)
        browser.find_element(By.XPATH,"/html//button[@id='addNewRecordButton']").click()
        time.sleep(1)

        # for handle in browser.window_handles:
        #     new_window = browser.switch_t(handle)

        browser.find_element(By.XPATH,"/html//input[@id='firstName']").send_keys("Arini") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='lastName']").send_keys("Dian") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='userEmail']").send_keys("pqa@gmail.com") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='age']").send_keys("25") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='salary']").send_keys("1000") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='department']").send_keys("PQA") 
        time.sleep(1)

        browser.find_element(By.ID,"submit").click() # 
        time.sleep(1)

        colFirtName = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[1]").text
        colLastName = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[2]").text
        colAge = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[3]").text
        colEmail = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[4]").text
        colSalary = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[5]").text
        colDepartment = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[4]/div[@role='row']/div[6]").text

        # validasi
        self.assertEqual(colFirtName, 'Arini')
        self.assertEqual(colLastName, 'Dian')
        self.assertEqual(colAge, '25')
        self.assertEqual(colEmail, 'pqa@gmail.com')
        self.assertEqual(colSalary, '1000')
        self.assertEqual(colDepartment, 'PQA')

    def d_delete_webTable(self): 

        def cek_sizeTable() :
            odd_row = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div/div[@class='rt-tr -odd']")
            even_row = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div/div[@class='rt-tr -even']")
            return len(odd_row)+len(even_row)

        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/webtables") # buka situs
        #cek size table before
        table_size_before = cek_sizeTable()
        print('size table before',table_size_before)
        #delete data
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[1]/div[@role='row']/div[7]//span[@title='Delete']").click()
        #cek size table after
        table_size_after = cek_sizeTable()
        print('check table size nya sudah berkurang')
        print('table size after ',table_size_after)
        self.assertEqual(table_size_after,table_size_before-1)

        # for j in range(7) :
        #     value = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='body-height']//div[@role='grid']/div[@class='rt-tbody']/div[3]/div[@role='row']/div["+str(j+1)+"]").text
        #     print('check value sudah kosong after delete')
        #     self.assertEqual(value, ' ')
    
    def test_e_checkbox(self) :
        browser = self.browser #buka web browser
        browser.get("https://demoqa.com/checkbox") # buka situs

        browser.find_element(By.XPATH,"//div[@id='tree-node']/ol/li/span/label/span[@class='rct-checkbox']").click()

        element = browser.find_elements(By.CSS_SELECTOR,"[for='tree-node-documents'] .rct-icon-check")

        element.get_attribute('svg')


    

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()