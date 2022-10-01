
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By # Very important to import this
from time import sleep

from config import email,pssword
browser = webdriver.Chrome()


browser.get("http://www.facebook.com")

tofill1 = browser.find_element(by="id",value="email")
tofill1.send_keys(email)


tofill2 = browser.find_element(by="id",value="pass")
tofill2.send_keys(pssword)


# sugnup = browser.find_element(by="name",value='login')
# sugnup.click()


bottona= browser.find_element(By.XPATH, '//button[text()="Se connecter"]')
bottona.click()


sleep(10)
print("done")


# # qi72231t n3hqoq4p r86q59rh b3qcqh3k fq87ekyn fsf7x5fv s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk cr00lzj9 rn8ck1ys s3jn8y49 f14ij5to l3ldwz01 icdlwmnq i85zmo3j qmqpeqxj e7u6y3za qwcclf47 nmlomj2f frfouenu bonavkto djs4p424 r7bn319e bdao358l alzwoclg jcxyg2ei srn514ro oxkhqvkx rl78xhln nch0832m om3e55n1 nq2b4knc bis24fgy a5wdgl2o

























