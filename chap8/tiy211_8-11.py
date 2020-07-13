def show_messages(text_messages):
    """Print text messages in a list"""
    for text_message in text_messages:
        print(text_message)

def send_messages(text_messages):
    """Print each text message in the list."""
    # new list to hold sent messages.
    sent_messages = []

    # Adding text messages in new list.
    while text_messages:
        text_message = text_messages.pop()
        sent_message = text_message
        sent_messages.append(sent_message)

    # making list of original messages.
    for sent_message in sent_messages:
        text_messages.append(sent_message)

    return text_messages

text_messages = [
    'Sam is not feeling well',
    'I will be late',
    'I am not coming',
    ]
show_messages(text_messages)

print("\nSent messages:")
sent_messages = send_messages(text_messages[:])
show_messages(sent_messages)

print("\nOriginal messages:")
show_messages(text_messages)





