function aleatorioEntero(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}


function lanzarD4(){
    return aleatorioEntero(1, 4)
}


function lanzarD6(){
    return aleatorioEntero(1, 6)
}


function lanzarD8(){
    return aleatorioEntero(1, 8)
}


function lanzarD10(){
    return aleatorioEntero(1, 10)
}


function lanzarD12(){
    return aleatorioEntero(1, 12)
}


function lanzarD20(){
    return aleatorioEntero(1, 20)
}


function lanzarD100(){
    return aleatorioEntero(1, 100)
}




// Segundo bloque (DOM): Declaramos las variables que hacen referencia a elementos de web
let resultado = 0;
const spanResultado = document.getElementById("resultado");
const D4 = document.getElementById("D4");
const D6 = document.getElementById("D6");
const D8 = document.getElementById("D8");
const D10 = document.getElementById("D10");
const D12 = document.getElementById("D12");
const D20 = document.getElementById("D20");
const D100 = document.getElementById("D100");

// Tercer bloque (lógica): establecemos el comportamiento de los botones
D4.addEventListener("click", () => {
    spanResultado.textContent = lanzarD4();
})

D6.addEventListener("click", () => {
    spanResultado.textContent = lanzarD6();
})

D8.addEventListener("click", () => {
    spanResultado.textContent = lanzarD8();
})

D10.addEventListener("click", () => {
    spanResultado.textContent = lanzarD10();
})

D12.addEventListener("click", () => {
    spanResultado.textContent = lanzarD12();
})

D20.addEventListener("click", () => {
    spanResultado.textContent = lanzarD20();
})

D100.addEventListener("click", () => {
    spanResultado.textContent = lanzarD100();
})

