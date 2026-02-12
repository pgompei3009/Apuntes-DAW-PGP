const form = document.getElementById("formTabla")
const resultadoSpan = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    resultadoSpan.textContent = ''
    event.preventDefault()

    const numero = document.getElementById('numero').value
    for (let i = 0; i < 11; i++){
        resultadoSpan.textContent = resultadoSpan.textContent + `${numero} x ${i} = ${numero*i}`;
    }
})