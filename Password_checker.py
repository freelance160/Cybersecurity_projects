import logging 

#Initiate logging function
logging.basicConfig(level=logging.INFO)

#new create password file
with open("passwords.txt", "w") as file:
    file.write("securepass\n")
    file.write("123456\n")
    file.write("password\n")
    file.write("myp@ssw0rd\n")
    file.write("guest\n")
    file.write("qwerty\n")

#Create custom function to check each password 
def password_quality_checker():
    logging.info("Program Started")

    #define weak passwords list
    predefined_weak_passwords = ["123456", "password", "123456789", "qwerty", "abc123"]
    try:
        with open("passwords.txt", "r") as file: #Open password file
           
            with open("report_file.txt", "w") as report_file: #Create new file to store results
                report_file.write("Weak Passwords found:\n")
                
                for line_number, line in enumerate(file, start=1):
                    password = line.strip()
                    
                    #Validation logic 
                    
                    if password in predefined_weak_passwords:
                            reason = "Predefined Weak Password"
                            report_file.write(f"Line {line_number}: {password} ({reason})\n")
                    elif len(password) < 8:
                            reason = "Shorter than 8 characters"
                            report_file.write(f"Line {line_number}: {password} ({reason})\n")
                    

                
                

    except FileNotFoundError:
        logging.error("File does not exist")    

#Run the program
password_quality_checker()