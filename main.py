from ai import call_gpt
from graphics import Canvas
import textwrap

CANVAS_WIDTH = 500 
CANVAS_HEIGHT = 500


THEMES = {
    "1": "Nature",
    "2": "Sea",
    "3": "Forest",
    "4": "City",
    "5": "Animals",
    "6": "Sky and Stars",
}

def show_menu():
    print("\n What kind of affirmation would you like to receive today?")
    for key, value in THEMES.items():
        print(f" [{key}] {value.capitalize()}")

def main():
    print("Hi friend! Welcome to my affirmations interactive game.")
    show_menu()
    user_response = input("\n Write your type's name: ")

    if user_response not in THEMES.values():
        print("Oops! That topic is not on our list. Please try again and make sure to type the name exactly as it shows, with uppercase and lowercase letters! 🌟")
        return

    #    tematica = TEMATICAS.get(opcion)
    #if not tematica:
    #    print("Opción no válida, intenta de nuevo.")
    #    return

    print(f"\n ✨ Creating your affirmation of the day {user_response} ✨ \n")

    response_chatgpt = call_gpt(f"Create an affirmation very positive, cute and short for little kids."
                        f"It must be related to '{user_response}'."
                        f"It should be short."
                        f"Return the affirmation without any explanations about it."
                        f"Response should be nice for little kids.")


    text_cut= textwrap.fill(response_chatgpt, width=500)
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(0,0,"background2.png")
    canvas.create_text(30, 150, text_cut, font="Arial", font_size=20, color="white")
    #print(f"\n {response_chatgpt} \n")


if __name__ == "__main__":
    main()
