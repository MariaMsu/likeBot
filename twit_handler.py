from driver import driver
from time import sleep


def subscribe_account(link):
    try:
        driver.get(link)
        #TODO
        print("a")
        button = driver.find_element_by_xpath("//*[text()='Follow']")
        print("b")
        button.click()
        print("c")
        sleep(1)
    except:
        pass


def retweet_post(link):
    driver.get(link)
    sleep(3)
    # button = driver.find_elements_by_xpath(
    #     "/html/body/div[45]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[6]/div[2]/div[2]/button[1]")
    button = driver.find_elements_by_xpath('//*[@data-modal="ProfileTweet-retweet"]')
    button.click()
    button = driver.find_elements_by_xpath("/html/body/div[24]/div/div[2]/form/div[2]/div[3]/button")
    button.click()


def twit_task_manager(task_list):
    for task in task_list:
        if task.find("аккаунт") != -1:
            print("29, twit")
            subscribe_account(task[task.find("href=") + 6:task.find(">") - 1])


# subscribe_account("https://twitter.com/RostecRussia")
# subscribe_account("https://www.google.ru")
# retweet_post("https://twitter.com/love2chiitan/status/971246677733642240")
# driver.get("https://www.google.ru")
