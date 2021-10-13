try:
    a  = list()
    print(f" lista a = {a[1]} ")
### : aqui adicionei um erro de indice ou seja estou pedindo 
### : para printar a lista a no indice 1 mas a lista está vazia 
except Exception as error:
    print(" Erro inesperado! ")
### caso  o except detecatar um eror qualquer oun seja qualquer erro ele printa : #### Erro inesperado! ####
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
### O finally será rodado todavez mas no final do cod 
#  