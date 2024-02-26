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

    return palavras
        .map(word => word.trim())
        .filter(word => verifica(word))
        .reduce((acc, word) => {
            acc.push(word);
            return acc;
    }, []);
}

// Retorna se dois aviões estão com perigo de colisão.
// Em geral, a margem de segurança entre dois aviões é de 1000 pés.
// Cada pé é igual a 0.3048 metros.
function perigoAcidente(altura_pes_aviao1, altura_met_aviao2) {

}

// Função que retorna uma lista sem nenhum item duplicado.
function apenasUnicos(lista) {

}

// Retorna a soma dos "qtde" primeiros números pares (zero é um número par!)
function somaNumerosPares(qtde) {

}

// Recebe uma lista numérica e retorna uma lista cujos valores foram multiplicados por 2.
// Deve ser implementada usando map/filter/reduce
function dobro(valores) {

}

// Recebe duas listas e retorna uma lista com a união das listas de entrada, sem repetições.
function uniao(v1, v2) {

}

// Função que recebe duas listas e retorna os elementos da primeira lista que não estejam na segunda lista.
function diff(v1, v2) {

}

// Recebe duas listas numéricas e retorna o vetor cuja soma dos valores é maior que a outra lista. Caso ambas as listas tenham mesmo valor, retorna FALSE. Considere vetor vazio com soma zero.
// Deve ser implementada usando map/filter/reduce
function maior(v1, v2) {

}

// Recebe um valor e uma lista. Retorna a lista sem nenhuma ocorrência do valor de entrada.
// Deve ser implementada usando map/filter/reduce
function removeValores(valor, lista) {

}

module.exports = { primos, palindromo, perigoAcidente, apenasUnicos, somaNumerosPares, dobro, uniao, diff, maior, removeValores }