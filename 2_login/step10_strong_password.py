def strong_password(password):
    return len(password) >= 6
   
if __name__ == "__main__":
    import checks
    checks.run(10)
