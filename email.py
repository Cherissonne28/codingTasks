### --- OOP Email Simulator --- ###

#  This programme uses OOP class methods along with dictionary, list and
# string methods to simulate an email programme.

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():
    # class variable

    email_address = " "
    subject_line = " "
    email_content = ""
    has_been_read = False
# Declare the class variable, with default value, for emails. 
    def __init__(self, email_address, subject_line, email_content): 
            self.email_address = email_address
            self.subject_line = subject_line
            self.email_content = email_content
            has_been_read = False

    # Initialise the instance variables for emails.
email_one = Email("volunteering@nature.com", "Volunteer Application Received",\
                  "Your application to volunteer with us has been received.")
email_two = Email("administration@nature.com", "Application Accepted",\
    "Congratulations! Your application to volunteer with us has been accepted.")
email_three = Email("operations@nature.com", "Volunteer Schedule",\
    "Please find attached your volunteering schedule.")


    # Create the method to change 'has_been_read' emails from False to True.
@classmethod   
def mark_as_read(cls,has_been_read): 
            cls.has_been_read == True
           
def show_email_state(self): 
    while self.has_been_read == True: 
        return "An email about " + self.subject_line + " has been read."
    while self.has_been_read == False:
        return "An email about " + self.subject_line + " is unread."

def un_read_emails(): 
    print(show_email_state(email_one))
    print(show_email_state(email_two))
    print(show_email_state(email_three))


    # --- Lists --- #
    # Initialise an empty list to store the email objects.
inbox = []
    # Using dictionary methods to organize the email sections.
email_one_object = {'Address':email_one.email_address, 
                    'Subject':email_one.subject_line, 
                    'Content':email_one.email_content}
email_two_object = {'Address':email_two.email_address,
                    'Subject':email_two.subject_line, 
                    'Content':email_two.email_content}
email_three_object = {'Address':email_three.email_address, 
                    'Subject':email_three.subject_line, 
                    'Content':email_three.email_content}

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    if email_one.has_been_read == False:
        inbox.append(email_one_object)
    if email_two.has_been_read == False:
        inbox.append(email_two_object)
    if email_three.has_been_read == False:
        inbox.append(email_three_object)


# Create a function which prints the email’s subject_line, along with a corresponding number.

def list_emails(): 
    sub_list = []
    for item in inbox: 
        j = (item['Subject'])
        k = "".join(j)
        sub_list.append(k)
        
    for index, item in enumerate(sub_list):
        print(f"{index} {item}")

    
# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.    

def read_email():
    chosen_email = (inbox[idx])
    for key in chosen_email.keys(): 
        print(key, ":", f"{chosen_email[key]}")
    
    if idx == 0: 
        print(f">The email from {email_one.email_address} has been read.")
        email_one.has_been_read = True
        
    elif idx == 1: 
        email_two.has_been_read = True
        print(f">The email from {email_two.email_address} has been read.")
    elif idx == 2: 
        email_three.has_been_read = True
        print(f">The email from {email_three.email_address} has been read.")
    else: 
        print("You seem to have mistyped.")
 
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        list_emails()
        idx = int(input("Please enter the email number you want to read: "))
        read_email()
                
    elif user_choice == 2:
        un_read_emails()
            
    elif user_choice == 3:
        print("Thank you, goodbye")
        exit()
    
    else:
        print("Oops - incorrect input.")
