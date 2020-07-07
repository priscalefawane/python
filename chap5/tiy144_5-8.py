# Looping through the list
usernames = ['john', 'neo',
             'admin', 'sam', 'lisa']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thanks for logging in again.")

