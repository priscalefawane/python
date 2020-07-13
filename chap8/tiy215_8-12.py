def make_sandwich(*items):
    """Making sandwiches with items."""
    print("\nMaking a delicious sandwich with the following items:")
    for item in items:
        print(f"-{item}")
    print("You sandwich is ready for collection!")

make_sandwich('egg', 'tomato')
make_sandwich('tuna')
make_sandwich('cheese', 'tomato')

