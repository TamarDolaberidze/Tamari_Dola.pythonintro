import random

from main import program_loop
from common import process_user_input
from db import sessions

def adminVerification():
    x = input("enter username: ")
    y = input("enter password: ")
    if x == "admin" and y == "admin":
        print("Welcome!")
    else:
        print("Invalid Passowrd, try again")
        return adminVerification()

def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    # TODO: session_id may be used already, need to check
    session_id = random.randint(1, 1000)
    used_ids = [s["session_id"] for s in sessions]

    while session_id in used_ids:
        session_id = random.randint(1, 1000)
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)

def removingSessions():
    print("Removing session")
    print("Enter the session ID")
    session_id = int(input("Session ID: "))
    for session in sessions:
        if session["session_id"] != session_id:
            print("No session ID found")
            return
        else:
            sessions.remove(session)
            print("Session removed successfully.")
            return



def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")

def edit_session():
    print("Editing session")
    session_id = int(input("Enter the session ID to edit: "))

    for session in sessions:
        if not sessions:
            print("No sessions found")
            return
        elif session["session_id"] == session_id:
            print(f"Editing session: {session}")
            
            new_length = int(input(f"Enter new room length (current: {session['room_length']}): "))
            new_width = int(input(f"Enter new room width (current: {session['room_width']}): "))
            
            session["room_length"] = new_length
            session["room_width"] = new_width
            session["capacity"] = new_length * new_width  
            
            print(f"Session updated successfully: {session}")
            return
    
    print(f"No session found with ID {session_id}.")

def admin_loop():
    greetings()
    adminVerification()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                removingSessions()
            case "3":
                add_session()
            case "4":
                edit_session()
            case _:
                print("Invalid input")

