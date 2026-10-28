"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(user_prefs, recommendations)


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Prints each recommendation with its title, score, and the reasons behind it."""
    divider = "=" * 60
    profile = ", ".join(f"{key}={value}" for key, value in user_prefs.items())

    print(f"\n{divider}")
    print(f"  Top {len(recommendations)} Recommendations")
    print(f"  Profile: {profile}")
    print(divider)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Why:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")

    print(f"\n{divider}")


if __name__ == "__main__":
    main()
