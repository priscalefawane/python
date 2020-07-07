# Loop through the new_users list to see
# if each new username has already been used.
current_users = ['John', 'neo', 'admin', 'sam', 'lisa']
new_users = ['Neo', 'eva', 'Sam', 'joe', 'NELLY']

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user.title()}, that name is taken.")
    else:
        print(f"{new_user.title()} is available.")


