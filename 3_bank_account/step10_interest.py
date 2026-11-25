def add_interest(account):
 account["balance"] = account["balance"] + account["balance"] * 4 / 100
pass

if __name__ == "__main__":
    import checks
    checks.run(10)
