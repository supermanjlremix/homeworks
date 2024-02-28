def get_smiles(number: int=0) -> str:
    smile = ';)'
    if type(number) is int and number > 0:
        return smile * number
    return 


def test_get_smiles():
    assert get_smiles(5) == ';););););)'
    assert get_smiles(4.5) == None
    assert get_smiles('3') == None
    assert get_smiles('One') == None
    assert get_smiles(True) == None
    assert get_smiles(False) == None
    assert get_smiles() == None


test_get_smiles()

number = input("Введите число для вывода смайликов: ")
try:
    number= int(number)
except ValueError as error:
    print(error)
    exit()
print(get_smiles(number))
