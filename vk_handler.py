


def like_on_page(link):



def vk_task_manager(task_list):
    for task in task_list:
        if task.find("странице") != -1:
            like_on_page(task[task.find("href=")+5:task.find(">")])
        if task.find("друзья") != -1:
            add_to_friends(task[task.find("href=")+5:task.find(">")])
        if task.find("сообщество") != -1:
            join_group(task[task.find("href=")+5:task.find(">")])
        #TODO
        #more options

