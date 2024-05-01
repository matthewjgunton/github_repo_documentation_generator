## ./git_src/mjg422/project.java:
The provided code is a Java program that simulates a banking system. Here's a summary of the key features:

1. **User Authentication**: The program prompts the user to enter a valid username and password to access the database. If the credentials are invalid, an error message is displayed, and the user is prompted to try again.

2. **Main Menu**: After successful login, the program displays a main menu with various options: "C" for customer-related operations, "L" for location-related operations, "D" for debt-related operations, and "Q" to exit the program.

3. **Customer Operations**: When the user selects "C", the program allows them to access customer-related options, which are handled by the `Customer` class.

4. **Location Operations**: When the user selects "L", the program allows them to access location-related options, which are handled by the `Location` class.

5. **Debt Operations**: When the user selects "D", the program allows them to access debt-related options, which are handled by the `Debt` class.

6. **Help Menu**: The program provides a help menu that displays the available commands and their descriptions.

7. **Color Formatting**: The program uses ANSI escape codes to format the output with various colors, such as yellow for prompts, red for error messages, and green for welcome messages.

Overall, this program appears to be a simple banking system that allows users to manage customers, locations, and debts.


## ./git_src/mjg422/makefile:
The provided `makefile` is a build script for a Java project. It contains a single target, `dev`, which performs the following actions:

1. Compiles all the Java source files (`*.java`) using the `javac` command.
2. Creates a JAR (Java Archive) file named `mjg422.jar` using the `jar` command. The JAR file includes the compiled classes (`project.class`, `Database.class`, `Customer.class`, `Transaction.class`, `Location.class`, and `Debt.class`) and the `Manifest.txt` file.
3. Moves the created `mjg422.jar` file to the parent directory (`..`).

The `all` target is a placeholder for additional build tasks, but it currently just executes the `dev` target.


## ./git_src/mjg422/Transaction.java:
The provided Java code defines a `Transaction` class that handles various banking transactions for a customer. The class has the following functionality:

1. **Purchase Transaction**: Allows the customer to make a purchase using a debit or credit card, and checks if the account has enough funds or if the credit limit will be exceeded.
2. **Loan Transaction**: Allows the customer to take out a loan, either secured or unsecured, and deposits the loan amount into the customer's account.
3. **Loan Payment Transaction**: Allows the customer to pay down a loan by transferring funds from one of their accounts.
4. **Transfer Transaction**: Allows the customer to transfer funds between their own accounts.
5. **Withdrawal/Deposit Transaction**: Allows the customer to withdraw or deposit funds into one of their accounts.

The class also includes various utility methods to retrieve customer account information, check account balances, and display customer assets and debts. The code uses a `Database` object to interact with the underlying database and perform the necessary operations.

Overall, the `Transaction` class provides a comprehensive set of banking functionalities for a customer, allowing them to perform various financial transactions and manage their accounts effectively.


## ./git_src/mjg422/Manifest.txt:
The provided source code appears to be a `Manifest.txt` file, which is commonly used in Java-based projects to define the main entry point (i.e., the `Main-class`) and the classpath (i.e., the `Class-Path`) for the application.

In this specific case, the `Manifest.txt` file contains the following information:

1. **Main-class**: The main entry point of the application is set to `project`.
2. **Class-Path**: The classpath for the application includes the `ojdbc8.jar` library, which is likely a Java Database Connectivity (JDBC) driver for an Oracle database.

Based on this information, it can be inferred that this project is a Java application that likely interacts with an Oracle database using the `ojdbc8.jar` library.


## ./git_src/mjg422/Location.java:
Here's a summary of the provided Java source code in Markdown format:

```markdown
The `Location` class is part of a banking application and provides functionality to interact with location-related data stored in a database. The main features include:

1. **Options Menu**: Displays a menu that allows users to search for a location by ID or browse all available locations. Once a location is selected, the user can view various information about the location, such as metadata, debt, withdrawals, deposits, transfers, and create a new customer.

2. **Create Customer**: Provides a step-by-step process to create a new customer, including input validation for the customer's name and date of birth.

3. **Location Information**: Allows the user to view detailed information about a selected location, including its type (ATM or not) and various transaction data (debts, withdrawals, deposits, transfers) within a specified time frame.

4. **Utility Methods**: Includes helper methods for converting date strings, checking user input, and retrieving the current time.

The code uses a `Database` class (not provided in the source code) to interact with the underlying database and retrieve the necessary information. The application also utilizes various ANSI escape codes to format the console output.
```


## ./git_src/mjg422/Debt.java:
The provided code is a Java class called `Debt` that provides several functions to interact with a database and retrieve information related to customer debt. Here's a summary of the key functionalities:

1. **Options Menu**: The `options()` method presents a menu of options for the user to choose from, including:
   - Viewing debt by time frame
   - Viewing the total amount of debt
   - Viewing the average debt per customer
   - Viewing the payment due to the bank this month

2. **Debt by Time**: The `printDebtByTime()` method allows the user to view the loans and their associated amounts based on different time frames (week, month, six months, year).

3. **Average Debt per Customer**: The `printAverageCustomerDebt()` method calculates and displays the average debt per customer who has a loan.

4. **Total Debt**: The `printTotalDebt()` method retrieves and displays the total debt owed to the bank.

5. **Payment Due**: The `printPaymentDue()` method displays the payment due to the bank this month, both per customer and in total.

The class utilizes a `Database` object and a `Scanner` input to interact with the database and receive user input, respectively. The code also includes some ANSI color codes for formatting the output.


## ./git_src/mjg422/Database.java:
The provided code is a Java class called `Database` that provides functionality for interacting with an Oracle database. The class has the following key features:

1. **Constructor**: The constructor takes a username and password as input, and establishes a connection to the database using the provided credentials.

2. **Check Method**: This method takes a SQL query and an array of arguments, and executes the query. It ensures that only one row is affected by the query.

3. **Insert Method**: This method takes a SQL query and executes it, ensuring that only one row is affected.

4. **CheckExecute Method**: This method takes a SQL query and an array of arguments, and executes the query. It then formats the result set in a tabular format and returns it as a string.

5. **Execute Method**: This method takes a SQL query and executes it, formatting the result set in a tabular format and returning it as a string.

6. **FunctionCall Method**: This method takes a SQL function call query and executes it, handling any exceptions that may occur, such as a credit limit being reached.

The class provides a set of utility methods for interacting with an Oracle database, with a focus on handling exceptions and ensuring that the expected number of rows are affected by the executed queries.


## ./git_src/mjg422/Customer.java:
The provided code is a Java class named `Customer` that represents a customer in a banking system. The class has several methods that allow the user to interact with the customer's information and perform various banking-related tasks.

Here's a summary of the key functionalities:

1. **Options**: The `options()` method provides the main menu for interacting with the customer, including options to search for a customer, view their personal information, transaction history, accounts, debts, assets, and cards, as well as perform various transactions and account management tasks.

2. **Customer Information**: The class includes methods to print the customer's personal information, transaction history, accounts, debts, and assets.

3. **Card Management**: The `updateCustomerCard()` method allows the user to add a new debit or credit card for the customer, including setting the credit limit and interest rate for credit cards.

4. **Asset Management**: The `updateCustomerAssets()` method allows the user to add new assets to the customer's profile, including the asset type and value.

5. **Account Management**: The `addNewAccount()` method allows the user to open a new checking or savings account for the customer, including setting the initial deposit and interest rate.

6. **Utility Methods**: The class includes several utility methods, such as `checkNumber()`, `checkDouble()`, and `checkForSciNo()`, which are used for input validation and data processing.

Overall, the `Customer` class provides a comprehensive set of functionalities for managing customer information and interacting with the banking system.


## ./git_src/mjg422:
The provided documents describe a Java-based banking system project with the following key features:

1. **Project.java**: This is the main Java program that simulates a banking system. It includes functionalities for user authentication, a main menu with options for customer, location, and debt-related operations, and a help menu. The program uses ANSI escape codes to format the output with various colors.

