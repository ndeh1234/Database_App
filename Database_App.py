import sqlite3 # Import the sqlite3 module

# Connect to database or opens database file
db = sqlite3.connect('chainsaw_juggling_records.db')

# Allows you to access columns by column name
db.row_factory = sqlite3.Row

# create cursor object to execute commands
cur = db.cursor()

# create a table called records if it doesn't exist
cur.execute('create table if not exists records(Name text, Country text, Num_Catches integer)')

# Function that prints menu selections and returns selection
def menu_print():
    print('1. Add Record')
    print('2. Search by Name')
    print('3. Update Catches')
    print('4. Delete Record')
    print('5. Exit')
    user_input = int(input('Enter the number of your selection. '))
    return user_input

# Function to add records to the database
def add_record():

    # Ask users for information about the person
    name = input("What is this person's name? ")
    country = input('What country is this person from? ')
    catches = int(input('How many catches did this person perform? '))

    # Populate the database
    # Use ? as placeholder for data that will filled in
    cur.execute('insert into records values(?, ?, ?)', (name, country, catches))

    # Save the changes
    db.commit()

# Function that searches records by name then prints the records
def search_record():

    # Taking inputs from users
    name = input('Who do you want to search for? ')

    cur.execute('select * from records where name = ?', (name,))
    records = cur.fetchall()
    for record in records:
        # printing record
        print('Name: ', record[0], ' Country: ', record[1], ' Catches: ', record[2])
        cur.close()


# function that updates number of catches in a record
def update_record():

    # Taking inputs from users
    name = input('Who do you want to update the number of catches for? ')
    catches = int(input('What is their new record of catches? '))
    # update the record
    cur.execute('update records set Num_Catches = ? where name = ?', (catches, name))

    # Save the changes
    db.commit()

# Function to delete a record
def delete_record():

    # Taking what to delete from users
    name = input("What is the name of the person who's record you want to delete? ")
    # Use WHERE clause to delete the record
    cur.execute('delete from records where name = ?', (name,))

    # Save the changes
    db.commit()

# Main function
def main():
    # displaying menu and getting the user inputs
    user_input = menu_print()
    # Looping over the menu
    while user_input != 5:
        if user_input == 1:
            add_record()
        elif user_input == 2:
            search_record()
        elif user_input == 3:
            update_record()
        elif user_input == 4:
            delete_record()

        user_input = menu_print()

    # Enter 5 to exit the program
    exit()


main() # Call main method
