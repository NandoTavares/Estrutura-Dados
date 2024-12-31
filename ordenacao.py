import time

# ler números de um arquivo
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        return []

def print_vector(vec):
    print(" ".join(map(str, vec)))

# Implementação do SelectionSort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Implementação do InsertionSort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():

    filename = input("Digite o caminho do arquivo: ").strip()
    
    # Leitura dos números do arquivo
    numbers = read_numbers_from_file(filename)
    if not numbers:
        return

    print("Array original:")
    print_vector(numbers)

    # Testando o SelectionSort
    selection_test = numbers[:]
    start_time = time.time()
    selection_sort(selection_test)
    selection_duration = (time.time() - start_time) * 1000  
    print("\nArray ordenado com SelectionSort:")
    print_vector(selection_test)
    print(f"Tempo de execução (SelectionSort): {selection_duration:.2f} ms")

    # Testando o InsertionSort
    insertion_test = numbers[:]
    start_time = time.time()
    insertion_sort(insertion_test)
    insertion_duration = (time.time() - start_time) * 1000  
    print("\nArray ordenado com InsertionSort:")
    print_vector(insertion_test)
    print(f"Tempo de execução (InsertionSort): {insertion_duration:.2f} ms")

    print("\nComparação dos tempos de execução:")
    print(f"SelectionSort: {selection_duration:.2f} ms")
    print(f"InsertionSort: {insertion_duration:.2f} ms")

if __name__ == "__main__":
    main()
