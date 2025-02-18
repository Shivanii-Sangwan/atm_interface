Overview

  The ATM Interface is a simple Python-based console application that simulates an ATM system. It allows users to authenticate, check their balance, withdraw money, deposit funds, and transfer money to another account.

Features:
  >User authentication with a predefined card number and PIN.
  >Check account balance.
  >Withdraw money with sufficient funds.
  >Deposit money into the account.
  >Transfer money to another card.
  >Simple menu-driven interface.

Technologies Used:
    Python

Installation and Usage:
1. Prerequisites:
  Ensure you have Python 3.x installed on your system.

2. Running the Application
    Clone or download the script.

    Open a terminal or command prompt in the script's directory.

    Run the script using:

       python atm_interface.py
  
    Follow the on-screen prompts to interact with the ATM system.

Usage Instructions:

1. Enter your card number and PIN to authenticate.

   Default credentials:

       Card Number: 1234-5678-9012-3456
        PIN: 1234

2. After successful authentication, choose an option from the menu:
   
    >Check Balance: View your account balance.
   
    >Withdraw Money: Enter an amount to withdraw (if sufficient funds are available).
   
    >Deposit Money: Enter an amount to deposit into your account.
   
    >Transfer Money: Enter the recipient's card number and amount to transfer.
   
    >Exit: Quit the application.

Example Interaction:

    Welcome to Advanced ATM Interface!
    Enter your card number: 1234-5678-9012-3456
    Enter your PIN: 1234
    Authentication successful!
  
    Menu:
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Transfer
    5. Exit
    Enter your choice: 1
    1000.0

Limitations:
  >Currently, authentication is hardcoded for a single user.

  >No persistent data storage (balance resets on restart).

  >Simple validation checks, but no advanced security measures.

Future Enhancements:
  >Implement a database for user accounts and transactions.

  >Add support for multiple users with unique credentials.
  >Improve security with encrypted PIN storage.
  >Implement a graphical user interface (GUI) for better usability.

License

  This project is open-source and free to use.
  Feel free to contribute or modify the project as needed!
