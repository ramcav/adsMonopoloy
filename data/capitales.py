# This file contains the dictionary of the capitales and their positions
# Prices increase by 15 each tile

capitales_dict = {
    "Washington": 100,
    "London": 115,
    "Paris": 130,
    "Berlin": 145,
    "Moscow": 160,
    "Beijing": 175,
    "Tokyo": 190,
    "New Delhi": 205,
    "Brasilia": 220,
    "Canberra": 235,
    "Ottawa": 250,
    "Rome": 265,
    "Madrid": 280,
    "Seoul": 295,
    "Mexico City": 310,
    "Cairo": 325,
    "Buenos Aires": 340,
    "Riyadh": 355,
    "Ankara": 370,
    "Jakarta": 385,
    "Kuala Lumpur": 400,
    "Bangkok": 415,
    "Hanoi": 430,
    "Islamabad": 445,
    "Baghdad": 460,
    "Tehran": 475,
    "Kabul": 490,
    "Athens": 505,
    "Oslo": 520,
    "Stockholm": 535,
    "Helsinki": 550,
    "Copenhagen": 565,
    "Vienna": 580,
    "Warsaw": 595,
    "Budapest": 610,
    "Dublin": 625,
    "Amsterdam": 640,
    "Brussels": 655,
    "Lisbon": 670,
    "Prague": 685
}

def __string_convert(string) -> str:
    buffer = 0
    if len(string) % 2:
        buffer = 1

    formated = '|'
    str_buffer = -1 * (len(string) - 17) // 2

    formated += ' ' * str_buffer
    formated += string
    formated += ' ' * (str_buffer - buffer)
    formated += '|'

    return formated


if __name__ == "__main__":
    for i in capitales_dict:
        print(__string_convert(i))
