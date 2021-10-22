
            

def jason():
    print("sla")
    

        

g = jason()

try:
    class Frutas:
        def __init__(self, frutas, carne):
            self.frutas = frutas
            self.carne = carne
        
            if (self.frutas == "frango"and "gado" and "porco"):
                u = list()
                print(u[1])
                raise IndexError('Fruta não pode ser um animal ')
                return IndexError

            if (self.carne == "maçã" and "laranja" and "abacaxi"):
                u = list()
                print(u[1])
                raise IndexError(' Animal não pode ser uma fruta ')



    f = Frutas("laranja", "frango")

except IndexError as erro: 
    raise
    print(erro)

else:
    g = f.carne
    h = f.frutas
    print(f" {g}  ,  {h} ")

finally:
    print("fim")






def teste_num(n, N):
    assert n > N, (n,' é maior que  ',N)

print(teste_num(6, 5))

import random


def pulou_sem_responder(n, m):
 

    try:
        d = n / m

    except ValueError as ZeroDivisionError:
        print(" erro de  calculo ")
            

        pass 
        
    else:
        numero_resposta = numero1 / numero2
        print("claculo sendo feito")
        print(f" O resultado é : {numero_resposta} ")

    finally:
        print("FIM")




    


class motion:
    def __init__(self):
        self.saldo_p = input("deseja ver seu saldo?(S/N)").upper()
        if (self.saldo_p == "N"):
            print("até a proxima")
        if (self.saldo_p == "S"):
            self.endress = input(" qual seu endereço de conta? ")
            self.saldo_v = random.randint(0, 1000000)
            print(f" seu saldo é de {self.saldo_v} ")

person1 = motion()


d = 9 / 2
print(d)



def erro_de_progress(numero):
    if (numero == float()):
        print("numero float")
    if (numero == int()):
        print("numero inteiro")
    if (numero == str()):
        print(" uma str() ")
    if (numero == list()):
        print(" uma lista ")
    else:
        print(" não é nada ")


person3 = erro_de_progress(9)