def create_account(name):
  return {"name": name, "balance": 0}
   
if __name__ == "__main__":
    import checks
    checks.run(3)
