# User Guide

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [User Roles](#user-roles)
  - [Administrator](#administrator)
- [Main Features](#main-features)
- [Navigating the Interface](#navigating-the-interface)
  - [Login Page](#login-page)
  - [Main Menu](#main-menu)
- [Data Entry and Management](#data-entry-and-management)
  - [Adding New Students](#adding-new-students)
  - [Adding Teachers](#adding-teachers)
  - [Managing Fees](#managing-fees)
- [Reporting and Data Export](#reporting-and-data-export)
- [Troubleshooting](#troubleshooting)
- [Contact Support](#contact-support)



## Introduction
This School Management System is a comprehensive platform designed to manage the operations of school of the school, which includes student enrolment, teacher assignments, fee payments, and more. This documentation provides the users with detailed instructions on how to navigate and use the system efficiently.

## System Requirements
### Hardware:
- A computer with at least 4GB of RAM
- Minimum of 2GB free storage
- A display with at least 1024x768 resolution
### Software:
- Operating System: Windows 7 or higher, Linux, or macOS
- Python 3.8 or later
- MySQL Server
- Tkinter library for GUI
- FPDF library for generating PDF reports

## Installation Guide

1. **Download the Source Code**  
   Download the provided source code for the School Management System.

2. **Install Python**  
   Ensure that Python 3.8+ is installed on your system.

3. **Set Up MySQL**  
   - Install MySQL Server.
   - Create a database named `schoolmanagementsystem`.
   - Set up tables by executing the provided SQL scripts.

4. **Install Dependencies**  
   - Open a terminal or command prompt.
   - Install the required libraries by running commands like:
     ```bash
     pip install mysql-connector-python
     pip install fpdf
     ```

5. **Run the Application**  
   - In your terminal, navigate to the project folder.
   - Execute the command:
     ```bash
     python main.py
     ```

## User Roles
The system has several distinct user roles, each with specific functions.

### Administrator
- Full login access to the system
- Enrol students and manage student data
- Manage teachers' data
- Manage fees and payments

## Main Features
## Enrollment Page

#### The Enrollment Page allows administrators to add and manage student details, including:
- Name
- Class
- Date of birth
- Parent information

![alt text](./ScreenshotEnrolment2024-10-31%20073102.png"Enrollment Page")

## Account Management

#### The Account Management section facilitates the management of fees and payments for students. Users can:
- Add new payments
- Update existing records
- Generate reports

![alt text](./ScreenshotAccount2024-10-31%20073228.png"Example Account page")

## Teacher Page

#### The Teacher Page is a dedicated section for managing teacher data. Administrators can use this page to:
- Manage teacher information, such as their assigned class
- Update contact information
- Enter and view salary details

![alt text](./ScreenshotTeacher2024-10-31%20073352.png"Example teacher page")

## Navigating the Interface
### Login Page
- 	Upon launching the system, users are required to log in using their credentials.
- 	Enter the username and password, then click the Login button

![alt text](./ScreenshotLogin2024-10-31%20074303.png"Example login page")

## Main Menu
- Once logged in, the main menu provides access to different modules such as Enrollment, Account, and Teacher.
- Select a module by clicking on the respective button.

![alt text](./ScreenshotMain2024-10-31%20074612.png"Example main menu")

## Data Entry and Management

### Adding New Students
- Navigate to the **Enrollment Page**.
- Fill in the student's details, including:
  - Name
  - Class
  - Date of birth
  - Parent information
- Click **Add New** to save the student's information.

### Adding Teachers
- Go to the **Teacher Page**.
- Enter the teacher's information, such as:
  - Name
  - Assigned class
  - Contact details
- Click **Save** to add the teacher to the database.

### Managing Fees
- On the **Account Page**, enter payment details for students, including:
  - Amount paid
  - Balance
  - Payment date

## Reporting and Data Export

The system allows users to generate PDF reports for fees and other data. On the **Account Page**, there is an option to generate and download fee records as PDF files.

### To generate a report:
1. Navigate to the **Account Page**.
2. Click the **Generate PDF** button after selecting the relevant data.
3. The PDF will be saved to your system for review.

## Troubleshooting

### Database Connection Errors
- Ensure that MySQL is running on your local system and that the correct credentials are provided in the system settings.

### Login Issues
- Verify your username and password. If issues persist, contact the administrator for password reset.

### Data Entry Errors
- Make sure that all required fields are filled before submitting a form.

## Contact Support
For any technical issues or further assistance, please contact the School Management System support team at:

- **Email**: [henryoluwaseyi@gmail.com](mailto:henryoluwaseyi@gmail.com)
- **Phone**: +491633375874


