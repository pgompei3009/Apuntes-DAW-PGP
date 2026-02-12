let contador = 0;

const spanContador = document.getElementById("contador");
const botonSuma = document.getElementById("btnIncrementar");
const botonRestar = document.getElementById("btnRestar");


botonSuma.addEventListener("click", () => {
    contador++;
    spanContador.textContent = contador;
});

botonRestar.addEventListener("click", () => {
    if (contador != 0){
        contador--;
        spanContador.textContent = contador;
    }
});