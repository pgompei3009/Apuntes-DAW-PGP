//Escribe una función que reciba dos números a y b y devuelva true si b es múltiplo de a, y false en caso contrario. Debes usar el operador módulo para realizar la comprobación.

function multiplo(a, b){
    let resto = b%a
    if (resto === 0){
        return true
    }
    else{
        return false
    }
}

multiplo(3, 2)