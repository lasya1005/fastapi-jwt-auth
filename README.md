# User Authentication System with JWT, FastAPI, and MongoDB

This project implements a secure user authentication system using **FastAPI**, **JWT** (JSON Web Tokens), and **MongoDB**. It includes user registration, login/logout, password hashing, and **Role-Based Access Control (RBAC)**. The system is designed to handle basic CRUD operations and ensure secure endpoints.

## Features
- User Registration and Login with Password Hashing
- JWT-based Authentication with Token Expiry
- Role-Based Access Control (RBAC)
- Basic CRUD operations for user management
- Logging and Scalability support

## Technologies Used
- **FastAPI**: Framework for building APIs.
- **MongoDB (Atlas)**: Database for user data storage.
- **JWT**: Secure token-based authentication.
- **bcrypt**: Hashing for secure password storage.
- **Pydantic**: Data validation and settings management.

## Project Structure
``
project_root/
│
├── app/
│   ├── main.py                  # Main application file
│   ├── models.py                # User and token models
│   ├── config.py                # Project configurations
│   ├── auth/
│   │   ├── jwt_handler.py       # JWT creation and decoding functions
│   │   └── auth_routes.py       # Authentication routes
│   ├── crud/
│   │   ├── user_crud.py         # User creation and verification functions
│   │   └── role_based_access.py # Role-based access control
│   ├── utils/
│   │   └── logger.py            # Logger setup for request logging
│
├── scripts/
│   └── create_user.py           # Script for creating a test user
│
├── .env                         # Environment variables file
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```
