from selenium import webdriver
from fixture.contacts import ContactsHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contacts = ContactsHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://addressbook:8080/")

    def destroy(self):
        self.wd.quit()
