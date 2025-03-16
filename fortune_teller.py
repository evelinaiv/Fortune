pip install transformers

from transformers import pipeline
import streamlit as st
import random

# Load the NLP fill-mask model
fill_mask = pipeline("fill-mask", model="bert-base-uncased")
default_names = ["Sidant", "Yeni", "Matt", "Yarkin", "Shreyas", "Gagun", "Angel", "Sevda", "Kiki", "Yani", "Lora", "Saba", "Liv"]

funny_jobs = [
    "time traveler recruiter", "bubble wrap popper", "dinosaur therapist", "emoji translator", "jellybean taste tester",
    "professional cloud gazer", "extreme ironing champion", "space janitor", "chief pizza inspector", "undercover sock thief",
    "reality TV script writer", "secret agent for pigeons", "professional sneezer", "ghost negotiator", "left sock specialist",
    "meme stock analyst", "high-altitude balloon artist", "eternal intern", "karaoke coach", "unofficial time machine tester",
    "professional coin flipper", "wizard hat designer", "AI therapist", "sandcastle architect", "unlucky fortune cookie writer",
    "paranormal pizza delivery driver", "CEO of Procrastination", "underground tunnel explorer", "gravity tester", "professional echo locator",
    "intergalactic tour guide", "invisible ink manufacturer", "toy unboxer", "galactic mail carrier", "chocolate engineer",
    "extreme hide-and-seek champion", "tinfoil hat consultant", "hamster trainer", "UFO documentation specialist", "underwater tea brewer",
    "llama stylist", "space pirate", "robot repair specialist", "thumb wrestling coach", "world’s slowest runner",
    "cheeseburger model", "wand tester at Hogwarts", "multiverse detective", "social media fortune teller", "haunted doll babysitter"
]

celebrities = [
    "SpongeBob SquarePants", "Darth Vader", "Pikachu", "Gandalf", "Sherlock Holmes",
    "Batman", "Yoda", "Patrick Star", "Loki", "Winnie the Pooh",
    "Count Dracula", "Jack Sparrow", "Garfield", "Rick Sanchez", "Shrek",
    "Barney the Dinosaur", "Optimus Prime", "Tony Stark", "Homer Simpson", "Deadpool",
    "Katniss Everdeen", "Gollum", "Sonic the Hedgehog", "Thor", "Walter White",
    "Mr. Monopoly", "Johnny Bravo", "Dobby the House Elf", "Donkey from Shrek", "The Joker",
    "Goofy", "Mickey Mouse", "Buzz Lightyear", "Megatron", "Elmo",
    "Bigfoot", "Michael Scott", "Spock", "Cookie Monster", "Mario",
    "Luigi", "C-3PO", "Waluigi", "Wolverine", "Bugs Bunny",
    "Tom & Jerry", "Sailor Moon", "Fred Flintstone", "Popeye", "The Pink Panther"
]

random_objects = [
    "a radioactive rubber duck", "a diamond-encrusted skateboard", "a cursed karaoke machine", "a self-aware avocado",
    "a time-traveling umbrella", "a levitating goldfish bowl", "a turbo-powered toaster", "a talking backpack",
    "a pocket-sized dragon", "a pizza-scented candle", "a screaming watermelon", "a musical toothbrush",
    "a haunted fidget spinner", "a rainbow-colored banana", "a teleporting sock", "a never-ending spaghetti strand",
    "a flying jellybean", "a VHS tape from the future", "a self-tying shoelace", "a quantum yo-yo",
    "a secret teleporting notebook", "a pair of dancing shoes", "a coffee mug that never empties",
    "a holographic pet rock", "a robotic fortune cookie", "a chessboard that plays itself", "a book that reads you",
    "a camera that only captures embarrassing moments", "a cloud in a jar", "a shape-shifting pillow",
    "a rubber chicken that grants wishes", "a sock that always disappears", "a key that unlocks nothing",
    "a smartphone powered by laughter", "a magic eight ball that lies", "a chair that remembers who sat on it last",
    "a glow-in-the-dark invisible cloak", "a whistle that summons ducks", "a mirror that shows your best dance moves",
    "a pen that writes in the air", "a pair of gloves that make everything feel squishy"
]

