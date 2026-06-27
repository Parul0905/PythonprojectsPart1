import textwrap

def bio_gen():
    name       = input('Enter your name: ').strip()
    profession = input('Enter your profession: ').strip()
    passion    = input('Enter your passion: ').strip()
    emoji      = input('Enter your favourite emoji: ').strip()
    website    = input('Enter your website: ').strip()

    bio = (
        f"Hello, everyone! My name is {name}, "
        f"I am a {profession}, I love doing {passion}. "
        f"If anyone wants to connect, here is my website: {website}\n{emoji}"
    )

    print(bio)

    save = input('Do you want to save this file? (y/n): ').lower().strip()

    if save == 'y':
        filename = f"{name.lower().replace(' ', '_')}_bio.txt"  # fixed: double quotes wrap, single inside
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(bio)
        print(f"Bio saved to '{filename}'!")

bio_gen()

