#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)
    
    class Meta:
        database = db
        

def initialize():
    '''Create the database and the table if they don't exist'''
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu_loop():
    '''Show the menu'''
    #Establishes a placeholder for the choice input
    choice = None
    
    #q provides an easy way to exit the application
    while choice != 'q':
        clear()
        #prompt for action, provide easy way to exit
        print("Please enter an action. Enter 'q' to quit.")
        #prints out the shorcut for each action
        #the value for each key is a function
        #__doc__ prints docstring for each function to show action
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print("----------------------------")
        choice = input('Action:').lower().strip()
        print("----------------------------")
        
        #if input is valid, performs the operation
        if choice in menu:
            clear()
            menu[choice]()
              

def add_entry():
    '''Add and entry'''
    #prints instructions for EOF sequence
    print("Enter your entry. When you are finished, please hit `return` followed by `ctrl+d`.")
    #reads in the user input data
    data = sys.stdin.read().strip()
    
    #if something was entered
    if data:
        #so long as they don't say 'n' anything will work
        if input('Save entry? [y/n]').lower() != 'n':
            #write to the database
            Entry.create(content = data)
            print("Saved successfully!")
    
    
def view_entries(search_query=None):
    '''View previous entries'''
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    was_deleted = False
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        if was_deleted == True:
            print('***')
            print("Your entry was deleted successfully!")
            print('***')
        was_deleted = False
        print(timestamp)
        print('')
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp))
        print('n) next entry')
        print('q) return to main menu')
        print('d) delete entry')
        
        next_action = input('Action: ').lower().strip()
        
        if next_action == 'q':
            break
            
        elif next_action == 'd':
            #if input matches criteria, calls delete_entry function
            #maintains navigation of entries
            delete_entry(entry)
            was_deleted = True
    

def search_entries():
    '''Search entries for a certain string'''
    #calls on the searching function and fulfills optional criteria for searching
    view_entries(input('Search query: '))
    
def delete_entry(entry):
    '''Delete an entry'''
    if input("Are you sure you want to delete this? [y/n]") == 'y':
        entry.delete_instance()

menu  = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
    ])

if __name__ == '__main__':
    initialize()
    menu_loop()
    