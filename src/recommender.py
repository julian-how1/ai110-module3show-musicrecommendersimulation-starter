import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into dicts, converting numeric columns to int/float."""
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

# Groups of genres/moods considered "similar" to each other (worth half points)
GENRE_FAMILIES = [
    {"pop", "indie pop", "synthwave", "edm"},
    {"lofi", "ambient", "jazz", "classical"},
    {"rock", "metal"},
    {"hip-hop", "r&b", "reggae", "latin"},
    {"country", "folk", "blues"},
]

MOOD_FAMILIES = [
    {"happy", "euphoric", "energetic", "confident"},
    {"chill", "relaxed", "peaceful", "laid-back", "focused", "romantic"},
    {"intense", "angry"},
    {"sad", "melancholic", "nostalgic", "moody"},
]

def _category_points(preferred: Optional[str], actual: str, families: List[set], full_points: float) -> float:
    """Returns full points for an exact match, half for a similar category, otherwise 0."""
    if not preferred:
        return 0.0
    preferred, actual = preferred.lower(), actual.lower()
    if preferred == actual:
        return full_points
    if any(preferred in family and actual in family for family in families):
        return full_points / 2
    return 0.0

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences, returning (score, list of reasons)."""
    score = 0.0
    reasons = []

    # Genre: 2.0 for exact match, 1.0 for a similar genre
    genre_points = _category_points(user_prefs.get("genre"), song["genre"], GENRE_FAMILIES, 2.0)
    if genre_points == 2.0:
        reasons.append(f"genre matches {song['genre']} (+2.0)")
    elif genre_points > 0:
        reasons.append(f"{song['genre']} is similar to {user_prefs['genre']} (+{genre_points:.1f})")
    score += genre_points

    # Mood: 1.0 for exact match, 0.5 for a similar mood
    mood_points = _category_points(user_prefs.get("mood"), song["mood"], MOOD_FAMILIES, 1.0)
    if mood_points == 1.0:
        reasons.append(f"mood matches {song['mood']} (+1.0)")
    elif mood_points > 0:
        reasons.append(f"{song['mood']} mood is similar to {user_prefs['mood']} (+{mood_points:.1f})")
    score += mood_points

    # Energy: up to 1.5, scaled by how close the song is to the target energy
    if "energy" in user_prefs:
        energy_points = 1.5 * (1 - abs(user_prefs["energy"] - song["energy"]))
        reasons.append(f"energy {song['energy']:.2f} vs target {user_prefs['energy']:.2f} (+{energy_points:.2f})")
        score += energy_points

    # Acousticness: up to 0.5, rewarding acoustic songs if the user likes them, electronic otherwise
    if "likes_acoustic" in user_prefs:
        acoustic_fit = song["acousticness"] if user_prefs["likes_acoustic"] else 1 - song["acousticness"]
        acoustic_points = 0.5 * acoustic_fit
        reasons.append(f"acousticness {song['acousticness']:.2f} (+{acoustic_points:.2f})")
        score += acoustic_points

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song and returns the top k as (song, score, explanation), highest first."""
    # Score every song once, keeping (song, score, explanation) together
    scored = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    # Highest score first, then keep the top k
    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
