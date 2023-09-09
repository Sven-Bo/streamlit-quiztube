# List of toast messages paired with their icons
TOAST_MESSAGES = [
    ("Ready to test your YouTube knowledge?", "🎥"),
    ("QuizTube welcomes you!", "🚀"),
    ("Think you caught all the details? Let's find out!", "🔍"),
    ("It's quiz time! No spoilers allowed.", "⏳"),
    ("Popped in for a quiz? You're in the right place!", "🍿"),
    ("Get your YouTube thinking cap on!", "🎓"),
    ("Your next YouTube challenge awaits!", "🏆"),
    ("Another video, another quiz!", "🔄"),
    ("Turn those video views into victories!", "🎖️"),
    ("Did you pay attention? It's quiz o'clock!", "⏰"),
    ("YouTube is fun, but quizzes? Even better!", "🎉"),
    ("Unleash your YouTube prowess here!", "🦸"),
    ("Knowledge check: Engage!", "🚦"),
    ("Video watched? Check. Quiz taken? Pending...", "✅"),
    ("Dive deeper into your YouTube content.", "🌊"),
    ("Up for a YouTube rewind in quiz form?", "⏪"),
    ("Let's decode your recent YouTube watch!", "🧩"),
    ("Adding some quiz spice to your YouTube binge!", "🌶️"),
    ("Transform your watch time into quiz time!", "🔄"),
    ("Here to validate your YouTube expertise?", "🔍")
]

def get_random_toast():
    """Returns a random toast message and icon."""
    import random
    return random.choice(TOAST_MESSAGES)