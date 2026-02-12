const form = document.getElementById("formCuenta")
let cuenta = document.getElementById("cuentaAtras")

form.addEventListener("submit", (event) => {
    event.preventDefault()
    cuenta.textContent = ''

    let numero = document.getElementById('numero').value
    while (true){
        cuenta.textContent = cuenta.textContent + `${numero}`;
        
        if (numero === 0){
            break
        }
        numero = numero - 1
    }
})
