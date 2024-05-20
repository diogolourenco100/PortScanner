import time

def Calctime(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Execution time: {tempo_execucao:.2f} seconds.")
        return resultado
    return wrapper
