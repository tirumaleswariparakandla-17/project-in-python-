def withdraw(account, amount):
    account["balance"] = account["balance"] - amount
    pass 
if __name__ == "__main__":
    import checks
    checks.run(6)
