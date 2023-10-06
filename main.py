import pickle


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_disk(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_disk(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, request):
        results = []
        request = request.lower()
        for contact in self.contacts:
            if request in contact.name.lower() or request in contact.phone_number:
                results.append(contact)
        return results

    @staticmethod
    def valid_name(name):
        if not name.isalpha() or not name.istitle():
            raise ValueError("Incorrect name:( The name must contain only letters and begin with" +
                             " a capital letter." + " Please, try again.")

    @staticmethod
    def valid_phone_number(phone_number):
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValueError("Incorrect phone number:( The number must contain exactly 10 digits."
                             + " Please, try again.")


address_book = AddressBook()


address_book.load_from_disk('address_book.pkl')

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Exit")

    Choice = input("Select an option: ")

    if Choice == '1':
        while True:
            name = input("Please, enter a name: ")
            try:
                AddressBook.valid_name(name)
                break
            except ValueError as e:
                print(str(e))

        while True:
            phone_number = input("Please, enter your phone number: ")
            try:
                AddressBook.valid_phone_number(phone_number)
                break
            except ValueError as e:
                print(str(e))

        contact = Contact(name, phone_number)
        address_book.add_contact(contact)
        print("Contact was added!")

    elif Choice == '2':
        request = input("Please, enter request for search: ")
        results = address_book.search_contacts(request)
        if results:
            print("Search result:")
            for result in results:
                print(f"Name: {result.name}, Phone number: {result.phone_number}")
        else:
            print("Sorry. No contacts found.")

    elif Choice == '3':
        address_book.save_to_disk('address_book.pkl')
        print("Data saved. Exit the program.")
        break

    else:
        print("Unknown option. Please choose another.")