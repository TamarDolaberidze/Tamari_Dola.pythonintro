Final Project - Parking Application

Project Overview
This is a vehicle parking application with both an administrator and a user interface, each with specific functionalities. The project includes three JSON files: one for user data, one for administrator login credentials, and one for parking zone details (users.json, adminPsw.json, parkingZones.json). The project logic is written in Python.

Description
On the user side, the application provides:

Registration and login functionalities.
Access to parking zones and car registration in available zones.
Removal of vehicles from parking zones after payment.
Checking the current balance and calculating charges for parked vehicles.
On the administrator side, the application enables:

Viewing, modifying, and deleting registered users.
Viewing parking zones with their status and charges.
Viewing parking history and managing parking zones (adding, editing, or deleting zones).
Technical Implementation
The project follows object-oriented programming principles, with each operation isolated in separate methods within classes. These functions are modular, allowing them to be imported or used in other files. The app uses data structures like lists, dictionaries, and tuples, and implements for and while loops, error handling, context managers, and JSON file handling. Interaction with users occurs through the command-line interface (CLI), and it uses modules like JSON, datetime, and getpass for functionality.

Application Flow
The main cycle of the application is controlled via the main() function, where users can register, log in, and interact with the parking system. The application is divided into several classes to handle different aspects of functionality, such as authentication, user management, parking zone management, and payment processing.

Classes and Methods

UserAuth: Manages user login, including three attempts for data entry.
User: Represents a user object, with attributes like user ID, username, password, and balance.
UserManager: Handles user registration, data saving, and retrieval.
UserFunctions: Provides user-facing functions like parking zone registration and balance checking.
ParkingPayment: Manages parking payments and updates user balances.
AdminAuth: Handles admin login and verifies credentials.
AdminMenu: Manages admin functionality, including user management, parking zone management, and viewing history.
Instructions for Running

Python version 3.8 or higher is required.
Run the file using the "Run Python File" command in the terminal.
No additional libraries are required.
