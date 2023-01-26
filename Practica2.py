import os


class OperasBas:
    # declaración de las propiedades

    # declaración de constructor
    def _init_(self):
        pass
    # declaración de métodos

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multi(self, num1, num2):
        res = num1 * num2
        return res

    def div(self, num1, num2):
        res = num1 / num2
        return res


def main():
        os.system('cls')
        ob = OperasBas()
        opt = -1
        res = 0
        while (opt != 0):
            print('calculadora de angel \n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n0.- Salir\n')
            opt = int(
                input('Que opcion elijes:'))
            if (opt == 0):
                break
            os.system('cls')
            num1 = int(input('Ingresa el primer número:'))
            num2 = int(input('Ingresa el segundo número:'))
            if (opt == 1):
                res = ob.suma(num1, num2)
            elif (opt == 2):
                res = ob.resta(num1, num2)
            elif (opt == 3):
                res = ob.multi(num1, num2)
            elif (opt == 4):
                res = ob.div(num1, num2)
            print('El resultado es: {}'.format(res))
            

if __name__ == '__main__':
    main()


    
