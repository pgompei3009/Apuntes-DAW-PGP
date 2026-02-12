const form = document.getElementById("formDatos")
const resultadoSpan = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    event.preventDefault()

    const peso = document.getElementById("peso").value
    const altura = document.getElementById("altura").value
    const imc = peso/(altura**2)
    let resultado

    if (imc<18.5){
        resultado = "Tienes bajo peso"
    }

    else if (imc>=18.5 && imc<24.9){
        resultado = "Tienes un peso normal"
    }

    else if (imc>=24.9 && imc<29.9){
        resultado = "Tienes sobrepeso"
    }

    else{
        resultado = "Tiene obesidad"
    }

    resultadoSpan.textContent = resultado;
})
