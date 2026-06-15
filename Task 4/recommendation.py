movies = {
    "action": ["Avengers", "John Wick", "Mad Max"],
    "comedy": ["The Mask", "Mr. Bean", "Home Alone"],
    "horror": ["Conjuring", "Insidious", "Annabelle"]
}

genre = input("Enter genre (action/comedy/horror): ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Genre not found.")
