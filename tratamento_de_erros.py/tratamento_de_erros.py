try:
    a  = list()
    print(f" lista a = {a[1]} ")
except Exception as error:
    print(" Erro inesperado! ")
except KeyError as erro_de_indice:
    print(" Erro de indice! ")
else:
    print(" O else carrega caso os except não rodar, ou seja caso não aver erros no cod ")
finally:
    a = [1, 2]
    print(" Apesar do erro o cod está funconando normal ")
print(f" a lista a :{a} ")