import re

from more_itertools import strip

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_name(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def select_contact_by_name(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type_contact_text("firstname", contact.firstname)
        self.type_contact_text("lastname", contact.lastname)
        self.type_contact_text("address", contact.address)
        self.type_contact_text("home", contact.homephone)
        self.type_contact_text("mobile", contact.mobile)
        self.type_contact_text("work", contact.workphone)
        self.type_contact_text("phone2", contact.secondaryphone)
        self.type_contact_text("fax", contact.fax)
        self.type_contact_text("email", contact.email)
        self.type_contact_text("email2", contact.email2)
        self.type_contact_text("email3", contact.email3)
        self.type_contact_text("homepage", contact.homepage)

    def type_contact_text(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
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
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = re.sub("\n", " ", cells[3].text)
                all_e_mails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = re.sub("\n", "", cells[5].text)
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_e_mails_from_home_page=all_e_mails))
        return list(self.contact_cache)

        # alternative for text from cells
        #
        # for element in wd.find_elements_by_name("entry"):
        #     contact = []
        #     for cell in element.find_elements_by_tag_name("td"):
        #         text = cell.text
        #         contact.append(text)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value").strip()
        lastname = wd.find_element_by_name("lastname").get_attribute("value").strip()
        address = ' '.join(wd.find_element_by_name("address").get_attribute("value").split())
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value").strip()
        workphone = wd.find_element_by_name("work").get_attribute("value").strip()
        mobile = wd.find_element_by_name("mobile").get_attribute("value").strip()
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value").strip()
        email = wd.find_element_by_name("email").get_attribute("value").strip()
        email2 = wd.find_element_by_name("email2").get_attribute("value").strip()
        email3 = wd.find_element_by_name("email3").get_attribute("value").strip()
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address, homephone=homephone, workphone=workphone,
                       mobile=mobile, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone,
                       secondaryphone=secondaryphone)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None