2. **Makefile**: This is a build script that compiles the Java source files, creates a JAR (Java Archive) file named `mjg422.jar`, and moves the JAR file to the parent directory.

3. **Transaction.java**: This Java class handles various banking transactions for a customer, including purchase, loan, loan payment, transfer, withdrawal, and deposit. It interacts with a `Database` object to perform the necessary operations.

4. **Manifest.txt**: This file defines the main entry point (`project`) and the classpath (`ojdbc8.jar`) for the application, indicating that it is a Java application that interacts with an Oracle database using the JDBC driver.

Overall, this project appears to be a comprehensive banking system that allows users to manage customers, locations, and debts, and perform various financial transactions. The use of a makefile and a manifest file suggests that this project is part of a larger software development process with a focus on build automation and deployment.
Based on the provided documents, the following can be summarized:

1. **Manifest.txt**:
   - The `Manifest.txt` file defines the main entry point (`Main-class`) and the classpath (`Class-Path`) for a Java-based application.
   - The main entry point is set to `project`, and the classpath includes the `ojdbc8.jar` library, which is a JDBC driver for an Oracle database.
   - This suggests that the project is a Java application that interacts with an Oracle database.

2. **Location.java**:
   - The `Location` class is part of a banking application and provides functionality to interact with location-related data stored in a database.
   - The class includes an options menu to search for locations, view location details (metadata, transactions, etc.), and create new customers.
   - The code uses a `Database` class to interact with the underlying database and retrieve the necessary information.
   - The application also uses ANSI escape codes for formatting the console output.

3. **Debt.java**:
   - The `Debt` class provides functions to interact with a database and retrieve information related to customer debt.
   - The class includes an options menu to view debt by time frame, total debt, average debt per customer, and payment due to the bank.
   - The class utilizes a `Database` object and a `Scanner` input to interact with the database and receive user input, respectively.
   - The code also includes some ANSI color codes for formatting the output.

4. **Database.java**:
   - The `Database` class provides functionality for interacting with an Oracle database, including methods to execute SQL queries, handle exceptions, and format the result set.
   - The class has a constructor that takes a username and password to establish a connection to the database.
   - The class includes methods to check, insert, execute, and call database functions, ensuring that the expected number of rows are affected by the executed queries.

Overall, the provided source code appears to be part of a Java-based banking application that interacts with an Oracle database to manage location-related data, customer debt, and other related functionality.
The provided code consists of two Java classes:

1. **Database.java**:
   - The `Database` class provides functionality for interacting with an Oracle database.
   - It includes a constructor to establish a connection to the database using provided credentials.
   - The class has methods to execute SQL queries, handle exceptions, and format the result sets in a tabular format.
   - The key methods are `check()`, `insert()`, `checkExecute()`, `execute()`, and `functionCall()`.

2. **Customer.java**:
   - The `Customer` class represents a customer in a banking system.
   - It provides various methods for managing customer information and performing banking-related tasks.
   - The main features include:
     - `options()` method to display the main menu for interacting with the customer.
     - Methods to retrieve and update customer information, such as personal details, transaction history, accounts, debts, and assets.
     - Card management functionality to add new debit or credit cards.
     - Asset management functionality to add new assets to the customer's profile.
     - Account management functionality to open new checking or savings accounts.
   - The class also includes utility methods for input validation and data processing.

Overall, these two Java classes provide a comprehensive set of functionalities for interacting with an Oracle database and managing customer information in a banking system.


## ./git_src/SQL/withdrawaltx (1).sql:
The provided SQL script is a set of `INSERT INTO` statements that add transaction numbers ranging from 101 to 150 into the `withdrawaltx` table. This is likely a script used to populate a database with sample withdrawal transaction data for testing or demonstration purposes.

Here is the summary in markdown format:

```markdown
The SQL script inserts 50 rows into the `withdrawaltx` table, with `txnum` values ranging from 101 to 150. This is likely a script used to populate a database with sample withdrawal transaction data for testing or demonstration purposes.
```


## ./git_src/SQL/used_card (1).sql:
The provided SQL code is a series of `INSERT` statements that add records to a table called `used_card`. Each `INSERT` statement includes two values: `txnum` (transaction number) and `cardnum` (card number). The values for `txnum` range from 76 to 100, and the values for `cardnum` range from 1 to 25. This suggests that the code is used to populate the `used_card` table with information about transactions involving various credit/debit cards.

Summary:

1. The SQL code is a set of `INSERT` statements that add records to a table called `used_card`.
2. Each `INSERT` statement includes two values: `txnum` (transaction number) and `cardnum` (card number).
3. The `txnum` values range from 76 to 100, and the `cardnum` values range from 1 to 25.
4. The purpose of this code is to populate the `used_card` table with information about transactions involving various credit/debit cards.


## ./git_src/SQL/transfertx (2).sql:
The provided SQL script is used to insert a series of records into a table named `transfertx`. Each insert statement includes two values: `txnum` (a unique transaction number) and `destinationaccountnum` (the destination account number for the transaction).

The script inserts 50 records, with `txnum` values ranging from 151 to 200 and `destinationaccountnum` values ranging from 1 to 50. This suggests that this script is likely part of a larger system that handles financial transactions and account management.

Here's the summary in markdown format:

```markdown
The provided SQL script inserts 50 records into the `transfertx` table, with transaction numbers (`txnum`) ranging from 151 to 200 and destination account numbers (`destinationaccountnum`) ranging from 1 to 50. This script is likely part of a larger system that handles financial transactions and account management.
```


## ./git_src/SQL/transactions (2).sql:
The provided SQL script is used to insert 200 rows of transaction data into a table named `transactions`. Each row contains the following information:

- `txnum`: a unique transaction number
- `accountnum`: the account number associated with the transaction
- `amount`: the amount of the transaction

The first 150 rows are inserted with unique transaction numbers, account numbers, and amounts. The remaining 50 rows are inserted with a mix of new and previously used account numbers, and various transaction amounts.

The overall purpose of this script is to populate a transactions table with sample data that can be used for testing or analysis purposes.


## ./git_src/SQL/purchasetx (1).sql:
The provided SQL script inserts 25 records into the `purchasetx` table, with each record containing a unique `txnum` (transaction number) and a `vendor` name. The vendor names appear to be fictional company names, such as "Vipe", "Dabshots", "Skynoodle", and so on. This script is likely used to populate the `purchasetx` table with sample data for testing or demonstration purposes.


## ./git_src/SQL/owns (1).sql:
The provided SQL script is used to insert data into an "owns" table. The table has two columns: "assetnum" and "customerid". The script inserts 50 rows, where each row associates an asset number (1 to 50) with a corresponding customer ID (1 to 50).

This script is likely part of a larger database management system, where the "owns" table is used to track the relationship between customers and the assets they own.


## ./git_src/SQL/owes (4).sql:
This SQL script inserts 50 rows of data into the `owes` table, with each row containing a unique `loannum` value (ranging from 1 to 50) and a corresponding `customerid` value (also ranging from 1 to 50). This is likely used to populate a database with sample data for a loan management system, where each row represents a customer who owes a specific loan.

```
insert into owes (loannum, customerid) values (1, 1);
insert into owes (loannum, customerid) values (2, 2);
...
insert into owes (loannum, customerid) values (50, 50);
```


## ./git_src/SQL/occured (3).sql:
The provided SQL script is a series of `INSERT INTO` statements that populate the `occured` table with data. Each insert statement includes three values: `txnum` (a transaction number), `locationid` (a location identifier), and `utc_time` (a Unix timestamp representing the time of occurrence). The script inserts 200 rows of data into the `occured` table.

Summary:
- The script is designed to populate an `occured` table with transaction data.
- Each insert statement includes a transaction number, a location ID, and a Unix timestamp.
- A total of 200 rows are inserted into the `occured` table.


