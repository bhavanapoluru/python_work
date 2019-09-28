contact={}
def add_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"contact has already exits...!!")
    else:
        contact[name]=ph_no
        print(" contact has added/saved sussucesfully...!!")
def display_contact():
    i=0
    for name,phone in contact.items():
        print(i+1,".name=",name,",phonenumber",phone)
        if(i>len(contact)):
            break
        i=i+1
def delete_contact(name,ph_no):
    if(name in contact.keys()):
        contact.pop(name)
        print("deleted")
    else:
        print("empty")
def update_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"already exits")
    else:
        contact[name]=ph_no
        contact.update()
        print("contact has updated sussucesfulli...!")
def search_contact(ph_no):
    if(ph_no in contact.values()):
        print("contact has exit")
    else:
        print("no contact exit")
  