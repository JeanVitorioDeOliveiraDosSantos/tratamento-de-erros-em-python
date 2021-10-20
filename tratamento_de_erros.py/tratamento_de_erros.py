try:
    a  = list()
    print(f" lista a = {a[1]} ")
### : aqui adicionei um erro de indice ou seja estou pedindo 
### : para printar a lista a no indice 1 mas a lista está vazia 
except Exception as error:
    print(" Erro inesperado! ")
### caso  o except detecatar um error qualquer ou seja qualquer erro ele printa : #### Erro inesperado! ####
except KeyError as erro_de_indice:
    print(" Erro de indice! ")
### caso o except detectar o erro especificamente o KeyError ele printa = ### Erro de indice! ###  
else:
    print(" O else carrega caso os except não rodar, ou seja caso não aver erros no cod ")
### Else terá a mesma função que tinha no if, ou seja caso o execpt não detectar erro o else será rodado
finally:
    a = [1, 2]
    print(" Apesar do erro o cod está funconando normal ")
print(f" a lista a :{a} ")
### O finally será rodado todavez independenete das outras estruturas (execpt, try) mas no final do cod. 


# Faça um programa que solicite ao usuário 2 números inteiros. A seguir, calcule e mostre a divisão do primeiro pelo segundo. 
# Obrigatório a inclusão do bloco try-except nas leituras (ValueError) e no cálculo da divisão (ZeroDivisionError). 
# O programa deve ter também uma clásula "finalmente" com a mensagem "FIM !!". Atenção: O programa só continua se não houver erro.

numero1 = 0
numero2 = 0
numero3 = str()
numero4 = 0
try:
    numero1 = int(input(" numero 1 "))
    numero2 = int(input(" numero 2 "))
except ValueError as ZeroDivisionError:
    if (numero1 != int()):
        numero3 = "Segundo numero digitado não é um inteiro"

    else:
        numero3 = "Primeiro numero digitado não é um inteiro"
    
    print(f" {numero3} ")
else:
    numero_resposta = numero1 / numero2
    print("claculo sendo feito")
    print(f" o resultado é : {numero_resposta} ")

finally:
    print("FIM")

# /////// fim 