## ./git_src/SQL/location (1).sql:
This SQL script is used to insert data into a `location` table. The table contains the following columns:

- `state`: the state where the location is located
- `city`: the city where the location is located
- `zip`: the zip code of the location
- `locationid`: a unique identifier for the location
- `type`: the type of location, which can be either "ATM" or "Teller"

The script inserts 30 different locations, with 5 being ATMs and the remaining 25 being Tellers. The locations are spread across various states, including Florida, South Dakota, Ohio, California, North Carolina, Missouri, Maryland, Texas, Utah, Oklahoma, Pennsylvania, Nevada, New York, Virginia, Louisiana, North Dakota, and Maryland.

The script can be used to populate a database with location information for a financial institution or a similar organization.


## ./git_src/SQL/loantx (2).sql:
The provided SQL script is a simple script that inserts a series of records into a table named `loantx`. Each insert statement adds a new row to the table, with the `txnum` column being assigned a unique sequential value, and the `loannum` column being assigned a value that matches the `txnum`. This script appears to be used for populating a test or sample database with a set of loan transaction data.

Here's the summary in markdown format:

```markdown
The SQL script inserts 50 rows into the `loantx` table, where the `txnum` column is assigned a unique value from 1 to 50, and the `loannum` column is assigned the same value as the corresponding `txnum`. This script is likely used for populating a test or sample database with loan transaction data.
```


## ./git_src/SQL/loan (1).sql:
The provided SQL script creates 50 loan records in a `loan` table. Each record contains the following columns:

- `principal`: The original amount of the loan
- `balance`: The current outstanding balance of the loan
- `interest`: The interest rate of the loan
- `paymentdue`: The due date for the next payment
- `loannum`: A unique identifier for the loan

The script populates the table with random values for each of these columns, creating a diverse set of loan records.


## ./git_src/SQL/is_secured (2).sql:
The provided SQL script inserts 40 rows into a table named `is_secured`. Each row contains a `loannum` and an `assetnum` value, which are sequential integers from 1 to 40.

This script appears to be used for populating a test or sample database with data, likely for the purpose of testing or demonstrating functionality related to a loan and asset management system.

```markdown
The SQL script inserts 40 rows into the `is_secured` table, with the `loannum` and `assetnum` values ranging from 1 to 40. This is likely a script used for populating a test or sample database with data for a loan and asset management system.
```


## ./git_src/SQL/dropall.sql:
The provided SQL script is used to drop all the tables in the database schema. The script includes the following table drops:

1. `owes`
2. `owns`
3. `creditcardaccount`
4. `credit_card`
5. `debit_card`
6. `card_owner`
7. `used_card`
8. `card`
9. `is_secured`
10. `asset`
11. `deposittx`
12. `withdrawaltx`
13. `purchasetx`
14. `transfertx`
15. `occured`
16. `loantx`
17. `transactions`
18. `location`
19. `loan`
20. `custodian`
21. `customer`
22. `checking`
23. `account`

The `purge` keyword is used after each `drop table` statement, which indicates that the table and its data will be permanently deleted from the database.


## ./git_src/SQL/deposittx (1).sql:
The SQL script provided inserts 25 records into a table named `deposittx`. Each insert statement adds a unique transaction number (`txnum`) to the table, with the values ranging from 76 to 100.

This script appears to be used for testing or populating a database with sample data, as it does not perform any other operations besides the basic `INSERT INTO` statements.

```
The SQL script inserts 25 unique transaction numbers (76 to 100) into the "deposittx" table.
```


## ./git_src/SQL/debit_card (1).sql:
The given SQL code is a series of `INSERT INTO` statements that add 40 rows of data into a table named `debit_card`. Each row contains a `cardnum` and an `accountnum` value, which are likely unique identifiers for a debit card and its associated account, respectively. The code appears to be a way to populate the `debit_card` table with sample data for testing or demonstration purposes.

Here's the summary in markdown format:

```markdown
The SQL code provided inserts 40 rows of data into a table named `debit_card`. Each row contains a `cardnum` and an `accountnum` value, which are likely unique identifiers for a debit card and its associated account, respectively. This code is likely used for populating the `debit_card` table with sample data for testing or demonstration purposes.
```


## ./git_src/SQL/customer (3).sql:
This SQL script inserts 200 customer records into a `customer` table. Each record contains the following columns:

- `dob`: The customer's date of birth
- `first`: The customer's first name
- `last`: The customer's last name
- `middle`: The customer's middle name
- `id`: A unique identifier for the customer

The script generates a diverse set of customer data, including a wide range of first, middle, and last names, as well as various dates of birth spanning from 2019 to 2020.


## ./git_src/SQL/custodian (1).sql:
This SQL script appears to be inserting 50 rows into the `custodian` table. Each row contains two columns: `accountnum` and `customerid`. The `accountnum` values range from 1 to 50, and the `customerid` values range from 1 to 50 respectively. This script is likely used to populate the `custodian` table with some initial data.

Here is the summary in Markdown format:

```markdown
This SQL script inserts 50 rows into the `custodian` table, with each row containing an `accountnum` value from 1 to 50 and a corresponding `customerid` value from 1 to 50. This script is likely used to populate the `custodian` table with some initial data.
```


## ./git_src/SQL/credit_card (3).sql:
The provided SQL script is used to insert 10 rows of data into a table called `credit_card`. Each row contains the following information:

- `cardnum`: a unique identifier for the credit card, ranging from 41 to 50
- `loannum`: a unique identifier for the loan associated with the credit card, also ranging from 41 to 50
- `1000`: the credit limit or balance for each credit card

In summary, this script is used to populate the `credit_card` table with sample data for 10 different credit cards and their associated loan information.


## ./git_src/SQL/checking (3).sql:
The provided SQL code is a series of `INSERT INTO` statements that populate a table called `checking` with 100 rows of data. Each row contains the following information:

- `accountnum`: A unique integer value representing the account number.
- `penalty`: An integer value representing the penalty associated with the account.
- `minimumbalance`: A constant value of `1500` representing the minimum balance required for the account.

The purpose of this code is to create a dataset of checking account information, with a range of different penalty values, that can be used for further analysis or testing.


## ./git_src/SQL/card_owner (2).sql:
The provided SQL script is used to insert data into a table called `card_owner`. The table has two columns: `cardnum` and `customerid`. The script inserts 50 rows into the table, where each row associates a unique card number with a corresponding customer ID.

The purpose of this script is likely to populate a database with initial data for a credit card or payment system, where each customer is associated with a specific card number.

```
insert into card_owner (cardnum, customerid) values (1, 1);
insert into card_owner (cardnum, customerid) values (2, 2);
...
insert into card_owner (cardnum, customerid) values (50, 50);
```


## ./git_src/SQL/card.sql:
The provided SQL code is a series of `INSERT INTO` statements that insert values from 1 to 50 into the `card` table, with the `cardnum` column being populated with the corresponding values.

This script is likely used to initialize or populate the `card` table with a set of pre-defined card numbers, which could be useful in a variety of scenarios, such as:

1. Setting up an initial set of cards for a game or application.
2. Preparing test data for development or debugging purposes.
3. Initializing a database with a known set of card numbers.

The code is straightforward and can be easily executed in a SQL environment to create the desired entries in the `card` table.


## ./git_src/SQL/asset (1).sql:
The provided SQL script inserts 50 records into the `asset` table, each with a unique `assetnum`, `type`, and `value`. The `assetnum` ranges from 1 to 50, the `type` values are a mix of various car models and other asset types, and the `value` ranges from around 1,300 to 9,000.

The purpose of this script is likely to populate a database with sample asset data for testing or development purposes.


## ./git_src/SQL/account (1).sql:
The provided SQL script inserts 150 rows of data into an `account` table. Each row contains the following columns:

- `balance`: a numeric value representing the account balance
- `interestrate`: a numeric value representing the interest rate of the account
- `accountnum`: a unique numeric identifier for the account

