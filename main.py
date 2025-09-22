from pyscript import Element

def show_info():
    name = Element("name").element.value
    age = Element("age").element.value
    school = Element("school").element.value

    info = f"Hello, my name is {name}. I am {age} years old and I go to {school}."
    output = Element("output").element
    output.innerText = info
    output.style.display = "block"