def student_row(s):
 return "<li>" + s["name"] + " - " + str(s["marks"]) + "</li>"
  
if __name__ == "__main__":
    import checks
    checks.run(5)