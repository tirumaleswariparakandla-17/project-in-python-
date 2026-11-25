def topper(students):
 return max(students, key=lambda s: s["marks"])

if __name__ == "__main__":
    import checks
    checks.run(8)
