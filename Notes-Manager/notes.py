def back_to_menu():
    choice = input( "\nDO YOU WANT TO GO BACK TO THE MENU? (YES/NO): ").strip().upper()
    return choice == "YES"


print("\n----- NOTES MANAGER -----\n")

while True:

    menu = input(
        "WHICH ACTION DO YOU WANT TO PERFORM ON NOTES?\n"
        "1. ADD NOTE\n"
        "2. VIEW NOTES\n"
        "3. SEARCH NOTE\n"
        "4. DELETE NOTE\n"
        "5. CLEAR ALL NOTES\n"
        "6. EXIT\n"
        "ENTER YOUR CHOICE HERE: ").strip().upper()

    # ---------------- ADD NOTE ---------------- #

    if menu in ["1", "ADD NOTE"]:
            while True:
                
              add_note = input("\nTYPE THE NOTE HERE: ")

              with open("notes.txt", "a") as file:
                  file.write(add_note + "\n")
                  print("Note Added Succesfully! ")

              again = input("ADD ANOTHER NOTE? (YES/NO) ").strip().upper()
              if again == "NO":
                  break
            
            if not back_to_menu():
                print("Thankyou for using Notes Manager! ")
                break

    # ---------------- VIEW NOTES ---------------- #

    elif menu in ["2", "VIEW NOTES"]:
        with open("notes.txt", "r") as file:
            notes = file.read()

            if notes:
                print("\n----- YOUR NOTES -----")
                print(notes)

            else:
                print("No notes available.")

            if not back_to_menu():
              print("Thankyou for using Notes Manager! ")
              break


    # ---------------- SEARCH NOTE ---------------- #

    elif menu in ["3", "SEARCH NOTE"]:
        while True:
            
          with open("notes.txt", "r") as file:
              notes = file.readlines()

          search = input("Enter text to search: ").strip()
          found = False

          for note in notes:
              if search.lower() in note.lower():
                  print("Note found:", note.strip() + "\n")
                  found = True

          if not found:
              print("Note not found.")

          again = input("SEARCH ANOTHER NOTE? (YES/NO) ").strip().upper()
          if again == "NO":
              break

        if not back_to_menu():
          print("Thank you for using Notes Manager! ")
          break

    # ---------------- DELETE NOTE ---------------- #

    elif menu in ["4", "DELETE NOTE"]:
        while True:
            
          with open("notes.txt", "r") as file:
              notes = file.readlines()
            
              for index, note in enumerate(notes, start = 1):
                  print(index, note.strip())
            
              choice = int(input("\nWhich Note Do You Want to Delete? Select the Number: "))
              deleted = notes.pop(choice -1)
              print(f'{deleted.strip()}, Deleted Succesfully!')

              with open("notes.txt", "w") as file:
                for note in notes:
                  file.write(note)
                
              print("UPDATED NOTES ARE: ")
              for note in notes:
                  print(note.strip())

              again = input("DELETE ANOTHER NOTE? (YES/NO) ").strip().upper()
              if again == "NO":
                  break

        if not back_to_menu():
          print("ThankYou For Using Notes Manager! ")
          break
            

    # ---------------- CLEAR NOTES ---------------- #

    elif menu in ["5", "CLEAR ALL NOTES"]:
        ask = input("ARE YOU SURE ? (YES/NO) ").strip().upper()
        
        if ask == "YES":
            with open("notes.txt", "w") as file:
                file.write("")
                print("ALL NOTES CLEARED SUCCESSFULLY! ")
        
        else:
          print("OPERATION CANCELLED ")

        if not back_to_menu():
          print("ThankYou For Using Notes Manager! ")
          break
        

    # ---------------- EXIT ---------------- #

    elif menu in ["6", "EXIT"]:
        print("Thank you for using Notes Manager.")
        break

    else:
        print("Invalid Choice.")