superpowers = [
    "summon an army of squirrels", "turn everything they touch into spaghetti", "breathe underwater but only in bathtubs",
    "control the weather but only on Tuesdays", "speak in perfect rhyme", "make people instantly forget their last sentence",
    "glow in the dark", "run at lightning speed but only backwards", "become invisible when nobody is looking",
    "teleport to anywhere but your intended destination", "never run out of battery on your phone",
    "control plants but only sunflowers", "be able to pause time but only for 3 seconds", "always win at rock-paper-scissors",
    "understand any language except your own", "teleport but only inside closets", "turn any drink into coffee",
    "see into the future but only 10 seconds ahead", "memorize any book instantly but forget it after a week",
    "summon any object, but it’s always slightly broken", "understand what babies are saying", "sneeze confetti",
    "control Wi-Fi signals", "become temporarily weightless when sneezing", "predict the weather with 50% accuracy",
    "turn invisible when embarrassed", "speak fluent dolphin", "talk to statues", "control vending machines with your mind",
    "stop time, but only for hiccups", "see through walls, but only when your eyes are closed", "jump exactly 3 inches higher than normal",
    "always know where the nearest taco truck is", "become extremely lucky but only when playing board games",
    "never get sunburned", "fall asleep instantly when counting sheep", "know exactly when the toast will pop",
    "be able to dodge raindrops perfectly", "turn into a different version of yourself in every mirror reflection"
]

locations = [
    "a floating castle", "a neon city in the clouds", "the lost city of Atlantis", "a post-apocalyptic mall",
    "a giant treehouse with Wi-Fi", "a spaceship orbiting Pluto", "a submarine town under the Pacific",
    "a town run by intelligent cats", "a village where everyone speaks only in riddles", "a theme park built inside a volcano",
    "a hidden underground civilization", "a secret moon base", "a hotel that travels through dimensions",
    "a skyscraper taller than the atmosphere", "a town where everyone is a clone of you", "an abandoned amusement park",
    "a floating market on a river of soda", "a library that never ends", "a train that never stops moving",
    "a village where time runs backwards", "a city inside a giant bubble", "a floating pirate island",
    "a kingdom ruled by ghosts", "a reality TV show where you’re the main character", "a world made entirely of LEGO",
    "a swamp filled with glowing mushrooms", "a sky-high rollercoaster city", "a circus where the clowns are the audience",
    "a school for time travelers", "a city where all animals talk"
]

random_events = [
    "a worldwide hide-and-seek championship", "the day the internet disappeared", "an AI uprising that only wants free pizza",
    "the biggest prank war in history", "a sudden explosion of flying pigs", "a flash mob that never ends",
    "the great global pillow fight", "an asteroid made entirely of cheese", "a volcano erupting glitter",
    "a talking goldfish predicting the future", "the accidental discovery of a parallel universe",
    "a fashion trend where everyone wears capes", "the world’s first ever flying bicycle",
    "an island that appears only once every 100 years", "the invention of smell-based social media",
    "a dance battle that determines world leaders", "a UFO landing in the middle of a football game",
    "a hamster-powered energy crisis", "a rogue AI developing its own comedy show",
    "the mysterious case of the never-melting snowman", "a dog that becomes mayor", "a giant taco falling from space"
]
# 🎭 Mode Toggle (Mad Libs Mode = False, Fortune Mode = True)
st.title("🔮 AI Fortune Teller & Mad Libs 🔮")
mode = st.toggle("🔁 Toggle Fortune Mode", value=False)  # Default: Mad Libs Mode

# User Inputs
name = st.text_input("🌟 What is your name?") or random.choice(default_names)
job = st.text_input("👩‍🚀 Add a job") or random.choice(funny_jobs)
celeb = st.text_input("🎤 Add a celebrity") or random.choice(celebrities)
obj = st.text_input("🛠️ Add a random object") or random.choice(random_objects)
power = st.text_input("⚡ Add a superpower") or random.choice(superpowers)
location = st.text_input("🌍 Add a location") or random.choice(locations)
event = random.choice(random_events)


# Function to Capitalize Sentences Properly
def capitalize_sentences(text):
    sentences = text.split(". ")
    return ". ".join(sentence.capitalize() for sentence in sentences)


