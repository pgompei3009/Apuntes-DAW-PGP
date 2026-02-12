const form = document.getElementById("formNumero")
const resultadoSpan = document.getElementById('resultado');

form.addEventListener("submit", (event) => {
    event.preventDefault()
    let numero = document.getElementById('numero')

    if (numero.value%2 === 0){
        resultadoSpan.textContent = 'Par';
    }
    else{
        resultadoSpan.textContent = 'Impar';
    }
});