# YogaEase by Manaswi Chiwande

The YogaEase is a web application built using the Flask web framework, designed to manage user registrations, class schedules, and payments for a yoga studio. The application uses SQLite as the database to store user information, class schedules, and payment records. The application is deployed on Render.


### Documentation is in "YogaEase - Manaswi.docx-pages.pdf"


###
## Table of Contents

- [Features](#features)
- [Deployed on Render](#deployed-on-render)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Design](#database-design)
- [FrontEnd Design](#frontend-design)
- [Backend Design](#backend-design)





## Features

- **User Registration:** Clients can register with their name, email, age, and preferred batch timeslot.
- **Schedule Change:** Enrolled users can change their class timeslot.
- **Payment:** Users can make payments for their class enrollment.
- **SQLite Database:** Lightweight database for storing user, batch, enrollment, and payment information.
- **HTML/CSS/JavaScript:** Frontend components for a user-friendly interface.

## Deployed on Render
The application is deployed on Render - Cloud Application. You can access it https://yogaease-manaswi-yoga-admission.onrender.com
#### The extended loading time during the initial visit is primarily attributed to cold start delays as the server initializes as i'm using render free without any subscription.

## Technologies Used

- **Flask:** Micro web framework for Python.
- **SQLite:** Lightweight, file-based relational database.
- **Waitress:** Production-ready WSGI server.
- **HTML/CSS/JavaScript:** Frontend development.

## Database Design Schema 
#### 1. ER diagram
  


![WhatsApp Image 2023-12-19 at 3 49 44 AM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/5922c83c-c26b-4d76-9176-66e5d5a18f76)
 #### 2. Tables in Database 


![WhatsApp Image 2023-12-19 at 4 08 05 AM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/aa0cf591-4111-4cc7-b88e-d0941f22e87e)

#### 3. Registration flow

 ![WhatsApp Image 2023-12-19 at 12 33 15 PM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/b014f879-1f84-4e99-9c56-748b938d29d6)

####  4. Renewal Flow


   ![WhatsApp Image 2023-12-19 at 12 33 15 PM (1)](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/531d6426-e33d-4d96-8334-d4c0b89de68d)
#### 5. Payment Flow
In payment flow we assume , All the payment work and updating in database is done by Mock function complete payment. 
   
![WhatsApp Image 2023-12-19 at 12 33 15 PM (2)](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/61bfc90d-6b6b-4c14-b2e4-076d2572d508)


## Frontend Designs
#### 1. index page
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/de6f0e7f-f795-472e-819e-76b35a6104f0)

#### 2. register page
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/68b7b74a-0037-43ce-a01b-be7ba4ed16c2)

#### 3. renew page
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/876d32c6-f56e-442a-8d8a-b730ea590d2f)

#### 4. payment page
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/a57a90e3-fd3c-4bea-8a0a-6dafd4a243c3)



## Backend Designs
#### 1. Validation page

![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/e359f133-94df-40cc-aff2-a228803120ff)

![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/5d7f47a7-2306-417d-bde0-be1748404852)

### Data entered in form is stored in sqlite database named yoga.db
#### 1. User Table
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/8be88f8f-8303-408a-99ff-7916ca8bc02e)
#### 2. Batch Table
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/ad2e5d45-15b8-44d0-8476-4197d16e9d44)

#### 3. Enrollment Table
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/382fa23c-0de2-493e-aa94-7ffb15c3bf63)

#### 4. payment page
![image](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/c5175528-d1a7-4a25-afec-6e94072dbd84)


## Installation

1. Clone the repository:

   git clone https://github.com/your-username/yoga-studio-app.git
   cd yoga-studio-app
2. Create a virtual environment 
3. Install dependencies:pip install -r requirements.txt
4. Run the application:python app.py

