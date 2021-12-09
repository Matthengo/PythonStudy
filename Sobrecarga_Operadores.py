'''
No Python, o comportamento dos operadores Ã© definido por mÃ©todos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuÃ¡rio.

Operador    MÃ©todo          OperaÃ§Ã£o
------------------------------------------------------
+           __add__         adiÃ§Ã£o
-           __sub__         subtraÃ§Ã£o
*           __mul__         multiplicaÃ§Ã£o
/           __div__         divisÃ£o
//          __floordiv__    divisÃ£o inteira
%           __mod__         MÃ³dulo
**          __pow__         PotÃªncia
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversÃ£o
'''
class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y
    
    def __repr__(self):
        return f"<class 'Retangulo({self.x},{self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(20, 10)
r3 = r1 + r2

print(r2 == r1)