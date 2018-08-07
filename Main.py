from pyvirtualdisplay import Display
from selenium import webdriver
from Log_in import *
import re
from time import sleep # this should go at the top of the file



find_tasks(task_list):
    vk_tasks, gplus_tasks, insta_tasks = [], [], []
    while task in task_list:
        if task.find("https://vk.com") != -1:
            vk_tasks.append(task)
        elif task.find("https://www.instagram.com") != -1:
            insta_tasks.append(task)
        elif task.find("https://plus.google.com") != -1:
            gplus_tasks.append(task)

    if vk_tasks:
        vk_handler(vk_tasks)
    if gplus_tasks:
        gplus_handler(gplus_tasks)
    if insta_tasks:
        insta_handler(insta_tasks)

        


driver = webdriver.Firefox() # webdriver init


display = Display(visible=1, size=[800, 800])
display.start()
target_login(driver)
# vk_login(driver)
driver.get("https://vktarget.ru/list/")

sleep(5) # ВАЖНО
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
#TODO:
print (html)


task_list = re.findall(r'<a rel="nofollow noopener" data-bind="url" target="_blank" href=".{1,128}</a>', html)
#TODO:
print(task_list)