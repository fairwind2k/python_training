import string
import random
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="",
                      mobile="", workphone="", fax="", email="",
                      email2="", email3 ="", homepage="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
            homephone=random_string("homephone", 15), mobile=random_string("mobile", 15), workphone=random_string("workphone", 15),
            fax=random_string("fax", 15), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20),
            homepage=random_string("homepage", 15), secondaryphone=random_string("secondaryphone", 15)
            )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))