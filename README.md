# Music Management Web

A Flask-based web application for managing your music collection with MongoDB as the database backend. This project allows users to add, organize, and manage their favorite songs with album artwork and detailed information.

## Features

- **Add New Songs**: Add songs with title, artist, year, album, and album artwork
- **Favorite System**: Mark songs as favorites with a star rating system
- **Visual Interface**: Display album artwork in a card-based layout
- **Responsive Design**: Mobile-friendly interface that adapts to different screen sizes
- **Database Integration**: Persistent storage using MongoDB
- **CRUD Operations**: Create, read, update, and delete music entries

## Technologies Used

### Frontend
- **HTML5**: Structure and semantic markup
- **CSS3**: Styling with responsive design and modern layouts
- **Jinja2**: Template engine for dynamic content rendering

### Backend
- **Python 3**: Core programming language
- **Flask**: Lightweight web framework for handling routes and requests
- **PyMongo**: MongoDB driver for Python

### Database
- **MongoDB**: NoSQL database for storing music collection data
- **MongoDB Atlas**: Cloud-hosted MongoDB service

## Project Structure

```
music-management-web/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── LICENSE.txt           # MIT License
├── README.md             # Project documentation
├── playground-1.mongodb.js # MongoDB setup script
│
├── static/
│   └── css/
│       └── style.css     # Main stylesheet
│
└── templates/
    └── index.html        # Main HTML template
```

## Installation

### Prerequisites
- Python 3.7 or higher
- MongoDB Atlas account (or local MongoDB installation)
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd music-management-web
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory with your MongoDB credentials:
   ```env
   USUARIO=your_mongodb_username
   CONTRASENA=your_mongodb_password
   NOMBRE_CLUSTER=your_cluster_name
   NOMBRE_DB=your_database_name
   ```

5. **Database Setup**
   - Create a MongoDB Atlas cluster
   - Create a database and collection named "Musics"
   - Update the connection string in your `.env` file

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   Open your browser and navigate to `http://localhost:5000`

3. **Add music**
   - Fill in the form with song details
   - Provide a valid URL for the album artwork
   - Click "Afegir" (Add) to save the song

4. **Manage your collection**
   - Click the star button to add/remove favorites
   - Use the delete button to remove songs
   - Browse your collection in the card layout

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display the main page with music collection |
| POST | `/Musics` | Add a new song to the collection |
| POST | `/Musics/<titulo>/favorito` | Mark a song as favorite |
| POST | `/Musics/<titulo>/nofavorito` | Remove favorite status |
| POST | `/Musics/<titulo>/eliminar` | Delete a song from collection |

## Database Schema

The application uses a MongoDB collection called "Musics" with the following document structure:

```json
{
  "titulo": "Song Title",
  "artista": "Artist Name",
  "ano": "Release Year",
  "album": "Album Name",
  "foto": "Album Artwork URL",
  "enFavorito": false
}
```

## Features in Detail

### Responsive Design
- Mobile-first approach with CSS media queries
- Flexible grid layout that adapts to screen size
- Touch-friendly buttons and navigation

### Favorite System
- Visual indicators with star icons
- Favorites appear first in the collection
- Toggle functionality for easy management

### Error Handling
- Form validation for required fields
- Database connection error handling
- Graceful fallbacks for missing images

## Development

### Running in Development Mode
The application runs in debug mode by default, providing:
- Automatic reloading on code changes
- Detailed error messages
- Development server on port 5000

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

- Built as a class project for learning web development with Flask and MongoDB
- Demonstrates modern web development practices with Python
- Responsive design principles for cross-device compatibility
