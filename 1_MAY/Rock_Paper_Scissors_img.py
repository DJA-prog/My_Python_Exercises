# ascii art source: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
def choice(choose):
    if (choose == 0):
        # Rock
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif (choose == 1):
        # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif (choose == 2):
        # Scissors
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
