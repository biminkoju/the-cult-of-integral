# Terrible spaghetti code by u/xSerpentine.

import random

YOUR_COMMENT_HERE = "People: stop being depressed.\nMy pills: haha hormones go brrrrr."  #\n for new line.
CHANCE_OF_EXTRA_COMMENT = 50  # i.e 1 in 50 chance.
NUMBER_OF_EDITS = 250  # The number of "edit: ..."s that will appear in the copypasta.
REWARD = "upvotes"  # Change to likes, etc. Remember to include 's' on the end to make the first "edit: ..." and phrases make sense (if you care about grammar).

phrases = ["It genuinely means so much to me.", "Holy shit, I can not believe it.", "Jesus Christ.", 
"Thank you so much.", "Thank you very much.", "I appreciate your consideration to do these things <3",
"I sincerely appreciate all the love you are giving me.",  f"OMG, I've never reached this number of {REWARD} before.",
"Just wow.", "I love you all.", "I'm literally famous rn wtf.", "<3", "Why are you all so nice to me rn ROFL.",
"I'm literally fucking famous holy shit.", "I love you stans <3 <3 <3", "Please stop it's growing so quickly!",
f"If I reach 9999 {REWARD} I'll start an OnlyFans ;)", "TFW when you realise you made the class laugh.",
"You're all amazing.", "Oh my fucking God."]  # Feel free to add more.


def main(algorithm = 1):
    with open("copypasta.txt", "w") as f:  # Put copypasta into file to make it easy to copy (OPEN FILE -> CTRL+A -> CTRL+C).
        f.write(YOUR_COMMENT_HERE + "\n\n")
        f.write(f"Edit: 1 {REWARD[:-1]}!\n")  # Grammar is cool.

        # ALGORITHM #1: GO UP TO A CERTAIN NUMBER OF LIKES.

        if str(algorithm) == "1":  # Using string because it's easier than dealing with exceptions lol.
            for i in range(2, NUMBER_OF_EDITS + 1):
                f.write(f"Edit: {i} {REWARD}!")
                n = random.randint(1, CHANCE_OF_EXTRA_COMMENT)
                if n < (CHANCE_OF_EXTRA_COMMENT // 5):  # Change if you want, this one makes edits stupidly common for purpose of demonstration.
                    try: 
                        index = random.randint(0, (len(phrases)-1))
                        f.write(f" {phrases[index]}\n")
                        del phrases[index]  # Remove this if you want same phrase to possibly appear twice.
                    except:
                        f.write("\n")
                else: f.write("\n")
            f.write(f"\nSeriously, thank you for all the {REWARD} guys. I've never had this many {REWARD} before.")
            f.close()
            return 0

        # ALGORITHM #2: GO UP UNTIL ALL PHRASES USED.

        elif str(algorithm) == "2":  # Using string because it's easier than dealing with exceptions lol.
            i = 2
            while True:
                f.write(f"Edit: {i} {REWARD}!")
                n = random.randint(1, CHANCE_OF_EXTRA_COMMENT)
                if n < (CHANCE_OF_EXTRA_COMMENT // 5):  # Change if you want, this one makes edits stupidly common for purpose of demonstration.
                    try: 
                        index = random.randint(0, (len(phrases)-1))
                        f.write(f" {phrases[index]}\n")
                        del phrases[index]  # DO NOT DELETE THIS LINE IN ALGORITHM #2!
                        i += 1
                    except:
                        f.write("\n")
                        break
                else: 
                    f.write("\n")
                    i += 1
            f.write(f"\nSeriously, thank you for all the {REWARD} guys. I've never had this many {REWARD} before.")
            f.close()
            return 0
        
        else:
            print("Algorithm must be either 1 or 2!")
            algorithm = input("Enter an algorithm number: ")
            main(algorithm)


main(2)  # Change to 2 if you wish.