The script generates random values for each of these columns and inserts them into the `account` table.

Summary:
- The script is used to populate an `account` table with 150 rows of data
- Each row contains information about the account balance, interest rate, and a unique account number
- The values for each column are randomly generated


## ./git_src/SQL/1makeall.sql:
The provided SQL script creates a database schema for a banking system with the following tables:

1. **customer**: Stores customer information such as date of birth, first name, last name, middle name, and a unique ID.
2. **loan**: Stores loan-related information such as loan number, balance, interest rate, payment due, and principal.
3. **account**: Stores account information such as balance, interest rate, and account number.
4. **checking**: Stores checking account-specific information such as penalty, minimum balance, and a foreign key to the `account` table.
5. **location**: Stores location information such as state, city, zip code, location ID, and type.
6. **transactions**: Stores transaction information such as transaction number and amount.
7. **loantx**: Stores information about loan-related transactions, including transaction number, account number, and loan number.
8. **purchasetx**: Stores information about purchase transactions, including transaction number, transaction type, and vendor.
9. **deposittx**: Stores information about deposit transactions, including transaction number and account number.
10. **withdrawaltx**: Stores information about withdrawal transactions, including transaction number and account number.
11. **transfertx**: Stores information about transfer transactions, including transaction number, source account number, and destination account number.
12. **asset**: Stores asset information such as asset number, type, and value.
13. **card**: Stores card information, including card number.
14. **credit_card**: Stores credit card-specific information, including card number, loan number, and credit limit.
15. **debit_card**: Stores debit card-specific information, including card number and account number.
16. **card_owner**: Stores the relationship between customers and their cards.
17. **owes**: Stores the relationship between customers and the loans they have.
18. **is_secured**: Stores the relationship between loans and the assets that secure them.
19. **custodian**: Stores the relationship between customers and the accounts they own.
20. **owns**: Stores the relationship between customers and the assets they own.
21. **used_card**: Stores the relationship between cards and the transactions they were used in.
22. **occured**: Stores the relationship between transactions and the locations where they occurred.

The script also defines various constraints, such as primary keys, foreign keys, and check constraints to ensure data integrity.


## ./git_src/SQL:
Here is a succinct summary of the provided SQL scripts in markdown format:

```markdown
1. `withdrawaltx (1).sql`: This script inserts 50 rows into the `withdrawaltx` table, with transaction numbers ranging from 101 to 150. It is likely used to populate the database with sample withdrawal transaction data for testing or demonstration purposes.

2. `used_card (1).sql`: This script inserts records into the `used_card` table, with transaction numbers ranging from 76 to 100 and card numbers ranging from 1 to 25. It is used to populate the table with information about transactions involving various credit/debit cards.

3. `transfertx (2).sql`: This script inserts 50 records into the `transfertx` table, with transaction numbers ranging from 151 to 200 and destination account numbers ranging from 1 to 50. It is likely part of a larger system that handles financial transactions and account management.

4. `transactions (2).sql`: This script inserts 200 rows of transaction data into the `transactions` table, including unique transaction numbers, account numbers, and amounts. It is used to populate the table with sample data for testing or analysis purposes.

5. `purchasetx (1).sql`: This script inserts 25 records into the `purchasetx` table, with unique transaction numbers and vendor names. It is likely used to populate the table with sample purchase transaction data for testing or demonstration purposes.
```
Based on the provided documents, the following is a succinct summary:

1. **purchasetx.sql**: This script inserts 25 records into the `purchasetx` table, with each record containing a unique `txnum` (transaction number) and a fictional vendor name. This is likely used to populate the table with sample data for testing or demonstration purposes.

2. **owns.sql**: This script inserts 50 rows into an "owns" table, where each row associates an asset number (1 to 50) with a corresponding customer ID (1 to 50). This is part of a larger database management system, where the "owns" table is used to track the relationship between customers and the assets they own.

3. **owes.sql**: This script inserts 50 rows of data into the `owes` table, with each row containing a unique `loannum` value (ranging from 1 to 50) and a corresponding `customerid` value (also ranging from 1 to 50). This is likely used to populate a database with sample data for a loan management system.

4. **occured.sql**: This script populates the `occured` table with 200 rows of data, where each row includes a transaction number, a location ID, and a Unix timestamp representing the time of occurrence. This is designed to populate the `occured` table with transaction data.

5. **location.sql**: This script inserts 30 different locations into a `location` table, with 5 being ATMs and the remaining 25 being Tellers. The locations are spread across various states, and this script can be used to populate a database with location information for a financial institution or a similar organization.

6. **loantx.sql**: This script inserts 50 rows into the `loantx` table, where the `txnum` column is assigned a unique value from 1 to 50, and the `loannum` column is assigned the same value as the corresponding `txnum`. This script is likely used for populating a test or sample database with loan transaction data.
Here's a succinct summary of the provided SQL scripts in markdown format:

1. `loantx (2).sql`: This script inserts 50 rows into the `loantx` table, where the `txnum` column is assigned a unique value from 1 to 50, and the `loannum` column is assigned the same value as the corresponding `txnum`. This script is likely used for populating a test or sample database with loan transaction data.

2. `loan (1).sql`: This script creates 50 loan records in a `loan` table, with each record containing information such as the original loan amount, current balance, interest rate, and next payment due date. This script is used to populate a test or sample database with diverse loan data.

3. `is_secured (2).sql`: This script inserts 40 rows into an `is_secured` table, with the `loannum` and `assetnum` values ranging from 1 to 40. This script is likely used for populating a test or sample database with data for a loan and asset management system.

4. `dropall.sql`: This script is used to drop all the tables in the database schema, including tables related to accounts, transactions, loans, assets, and credit/debit cards. The `purge` keyword is used, indicating that the tables and their data will be permanently deleted.

5. `deposittx (1).sql`: This script inserts 25 unique transaction numbers (76 to 100) into the `deposittx` table. It appears to be used for testing or populating a database with sample data.
Based on the provided SQL scripts, the following can be summarized:

1. `deposittx.sql`: This script inserts 25 unique transaction numbers (ranging from 76 to 100) into a table named `deposittx`. This is likely used for testing or populating a database with sample data.

2. `debit_card.sql`: This script inserts 40 rows of data into a table named `debit_card`. Each row contains a `cardnum` and an `accountnum` value, which are likely unique identifiers for a debit card and its associated account, respectively. This code is likely used for populating the `debit_card` table with sample data for testing or demonstration purposes.

3. `customer.sql`: This script inserts 200 customer records into a `customer` table. Each record contains the customer's date of birth, first name, last name, middle name, and a unique identifier. The script generates a diverse set of customer data, including a wide range of first, middle, and last names, as well as various dates of birth spanning from 2019 to 2020.

4. `custodian.sql`: This script inserts 50 rows into the `custodian` table, with each row containing an `accountnum` value from 1 to 50 and a corresponding `customerid` value from 1 to 50. This script is likely used to populate the `custodian` table with some initial data.

5. `credit_card.sql`: This script inserts 10 rows of data into a table called `credit_card`. Each row contains a unique `cardnum` (ranging from 41 to 50), a unique `loannum` (also ranging from 41 to 50), and a credit limit or balance of 1000. This script is used to populate the `credit_card` table with sample data.
The provided SQL scripts are used to populate various tables in a database with sample data for testing or development purposes. Here's a summary of the scripts:

1. `credit_card.sql`: This script inserts 10 rows into the `credit_card` table, with each row containing a unique `cardnum` and `loannum` value, along with a credit limit of 1000.

2. `checking.sql`: This script inserts 100 rows into the `checking` table, with each row containing a unique `accountnum`, a `penalty` value, and a constant `minimumbalance` of 1500.

3. `card_owner.sql`: This script inserts 50 rows into the `card_owner` table, associating each unique `cardnum` with a corresponding `customerid`.

4. `card.sql`: This script inserts 50 rows into the `card` table, with the `cardnum` column populated with values from 1 to 50.

