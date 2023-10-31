#Aluno= [ 'nomeAluno', idadeAluno, [nota1, nota2, nota3, ...., notaN] ]
#Turma=[ Aluno1, Aluno2, ...., AlunoN ]
#Escola=[ Turma1, Turma2, ...., TurmaN ]
#Disciplina=[Disciplina1, Disciplina2, ...., DisciplinaN]

Disciplinas=['Algoritmos e Programação', 'Segurança']
Escola=[
    [
        ['André Coelho', 19, [7.5, 9.2, 8.9, 6.0]], ['Rebeca Farias', 20, [9.5, 7.8]]
    ],
    [
        ['Tiago Silva', 19, [4.5, 6.1, 7.4]], ['Bárbara Andrade', 18, [5.0, 8.2, 7.6]]
    ]
]

def cadastrar_turma(nDisciplina,listaD,listaE):
    
