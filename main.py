# NOUS v0.0.2
# Core Assistant Framework

from brain.brain import think


def start_nous():

    print("NOUS: Systems online.")
    print("NOUS: How can I assist you?")


    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("NOUS: Shutting down.")
            break

        answer = think(user_input)

        print("NOUS:", answer)


if __name__ == "__main__":
    start_nous()# NOUS v0.0.1
# Initial boot sequence

print("NOUS is coming online...")