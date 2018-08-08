from driver import driver
from time import sleep


def subscribe_account(link):
    try:
        driver.get(link)
        sleep(2)
        try:
            button = driver.find_element_by_xpath("//*[text()='Follow']")
        except:
            button = driver.find_element_by_xpath("//*[text()='Читать']")
        button.click()
        sleep(1)
    except:
        pass


def retweet_post(link):
    driver.get(link)
    button = driver.find_elements_by_xpath('//button[@data-modal="ProfileTweet-retweet"]')
    button[0].click()
    button = driver.find_elements_by_xpath("/html/body/div[24]/div/div[2]/form/div[2]/div[3]/button")
    button[0].click()


def twit_task_manager(task_list):
    for task in task_list:
        if task.find("аккаунт") != -1:
            subscribe_account(task[task.find("href=") + 6:task.find(">") - 1])
        if task.find("запись") != -1:
            retweet_post(task[task.find("href=") + 6:task.find(">") - 1])
