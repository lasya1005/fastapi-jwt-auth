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

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd project_root
```

### 2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up MongoDB
   - [Sign up](https://www.mongodb.com/cloud/atlas) for MongoDB Atlas.
   - Create a new cluster and set up a **Database User** with read and write permissions.
   - Add your IP or use "Allow access from anywhere" under **Network Access**.
   - Copy the connection URI (replace `<username>` and `<password>` in the URI).

### 5. Configure Environment Variables
Create a `.env` file in the root directory and add your MongoDB URI, JWT secret, and token expiry:
```bash
MONGODB_URI="your_mongodb_uri"
JWT_SECRET_KEY="your_jwt_secret"
JWT_EXPIRY_MINUTES=30
```

### 6. Run the Application
```bash
uvicorn app.main:app --reload
```

The application will start on [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

### Authentication
- **POST /login**: Authenticates the user and returns a JWT if valid.
  - **Payload**: `{ "username": "example", "password": "password" }`
- **POST /register**: Registers a new user (use `create_user.py` for test registration).

### User Management (CRUD)
- **POST /users**: Create a new user (Admin-only).
- **GET /users**: Retrieve all users (Admin-only).
- **GET /users/{id}**: Retrieve a single user by ID (Admin-only).
- **PUT /users/{id}**: Update user details (Admin-only).
- **DELETE /users/{id}**: Delete user (Admin-only).

## Testing with Postman
1. **Import Endpoints**: Open Postman, create a new collection, and add the API endpoints.
2. **Environment Setup**: Add your local environment variables (base URL, token) to Postman.
3. **Login**: Send a POST request to `/login` to get a JWT. Use the token in the **Authorization** header (Bearer Token) for secured endpoints.
4. **Register New User**: Use `/register` to create test users.
5. **Testing RBAC**: Test role-based access by creating different roles and accessing the restricted endpoints.

## Troubleshooting
- **Database Connection Errors**: Verify MongoDB URI and network access.
- **JWT Errors**: Check `JWT_SECRET_KEY` and expiry time in `.env`.
- **Permissions**: Ensure RBAC is correctly implemented for each endpoint.
```
