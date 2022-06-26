#Coded By : UCHIT N M
#Mentor : SUMANTH L

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



from_country = input("Source Country : ")
to_country = input("Required Country : ")

orgin_money = int(input("Enter the amount from the Source Country : "))


options = Options() # to surpress opening of the browser
options.headless = True

# website source

website = f"https://www.google.com/search?q={from_country}currencyto{to_country}currency"

# driver path

path = "<your driver path>" 

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)

driver.get(website)

# value per unit currency of the orgin country
amount_value= driver.find_element(by="xpath",value='//div[@class="H07hi"]/table/tbody/tr/td/input[@class = "a61j6 vk_gy vk_sh Hg3mWc"]').get_attribute("value")

# final country currency name
suffix = driver.find_element(by="xpath",value='//div[@class = "dDoNo ikb4Bb gsrt GDBPqd"]/span[@class = "MWvIVe"]').get_attribute("data-name")


print(f"The value as per requird country : {float(amount_value)*2} {suffix}") # final value

driver.quit()

