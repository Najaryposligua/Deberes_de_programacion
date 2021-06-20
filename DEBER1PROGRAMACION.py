#EJERCICIO 
class Clases:
    def __init__(self):
        pass

    def Calculo(self):
        sb = float(input("Ingrese salario base: "))
        v1 = float(input("Ingrese total de la primera Ventas: "))
        v2 = float(input("Ingrese total de la segunda Ventas: "))
        v3 = float(input("Ingrese total de la tercera Ventas: "))
        con = (v1+v2+v3)*0.10
        print("el sueldo base es: $",sb)
        print("la comisiion es %",con)
        print("sueldo tota: $", sb+con)

    def Circulo(self):
        print("Calculo area de un circulo: ")
        r = float(input("Ingresar radio del circulo: "))
        pi = 3.1416
        ar = pi * r
        print("El area del circulo es:", ar)


    def Aprobado(self):
        cal = float(input("Ingrese nota: "))
        if cal >= 7:
            print("Aprobado")
        else:
            print("Reprobado")

    def sueldo(self):
        hora = int(input("Ingresar el numero de horas trabajadas por el empleado: "))
        valor = float(input("Ingresar el valor de pago por cada hora: "))
        hoex = hora - 40
        tt = 0
        if hora > 40:
            if hoex > 8:
                ho1 = hoex - 8
                tt = (valor * 2 * 8) + (valor * 3 * ho1)
            else:
                tt = valor * 2 * hora
        else:
            tt = valor * hora
        print(
            "El trabajador trabajo:{} de horas, "
            "cada hora es pagada con un valor de:{}, "
            "por lo tanto su pago es de:{}".format(hora, valor, tt))

    def valoralto(self):
        nun1 = int(input("Ingresar el primer valor: "))
        nun2 = int(input("Ingresar el segundo valor: "))
        nun3 = int(input("Ingresar el tercer valor: "))
        if nun1 > nun2 and nun1 > nun3:
            print("El primer valor ingresado es el mayor")
        elif nun2 > nun3:
            print("El segundo valor ingresado es el mayor")
        elif nun1 == nun2 == nun3:
            print("Los tres valores ingresados son iguales")
        else:
            print("El tercer valor ingresado es el mayor")

    def tresvalores(self):
        num = int(input("Ingresar un valor entero para la accion del 1 al 3: "))
        con = int(input("Ingresar un numero: "))
        if num == 1:
            p = 100 * con
            print(
                "La accion:{}, hace que el valor constante se multiple con el segun valor ingresado por lo tanto la respuesta es:{}".format(
                    num, p))
        elif num == 2:
            p = 100 ** num
            print(
                "La accion:{}, hace que el valor constante se eleve con el segun valor ingresado por lo tanto la respuesta es:{}".format(
                    num, p))
        elif num == 3:
            p = 100 / num
            print(
                "La accion:{}, hace que el valor constante se divida con el segun valor ingresado por lo tanto la respuesta es:{}".format(
                    num, p))
        else:
            p = 0
            print("No realiza ninguna accion por lo tanto su valor es reemplazo con", p)

    def cicloswf(self):
        n1 = int(input("Ingresar un numero entero: "))
        sum = 0
        for i in range(n1):
            sum = sum + i
        print("La suma de:{} da un total de:{}".format(n1, sum))

        print("Ciclo while")
        n2 = int(input("Ingresar un numero entero: "))
        t1 = 0
        pro = 1
        c = 1
        while c <= n2:
            t1 = t1 + c
            pro = pro * c
            c += 1
        print("El  total de la suma de:{} es de:{} y el de los productos es de:{}".format(n2, t1, pro))


objclases = Clases()
objclases.Calculo()
objclases.Circulo()
objclases.Aprobado()
objclases.sueldo()
objclases.valoralto()
objclases.tresvalores()
objclases.cicloswf()