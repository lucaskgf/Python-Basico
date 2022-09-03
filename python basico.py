notas= int (input("Quantas notas?")) #entrada de dado
aluno=input("Nome do aluno:") #entrada de dado

count=1 ; soma = 0.0
while count <= notas:
    print( "Nota do aluno", count, ":")
    nota = float (input())
    if nota >= 0 and nota <=10: #O uso do if serve para determinar uma condição ex: um numero = ou maior que  10 ele rotarna um valor epecifico
        print("------------")
        soma += nota
        count += 1
    else:
        print("#############") # Print é usado para eibir um teto na tela
        print("Nota errada, ", nota, ":")
        print("Digite novamente a nota do aluno", count, ":")
        nota = float (input ( ))
        soma += nota
        count +=nota

    print("Media do aluno:", aluno, "-" , (soma/notas))
    if soma/notas == 10:
        print("Aprovado com distinção")
    elif soma/notas < 7:
        print("Reprovado!")
    else:
        print("Aprovado")

#poderia usar else elif mas o mais facil deu certo entao tudo ok kkkkk


