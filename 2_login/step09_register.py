def register(users, username, password):
    users[username] = password
    pass 

if __name__ == "__main__":
    import checks
    checks.run(9)
