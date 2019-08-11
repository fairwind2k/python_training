from model.contact import Contact


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php?id=") and len(wd.find_elements_by_name("update")) > 0):
            wd.get("http://addressbook:8080/edit.php")

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # create new contact
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook:8080/") and len(wd.find_elements_by_name("searchstring")) >0 ):
            wd.get("http://addressbook:8080/")

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type_contact_text("firstname", contact.firstname)
        self.type_contact_text("lastname", contact.lastname)
        self.type_contact_text("address", contact.address)
        self.type_contact_text("home", contact.home)
        self.type_contact_text("mobile", contact.mobile)
        self.type_contact_text("work", contact.work)
        self.type_contact_text("fax", contact.fax)
        self.type_contact_text("email", contact.email)
        self.type_contact_text("email2", contact.email2)
        self.type_contact_text("homepage", contact.homepage)

    def type_contact_text(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    # def edit_contact(self, contact):
    #     wd = self.app.wd
    #     self.open_home_page()
    #     # edition
    #     wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
    #     self.fill_contact_form(contact)
    #     # submit update
    #     wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
    #     self.return_to_home_page()

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                contact = []
                for cell in element.find_elements_by_tag_name("td"):
                    text = cell.text
                    contact.append(text)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=contact[1], firstname=contact[2], id=id))
        return list(self.contact_cache)
