class tupla_transicion:
    def __init__(self, _estado, _caracter , _direccion):
        self.estado = _estado
        self.caracter = _caracter
        self.direccion = _direccion

class turing_machine:
    def __init__(self, transicion, string_cinta):
        if isinstance(transicion, dict):
            self.tabla_transicion = transicion
        self.cinta = list(string_cinta)
        self.current_state = 's'
        self.current_position = 0
    def strart(self):
        result = False
        if self.current_state == 's':
            while (self.current_state!= 'Alto' and self.current_state!= 'Si' and self.current_state!= 'No' and self.current_state !='Error'):
                car = self.cinta[self.current_position]
                tupla = "('" + self.current_state + "', '" + car + "')"
                if  tupla in self.tabla_transicion:
                    accion = self.tabla_transicion[tupla]
                    if isinstance(accion, tupla_transicion):
                        self.current_state = accion.estado
                        print(self.cinta[self.current_position], accion.caracter, accion.direccion, accion.estado)
                        self.cinta[self.current_position] = accion.caracter
                        if accion.direccion == 'l':
                            self.current_position = self.current_position - 1
                        else:
                            if accion.direccion == 'r':
                                self.current_position = self.current_position + 1
                            else:
                                if accion.direccion != 'o':
                                    #salida si hay error
                                    self.current_state = 'Error'

        if self.current_state!= 'Alto' or self.current_state!= 'Si' or  self.current_state!= 'No':
            result = True
        return result

        # { a^nb^2n | n > 0 } Acepta cadena donde por cada a bebe haber el dooble de b, ejemplo abb, aabbbb, aabbb, n es mayor a 0
        #Andres Sebastian Sierra Ruiz, Teoría Automatas, grupo:008 #1747193
MT = dict()

stri = '@'
stri2 = 'aabbbb@' #Probar @aaabbbb, @aaabbb, @aaaabbbbbbbb, @aaaabb
#q0 = s , q1 = t q2= u q3 = v

MT["('s', '@')"] = tupla_transicion('No', '@', 'o')
MT["('s', 'a')"] = tupla_transicion('t', 'x', 'r')
MT["('t', 'a')"] = tupla_transicion('t', 'a', 'r')
MT["('t', 'y')"] = tupla_transicion('t', 'y', 'r')
MT["('t', 'b')"] = tupla_transicion('u', 'y', 'r')
MT["('u', 'b')"] = tupla_transicion('v', 'y', 'l')
MT["('v', 'a')"] = tupla_transicion('v', 'a', 'l')
MT["('v', 'y')"] = tupla_transicion('v', 'y', 'l')
MT["('v', 'x')"] = tupla_transicion('s', 'x', 'r')
MT["('s', 'y')"] = tupla_transicion('Sí', '@', 'o')



tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)



tm = turing_machine(MT,stri2)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)
