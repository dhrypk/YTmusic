from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic()

# Root endpoint to list all available endpoints
@app.route("/", methods=["GET"])
def index():
    endpoints = {
        "/search": "Search for songs. Query parameter: 'q' (song name)",
        "/song": "Get song details. Query parameter: 'id' (videoId)",
        "/album": "Get album details. Query parameter: 'id' (albumId)",
        "/playlist": "Get playlist details. Query parameter: 'id' (playlistId)",
        "/artist": "Get artist details. Query parameter: 'id' (artistId)",
        "/recommendations": "Get recommendations based on a song. Query parameter: 'id' (videoId)"
    }
    return jsonify(endpoints)

# Endpoint to search for songs
@app.route("/search", methods=["GET"])
def search_song():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    results = ytmusic.search(query)
    return jsonify(results)

# Endpoint to get song details by videoId
@app.route("/song", methods=["GET"])
def get_song_details():
    video_id = request.args.get("id")
    if not video_id:
        return jsonify({"error": "Query parameter 'id' is required"}), 400
    details = ytmusic.get_song(video_id)
    return jsonify(details)

# Endpoint to get album details by browseId
@app.route("/album", methods=["GET"])
def get_album_details():
    album_id = request.args.get("id")
    if not album_id:
        return jsonify({"error": "Query parameter 'id' is required"}), 400
    details = ytmusic.get_album(album_id)
    return jsonify(details)

# Endpoint to get playlist details by playlistId
@app.route("/playlist", methods=["GET"])
def get_playlist_details():
    playlist_id = request.args.get("id")
    if not playlist_id:
        return jsonify({"error": "Query parameter 'id' is required"}), 400
    details = ytmusic.get_playlist(playlist_id)
    return jsonify(details)

# Endpoint to get artist details by artistId
@app.route("/artist", methods=["GET"])
def get_artist_details():
    artist_id = request.args.get("id")
    if not artist_id:
        return jsonify({"error": "Query parameter 'id' is required"}), 400
    details = ytmusic.get_artist(artist_id)
    return jsonify(details)

# Endpoint to get user recommendations
@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    video_id = request.args.get("id")
    if not video_id:
        return jsonify({"error": "Query parameter 'id' is required"}), 400
    recommendations = ytmusic.get_watch_playlist(video_id)["tracks"]
    return jsonify(recommendations)

# Vercel handler to expose the Flask app to serverless
def handler(request):
    return app(request.environ, start_response=lambda *args: None)
