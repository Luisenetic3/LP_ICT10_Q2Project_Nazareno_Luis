from pyscript import document, display

def Calculate(e):
    fname = document.getElementById("Fname").value
    lname = document.getElementById("Lname").value
    science_val = document.getElementById("science").value
    math_val = document.getElementById("Math").value
    english_val = document.getElementById("English").value
    ict_val = document.getElementById("ICT").value
    fil_val = document.getElementById("Filipino").value
    pe_val = document.getElementById("PE").value

    # Check for empty inputs BEFORE converting to int
    if (fname == "" or lname == "" or
        science_val == "" or math_val == "" or english_val == "" or
        ict_val == "" or fil_val == "" or pe_val == ""):

        display("⚠️ Please fill in ALL fields before calculating.",
                target="average", append=False)
        display("", target="grades", append=False)
        display("", target="name", append=False)
        return

    # Safe to convert now
    science = int(science_val)
    math = int(math_val)
    english = int(english_val)
    ict = int(ict_val)
    fil = int(fil_val)
    pe = int(pe_val)

    equation = (science + math + english + ict + fil + pe) / 6
    averagegrade = round(equation, 2)

    display(f"Name: {fname} {lname}", target="name", append=False)
    display(f"Science: {science}", target="grades", append=False)
    display(f"Math: {math}", target="grades")
    display(f"English: {english}", target="grades")
    display(f"ICT: {ict}", target="grades")
    display(f"Filipino: {fil}", target="grades")
    display(f"PE: {pe}", target="grades")
    display(f"Your general weighted average is {averagegrade}",
            target="average", append=False)
