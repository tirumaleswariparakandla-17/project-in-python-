def grade(marks):
    if marks >= 90:
        return "A"
    
    elif marks >= 75:
         return "B"
    elif marks >= 60:
        return "C"
   
    else:
        return "D"

if __name__ == "__main__":
    import checks
    checks.run(7)