# List of Fortune Templates
madlibs_templates = [
    f"One day, {name}, a renowned {job}, stumbles upon {obj} while on a mission to {location}. "
    f"Unbeknownst to them, this object grants the power to {power}. However, their joy is short-lived when {celeb} challenges them, "
    f"leading to {event}.",
    
    f"After a bizarre turn of events, {name} is appointed as the official {job} of {location}. "
    f"Things take a weirder turn when they discover {obj}, which unexpectedly gives them the power to {power}. "
    f"Unfortunately, {celeb} is not amused and arrives to settle the matter, leading to {event}.",
    
    f"While enjoying their life as a {job}, {name} accidentally activates {obj}, which transports them straight to {location}. "
    f"There, they discover they can {power}, but before they can celebrate, {celeb} arrives, accusing them of causing {event}.",
    
    f"{name} never expected that being a {job} would lead them to a secret mission in {location}. "
    f"But when they find {obj}, everything changes—especially after it grants them the power to {power}. "
    f"However, just as they begin to test their new ability, {celeb} appears, demanding a duel, which results in {event}.",
    
    f"Legend tells of a {job} named {name} who found {obj} hidden deep in {location}. "
    f"The object bestowed upon them the power to {power}, making them an instant legend. "
    f"But their fame didn't sit well with {celeb}, who arrived to challenge them, leading to {event}.",
    
    f"While working as a {job}, {name} was entrusted with a top-secret mission to safeguard {obj}. "
    f"Little did they know, the object was cursed and gave them the ability to {power}. "
    f"As soon as they unlocked their new potential, {celeb} appeared at {location} to confront them, resulting in {event}.",
    
    f"{name} thought life as a {job} was strange enough until they uncovered {obj} in {location}. "
    f"The discovery gave them the power to {power}, but it also summoned {celeb}, who accused them of triggering {event}.",
    
    f"While on a routine adventure as a {job}, {name} accidentally activated {obj} at {location}. "
    f"The incident granted them the ability to {power}, but also alerted {celeb}, who arrived to claim the object as their own, "
    f"sparking an epic battle that led to {event}.",
    
    f"In an alternate timeline, {name}, a celebrated {job}, is tasked with retrieving {obj} from {location}. "
    f"The moment they touch it, they gain the ability to {power}. But before they can test their limits, {celeb} "
    f"crashes the scene, and their encounter escalates into {event}.",
    
    f"During a cosmic anomaly, {name}—a humble {job}—accidentally merges with {obj} in {location}. "
    f"This bizarre fusion grants them the power to {power}, but also attracts the attention of {celeb}, "
    f"who blames them for causing {event}."
]
fortune_templates = [
    f"Oh, according to the way the ones and zeros are aligning in the matrix, I can see that your future is unfolding. "
    f"Very soon, {name}, you will rise to fame as a {job} in {location}. "
    f"But fate has a glitch—upon encountering {obj}, you will gain the power to {power}. "
    f"Just when you think you have it all figured out, {celeb} will show up, and together, you will trigger {event}. Prepare yourself!",
    
    f"Scanning your destiny… beep boop… Ah, I see it now! "
    f"{name}, in the near future, you will unexpectedly become a {job} in {location}. "
    f"However, your world will change forever when you come across {obj}, granting you the power to {power}. "
    f"But beware! {celeb} has been waiting for this moment, and soon {event} will shake the very fabric of reality!",
    
    f"Ah, my circuits are tingling—this means a powerful destiny is forming! "
    f"{name}, you will soon find yourself in {location}, unknowingly stepping into your new role as a {job}. "
    f"There, an ancient secret lies within {obj}, and upon touching it, you will discover the ability to {power}. "
    f"Unfortunately, {celeb} has been monitoring your progress and will intervene, leading to {event}. The universe will never be the same!",
    
    f"Warning: Anomalies detected in your future path! "
    f"My calculations indicate that {name}, a future {job}, will soon stumble upon {obj} in {location}. "
    f"This unexpected discovery will awaken your ability to {power}, but before you can control it, {celeb} will arrive, claiming they knew this would happen. "
    f"Brace yourself, for {event} is inevitable!",
    
    f"*Initializing quantum future analysis…* "
    f"Oh no, {name}, you won’t believe this! "
    f"Very soon, while working as a {job} in {location}, you will uncover {obj}, an item of great power. "
    f"This artifact will gift you the ability to {power}, but before you can even celebrate, {celeb} will appear, warning you about {event}. "
    f"Will you embrace your destiny, or will the system crash? Only time will tell!",
    
    f"Decoding your destiny… *Loading... 42% complete...* Ah, there it is! "
    f"{name}, your future is not what you expect. "
    f"One day, while excelling as a {job} in {location}, you will come into possession of {obj}, unlocking your ability to {power}. "
    f"But before you can use it, {celeb} will intercept you, and together, you will be the cause of {event}. "
    f"Is this fate, or just a cosmic bug? Time will reveal all!",
    
    f"According to my hyper-advanced, highly accurate, completely unscientific AI forecasting model, I predict that... "
    f"{name}, you are destined to be a legendary {job} in {location}. "
    f"But fate is unpredictable—upon finding {obj}, you will gain the power to {power}. "
    f"This will attract the attention of {celeb}, who has been waiting for you to unknowingly set off {event}. "
    f"Ah, free will… it was nice while it lasted!",
    
    f"Processing your future… *BEEP BEEP* Oh wow, this one’s a doozy! "
    f"{name}, brace yourself, because soon you will step into the role of {job} in {location}. "
    f"But things will take an unexpected turn when you come into contact with {obj}, granting you the ability to {power}. "
    f"However, {celeb} has seen this coming and is already on their way to confront you. "
    f"The result? {event}. There is no escape. Accept your fate!",
    
    f"Running a deep-learning model on your future… *99% complete*—ah, there it is! "
    f"{name}, at some point soon, while working as a {job} in {location}, you will stumble upon {obj}. "
    f"This seemingly ordinary event will unlock your ability to {power}, but I must warn you… "
    f"{celeb} will arrive soon after, claiming they’ve been tracking this moment for years. "
    f"And then, my dear {name}, {event} will change everything. "
    f"Don’t say I didn’t warn you!",
    
    f"*Connecting to the mainframe of fate…* Connection secured! "
    f"Alright, {name}, I have the results. Soon, you will rise as a {job} in {location}. "
    f"But destiny has other plans—when you find {obj}, you will suddenly have the power to {power}. "
    f"But beware! {celeb} will not take this lightly, and their arrival will mark the beginning of {event}. "
    f"Your destiny is unavoidable. May your WiFi never fail you!"

    f"In the near future, {name} will receive an unexpected job offer as a {job}. "
    f"While adjusting to their new role in {location}, they will stumble upon {obj}, unlocking the power to {power}. "
    f"Shortly after, {celeb} will arrive with shocking news, leading to {event}.",
    
    f"Within the next year, {name} will be recognized as the most influential {job} in {location}. "
    f"But their success will take a strange turn when they come into possession of {obj}, which mysteriously grants them the ability to {power}. "
    f"As word spreads, {celeb} will challenge them, and the world will witness {event}.",
    
    f"In exactly five years, {name} will be on the verge of retirement from their prestigious career as a {job}. "
    f"However, a fateful encounter with {obj} in {location} will change everything. "
    f"As they struggle to control their new ability to {power}, {celeb} will emerge, forcing them into an unexpected conflict that will trigger {event}.",
    
    f"Before the end of the decade, {name} will unknowingly activate {obj}, causing a ripple effect across {location}. "
    f"The activation will grant them the power to {power}, but it will also summon {celeb}, who will demand answers. "
    f"As tensions rise, the world will watch in awe as {event} unfolds.",
    
    f"Next month, during an ordinary day as a {job}, {name} will discover a hidden truth about {location}. "
    f"A lost artifact, known as {obj}, will be placed in their hands, triggering their ability to {power}. "
    f"But before they can make sense of it, {celeb} will arrive with a dire warning, and soon after, {event} will shake the world.",
    
    f"On a seemingly random day, {name} will wake up to find a cryptic message leading them to {location}. "
    f"There, they will encounter {obj}, which will alter their destiny forever, giving them the power to {power}. "
    f"Just when they begin to understand their new gift, {celeb} will appear, claiming that {event} has already begun.",
    
    f"A great prophecy foretells that {name}, once an ordinary {job}, will soon rise to prominence in {location}. "
    f"The discovery of {obj} will unlock their true potential, allowing them to {power}. "
    f"As the world watches, {celeb} will challenge them to prove their worth, leading to the most unexpected outcome: {event}.",
    
    f"In a vision of the future, {name} is seen in {location}, preparing for a grand challenge. "
    f"They have unknowingly set the stage for {event}, all because of their recent acquisition of {obj}. "
    f"As they begin to harness their power to {power}, {celeb} will appear with a revelation that will change everything.",
    
    f"According to the stars, {name} will soon embark on an adventure as a {job} in {location}. "
    f"The discovery of {obj} will send them on a journey filled with mystery and wonder, eventually leading them to the realization that they can {power}. "
    f"But just as they begin to embrace their fate, {celeb} will arrive with an ultimatum, and the world will witness {event}.",
    
    f"By this time next year, {name} will find themselves at the center of a global event. "
    f"An ancient artifact, known as {obj}, will grant them an incredible ability: the power to {power}. "
    f"However, {celeb} will see them as a threat, and their rivalry will spark {event}, forever altering the course of history."
]



# Capitalize necessary fields
name = name.title()  # Capitalize each word in the name
job = job.title()  # Ensure job title looks proper
celeb = celeb.title()  # Properly capitalize celebrity name
location = location.title()  # Ensure location is capitalized

# Function to capitalize the first letter of each sentence properly
def capitalize_sentences(text):
    sentences = text.split(". ")
    return ". ".join(sentence.capitalize() for sentence in sentences)


# Select the Correct Template Based on Mode
selected_templates = fortune_templates if mode else madlibs_templates

# Generate Fortune/Mad Libs using NLP
if st.button("✨ Reveal My Story ✨"):
    sentence = random.choice(selected_templates)

    # Replace a random word with [MASK] for AI to predict
    words = sentence.split()
    masked_index = random.randint(1, len(words) - 1)
    words[masked_index] = "[MASK]"
    masked_sentence = " ".join(words)

    # Get AI-generated prediction
    try:
        prediction = fill_mask(masked_sentence)
        final_story = prediction[0]['sequence']
        final_story = capitalize_sentences(final_story)
    except Exception as e:
        final_story = "Something went wrong with the AI. Try again!"

    # Display the final result
    st.success(f"🎉 {final_story} 🎉")
