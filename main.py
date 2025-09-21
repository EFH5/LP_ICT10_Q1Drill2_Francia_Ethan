from pyscript import document

def gather_info(event): 
    name = document.getElementById("name_input").value
    age = document.getElementById("age_input").value
    school = document.getElementById("school_input").value

    document.getElementById("name").innerText = name
    document.getElementById("age").innerText = age
    document.getElementById("school").innerText = school
    
    info = f"""{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed using
a multiline string in Python via PyScript."""

    document.getElementById("info").innerText = info