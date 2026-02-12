let visible = true
const parrafo = document.getElementById("texto");
const boton = document.getElementById("boton");

boton.addEventListener("click", () => {
    if (visible == true) {
        parrafo.style.visibility = "hidden";
        visible = false
    }
    else {
        parrafo.style.visibility = "visible";
        visible = true
    }
});
