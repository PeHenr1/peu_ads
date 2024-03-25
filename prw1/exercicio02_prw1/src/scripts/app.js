function mostrarTabela(Nome, Peso, Altura, IMC, Status) {

    let tabela = document.querySelector('#dados');
    let tr = tabela.insertRow();
    let tdNome = tr.insertCell(0);
    let tdPeso = tr.insertCell(1);
    let tdAltura = tr.insertCell(2);
    let tdIMC = tr.insertCell(3);
    let tdStatus = tr.insertCell(4);
    let tdOpcoes = tr.insertCell(5);
    tdNome.innerHTML = Nome;
    tdPeso.innerHTML = Peso;
    tdAltura.innerHTML = Altura;
    tdIMC.innerHTML = IMC;
    tdStatus.innerHTML = Status;
    let btnExclude = document.createElement("button");
    let btnPlusPeso = document.createElement("button");
    let btnMinusPeso = document.createElement("button");
    btnExclude.classList.add("exclude");

    btnPlusPeso.classList.add("plus");
    btnMinusPeso.classList.add("minus");
    btnPlusPeso.innerText = "+";
    btnMinusPeso.innerText = "-";
    btnExclude.innerText = "x";

    tdOpcoes.append(btnPlusPeso);
    tdOpcoes.append(btnMinusPeso);
    tdOpcoes.append(btnExclude);

    plusPeso(btnPlusPeso);
    minusPeso(btnMinusPeso);
    exclude(btnExclude);
    
}

function exclude(botaoExclude) {
    botaoExclude.addEventListener("click", (e) => {
        e.stopPropagation()
        e.target.parentElement.parentElement.remove()
    })
}

function plusPeso(botaoPlus) {
    botaoPlus.addEventListener("click", (e) => {
        e.stopPropagation()
        let linha = e.target.parentElement.parentElement
        let novoPeso = parseFloat(linha.children[1].innerText) + 0.5
        let novaAltura = parseFloat(linha.children[2].innerText)
        let novoIMC = parseFloat((novoPeso / (novaAltura * novaAltura))).toFixed(2)
        let novoStatus
        if (novoIMC < 18.5) {
            novoStatus = "Magreza";
        } else if (novoIMC >= 18.5 && novoIMC < 25) {
            novoStatus = "Saudável";
        } else if (novoIMC >= 25.0 && novoIMC < 30.0) {
            novoStatus = "Sobrepeso";
        } else if (novoIMC >= 30.0 && novoIMC < 35.0) {
            novoStatus = "Obesidade I";
        } else if (novoIMC >= 35.0 && novoIMC < 40.0) {
            novoStatus = "Obesidade II";
        } else if (novoIMC >= 40.0) {
            novoStatus = "Obesidade III";
        }
        linha.children[1].innerText = novoPeso
        linha.children[2].innerText = novaAltura
        linha.children[3].innerText = novoIMC
        linha.children[4].innerText = novoStatus
    })
}

function minusPeso(botaoMinus) {
    botaoMinus.addEventListener("click", (e) => {
        e.stopPropagation()
        let linha = e.target.parentElement.parentElement
        let novoPeso = parseFloat(linha.children[1].innerText)
        if (novoPeso - 0.5 > 0.0) {
            novoPeso = novoPeso - 0.5
        } else {
            novoPeso = 0.0
        }
        let novaAltura = parseFloat(linha.children[2].innerText)
        let novoIMC = parseFloat((novoPeso / (novaAltura * novaAltura))).toFixed(2)
        let novoStatus
        if (novoIMC < 18.5) {
            novoStatus = "Magreza";
        } else if (novoIMC >= 18.5 && novoIMC < 25) {
            novoStatus = "Saudável";
        } else if (novoIMC >= 25.0 && novoIMC < 30.0) {
            novoStatus = "Sobrepeso";
        } else if (novoIMC >= 30.0 && novoIMC < 35.0) {
            novoStatus = "Obesidade I";
        } else if (novoIMC >= 35.0 && novoIMC < 40.0) {
            novoStatus = "Obesidade II";
        } else if (novoIMC >= 40.0) {
            novoStatus = "Obesidade III";
        }
        linha.children[1].innerText = novoPeso
        linha.children[2].innerText = novaAltura
        linha.children[3].innerText = novoIMC
        linha.children[4].innerText = novoStatus
    })
}

const botao = document.querySelector("#calculate");
botao.addEventListener("click", (e) => {
    e.stopPropagation()
    let nome = document.querySelector('[name="name"]').value
    let peso = parseFloat(document.querySelector('[name="weight"]').value)
    let altura = parseFloat(document.querySelector('[name="height"]').value) / 100

    let imc = parseFloat((peso / (altura * altura))).toFixed(2)
    let status
    if (imc < 18.5) {
        status = "Magreza";
    } else if (imc >= 18.5 && imc < 25) {
        status = "Saudável";
    } else if (imc >= 25.0 && imc < 30.0) {
        status = "Sobrepeso";
    } else if (imc >= 30.0 && imc < 35.0) {
        status = "Obesidade I";
    } else if (imc >= 35.0 && imc < 40.0) {
        status = "Obesidade II";
    } else if (imc >= 40.0) {
        status = "Obesidade III";
    }

    if (nome !== "" && altura > 0 && peso > 0) {
        e.preventDefault();

        document.querySelector('[name="name"]').value = '';
        document.querySelector('[name="weight"]').value = '';
        document.querySelector('[name="height"]').value = '';
        document.querySelector('#imc').textContent = '';

        mostrarTabela(nome, peso, altura, imc, status)
    }
    else {
        e.preventDefault();
        alert("Há campos vazios ou com informações inválidas!");
    }

})

const botaoMaiorIMC = document.querySelector("#maiorIMC");
botaoMaiorIMC.addEventListener("click", (e) => {
    e.stopPropagation();
    let listaIMC = document.querySelectorAll('tr')
    if (listaIMC.length > 1) {
        let indexMaior = 1
        let maiorIMC = parseFloat(listaIMC[1].children[3].innerText)
        for (let i = 1; i < listaIMC.length; i++) {
            if (parseFloat(listaIMC[i].children[3].innerText) > maiorIMC) {
                maiorIMC = parseFloat(listaIMC[i].children[3].innerText)
                indexMaior = i
            }
        }

        listaIMC[indexMaior].remove()
    }
})

const botaoMenorIMC = document.querySelector("#menorIMC");
botaoMenorIMC.addEventListener("click", (e) => {
    e.stopPropagation();
    let listaIMC = document.querySelectorAll('tr')
    if (listaIMC.length > 1) {
        let indexMenor = 1
        let menorIMC = parseFloat(listaIMC[1].children[3].innerText)
        for (let i = 1; i < listaIMC.length; i++) {
            if (parseFloat(listaIMC[i].children[3].innerText) < menorIMC) {
                menorIMC = parseFloat(listaIMC[i].children[3].innerText)
                indexMenor = i
            }
        }

        listaIMC[indexMenor].remove()
    }
})

function calcularIMC() {
    let peso = parseFloat(document.querySelector('[name="weight"]').value)
    let altura = parseFloat(document.querySelector('[name="height"]').value) / 100
    let imc = peso / (altura * altura);

    document.querySelector('#imc').textContent = imc.toFixed(2);
}
document.querySelector('[name="weight"]').addEventListener('input', calcularIMC);
document.querySelector('[name="height"]').addEventListener('input', calcularIMC);


