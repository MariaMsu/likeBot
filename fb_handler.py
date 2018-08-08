from driver import driver
from time import sleep


def like_on_page(link):
    try:
        driver.get(link)
        page = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/button")
        page.click()
    except:
        pass


def fb_task_manager(task_list):
    for task in task_list:
        if task.find("странице") != -1:
            like_on_page(task[task.find("href=")+6:task.find(">")-1])



