def show_messages(msgs):
    """Print text messages in a list"""
    for msg in msgs:
        print(msg.title())
text_messages = [
    'sam is not feeling well',
    'i will be late',
    'i am not coming',
    ]
show_messages(text_messages)