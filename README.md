# Parking FastAPI

## 🚀 Introduction
Parking FastAPI is a web server for managing a car parking service. It allows users to register, rent parking lots, create new lots, and retrieve parking lot information. The system also provides admin functionalities for managing parking slots and user accounts. Payments are handled through a client management system, and drivers are available to assist with vehicle repositioning.

## 📌 Features
- User registration and authentication
- Booking and renting of parking slots
- Admin control over parking slots (create, update, delete)
- Password reset functionality
- Secure password hashing and email notifications
- PostgreSQL database integration
- FastAPI for high-performance API development

## 🛠️ Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- PostgreSQL (for database storage)
- Virtual environment (optional but recommended)

### Steps
```bash
# Clone the repository
git clone https://github.com/jidris-spec/Parking-FastApi.git
cd Parking-FastApi

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (example for .env file)
cp .env.example .env

# Apply database migrations
python scripts/add_columns.py

# Start the FastAPI server
uvicorn app.main:app --reload
```

## 🔥 API Endpoints

### **Authentication & Users**
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - List all users
- `GET /api/v1/users/{user_id}` - Retrieve user details by ID
- `PATCH /api/v1/users/{user_id}` - Update user details
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/forgot-password` - Send password reset email
- `POST /api/v1/auth/reset-password` - Reset user password

### **Parking Slots & Bookings**
- `POST /api/v1/slots/` - Create a new parking slot (admin only)
- `GET /api/v1/slots/` - List available parking slots
- `PATCH /api/v1/slots/{slot_id}` - Update slot details
- `DELETE /api/v1/slots/{slot_id}` - Delete a parking slot
- `POST /api/v1/bookings/` - Book a parking slot
- `GET /api/v1/bookings/` - List all bookings
- `DELETE /api/v1/bookings/{booking_id}` - Cancel a booking

## 📜 Database Schema
The system uses PostgreSQL, and key tables include:
- `users`: Stores user details
- `slots`: Stores parking slot information
- `bookings`: Manages user reservations

## 🎯 Contribution
We welcome contributions! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to GitHub and create a pull request

## 📝 License
This project is licensed under the MIT License.

## 📞 Contact
For support or inquiries:
- **GitHub**: [jidris-spec](https://github.com/jidris-spec)
- **Email**: your-email@example.com

