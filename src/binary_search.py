


def binary_search(array, target: int) -> int:
    baixo = 0
    alto = len(array) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = array[meio]

        if chute == target:
            return meio
        if chute > target:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    return -1