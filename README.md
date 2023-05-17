# Automatic-exam-registration-form-filler
## Objectives
* To provide an online interface to the users where they can fill in their personal details.
* To provide the controller concerned with the issue of hall tickets an online platform to use this system to reduce his workload and process the registration in a speedy manner.
* To provide a communication platform between the student and the controller.
* To let know the status of their registration and the date on which they have to appear for the examination.

## Hardware Requirements
*  System should be able to handle the graphical interface operations
*  System should have XAMPP to process SQL server data
   ### Platforms Include
   #### GNU/Linux
   * CPU Type: Pentium 4 or higher; 2 GHz or higher
   * Memory/RAM: 1 GB minimum, up to the system limit
   * Hard Disk: 4 GB or higher
   * Graphics: X Window server or similar graphics server
   #### Windows 
   * Processor: 1 gigahertz (GHz) or faster
   * RAM: 1 gigabyte (GB) (32-bit) or 2 GB (64-bit)
   * Free hard disk space: 16 GB 
   * Graphics card: Microsoft DirectX graphics device with WDDM driver

## Software Requirements
To implement the Automatic exam registration form filler system, we require the following
software:
* MySQL – version 8.0
* PAGE GUI builder – version 5.6
* PyCharm IDE – version 2020.3
* MongoDB – version 4.4.2
* MongoDB compass – version 1.24.1

## Functional Requirements
Python code to handle the following functions with GUI as a frontend:
* Display student information
* Display the courses that student opted
* Display the department to which the student belongs to
* Display the exam Centre details
* Generate the hall ticket and show

Logins will be provided for Students, Exam department, staff, bank manager and for
college Administrator with following functionalities.
1. Exam department login:
   * Exam department can schedule the exams to be conducted.
   * Exam department can check the number of students registered for the exams of different courses.
   * Exam department can allot exam centers to students and manage the centers.
   * Exam department can see the exam registration form of a student by entering their USN.
2. Student login:
   * Students can automatically fill the registration form provided to them.
   * After submission of the registration details, the fee payment status is checked and meanwhile students should wait for the Hall ticket which will be sent through mail.
3. Bank login:
   * Bank can update the fee payment status of the student.
4. Staff login:
   * Staff can manage the courses.
   * Staff can manage the attendance details of the student.
5. College Admin login:
   * College administration staff can manage the student data.
