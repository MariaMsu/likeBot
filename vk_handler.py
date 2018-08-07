from driver import driver


def like_on_page(link):
    driver.get(link)
    try:
        like = driver.find_element_by_xpath("//a[@onclick='return ajax.click(this, Like);']")
        like.click()
    except:
        pass


def join_group(link):  #work
    driver.get(link)
    try:
        join = driver.find_element_by_xpath("//a[@class='button wide_button']")
        join.click()
    except:
        pass


def add_to_friends(link):
    driver.get(link)
    try:
        add = driver.find_element_by_xpath("//a[@class='button wide_button acceptFriendBtn']")
        add.click()
    except:
        pass

def vk_task_manager(task_list):
    for task in task_list:
        task = task.replace("https://vk.com", "https://m.vk.com")
        if task.find("странице") != -1:
            like_on_page(task[task.find("href=") + 6:task.find(">")-1])
        if task.find("друзья") != -1:
            add_to_friends(task[task.find("href=") + 6:task.find(">")-1])
        if task.find("сообщество") != -1:
            join_group(task[task.find("href=") + 6:task.find(">")-1])
        # TODO
        # more options
