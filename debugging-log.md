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

