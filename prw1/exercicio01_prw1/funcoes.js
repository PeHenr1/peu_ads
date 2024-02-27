// Retorna uma lista com os "qtde" primeiros números primos, começando em 1.
function primos(qtde) {
    var lista = Array();
    if(qtde > 0){
        let entrou = false
        let primo = 1 
        
        while(lista.length !== qtde){

            for(let div = 2; div < primo; div++){

                if(primo % div === 0){
                    entrou = true
                }

            }
            if(!entrou){
                lista.push(primo)
            }
            entrou = false
            primo++
        }
    }
    
    return lista
}

// Retorna a lista de palavras palíndromas
// Deve ser implementada usando map/filter/reduce
function palindromo(palavras) {
    function verifica(word){
        word = word.toLowerCase()
        let invert = word.split("").reverse().join("")
        return invert === word
    }

    var palindromos = palavras.filter(verifica)
    return palindromos
}

// Retorna se dois aviões estão com perigo de colisão.
// Em geral, a margem de segurança entre dois aviões é de 1000 pés.
// Cada pé é igual a 0.3048 metros.
function perigoAcidente(altura_pes_aviao1, altura_met_aviao2) {
    let alt_aviao2_pes = (altura_met_aviao2 / 0.3048)
    let distancia; 

    if(altura_pes_aviao1 > alt_aviao2_pes){
        distancia = altura_pes_aviao1 - alt_aviao2_pes
    }
    else{
        distancia = alt_aviao2_pes - altura_pes_aviao1
    }

    if(distancia < 1000){
        return true
    }
    else{
        return false
    }
}

// Função que retorna uma lista sem nenhum item duplicado.
function apenasUnicos(lista) {
    function filtragem(inp){
        let cont = 0
        for(let x = 0; x < lista.length; x++){
            if(inp === lista[x]){
                cont++
            }
        }
        if(cont === 1){
            return inp
        }
    }           
    
    let unicos = lista.filter(filtragem)
    return unicos
}

// Retorna a soma dos "qtde" primeiros números pares (zero é um número par!)
function somaNumerosPares(qtde) {
    let soma = 0, cont = 0, pares = 0
    while (pares !== qtde){
        if(cont % 2 === 0){
            soma += cont
            pares++
        }
        cont++
    }
    return soma
}

// Recebe uma lista numérica e retorna uma lista cujos valores foram multiplicados por 2.
// Deve ser implementada usando map/filter/reduce
function dobro(valores) {
    function mult(inp){
        return inp * 2
    }

    let multiplicados = valores.map(mult);
    return multiplicados
}

// Recebe duas listas e retorna uma lista com a união das listas de entrada, sem repetições.
function uniao(v1, v2) {
    let unidos = Array()

    function filtra(inp){
        if(unidos.indexOf(inp) === -1){
            unidos.push(inp)
            
        }
        return unidos
    }

    v1.filter(filtra)
    v2.filter(filtra)
    return unidos
}

// Função que recebe duas listas e retorna os elementos da primeira lista que não estejam na segunda lista.
function diff(v1, v2) {
    let diferent = Array()

    function checa(inp){
        if(v2.indexOf(inp) === -1){
            diferent.push(inp)
            
        }
        return diferent
    }

    v1.filter(checa)
    return diferent
}

// Recebe duas listas numéricas e retorna o vetor cuja soma dos valores é maior que a outra lista. Caso ambas as listas tenham mesmo valor, retorna FALSE. Considere vetor vazio com soma zero.
// Deve ser implementada usando map/filter/reduce
function maior(v1, v2) {
    function somar(acc,v){
        return acc + v
    }

    let s1 = 0, s2 = 0

    if(v1.length > 0){
        s1 = v1.reduce(somar)
    }
    if(v2.length > 0){
        s2 = v2.reduce(somar)
    }
    
    if(s1 === s2){
        return false
    }
    else{
        if(s2 > s1){
            return v2
        }
        else{
            return v1
        }
    }
}

// Recebe um valor e uma lista. Retorna a lista sem nenhuma ocorrência do valor de entrada.
// Deve ser implementada usando map/filter/reduce
function removeValores(valor, lista) {
    function remove(npm){
        return npm !== valor
    }

    let retorno = lista.filter(remove)
    return retorno
}

module.exports = { primos, palindromo, perigoAcidente, apenasUnicos, somaNumerosPares, dobro, uniao, diff, maior, removeValores }