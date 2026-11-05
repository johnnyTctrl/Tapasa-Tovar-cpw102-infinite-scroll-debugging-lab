# Incident Note — INC-204

**Responders:**

## Investigation log

Record **every debugging step in chronological order as you work**, including unsuccessful attempts and changes you undo. Commit your work as you go. 

For each step, briefly note what you tried and why, what you observed, and what you concluded or decided to try next.

Include relevant inputs, code changes, or output so someone else can follow your investigation. 

Use numbered entries or timestamps. Use Markdown formatting to make it easy to read.

## Resolution

Explain the causes, your repairs, and the evidence that verifies them. Identify
anything still uncertain or unresolved. Make code changes in `feed.py`.

--ran the code with 'y' as it is the program returned Your Feed:

- New campus coffee shop opens
- Python workshop this Friday
- Robotics club builds a drone
- New campus coffee shop opens
- Python workshop this Friday
- Robotics club builds a drone
- New campus coffee shop opens
- Python workshop this Friday
- Robotics club builds a drone
- New campus coffee shop opens
- Python workshop this Friday
- Robotics club builds a drone

Loaded 12 posts.

-- added if not new_posts:
        print("No more posts to load.")
        break this stops the loop when there are no more posts available

-- added =+ 1 it allows the program to run to the next page 

-- after adding our changes 
Your Feed:
- New campus coffee shop opens
- Python workshop this Friday
- Robotics club builds a drone
- Students launch a weather app
- Hackathon registration is open
- New library study spaces
- Campus Wi-Fi gets upgraded
- CS students build a game

Loaded 8 posts

Scroll? (y/n): Y

No more posts to load.
Session ended.

This is the results we have gotten 

-- When typed Maybe into the terminal the program returns session ended.
-- added  if action == 'y':
        page += 1
        break
    elif action == 'n':
        print("Session ended.")
        break added this so that if the user enters y it will add 1 
        if the user enters N it will break print session end 

 -- moved  print("\nYour Feed:") from line 33 to line 31 because my program kept running Your Feed: before every individual post
 causing it to look spaced out like this.
 
  Your Feed:
- New library study spaces

Loaded 3 new posts.

Scroll? (y/n): y

Your Feed:
- Campus Wi-Fi gets upgraded

Your Feed:
- CS students build a game

-- with moving it to line 31 it took your feed out of the loop 