5. `asset.sql`: This script inserts 50 rows into the `asset` table, with each row containing a unique `assetnum`, a `type` (such as car models or other asset types), and a `value` ranging from around 1,300 to 9,000.

These scripts are likely used to set up initial data for testing or development purposes, allowing developers to work with a pre-populated database and explore various functionalities of the application.
The provided documents contain SQL scripts that are used to create and populate a database schema for a banking system. Here's a summary of the documents:

1. **`asset (1).sql`**:
   - This script inserts 50 records into the `asset` table, with each record having a unique `assetnum`, `type`, and `value`.
   - The purpose of this script is to populate the database with sample asset data for testing or development purposes.

2. **`account (1).sql`**:
   - This script inserts 150 rows of data into the `account` table.
   - Each row contains information about the account balance, interest rate, and a unique account number.
   - The values for each column are randomly generated.

3. **`1makeall.sql`**:
   - This script creates a database schema for a banking system, including the following tables:
     - `customer`, `loan`, `account`, `checking`, `location`, `transactions`, `loantx`, `purchasetx`, `deposittx`, `withdrawaltx`, `transfertx`, `asset`, `card`, `credit_card`, `debit_card`, `card_owner`, `owes`, `is_secured`, `custodian`, `owns`, `used_card`, and `occured`.
   - The script defines various constraints, such as primary keys, foreign keys, and check constraints, to ensure data integrity.

Overall, these SQL scripts are used to set up a database schema for a banking system and populate it with sample data for testing or development purposes.


## ./git_src/README:
Here is a succinct and accurate summary of the Nickel Savings and Loan Database Application in markdown format:

## Nickel Savings and Loan Database Application

This application is a Java-based database application that manages customer accounts, transactions, and debt information for a bank. The application consists of several key components:

1. **Home Interface**: The main entry point that allows the user to access the Customer, Location, and Debt interfaces.
2. **Customer Interface**: Provides functionalities to retrieve customer information, perform transactions (deposits, withdrawals, transfers), and view transaction history.
3. **Location Interface**: Allows bank management to view and create new customer accounts, as well as monitor transaction activities at different bank locations.
4. **Debt Interface**: Provides a high-level view of the bank's debt, including total loans, monthly payments, and average debt per customer.

The application utilizes a JDBC-based connection to an Oracle database, with the database design choices focused on maintaining transaction records and preventing data loss or potential money laundering activities.

The project includes several deliberate design choices, such as:
- No cascading deletions for transactions to maintain a record of all transactions
- Requiring card-based transactions to ensure visibility into all customer activities
- Allowing assets and loans to be shared among multiple people
- Storing vendor IDs separately from the database, as the bank's focus is on ensuring available funds for transactions.

The project also includes plans for future development, such as improving the efficiency of the database connection, implementing role-based access control, and expanding the functionality of the card-based transactions.


## ./git_src/PLSQL/savingsTrigger.plsql:
The provided source code is a PL/SQL trigger named `savingsTrigger` that is executed after an update on the `account` table. The trigger performs the following actions:

1. It retrieves the count of rows from the `checking` table where the `accountnum` matches the `NEW` value of the `accountnum` column in the updated row of the `account` table.
2. If the count is 0 (i.e., there is no corresponding row in the `checking` table) and the `NEW` value of the `balance` column is less than 0 (i.e., the account is overdrawn), the trigger raises an application error with the message "Savings accounts cannot be overdrawn".

In summary, this trigger ensures that savings accounts cannot be overdrawn, and it applies this rule only to accounts that do not have a corresponding row in the `checking` table.


## ./git_src/PLSQL/readTime.plsql:
The provided code defines a PL/SQL function called `readTime` that takes a numeric input `chronos` and returns a `DATE` value. The function performs the following steps:

1. It initializes the date to `1970-01-01`.
2. It then adds the `chronos` value, interpreted as the number of seconds, to the initial date using the `numtodsinterval` function.
3. The function returns the resulting date.

If an exception occurs during the execution of the function, the function catches the exception and returns the default date of `1970-01-01`.

The purpose of this function is likely to convert a numeric representation of time (e.g., a Unix timestamp) into a standard date and time format.


## ./git_src/PLSQL/purchaseTransaction.plsql:
This PL/SQL function, `purchaseTransaction`, is responsible for handling purchase transactions for customers. It takes various input parameters such as the customer ID, account number, transaction amount, card number, vendor ID, and transaction type (debit or credit).

The function performs the following main tasks:

1. Validates the input data, checking for the existence of the customer, account, and card, as well as the validity of the transaction amount and credit limit (for credit card transactions).
2. Generates a unique transaction number and calculates the timestamp of the transaction.
3. Updates the account balance (for debit transactions) or the loan balance and principal (for credit transactions) accordingly.
4. Inserts the transaction details into the `Transactions`, `purchasetx`, `occured`, and `used_card` tables.
5. Commits the transaction and returns an appropriate status code (1 for success, 0 for various errors, or -3 for insufficient credit).
6. Handles various exceptions that may occur during the transaction processing.

The function ensures data integrity and consistency by performing necessary validations and updating the relevant tables accordingly.


## ./git_src/PLSQL/payLoanTransaction.plsql:
The provided code is a PL/SQL function called `payLoanTransaction` that allows a customer to make a payment on a loan. The function takes the following parameters:

1. `customId`: The ID of the customer making the payment.
2. `accountNo`: The account number to be used for the payment.
3. `amount`: The amount of the payment.
4. `locId`: The location ID where the payment is being made.
5. `loanNo`: The loan number to be paid.
6. `cardId`: The ID of the card used for the payment (optional).

The function performs the following steps:

1. Checks if the customer, account, location, and loan exist in the database.
2. Checks if the card used for the payment is valid for the customer.
3. Checks if the account balance is sufficient to make the payment.
4. Calculates the new loan balance and payment due date after the payment.
5. Updates the transaction table, withdrawal transaction table, and the occurred table with the payment details.
6. Updates the loan and account balances accordingly.
7. If a card is used, it inserts the card information into the used_card table.
8. Commits the transaction and returns 1 to indicate success.

The function also handles various exceptions, such as no customer, no account, bad amount, and others, and rollbacks the transaction in case of an error, returning 0 to indicate failure.


## ./git_src/PLSQL/openAccount.plsql:
The provided PL/SQL code defines a function called `openAccount` that is responsible for creating a new account for a customer. The function takes several input parameters, such as the customer ID, account type, initial balance, interest rate, and location ID. The function performs the following tasks:

1. Checks if the provided customer ID is valid by querying the `customer` table.
2. Generates a new account number by fetching the maximum account number from the `account` table and incrementing it.
3. Validates the initial balance based on the account type (checking account requires a minimum of $1,500).
4. Calculates the current timestamp and converts it to a chronological number.
5. Inserts the new account information into the `account`, `custodian`, `transactions`, `deposittx`, and `occured` tables.
6. If the account type is checking, it also inserts the account details into the `checking` table.
7. Commits the transaction and returns `1` to indicate success.
8. Handles exceptions, such as invalid customer ID or negative initial balance, by rolling back the transaction and returning `0`.

Overall, the `openAccount` function is responsible for creating a new account for a customer, ensuring that the necessary data is inserted into the appropriate tables, and handling any errors that may occur during the process.


## ./git_src/PLSQL/newCustomer.plsql:
The provided code is a PL/SQL function named `newCustomer` that inserts a new customer record into a database table named `customer`. Here's a summary of the function:

1. The function takes four input parameters: `first` (first name), `middle` (middle name), `last` (last name), and `dayte` (date of birth in the format 'yyyymmdd').
2. The function generates a new customer ID by selecting the maximum existing ID and incrementing it by 1.
3. The function converts the input `dayte` string to a date format and stores it in the `intermediate` variable.
4. The function inserts the new customer record into the `customer` table, using the generated customer ID, the input name parameters, and the converted date of birth.
5. The function commits the transaction and returns 1 to indicate successful execution.
6. If an exception occurs during the execution, the function prints a message 'Fail safe', rolls back the transaction, and returns 0 to indicate failure.

