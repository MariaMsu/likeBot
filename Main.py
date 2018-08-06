from pyvirtualdisplay import Display
from Log_in import vk_Login

display = Display(visible=1, size=[800, 800])
display.start()
vk_Login()