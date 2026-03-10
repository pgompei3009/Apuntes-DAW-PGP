function filtrar_por_letra(palabras, letra){
    let palabras_filtradas = []
    for (let p of palabras){
        if (p.startsWith(letra)){
            palabras_filtradas.push(p)
        }
    }
    return palabras_filtradas
}

let palabras = ['ave', 'barco', 'cacerola']

console.log(filtrar_por_letra(palabras, "a"))