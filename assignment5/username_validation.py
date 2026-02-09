usernames = ["alice", "bob_smith", "charlie", "davidjones", "eve"]

print("All usernames:")
for username in usernames:
    print(username)
print("\nUsernames longer than 6 characters:")
for username in usernames:
    if len(username) > 6:
        print(username)