```markdown
The `newCustomer` function is responsible for creating a new customer record in the `customer` database table. It generates a unique customer ID, converts the input date of birth to the appropriate format, and inserts the new record. If an exception occurs during the process, the function handles it by rolling back the transaction and returning a failure status.
```


## ./git_src/PLSQL/createTransferTransaction.plsql:
The provided PL/SQL code defines a function called `createTransferTransaction` that is responsible for creating a transaction to transfer funds between accounts. Here's a summary of the function:

1. The function takes several parameters as input:
   - `customId`: the ID of the customer performing the transaction
   - `accountNo`: the account number of the customer's source account
   - `amount`: the amount to be transferred
   - `destAccount`: the destination account number
   - `locId`: the location ID where the transaction is occurring
   - `cardId`: the card number used for the transaction (optional)

2. The function performs various checks to ensure the validity of the input data:
   - Checks if the customer and source account exist
   - Checks if the destination account exists
   - Checks if the location exists
   - Checks if the card is valid and belongs to the customer (if provided)
   - Checks if the source account has sufficient balance to perform the transfer

3. If all checks pass, the function proceeds to update the balances of the source and destination accounts, and creates the necessary records in the `Transactions`, `transfertx`, `occured`, and `used_card` tables.

4. The function returns `1` on successful completion of the transaction, and `0` if any of the checks fail.

5. The function includes exception handling to handle various scenarios, such as when the customer or account does not exist, the amount is invalid, or there is a general failure.

In summary, the `createTransferTransaction` function is a crucial component of a banking or financial system, responsible for managing and validating fund transfer operations between customer accounts.


## ./git_src/PLSQL/createLoanTransaction.plsql:
The provided code is a PL/SQL function named `createLoanTransaction` that takes several input parameters (customer ID, account number, transaction amount, location ID, interest rate, card number, and asset number) and performs the following operations:

1. Checks if the customer, account, location, and card (if provided) exist in the database.
2. Retrieves the current account balance for the given customer and account.
3. Generates a new transaction number and loan number.
4. Calculates the payment due for the loan based on the provided interest rate.
5. Updates the account balance by adding the transaction amount.
6. Inserts the transaction, loan, and associated records (owes, is_secured, loantx, occured, used_card) into the respective tables.
7. Commits the transaction.
8. Returns 1 on successful execution or 0 on encountering specific exceptions (no customer, no account, bad amount).

The function also includes exception handling to handle various error scenarios and rollback the transaction if an exception occurs.


## ./git_src/PLSQL/createBasicTransaction.plsql:
This PL/SQL function, `createBasicTransaction`, is designed to handle the creation of a basic transaction in a banking or financial system. The function takes several input parameters, including the customer ID, account number, transaction amount, transaction type (deposit or withdrawal), location ID, and card number (if applicable). The function performs the following steps:

1. Checks if the customer and account exist, and raises exceptions if they do not.
2. Checks if the location ID is valid, and raises an exception if it is not.
3. If a card number is provided, checks if the card is associated with the customer, and raises an exception if it is not.
4. Checks the account balance and raises an exception if the withdrawal amount exceeds the balance or if the transaction amount is greater than $99,999.99.
5. Calculates the penalty fee, if applicable, for the account.
6. Generates a unique transaction number and retrieves the current timestamp.
7. Performs the transaction (deposit or withdrawal) by updating the account balance and inserting relevant records into the `Transactions`, `deposittx` or `withdrawaltx`, and `occured` tables.
8. If a card number is provided, records the card usage in the `used_card` table.
9. Commits the transaction.
10. Returns 1 on successful completion, or 0 on any exception.

The function handles several exceptions, including `noCustomer`, `noAccount`, `badAmount`, and a generic `others` exception, and performs appropriate rollback and error logging actions.


## ./git_src/PLSQL/checkingPenaltyTrigger.plsql:
The provided code is a PL/SQL trigger named `display_salary_changes` that is designed to update the penalty amount for a checking account based on certain conditions. The trigger is executed after an update on the `account` table.

The key points of the trigger are:

1. It retrieves the count of rows in the `checking` table where the `accountnum` matches the updated `accountnum` in the `account` table.
2. If there is only one row in the `checking` table and the updated `balance` in the `account` table is less than $1,500, the trigger performs the following actions:
   - Retrieves the current `penalty` value from the `checking` table for the updated `accountnum`.
   - If the updated `balance` is less than $1,500, it adds $50 to the `penalty`.
   - If the updated `balance` is less than $0, it adds $100 to the `penalty`.
   - It updates the `penalty` value in the `checking` table for the updated `accountnum`.
3. The trigger also outputs the updated `penalty` value and the `accountnum` using `dbms_output.put_line()`.

In summary, this trigger is used to automatically update the penalty amount for a checking account based on the account balance, and it logs the updated penalty value.


## ./git_src/PLSQL/addCard.plsql:
The provided code is a PL/SQL function named `addCard` that allows for the creation of a new credit or debit card for a customer. The function takes in the following parameters:

1. `customId`: the ID of the customer
2. `acctno`: the account number
3. `creditLimit`: the credit limit for the card
4. `txType`: the type of transaction (1 for debit card, 2 for credit card)

The function performs the following steps:

1. Checks if the customer exists in the `customer` table. If the customer does not exist, it raises a `badAmount` exception.
2. Generates a new card number by retrieving the maximum card number from the `card` table and incrementing it.
3. If the `txType` is 1 (debit card), it checks if the customer is the custodian of the specified account. If not, it raises a `badAmount` exception.
4. Inserts a new record in the `card` and `card_owner` tables.
5. If the `txType` is 1 (debit card), it inserts a new record in the `debit_card` table.
6. If the `txType` is 2 (credit card), it generates a new loan number, inserts a new record in the `loan`, `owes`, and `credit_card` tables.
7. Commits the transaction and returns 1 to indicate success.
8. If any exception occurs, it rolls back the transaction and returns 0 to indicate failure.

Overall, this function provides a way to add a new credit or debit card for a customer, with appropriate checks and validations to ensure the integrity of the data.


## ./git_src/PLSQL:
Here's a succinct summary of the provided PL/SQL source code documents:

1. **savingsTrigger.plsql**: This trigger ensures that savings accounts cannot be overdrawn. It checks if the updated account has a corresponding row in the `checking` table. If not and the new balance is less than 0 (overdrawn), it raises an application error.

2. **readTime.plsql**: This function converts a numeric representation of time (e.g., a Unix timestamp) into a standard date and time format. It takes a numeric input `chronos`, interprets it as the number of seconds, and adds it to the initial date of `1970-01-01`.

3. **purchaseTransaction.plsql**: This function handles purchase transactions for customers. It validates the input data, generates a unique transaction number, updates the account balance or loan balance and principal, and inserts the transaction details into various tables. It also handles exceptions and returns appropriate status codes.

4. **payLoanTransaction.plsql**: This function allows a customer to make a payment on a loan. It checks the existence of the customer, account, location, and loan, ensures the account balance is sufficient, updates the transaction details, and calculates the new loan balance and payment due date. It handles exceptions and returns a status code.

5. **openAccount.plsql**: This function is responsible for creating a new account for a customer. It checks the validity of the customer, generates a new account number, validates the initial balance, and inserts the new account information into various tables. It also handles exceptions and returns a status code.
The provided PL/SQL code defines three functions that are crucial for a banking or financial system:

1. **`openAccount`**:
   - Creates a new account for a customer.
   - Checks if the customer ID is valid, generates a new account number, and validates the initial balance.
   - Inserts the new account details into various database tables, including `account`, `custodian`, `transactions`, `deposittx`, and `occured`.
   - If the account type is checking, it also inserts the account details into the `checking` table.
   - Handles exceptions and rolls back the transaction if necessary.

