print("Welcome To Mad Libs Game! 🎮")

playing = input("Let's Play, Shall We? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time! 😊")
    quit()

print("Okay, let's play the game! \n")

# Get user inputs
noun1 = input("Enter Your Name: ")
noun2 = input("Enter Your Friend's Name: ")
noun3 = input("Enter Another Friend's Name: ")
place = input("Enter a Place Name: ")
adjective1 = input("Enter an Adjective: ")
adjective2 = input("Enter Another Adjective: ")
adjective3 = input("Enter One More Adjective: ")
adverb1 = input("Enter an Adverb: ")
adverb2 = input("Enter Another Adverb: ")
exclamation = input("Enter an Emotion: ")

# Create the Mad Libs story
story = (
    f"One day, {noun1} went to {place}. "
    f"He felt very lonely, even though the view was {adjective1}. "
    f"He decided to call his friends {noun2} and {noun3}.\n"
    f"When they came, they told {noun1} something {adjective2} had happened. "
    f"{noun1} went there very {adverb1}. "
    f"When he arrived, he found out that his other friend was falling off a cliff! "
    f"{noun1} said, '{exclamation}!' Inside, he was feeling {adjective3}. "
    f"{noun1} managed to save him. "
    f"After that, they had a {adverb2} celebration 🎉. "
    f"They all laughed 😂 and lived happily ever after!"
)

# Print the story
print("\nHere's your Mad Libs story:\n")
print(story)