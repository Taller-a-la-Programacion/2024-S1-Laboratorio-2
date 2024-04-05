import Laboratorio2;
import pytest;

    
def test_sumaImparesPares_1():
    assert Laboratorio2.sumaImparesPares([0,2,3,4], [4, 8, 6, 0]) == [13, 14]
    
def test_sumaImparesPares_2():
    assert Laboratorio2.sumaImparesPares([10, 0], [100, 2]) == [110, 2]
    
def test_sumaImparesPares_3():
    assert isinstance(Laboratorio2.sumaImparesPares([1,2], "dos"), str) == isinstance("Error: segundo argumento debe ser entero", str)


def test_descomponerNumeros_1():
    assert Laboratorio2.descomponerNumeros([8524,256,1023,3698,-204,139]) == [[8,2,4],[2,6],[0,2],[6,8],[-2,0,-4]]

def test_descomponerNumeros_2():
    assert isinstance(Laboratorio2.descomponerNumeros([]), str) == isinstance("Error: Lista Vacia", str)



def test_construirNumeros_1():
    assert Laboratorio2.construirNumeros( [[8,2,4], [2,6],[2],[6,8],[-2,0,-4]] ) ==  [824, 26, 2, 68, -204]

def test_construirNumeros_1():
    assert Laboratorio2.construirNumeros( [[18,2,4], [2,6],[60,800]] ) == [1824, 26, 60800]