2. **`newCustomer`**:
   - Inserts a new customer record into the `customer` database table.
   - Generates a new customer ID by incrementing the maximum existing ID.
   - Converts the input date of birth to the appropriate format and inserts the new customer record.
   - Handles exceptions by rolling back the transaction and returning a failure status.

3. **`createTransferTransaction`**:
   - Manages the process of transferring funds between customer accounts.
   - Performs various checks to ensure the validity of the input data, such as existence of the customer, source account, destination account, and location.
   - If all checks pass, it updates the balances of the source and destination accounts and creates the necessary records in the `Transactions`, `transfertx`, `occured`, and `used_card` tables.
   - Includes exception handling to handle various error scenarios and roll back the transaction if necessary.

4. **`createLoanTransaction`**:
   - Handles the creation of a new loan transaction.
   - Checks the existence of the customer, account, location, and card (if provided).
   - Retrieves the current account balance, generates a new transaction number and loan number, and calculates the payment due for the loan.
   - Updates the account balance and inserts the transaction, loan, and associated records into the respective tables.
   - Commits the transaction and returns 1 on successful execution or 0 on encountering specific exceptions.

These functions are essential components of a banking or financial system, responsible for managing customer accounts, creating new customers, and handling fund transfers and loan transactions, while ensuring data integrity and handling various error scenarios.
The provided documents contain three PL/SQL functions and one PL/SQL trigger that are part of a banking or financial system:

1. `createLoanTransaction`:
   - This function creates a new loan transaction, handling various checks and updates to the database.
   - It verifies the existence of the customer, account, location, and card (if provided).
   - It generates a new transaction number and loan number, calculates the payment due, and updates the account balance.
   - It inserts the transaction, loan, and associated records into the respective tables.
   - It includes exception handling and rollback functionality.

2. `createBasicTransaction`:
   - This function handles the creation of a basic transaction, such as a deposit or withdrawal.
   - It performs checks on the customer, account, location, and card (if provided).
   - It calculates the penalty fee, if applicable, and updates the account balance.
   - It records the transaction in the relevant tables, including the `Transactions`, `deposittx`/`withdrawaltx`, and `used_card` tables.
   - It includes exception handling and rollback functionality.

3. `checkingPenaltyTrigger`:
   - This trigger is executed after an update on the `account` table.
   - It checks the balance of a checking account and updates the `penalty` value in the `checking` table accordingly.
   - If the balance is less than $1,500, it adds $50 to the penalty; if the balance is less than $0, it adds an additional $100.
   - It logs the updated penalty value and the account number.

4. `addCard`:
   - This function allows the creation of a new credit or debit card for a customer.
   - It checks if the customer exists and generates a new card number.
   - For a debit card, it verifies that the customer is the custodian of the specified account.
   - It inserts the new card information into the `card`, `card_owner`, and `debit_card` or `loan`, `owes`, and `credit_card` tables, depending on the card type.
   - It includes exception handling and rollback functionality.

These functions and the trigger are designed to maintain the integrity and consistency of the banking or financial system by performing various validations, updates, and record-keeping operations related to customer accounts, transactions, and card management.</response>
The provided code is a PL/SQL function named `addCard` that allows for the creation of a new credit or debit card for a customer. The function takes the following parameters:

1. `customId`: the ID of the customer
2. `acctno`: the account number
3. `creditLimit`: the credit limit for the card
4. `txType`: the type of transaction (1 for debit card, 2 for credit card)

The function performs the following steps:

1. Checks if the customer exists in the `customer` table. If the customer does not exist, it raises a `badAmount` exception.
2. Generates a new card number by retrieving the maximum card number from the `card` table and incrementing it.
3. If the `txType` is 1 (debit card), it checks if the customer is the custodian of the specified account. If not, it raises a `badAmount` exception.
4. Inserts a new record in the `card` and `card_owner` tables.
5. If the `txType` is 1 (debit card), it inserts a new record in the `debit_card` table.
6. If the `txType` is 2 (credit card), it generates a new loan number, inserts a new record in the `loan`, `owes`, and `credit_card` tables.
7. Commits the transaction and returns 1 to indicate success.
8. If any exception occurs, it rolls back the transaction and returns 0 to indicate failure.

Overall, this function provides a way to add a new credit or debit card for a customer, with appropriate checks and validations to ensure the integrity of the data.


## ./git_src/META-INF/services/java.sql.Driver:
The provided text appears to be the contents of a file located at `./git_src/META-INF/services/java.sql.Driver`. This file contains a single line, which specifies the `oracle.jdbc.OracleDriver` as the implementation of the `java.sql.Driver` interface.

This file is likely part of the configuration for a Java application that uses the Oracle JDBC driver to interact with an Oracle database. The `java.sql.Driver` interface is a part of the Java Database Connectivity (JDBC) API, and this file serves to register the Oracle JDBC driver as a service provider for this interface, allowing the application to use the Oracle JDBC driver to connect to and interact with an Oracle database.

In summary, this file is a configuration file that specifies the Oracle JDBC driver as the implementation of the `java.sql.Driver` interface, which is used by a Java application to interact with an Oracle database.


## ./git_src/META-INF/services:
The document provided contains the contents of a file located at `./git_src/META-INF/services/java.sql.Driver`. This file is a configuration file that specifies the `oracle.jdbc.OracleDriver` as the implementation of the `java.sql.Driver` interface.

This file is likely used in a Java application that interacts with an Oracle database using the JDBC (Java Database Connectivity) API. The `java.sql.Driver` interface is part of the JDBC API, and the file serves to register the Oracle JDBC driver as a service provider for this interface, allowing the application to use the Oracle JDBC driver to connect to and interact with an Oracle database.

In summary, this configuration file is used to specify the Oracle JDBC driver as the implementation of the `java.sql.Driver` interface, enabling a Java application to use the Oracle JDBC driver to interact with an Oracle database.


## ./git_src/META-INF/MANIFEST.MF:
The provided source code appears to be the `MANIFEST.MF` file for a Java application. This file contains metadata about the application, including:

- **Manifest-Version**: The version of the manifest file, which is 1.0.
- **Implementation-Title**: The title of the implementation, which is "JDBC".
- **Implementation-Version**: The version of the implementation, which is 18.3.0.0.0.
- **Specification-Vendor**: The vendor of the specification, which is "Sun Microsystems Inc.".
- **Specification-Title**: The title of the specification, which is "JDBC".
- **Class-Path**: The class path, which includes "oraclepki.jar".
- **Implementation-Vendor**: The vendor of the implementation, which is "Oracle Corporation".
- **Main-Class**: The main class of the application, which is "oracle.jdbc.OracleDriver".
- **Ant-Version**: The version of Apache Ant used to build the application, which is 1.7.1.
- **Repository-Id**: The repository ID, which is "JAVAVM_18.1.0.0.0_LINUX.X64_180620".
- **Created-By**: The version of the Java Virtual Machine used to create the application, which is "25.171-b11 (Oracle Corporation)".
- **Specification-Version**: The version of the specification, which is 4.0.

The file also lists several packages that are not sealed, including "oracle/sql/", "oracle/sql/converter/", "oracle/jdbc/logging/annotations/", and "oracle/sql/converter_xcharset/".


## ./git_src/META-INF:
The provided documents describe the configuration files for a Java application that interacts with an Oracle database using the JDBC (Java Database Connectivity) API.

1. `META-INF/services/java.sql.Driver`: This file specifies the `oracle.jdbc.OracleDriver` as the implementation of the `java.sql.Driver` interface, which is part of the JDBC API. This configuration allows the application to use the Oracle JDBC driver to connect to and interact with an Oracle database.

