from decorator import input_error

@input_error
def add_contact(args, contacts):
        if len(args) !=2:
             raise ValueError
        name, phone = args
        contacts[name] = phone
        return "Contact added."

    
@input_error
def change_contact (args, contacts):
        if len(args) !=2:
             raise ValueError
        name, phone = args 
        if name not in contacts:
            raise KeyError
        contacts[name] = phone
        return "Contact updated."
    

@input_error
def show_phone(args, contacts):
        if len(args) !=1:
             raise ValueError("Please provide the required argument for the command.")
        name = args[0]
        if name not in contacts:
            raise KeyError
        return contacts[name]
    

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved!"
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])