def total_marks(students):
    total = 0
    for s in students:
      total = total + s["marks"]
    return total

if __name__ == "__main__":
    import checks
    checks.run(6)
