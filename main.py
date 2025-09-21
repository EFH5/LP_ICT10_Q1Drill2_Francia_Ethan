from pyscript import document

def gather_info(event): 
    
    name = str(document.getElementById("name"))
    age = str(document.getElementById("age"))
    school = str(document.getElementById("school"))

info = "{name} is currently {age} years old and studies at {school} \n This information was gathered through input fields and displayed using \t a multiline string in Python via Pyscript"
document.getElementById("info").innerText = info

