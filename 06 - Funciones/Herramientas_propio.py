class Herramientas:
    def __init__(self, lista):
        self.lista = lista
    
    def es_primo(self):
        for i in self.lista:
            if self.verifica_primo (i):
                print(f"el número {i} es primo")
            else:
                print(f"el número {i} no es primo")

    def grados (self, origen, destino):
        for i in self.lista:
            print(f"{i}grados {origen} equivale a {self.__grados(i,origen,destino)} {destino}")

    def factorial(self):
        for i in self.lista:
            print(f"el factiorial de {i} es {self.fac(i)}")

    
    def verifica_primo (self, num):
        self.num = num
        es_primo = True
        for i in range (2, self.num):
            if self.num % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal (self):
        lista_unicos = []
        lista_repeticiones = []

        if len(self.lista) == 0:
            return None

        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append (elemento)
                lista_repeticiones.append(1)

        moda = lista_unicos [0]
        maximo = lista_repeticiones [0]

        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos [i]
                maximo = lista_repeticiones[i]

            return moda, maximo
        

    def __grados(self, val, med_or, med_dest):
        self.val = val
        self.med_or = med_or
        self.med_dest = med_dest
    
        if self.med_or == "F":
            if self.med_dest == "F":
                val_dest = val
            elif self.med_dest == "C":
                val_dest = (val-32) * 5 / 9
            elif self.med_dest  == "K" or "k":
                val_dest = (val - 32) * (5 / 9) + 273.15
            else:
                print ("Medida incorrecta, revisa de nuevo")
        
        elif self.med_or == "K":
            if self.med_dest == "K":
                val_dest = val
            elif self.med_dest == "C":
                val_dest = val -273.15
            elif self.med_dest == "F":
                val_dest = (val - 273.15) * (9 / 5) + 32
            else:
                print ("Medida incorrecta, revisa de nuevo")
        
        elif self.med_or == "C":
            if self.med_dest == "C":
                val_dest = val
            elif self.med_dest == "F":
                val_dest = val * (9 / 5) + 32
            elif self.med_dest == "K":
                val_dest = val + 273.15
            else:    
                print ("Medida incorrecta, revisa de nuevo")
        
        else:
            print ("el valor es incorrrecto, revisalo")
        
        return val_dest
                
    def fac (self, num):
        self.num = num
        if type(self.num) != int:
            print ("el valor ingresado no es un número entero")
        
        elif self.num <= 0:
            print ("el valor ingresado es un número negativo")

        elif type (self.num) == int:
            for i in range(2,self.num):
                self.num = i * self.num    
            return self.num