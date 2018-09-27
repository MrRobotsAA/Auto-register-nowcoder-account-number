from selenium import webdriver
from validation import *
import os
import threading
import time

chrome_driver = r"D:\geckodriver.exe"
url = 'https://www.nowcoder.com/register?from=YQ318'
cycle = 43
o = 0
if __name__ == '__main__':
    for i in range(cycle):
        # 打开浏览器

        driver = webdriver.Firefox(executable_path=chrome_driver)
        driver.get(url)

        # 填写密码及重复密码
        driver.find_element_by_id('jsPasswordIpt').send_keys('nowcode')
        driver.find_element_by_id('jsPasswordIpt2').send_keys('nowcode')

        # 获取手机号码，并点击按钮，等待 5s
        number = get_phone()
        print(number)
        driver.find_element_by_id('jsEmailIpt').send_keys(number)
        time.sleep(2)
        driver.find_element_by_id('jsSendCaptcha').click()
        driver.close()
        time.sleep(30)
        print('睡完了')
       #print(get_validation('13484014247'))
       # 获取验证码
        validation = get_validation(number)[23:27]
        print(get_validation(number))
        print('验证码给你了')
        if validation:
            o = o+1
        print(validation)



        time.sleep(5)
        driver2 = webdriver.Firefox(executable_path=chrome_driver)
        driver2.get(url)
        # 填写密码及重复密码
        driver2.find_element_by_id('jsPasswordIpt').send_keys('newcode')
        driver2.find_element_by_id('jsPasswordIpt2').send_keys('newcode')
        driver2.find_element_by_id('jsEmailIpt').send_keys(number)
        driver2.find_element_by_id('jsCaptcha').send_keys(validation)
       # 提交
        driver2.find_element_by_id('jsRegisterBtn').click()
        time.sleep(2)
        driver2.close()
        print('当前已成功注册'+str(o)+'个')
        time.sleep(50)


