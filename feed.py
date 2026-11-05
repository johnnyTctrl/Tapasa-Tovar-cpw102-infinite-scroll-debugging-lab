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
    current_posts = fetch_page(page)

    if not current_posts:
        print("No more posts.")
        break 

    for post in current_posts:
        feed.append(post)

    print("\nYour Feeed:")
    for post in feed:
        print("_", post)
    print(f"\nTotal posts loaded: {len(feed)}")
    if len(current_posts) < PAGE_SIZE or len(feed) == len(posts):
     print("No more posts.")
     break

    
    while True:
        action = input("\nScroll? (y/n): ").strip().lower()
            
        if action == 'y':
            page += 1
            break
        elif action == 'n':
            break
        else:
             print(" Enter 'y' or 'n' ")

    if action == 'n':       
     break   
print("Session ended.")
