# Calling a function using positional and keyword arguments.
def make_shirt(shirt_size, shirt_message):
    """Display information on a shirt."""
    print(f"I have a white {shirt_size} shirt.")
    print(f"My white {shirt_size} shirt is written, "
          f"'{shirt_message.title()}' in front of it.\n")

make_shirt('medium', '<i love python!/>')
make_shirt(shirt_size='medium', shirt_message='<i love python!/>')