2. `META-INF/MANIFEST.MF`: This file contains metadata about the Java application, including:
   - The version of the manifest file, the implementation, and the specification.
   - The vendor of the specification and implementation.
   - The class path, including the `oraclepki.jar` file.
   - The main class of the application, which is `oracle.jdbc.OracleDriver`.
   - The version of Apache Ant and the Java Virtual Machine used to build and create the application.
   - The repository ID and the packages that are not sealed.

In summary, these configuration files are used to specify the Oracle JDBC driver as the implementation of the `java.sql.Driver` interface and provide metadata about the Java application, enabling it to interact with an Oracle database using the JDBC API.


## ./git_src:
Based on the provided documents, here is a succinct summary in markdown format:

1. **Git Source Code (`./git_src/mjg422`):**
   - The code includes a Java-based banking system project with various features:
     - `Project.java`: The main Java program that simulates a banking system, including user authentication, a main menu, and various banking operations.
     - `Makefile`: A build script that compiles the Java source files and creates a JAR file.
     - `Transaction.java`: A Java class that handles different banking transactions, such as purchase, loan, transfer, and deposit.
     - `Manifest.txt`: A file that defines the main entry point and the classpath for the application, indicating it interacts with an Oracle database.
   - The project appears to be a comprehensive banking system that allows users to manage customers, locations, and debts, and perform various financial transactions.

2. **SQL Scripts (`./git_src/SQL`):**
   - The SQL scripts are used to create and populate a database schema for the banking system, including tables for customers, loans, accounts, transactions, assets, and credit/debit cards.
   - The scripts insert sample data into the tables, allowing for testing and development of the banking application.
   - The scripts cover various aspects of the banking system, such as loan management, asset ownership, transaction history, and customer data.

3. **Additional SQL Scripts:**
   - The provided documents also include additional SQL scripts that perform various tasks:
     - `1makeall.sql`: Creates the database schema for the banking system, including all the necessary tables and constraints.
     - Scripts for inserting sample data into tables, such as `asset.sql`, `credit_card.sql`, `checking.sql`, and `card_owner.sql`.
   - These scripts are used to set up a complete database environment for the banking system, enabling testing and development of the application.

Overall, the provided documents describe a Java-based banking system project that interacts with an Oracle database, along with the SQL scripts used to set up and populate the database schema for the system.
Based on the provided documents, here is a succinct summary in markdown format:

## Summary

The documents describe a set of SQL scripts and a Java-based database application for a banking system called "Nickel Savings and Loan".

### SQL Scripts

The SQL scripts are used to create and populate a database schema for the banking system. The key features of the scripts are:

1. **Database Schema Creation**: The `1makeall.sql` script creates the database schema, including tables for customers, loans, accounts, transactions, assets, cards, and more.
2. **Data Population**: Various scripts (e.g., `asset.sql`, `account.sql`, `credit_card.sql`) insert sample data into the tables to populate the database for testing and development purposes.
3. **Data Cleanup**: The `dropall.sql` script is used to drop all the tables in the database schema, effectively removing all data.

### Nickel Savings and Loan Database Application

The Nickel Savings and Loan Database Application is a Java-based application that interacts with the database to manage customer accounts, transactions, and debt information. The key components of the application are:

1. **Home Interface**: The main entry point that allows the user to access the Customer, Location, and Debt interfaces.
2. **Customer Interface**: Provides functionalities to retrieve customer information, perform transactions (deposits, withdrawals, transfers), and view transaction history.
3. **Location Interface**: Allows bank management to view and create new customer accounts, as well as monitor transaction activities at different bank locations.
4. **Debt Interface**: Provides a high-level view of the bank's debt, including total loans, monthly payments, and average debt per customer.

The application is designed with several deliberate choices, such as:

- Maintaining a record of all transactions to prevent data loss and potential money laundering activities.
- Requiring card-based transactions to ensure visibility into all customer activities.
- Allowing assets and loans to be shared among multiple people.
- Storing vendor IDs separately from the database, as the bank's focus is on ensuring available funds for transactions.

The project also includes plans for future development, such as improving the efficiency of the database connection, implementing role-based access control, and expanding the functionality of the card-based transactions.
## Summary

The provided documents describe a Java-based database application for a bank, the Nickel Savings and Loan, as well as several PL/SQL functions and a trigger that are part of the application's database implementation.

### Nickel Savings and Loan Database Application

The application consists of the following key components:

1. **Home Interface**: The main entry point for the application, allowing access to the Customer, Location, and Debt interfaces.
2. **Customer Interface**: Provides functionalities to manage customer information, transactions (deposits, withdrawals, transfers), and transaction history.
3. **Location Interface**: Allows bank management to view and create new customer accounts, as well as monitor transaction activities across different bank locations.
4. **Debt Interface**: Provides a high-level view of the bank's debt, including total loans, monthly payments, and average debt per customer.

The application utilizes a JDBC-based connection to an Oracle database, with design choices focused on maintaining transaction records and preventing data loss or potential money laundering activities.

### PL/SQL Functions and Trigger

The provided PL/SQL code includes the following functions and a trigger:

1. **`openAccount`**: Creates a new account for a customer, including checks for valid customer ID, generating a new account number, and inserting the account details into various database tables.
2. **`newCustomer`**: Inserts a new customer record into the `customer` table, generating a new customer ID.
3. **`createTransferTransaction`**: Manages the process of transferring funds between customer accounts, performing various checks and updating the necessary records.
4. **`createLoanTransaction`**: Handles the creation of a new loan transaction, including checks for the existence of the customer, account, location, and card (if provided), and updating the necessary records.
5. **`checkingPenaltyTrigger`**: A trigger that updates the `penalty` value in the `checking` table based on the account balance, adding $50 if the balance is less than $1,500 and an additional $100 if the balance is less than $0.
6. **`addCard`**: Allows the creation of a new credit or debit card for a customer, performing relevant checks and inserting the card information into the appropriate tables.

These functions and the trigger are essential components of the banking or financial system, responsible for managing customer accounts, creating new customers, and handling fund transfers and loan transactions, while ensuring data integrity and handling various error scenarios.
Here is a succinct summary of the provided documents:

1. **PL/SQL Source Code Documents**:
   - The PL/SQL code defines several functions and a trigger for a banking or financial system:
     - `savingsTrigger`: Ensures that savings accounts cannot be overdrawn.
     - `readTime`: Converts a numeric representation of time to a standard date and time format.
     - `purchaseTransaction`: Handles purchase transactions for customers.
     - `payLoanTransaction`: Allows a customer to make a payment on a loan.
     - `openAccount`: Creates a new account for a customer.

2. **Java Application Configuration**:
   - The configuration files in the `META-INF` directory are used to set up a Java application that interacts with an Oracle database using the JDBC API.
   - The `java.sql.Driver` file specifies the `oracle.jdbc.OracleDriver` as the implementation of the `java.sql.Driver` interface.
   - The `MANIFEST.MF` file provides metadata about the Java application, including the class path, the main class, and the versions of the build tools and Java Virtual Machine used.

These documents describe the functionality of the PL/SQL code and the configuration of the Java application, which together form a banking or financial system that interacts with an Oracle database.
The provided documents describe the configuration files for a Java application that interacts with an Oracle database using the JDBC (Java Database Connectivity) API. The key points are:

1. `META-INF/services/java.sql.Driver`: This file specifies the `oracle.jdbc.OracleDriver` as the implementation of the `java.sql.Driver` interface, which is part of the JDBC API. This allows the application to use the Oracle JDBC driver to connect to and interact with an Oracle database.

2. `META-INF/MANIFEST.MF`: This file contains metadata about the Java application, including the version of the manifest file, the implementation and specification, the vendor, the class path (which includes the `oraclepki.jar` file), the main class (`oracle.jdbc.OracleDriver`), the version of Apache Ant and the Java Virtual Machine used to build and create the application, and the repository ID and packages that are not sealed.

These configuration files are used to specify the Oracle JDBC driver as the implementation of the `java.sql.Driver` interface and provide metadata about the Java application, enabling it to interact with an Oracle database using the JDBC API.


