# Equivalent function calls.
def make_shirt(shirt_size='large', shirt_message='i love python'):
    """Display information on a shirt."""
    print(f"I have a white {shirt_size} shirt.")
    print(f"My white {shirt_size} shirt is written, "
          f"'{shirt_message.title()}' in front of it.\n")
make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_size='extra large', shirt_message='python is the simplest language')