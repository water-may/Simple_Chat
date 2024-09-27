# Simple_Chat

A full-stack chat application demonstrating real-time communication using Django, Django Rest Framework, Django Channels, and React. The goal of this project is to create a modern web chat application with WebSocket support for real-time messaging and API-based interactions.

## Key Technologies

- **Django Rest Framework**: Handles RESTful API endpoints.
- **Django Channels**: Enables WebSocket communication for real-time functionality.
- **React**: Provides a dynamic and responsive user interface.
- **Redis**: Acts as the message broker for Django Channels.
- **PostgreSQL**: Backend database to store user data and chat messages.

## Features

- **User Authentication**: Login and registration system using Django's built-in authentication.
- **Real-time Messaging**: Using WebSockets to send and receive messages without refreshing the page.
- **Chat Rooms**: Users can create and join chat rooms.
- **Message History**: Persistent chat messages stored in the database.
- **React Frontend**: Built with React, providing a single-page application (SPA) experience.
- **API-Driven**: RESTful API endpoints for managing users, messages, and chat rooms.

## Project Structure

```plaintext
Simple_Chat/
├── backend/                # Django project folder
│   ├── chat/               # Django app handling chat functionality
│   ├── users/              # Django app managing user authentication
│   ├── settings.py         # Django project settings
│   └── manage.py           # Django management script
├── frontend/               # React frontend
│   ├── public/             # Public folder for static files
│   ├── src/                # React source code
│   └── package.json        # Frontend dependencies
└── requirements.txt        # Backend Python dependencies
```

## Setup Instructions

### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/water-may/Simple_Chat.git
   cd Simple_Chat/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for database and Redis configuration. You can use `.env` files or manually add them in `settings.py`.

5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```

2. Install the required npm packages:
   ```bash
   npm install
   ```

3. Run the React development server:
   ```bash
   npm start
   ```

The app should now be accessible at `http://localhost:3000`.

### Redis Setup

1. Install Redis and make sure it is running. Django Channels requires Redis as a message broker.

## Usage

- Users can create accounts, log in, and join chat rooms.
- Real-time messaging is supported within chat rooms.
- Persistent message history is saved in the database for each chat room.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
