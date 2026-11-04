posts = [
    "New campus coffee shop opens",
    "Python workshop this Friday",
    "Robotics club builds a drone",
    "Students launch a weather app",
    "Hackathon registration is open",
    "New library study spaces",
    "Campus Wi-Fi gets upgraded",
    "CS students build a game",
]

PAGE_SIZE = 3


def fetch_page(page):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    return posts[start:end]


page = 0
feed = []

while True:
    action = input("\nScroll? (y/n): ").strip().lower()

    if not posts:
        print("No more posts.")
        break   

    for post in fetch_page(page):
        feed.append(post)
        print("\nYour Feed:")
        print("-", post)

    print(f"\nLoaded {len(feed)} new posts.")

    if len(posts) < PAGE_SIZE or len(feed) == len(posts):
        print("No more posts.")
        break   

    while True:
        action = input("\nScroll? (y/n): ").strip().lower()
        
    if action == 'y':
        page += 1
        break
    elif action == 'n':
        print("Session ended.")
        break
    else:
        print(" Enter 'y' or 'n' ")

    if action == "n":
        break

print("Session ended.")
