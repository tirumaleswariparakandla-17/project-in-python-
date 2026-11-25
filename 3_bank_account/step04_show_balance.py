def balance_html(account):
     return "<h2>Balance: ₹" + str(account["balance"]) + "</h2>"
    
if __name__ == "__main__":
    import checks
    checks.run(4)
