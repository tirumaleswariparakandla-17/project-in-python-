def password_ok(users, username, password):
     return users[username] == password
  
if __name__ == "__main__":
    import checks
    checks.run(7)
