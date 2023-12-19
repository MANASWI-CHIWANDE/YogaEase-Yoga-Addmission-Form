# YogaEase by Manaswi Chiwande

The Yoga Studio Management System is a web application built using the Flask web framework, designed to manage user registrations, class schedules, and payments for a yoga studio. The application uses SQLite as the database to store user information, class schedules, and payment records. The application is deployed on Render.

### Documentation is in YogaEase - Manaswi.docx-pages pdf 
###
## Table of Contents

- [Features](#features)
- [Deployed on Render](#deployed-on-render)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Registration:** Clients can register with their name, email, age, and preferred batch timeslot.
- **Schedule Change:** Enrolled users can change their class timeslot.
- **Payment:** Users can make payments for their class enrollment.
- **SQLite Database:** Lightweight database for storing user, batch, enrollment, and payment information.
- **HTML/CSS/JavaScript:** Frontend components for a user-friendly interface.

## Deployed on Render
The application is deployed on Render - Cloud Application. You can access it https://yogaease-manaswi-yoga-admission.onrender.com

## Technologies Used

- **Flask:** Micro web framework for Python.
- **SQLite:** Lightweight, file-based relational database.
- **Waitress:** Production-ready WSGI server.
- **HTML/CSS/JavaScript:** Frontend development.

## Database Design Schema 
1. ER diagram
   ![WhatsApp Image 2023-12-19 at 12 33 15 PM (2)](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/be924037-09f7-4183-abfc-8b73ca66c939)
![WhatsApp Image 2023-12-19 at 12 33 15 PM (1)](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/531d6426-e33d-4d96-8334-d4c0b89de68d)
![WhatsApp Image 2023-12-19 at 12 33 15 PM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/aeb34922-c1c9-407c-a7f7-ac2a5f58c8b9)
![WhatsApp Image 2023-12-19 at 4 08 05 AM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/aa0cf591-4111-4cc7-b88e-d0941f22e87e)
![WhatsApp Image 2023-12-19 at 3 49 44 AM](https://github.com/MANASWI-CHIWANDE/YogaEase-Yoga-Addmission-Form/assets/86121472/5922c83c-c26b-4d76-9176-66e5d5a18f76)
3. nm
## Installation

1. Clone the repository:

   git clone https://github.com/your-username/yoga-studio-app.git
   cd yoga-studio-app
2. Create a virtual environment 
3. Install dependencies:pip install -r requirements.txt
4. Run the application:python app.py

