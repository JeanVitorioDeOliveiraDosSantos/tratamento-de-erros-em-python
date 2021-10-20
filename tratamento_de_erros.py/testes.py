# Crie uma exeption que faça uma interrupção caso um obj seja com um valor inteiro superior a 100

class Numero:
    b = str()
    c = str() 

    b = int(input(" Qual o numero a para ser multiplicado? :  "))
    c = int(input(" Qual o lado b para ser multiplicado? :  "))
    a = b ** c 
    h = a
    IOO = 100
    try:
        IOO >= h
    except ValueError as NumeroDeErro:
        print(" Numeros maiores que 100 não serão imprimidos ")
    else:
        print(" O resultado é :  --> ")
        print(f"numero é :  {h}")
    finally:
        print(" Opercao finalizada ")