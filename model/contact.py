from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobile=None,
                 workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 id=None, secondaryphone=None, all_phones_from_home_page=None, all_e_mails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_e_mails_from_home_page = all_e_mails_from_home_page
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "\n%s:%s:%s:%s;%s:%s:%s:%s;%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname , self.address, self.homephone,
                      self.mobile, self.workphone, self.fax, self.email, self.email2, self.email3, self.homepage,
                                                           self.secondaryphone, self.all_phones_from_home_page, self.all_e_mails_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
