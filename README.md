# Web3 Decentralized Identity Verifier

## Overview
The Web3 Decentralized Identity Verifier is an innovative platform that leverages blockchain technology to offer secure and reliable identity management solutions. This project provides a comprehensive and user-friendly interface for creating, managing, and verifying decentralized identities (DIDs). By utilizing FastAPI for backend operations and a lightweight SQLite database, the application ensures privacy and reliability for its users. It is particularly beneficial for developers, organizations, and individuals who are looking to implement decentralized identity verification systems.

In today's digital age, traditional identity verification methods often fall short in terms of security and user control. This project addresses these challenges by decentralizing identity management, allowing users to maintain control over their personal data and significantly reducing the risk of identity theft and fraud.

## Features
- **Decentralized Identity Creation**: Users can easily create new identities with a unique DID, name, and email.
- **Identity Verification**: A simple and efficient process to verify identities.
- **Identity Management**: Users can view and manage all created identities in a structured format.
- **Responsive Web Interface**: User-friendly web pages for creating, verifying, and managing identities.
- **Secure Data Handling**: Utilizes SQLite for secure and efficient data storage.
- **Mock Verification Logic**: Simulates verification processes for demonstration purposes.
- **Static File Serving**: Includes CSS and JavaScript for enhanced user experience.

## Tech Stack
| Component     | Technology   |
|---------------|--------------|
| Backend       | FastAPI      |
| Frontend      | HTML/CSS/JS  |
| Database      | SQLite       |
| Web Server    | Uvicorn      |
| CSS Framework | Bootstrap    |
| Language      | Python 3.11+ |

## Architecture
The project consists of a FastAPI backend that serves a static HTML/CSS/JavaScript frontend. The backend handles API requests for identity creation, retrieval, and verification, while the frontend provides a user interface for interacting with these functionalities.

### Project Structure
```plaintext
web3-decentralized-identity-verifier-auto/
│
├── app.py                      # Main application file with API logic
├── Dockerfile                  # Docker configuration for containerization
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the application
├── static/                     # Static files directory
│   ├── bootstrap.min.css       # Bootstrap CSS for styling
│   ├── css/
│   │   └── style.css           # Custom CSS for additional styling
│   └── js/
│       └── main.js             # JavaScript for frontend interactions
├── templates/                  # HTML templates for web pages
│   ├── about.html              # About page
│   ├── create_identity.html    # Identity creation page
│   ├── index.html              # Home page
│   ├── manage_identities.html  # Identity management page
│   └── verify_identity.html    # Identity verification page
└── identities.db               # SQLite database file
```

### Data Flow Diagram
```plaintext
+-------------------------+
|       User Interface    |
| (HTML/CSS/JS Frontend)  |
+------------+------------+
             |
             v
+------------+------------+
|        FastAPI Backend  |
| (Handles API Requests)  |
+------------+------------+
             |
             v
+------------+------------+
|         SQLite Database |
| (Stores Identities and  |
| Verification Results)   |
+-------------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web3-decentralized-identity-verifier-auto.git
   cd web3-decentralized-identity-verifier-auto
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit `http://localhost:8000` to access the application.

## API Endpoints
| Method | Path                     | Description                            |
|--------|--------------------------|----------------------------------------|
| POST   | /api/identities          | Create a new user identity             |
| GET    | /api/identities          | Retrieve all user identities           |
| GET    | /api/identities/{id}     | Retrieve a specific user identity      |
| POST   | /api/verify              | Verify a user identity                 |

## Project Structure
```
web3-decentralized-identity-verifier-auto/
│
├── app.py                      # Main application file with API logic
├── Dockerfile                  # Docker configuration for containerization
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the application
├── static/                     # Static files directory
│   ├── bootstrap.min.css       # Bootstrap CSS for styling
│   ├── css/
│   │   └── style.css           # Custom CSS for additional styling
│   └── js/
│       └── main.js             # JavaScript for frontend interactions
├── templates/                  # HTML templates for web pages
│   ├── about.html              # About page
│   ├── create_identity.html    # Identity creation page
│   ├── index.html              # Home page
│   ├── manage_identities.html  # Identity management page
│   └── verify_identity.html    # Identity verification page
└── identities.db               # SQLite database file
```

## Screenshots
- Home Page
- Create Identity Page
- Verify Identity Page
- Manage Identities Page

## Docker Deployment
To build and run the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t web3-identity-verifier .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 web3-identity-verifier
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
Built with Python and FastAPI.