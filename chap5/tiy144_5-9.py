# Adding if test to make sure the list is not empty.
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to "
                  "see a status report?")
        else:
            print(f"Hello {username.title()},"
                  f" thanks for logging in again.")
else:
    print("We need to find some users!")