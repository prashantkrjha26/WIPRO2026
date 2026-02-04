from flask import Flask, jsonify, request

# Create Flask application
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Movie Ticket Booking"


# In-memory storage for movies
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    },
    {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 220
    },
    {
        "id": 103,
        "movie_name": "3 Idiots",
        "language": "Hindi",
        "duration": "2h 50m",
        "price": 200
    },
    {
        "id": 104,
        "movie_name": "Parasite",
        "language": "Korean",
        "duration": "2h 12m",
        "price": 230
    }
]

# In-memory storage for bookings
bookings = []


# Return all movies
@app.route("/api/movies", methods=["GET"])
def get_all_movies():
    return jsonify(movies), 200


# Return a movie by its ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


# Add a new movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.get_json()

    # Validate JSON input
    if not data:
        return jsonify({"error": "Invalid JSON input"}), 400

    movies.append(data)
    return jsonify(data), 201


# Update an existing movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()

    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie), 200

    return jsonify({"error": "Movie not found"}), 404


# Delete a movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted successfully"}), 200

    return jsonify({"error": "Movie not found"}), 404


# Book movie tickets
@app.route("/api/bookings", methods=["POST"])
def book_tickets():
    data = request.get_json()

    # Validate booking request
    if not data:
        return jsonify({"error": "Invalid booking data"}), 400

    movie_id = data.get("movie_id")
    seats = data.get("seats")

    # Validate required fields
    if not movie_id or not seats:
        return jsonify({"error": "movie_id and seats are required"}), 400

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "seats": seats,
                "price_per_seat": movie["price"],
                "total_price": seats * movie["price"]
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Movie not found"}), 404


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)
