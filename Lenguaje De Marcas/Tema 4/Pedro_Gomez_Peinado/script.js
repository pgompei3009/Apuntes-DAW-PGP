function aleatorioEntero(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}


const formulario = document.getElementById("formulario")
const marcador = document.getElementById("marcador")
const resumen = document.getElementById("resumen")
const jugar = document.getElementById("jugar")

const piedra = document.getElementById("piedra")
const papel = document.getElementById("papel")
const tijeras = document.getElementById("tijeras")
const lagarto = document.getElementById("lagarto")
const spock = document.getElementById("spock")

const opciones_maquina = ["piedra", "papel", "tijeras", "lagarto", "spock"]
let jugada = ""
let resultado = ""
let ganador = ""
let elecciones_jugadores = [null, null]
let partida_terminada = false
let puntos_jugador = 0
let puntos_maquina = 0

jugar.disabled = true

piedra.addEventListener("click", () => {
    elecciones_jugadores[0] = "piedra"
    jugar.disabled = false
})

papel.addEventListener("click", () => {
    elecciones_jugadores[0] = "papel"
    jugar.disabled = false
})

tijeras.addEventListener("click", () => {
    elecciones_jugadores[0] = "tijeras"
    jugar.disabled = false
})

lagarto.addEventListener("click", () => {
    elecciones_jugadores[0] = "lagarto"
    jugar.disabled = false
})

spock.addEventListener("click", () => {
    elecciones_jugadores[0] = "spock"
    jugar.disabled = false
})


formulario.addEventListener("submit", (e) => {
    e.preventDefault()

    if (partida_terminada === true) {
        jugar.disabled = true
        alert("LA PARTIDA HA FINALIZADO, REFRESCA LA PÁGINA PARA VOLVER A JUGAR")
    } else {
        elecciones_jugadores[1] = opciones_maquina[aleatorioEntero(0, 4)]

        if (elecciones_jugadores.includes("piedra") && elecciones_jugadores.includes("tijeras")){
            jugada = "Piedra rompe tijeras"
        } else if (elecciones_jugadores.includes("piedra") && elecciones_jugadores.includes("lagarto")){
            jugada = "Piedra aplasta lagarto"
        } else if (elecciones_jugadores.includes("papel") && elecciones_jugadores.includes("piedra")){
            jugada = "Piedra envuelve piedra"
        } else if (elecciones_jugadores.includes("papel") && elecciones_jugadores.includes("spock")){
            jugada = "Papel deshabilita Spock"
        } else if (elecciones_jugadores.includes("tijeras") && elecciones_jugadores.includes("papel")){
            jugada = "Tijeras corta papel"
        } else if (elecciones_jugadores.includes("tijeras") && elecciones_jugadores.includes("lagarto")){
            jugada = "Tijeras decapita lagarto"
        } else if (elecciones_jugadores.includes("lagarto") && elecciones_jugadores.includes("papel")){
            jugada = "Lagarto come papel"
        } else if (elecciones_jugadores.includes("lagarto") && elecciones_jugadores.includes("spock")){
            jugada = "Lagarto envenena Spock"
        } else if (elecciones_jugadores.includes("spock") && elecciones_jugadores.includes("piedra")){
            jugada = "Spock vaporiza piedra"
        } else if (elecciones_jugadores.includes("spock") && elecciones_jugadores.includes("tijeras")){
            jugada = "Spock aplasta tijeras"
        } 


        if (elecciones_jugadores[0] === "piedra" && ["tijeras", "lagarto"].includes(elecciones_jugadores[1])){   
            resultado = "1+ punto para el jugador"      
            puntos_jugador++
        } else if (elecciones_jugadores[0] === "papel" && ["piedra", "spock"].includes(elecciones_jugadores[1])){
            resultado = "1+ punto para el jugador"
            puntos_jugador++
        } else if (elecciones_jugadores[0] === "tijeras" && ["papel", "lagarto"].includes(elecciones_jugadores[1])){
            resultado = "1+ punto para el jugador"
            puntos_jugador++
        } else if (elecciones_jugadores[0] === "lagarto" && ["papel", "spock"].includes(elecciones_jugadores[1])){
            resultado = "1+ punto para el jugador"
            puntos_jugador++
        } else if (elecciones_jugadores[0] === "spock" && ["piedra", "tijeras"].includes(elecciones_jugadores[1])){
            resultado = "1+ punto para el jugador"
            puntos_jugador++
        } else if (elecciones_jugadores[0] === elecciones_jugadores[1]){
            jugada = "Habeis sacado lo mismo"
            resultado = "EMPATE"
        } else {
            resultado = "1+ punto para la CPU"
            puntos_maquina++
        }

        if (((puntos_jugador - puntos_maquina)%2 === 0) && (puntos_jugador >= 3 || puntos_maquina >= 3) && (puntos_jugador - puntos_maquina != 0) || (puntos_jugador === 3 && puntos_maquina === 0) || (puntos_jugador === 0 && puntos_maquina === 3)){
            partida_terminada = true
            if (puntos_jugador > puntos_maquina){
                ganador = "¡Ha ganado el jugador!"
            } else {
                ganador = "Ha ganado la máquina..."
            }
        }
        
        marcador.textContent = `${puntos_jugador} - ${puntos_maquina}`
        resumen.textContent = `El jugador ha sacado ${elecciones_jugadores[0]} y la CPU ha sacado ${elecciones_jugadores[1]}. ${jugada}. ${resultado}. ${ganador}`
    }
});

