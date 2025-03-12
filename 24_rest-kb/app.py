from flask import Flask, request, redirect, session, jsonify, render_template
import requests
import base64
import os
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(32) 

# Spotify API Details (Need to create files for keys for this code to work!!)
with open("client_id.txt", "r") as key_file:
    CLIENT_ID = key_file.read().strip()
with open("client_secret.txt", "r") as key_file:
    CLIENT_SECRET = key_file.read().strip()
REDIRECT_URI = "http://localhost:5000/callback"
AUTHORIZATION_ENDPOINT = "https://accounts.spotify.com/authorize"
SPOTIFY_API_ME = "https://api.spotify.com/v1/me"
TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
SCOPE = "user-read-private user-read-email user-read-recently-played"

@app.route('/login')
def main():
    # Creates a random string of characters
    code_verifier = base64.urlsafe_b64encode(os.urandom(64)).decode('utf-8').rstrip('=')

    session['code_verifier'] = code_verifier
    print(session['code_verifier'])

    # Uses random string of characters and hashes it using SHA256
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode('utf-8').rstrip('=')

    # Building Spotify Auth URL
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': SCOPE,
        'redirect_uri': REDIRECT_URI,
        'code_challenge_method': 'S256',
        'code_challenge': code_challenge
    }
    
    auth_url = f"{AUTHORIZATION_ENDPOINT}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Retrieve the authorization code from the callback
    code = request.args.get('code')
    code_verifier = session.get('code_verifier')

    if not code_verifier:
        return "Code verifier missing", 400

    # Exchange the authorization code for an access token
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'code_verifier': code_verifier
    }

    token_response = requests.post(TOKEN_ENDPOINT, data=token_data)
    token_json = token_response.json()

    if token_response.status_code != 200:
        return jsonify(token_json), token_response.status_code

    # Store the token in the session
    session['access_token'] = token_json.get('access_token')
    session['refresh_token'] = token_json.get('refresh_token')
    session['expires_in'] = token_json.get('expires_in')

    # Redirect to profile page after successful authentication
    return redirect('/profile')

    
@app.route('/refresh')
def refresh_token():
    refresh_token = session.get('refresh_token')
    if not refresh_token:
        return "No refresh token available", 400

    token_data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID
    }

    token_response = requests.post(TOKEN_ENDPOINT, data=token_data)
    token_json = token_response.json()

    # Update session with the new token
    session['access_token'] = token_json.get('access_token')
    session['expires_in'] = token_json.get('expires_in')

    return jsonify(token_json)

@app.route('/profile')
def profile():
    # Retrieve data from the session
    access_token = session.get('access_token')
    if not access_token:
        return redirect('/login')

    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch user profile data
    user_response = requests.get(SPOTIFY_API_ME, headers=headers)
    if user_response.status_code != 200:
        return f"Failed to fetch profile: {user_response.json()}", user_response.status_code

    user_data = user_response.json()
    name = user_data.get('display_name', 'Unknown')
    profile_pic = user_data.get('images', [])
    profile_pic = profile_pic[0]['url'] if profile_pic else None

    # Fetch recently played track
    recently_played_endpoint = "https://api.spotify.com/v1/me/player/recently-played?limit=1"
    recent_response = requests.get(recently_played_endpoint, headers=headers)

    if recent_response.status_code == 200:
        recent_data = recent_response.json()
        if recent_data.get('items'):
            track = recent_data['items'][0]['track']
            recent_track_name = track['name']
            recent_track_artist = ", ".join(artist['name'] for artist in track['artists'])
            recent_track_image = track['album']['images'][0]['url'] if track['album']['images'] else None
        else:
            recent_track_name = "No recently played tracks"
            recent_track_artist = ""
            recent_track_image = None
    else:
        recent_track_name = "Error fetching recently played track"
        recent_track_artist = ""
        recent_track_image = None

    # Fetch user's playlists
    playlists_endpoint = "https://api.spotify.com/v1/me/playlists"
    playlists_response = requests.get(playlists_endpoint, headers=headers)

    if playlists_response.status_code == 200:
        playlists_data = playlists_response.json()
        playlists = [
            {
                "name": playlist["name"],
                "image": playlist["images"][0]["url"] if playlist["images"] else None,
                "url": playlist["external_urls"]["spotify"]
            }
            for playlist in playlists_data.get("items", [])
        ]
    else:
        playlists = []

    # Render the profile page
    return render_template(
        'profile.html',
        name=name,
        profile_pic=profile_pic,
        access_token=access_token,
        refresh_token=session.get('refresh_token'),
        expires_in=session.get('expires_in'),
        recent_track_name=recent_track_name,
        recent_track_artist=recent_track_artist,
        recent_track_image=recent_track_image,
        playlists=playlists
    )



@app.route('/me')
def get_user_data():
    access_token = session.get('access_token')
    if not access_token:
        return redirect('/login')

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(SPOTIFY_API_ME, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)