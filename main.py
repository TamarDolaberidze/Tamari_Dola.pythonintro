from admin import admin_loop
from common import process_user_input
from db import sessions

def list_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. my tickets")
    print("4. admin")
    return process_user_input()

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                print("Listing sessions")
            case "2":
                search_movie()
            case "3":
                print("Listing tickets")
            case "4":
                admin_loop()
            case _:
                print("Invalid input")

def main():
    greetings()
    program_loop()

def search_movie():
    print("Search Movie")
    movie = input("Enter the movie name to search: ").strip().lower()

    # Find matching sessions
    matching_sessions = [
        session for session in sessions if movie in session["film_name"].lower()
    ]

    if matching_sessions:
        for session in matching_sessions:
            print(
                f"Session ID: {session['session_id']}, "
                f"Film: {session['film_name']}, "
                f"Time: {session['start_time']}, "
                f"Room: {session['room_number']}, "
                f"Capacity: {session['capacity']}"
            )
    else:
        print("No matching movies found.")


if __name__ == "__main__":
    main()
