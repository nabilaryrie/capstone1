from tabulate import tabulate

# Main database
pData = [
    {"Reg No.": "P0001", "Name": "Anya Kasim", "Age": 21, "Diagnosis": "Depression", "Hospital Status": "Admitted"},
    {"Reg No.": "P0002", "Name": "Nadia Budianto", "Age": 17, "Diagnosis": "Anxiety", "Hospital Status": "Consultation"},
    {"Reg No.": "P0003", "Name": "Brian Mamangkey", "Age": 50, "Diagnosis": "Tourette Syndrome", "Hospital Status": "Critical"},
    {"Reg No.": "P0069", "Name": "Sabrina Putribening", "Age": 25, "Diagnosis": "K-Pop Addiction", "Hospital Status": "Emergency"}
]

# Function to display data
def showData(): 
    print("Current Patient Data")
    print(tabulate(pData, headers="keys", tablefmt="simple"))

# Some extra function I'm playing around with
def ifContinue():
    print("Would you like to continue?")
    while True:
        ifCon = str(input("Y/N: ")).capitalize()
        if ifCon == 'Y':
            return showData()
        elif ifCon == 'N':
            print("Thank you for visiting our database!")
            ("\n")
        else:
            print("Please input the correct format.")

# add def hospital status
def hospitalStatus():
    print("\n")
    print("Select Hospital Status:")
    print("a. Consultation")
    print("b. Admitted")
    print("c. Discharged")
    print("d. Emergency")
    print("e. Surgery")
    print("f. Recovery")
    print("g. Outpatient")
    print("h. Critical")
    print("i. Transferred")
    print("j. Awaiting Diagnosis")
    print("\n")

# Main Loop and Menu
while True:
    print('''Welcome to Purwadhika Hospital Database!\n''')
    print('''Select Menu:
        1. Current Patient Data
        2. Add a new Patient
        3. Remove Patient
        4. Modify Patient Data
        5. Look for Specific Patient Data
        6. Exit Program\n''')

    menu = input('Please pick a number from the menu: ')

    try:
        menu = int(menu)

        # MENU TO SHOW DATA
        if menu == 1:
            showData()
            ifContinue()

        # MENU TO ADD DATA
        elif menu == 2:
            newReg =  "P" + str(input("Enter new patient registration number: "))
            if any(patient["Reg No."] == newReg for patient in pData):
                print("Patient with the given Registration No. already exists.")
                print("\n") # should I make a go back to main menu?
                continue
            else:
                newName = input("Enter new patient's Name: ").capitalize()
                newAge = (abs(int(input("Enter new patient's Age: "))))
                newDiag = str(input("Enter new patient's Diagnosis: ")).capitalize()
                
            # Displaying hospital status options
            hospitalStatus()

            # Hospital status input 
            status_choice = input("Enter the corresponding letter (a-j) for Hospital Status: ").lower()

            # Dict for statuses # maybe put as a function? 
            status_mapping = {
                'a': 'Consultation',
                'b': 'Admitted',
                'c': 'Discharged',
                'd': 'Emergency',
                'e': 'Surgery',
                'f': 'Recovery',
                'g': 'Outpatient', 
                'h': 'Critical',
                'i': 'Transferred',
                'j': 'Awaiting Diagnosis'
            }

            # declaring new status options
            newStat = status_mapping.get(status_choice)

            # Adding new patient data to database
            pData.append({"Reg No.": newReg, "Name": newName, "Age": newAge, "Diagnosis": newDiag, "Hospital Status": newStat})
            print("Patient added successfully!")
            showData()
            ifContinue()

        # MENU TO REMOVE DATA
        elif menu == 3:
            showData()
            remReg = input("Enter the Registration No. of the patient to remove: ").upper()  # Convert to capitals

            # Find the index of the patient with the specified registration number
            indexToRemove = None
            for i in range(len(pData)):
                if pData[i]["Reg No."].upper() == remReg:
                    del pData[i]
                    print(f"Patient with Registration No. {remReg.capitalize()} removed successfully.")
                    print("\n")
                    ifContinue()
                    break
            else:
                print(f"Patient with Registration No. {remReg.capitalize()} was not found.")

        # MENU TO MODIFY DATA 
        elif menu == 4:
            showData()
            regNoToModify = str(input("Enter the Registration No. of the patient to modify: ").capitalize())

            # Find the index of the patient with the specified registration number
            indexToModify = None
            for i in range(len(pData)):
                if pData[i]["Reg No."] == regNoToModify:
                    indexToModify = i
                    break

            # Modify the patient data if found
            if indexToModify is not None:
                print(f"Modifying data for patient with Registration No. {regNoToModify}")
                newAge = int(input("Enter the new age: "))
                newDiag = str(input("Enter new patient's Diagnosis: ")).capitalize()

                # Display hospital statuses? statii what is the plural for status
                hospitalStatus()

                # Picking hospital status from user
                status_choice = input("Enter the corresponding letter (a-b) for Hospital Status: ").lower()

                # Dict for hospital status
                status_mapping = {
                        'a': 'Consultation',
                        'b': 'Admitted',
                        'c': 'Discharged',
                        'd': 'Emergency',
                        'e': 'Surgery',
                        'f': 'Recovery',
                        'g': 'Outpatient',
                        'h': 'Critical',
                        'i': 'Transferred',
                        'j': 'Awaiting Diagnosis'
                    }
                
                # Receiving hospital status based on user choice
                newStatus = status_mapping.get(status_choice)

                # Update the patient data
                pData[indexToModify]["Age"] = newAge
                pData[indexToModify]["Diagnosis"] = newDiag
                pData[indexToModify]["Hospital Status"] = newStatus
                print("Patient data modified successfully.")
                print("\n")
                showData()
                print("\n")
                ifContinue()
            else:
                print(f"Patient with Registration No. {regNoToModify} not found.")

        # MENU TO LOOK UP PATIENT DATA
        elif menu == 5:
            regNoToSearch = input("Enter the Registration No. of the patient to search for: ").capitalize()

            # Find patient from 0
            found_patient = 0
            for patient in pData:
                if patient["Reg No."] == regNoToSearch:
                    found_patient = patient
                    break

            if found_patient != 0:
                # Display the patient's information
                print("Patient Data:")
                print(f"Registration No.: {found_patient['Reg No.']}")
                print(f"Name: {found_patient['Name']}")
                print(f"Age: {found_patient['Age']}")
                print(f"Diagnosis: {found_patient['Diagnosis']}")
                print(f"Hospital Status: {found_patient['Hospital Status']}")
                print("\n")
            else:
                print(f"Patient with Registration No. {regNoToSearch} was not found.")

        # MENU EXIT 
        elif menu == 6:
            print("Thank you for visiting our database. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        
