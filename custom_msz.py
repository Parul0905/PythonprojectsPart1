emoji_map = {
    "happy": "😀",
    "sad": "😟",
    "angry": "😤",
    "extremely happy": "😂",
    "love": "🥰",
    "hug": "🫂",
    "kiss": "😘"
}

custom_messages = {
    "happy":          "Good to see you are happy today! Keep smiling! 😀",
    "sad":            "Aww, hope your day gets better soon! 😟",
    "angry":          "Take a deep breath, things will calm down! 😤",
    "extremely happy":"You're on fire today! Love the energy! 😂",
    "love":           "Spreading love is the best thing! 🥰",
    "hug":            "Sending you a big warm hug! 🫂",
    "kiss":           "Mwah! Hope your day is as sweet as you! 😘"
}

print("How are you feeling today? Choose from:")
for feeling, emoji in emoji_map.items():
    print(f"  {feeling} {emoji}")

message = input("\nYour feeling: ").strip().lower()

if message in emoji_map:
    print(custom_messages[message])
else:
    print("Hmm, I don't recognize that feeling. Try one from the list!")