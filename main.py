from pyscript import document

def gather_info(event): 

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    document.getElementById("name").innerText = name
    document.getElementById("age").innerText = age
    document.getElementById("school").innerText = school

info = "{name} is currently {age} years old and studies at {school} \n This information was gathered through input fields and displayed using \t a multiline string in Python via Pyscript"
document.getElementById("info").innerText = info
