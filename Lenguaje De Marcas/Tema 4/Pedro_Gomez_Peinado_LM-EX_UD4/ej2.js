function calcular_consumo(L, km){
    return (L/km*100).toFixed(2)
}

function calcular_coste(L, precio){
    return (L*precio).toFixed(2)
}

const formulario = document.getElementById('formulario')
const consumo = document.getElementById('consumo')
const coste = document.getElementById('coste')

formulario.addEventListener('submit', (event) => {
    event.preventDefault()
    const km = document.getElementById('km').value
    const L = document.getElementById('L').value
    const precio = document.getElementById('€').value

    let r_consumo = calcular_consumo(L, km)
    let r_coste = calcular_coste(L, precio)

    consumo.textContent = `${r_consumo} L/100 km`
    coste.textContent = `${r_coste} €`
})