

from view.home import HomeView
from controller.home import HomeController


home_view = HomeView()
home_controller = HomeController(home_view)

home_view.mainloop()