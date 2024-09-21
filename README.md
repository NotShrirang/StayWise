# StayWise

[![DB Diagram](https://img.shields.io/badge/DB%20Diagram-blue?style=for-the-badge&logo=sqlite&logoColor=white&logoSize=amd)](https://dbdiagram.io/d/64b9548802bd1c4a5e6c12d4)

![GitHub stars](https://img.shields.io/github/stars/NotShrirang/StayWise?style=social)
![GitHub forks](https://img.shields.io/github/forks/NotShrirang/StayWise?style=social)
![GitHub commits](https://img.shields.io/github/commit-activity/t/NotShrirang/StayWise)
![GitHub issues](https://img.shields.io/github/issues/NotShrirang/StayWise)
![GitHub pull requests](https://img.shields.io/github/issues-pr/NotShrirang/StayWise)
![GitHub](https://img.shields.io/github/license/NotShrirang/StayWise)
![GitHub last commit](https://img.shields.io/github/last-commit/NotShrirang/StayWise)
![GitHub repo size](https://img.shields.io/github/repo-size/NotShrirang/StayWise)

**StayWise** is a modern, intuitive, and feature-rich place booking platform built using Django Rest Framework (DRF). With StayWise, users can seamlessly search for places to stay, make reservations, and enjoy a comfortable, user-friendly booking experience similar to Airbnb.

## Features

- **Property Listings**: Hosts can list their places with detailed descriptions, pricing, and amenities like Wi-Fi, TV, and self-check-in options.
- **City-Based Search**: Users can search for places by city and view available properties in various locations.
- **Booking System**: Users can book available places by selecting check-in and check-out dates.
- **Guest Capacity Management**: Each place has a specific capacity, so users can filter based on the number of guests.
- **Ratings & Reviews**: Guests can leave ratings and remarks after their stay to help future users find the best places.
- **Image Gallery**: Hosts can upload multiple images of their property to give potential guests a virtual tour.
- **User Profiles**: Both hosts and guests can manage their profiles, bookings, and personal details like email and phone.
- **Pet-Friendly Options**: Users can filter places that allow pets for their stay.
- **Self-Check-In**: Some places allow users to check in at their convenience.
- **Wi-Fi Availability**: Search for properties based on Wi-Fi availability.

## Tech Stack

- **Backend**: Django Rest Framework (DRF)
- **Database**: By default SQLite3, but you can configure any database supported by Django.
- **Authentication**: JWT-based authentication for secure login and registration.
  
## Installation

To run StayWise locally, follow these steps:

### Prerequisites

- Python 3.8+
- Virtual environment tool (e.g., `virtualenv` or `conda`)

### Steps

1. **Clone the repository**:
   ```bash
     git clone https://github.com/NotShrirang/StayWise.git
     cd StayWise
   ```
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the app: Open your browser and visit http://127.0.0.1:8000/ to start exploring StayWise.

### Contributing
We welcome contributions! To contribute, fork the repository and create a pull request. Please make sure your changes are well-documented and pass all tests.

### License
StayWise is licensed under the GPLv3 License. See LICENSE for more information.
