def enough_money(account, amount):
      return amount <= account["balance"]

if __name__ == "__main__":
    import checks
    checks.run(7)
