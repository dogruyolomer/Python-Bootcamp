import json

def save_file(contact: dict, filename: str):
        with open(filename, "a") as f:
            json.dump(contact, f)

while True:
    
    name = input("What is your contact name? ")
    surname = input("What is your contact surname? ")
    phone = input("What is your contact's phone number? ")
    email = input("what is your contact's email? ")

    contact = {
        "name": name,
        "surname": surname,
        "phone":phone,
        "email":email
    }
    save_file(contact, "contact.json")

    print(f'{contact} is added succesfully.')

    q = input("Do you want to add more contact? (y/n) ").lower()
    if q == "y":
         continue
    else:
         print("Have a nice day!")
         break
    