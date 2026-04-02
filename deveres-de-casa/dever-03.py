def eh_palindromo(arr, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1

    if inicio >= fim:
        return True
    
    if arr[inicio] != arr[fim]:
        return False
    
    return eh_palindromo(arr, inicio + 1, fim - 1)


# Testes

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(eh_palindromo(array1))
print(eh_palindromo(array2))
print(eh_palindromo(array3))
print(eh_palindromo(array4))
