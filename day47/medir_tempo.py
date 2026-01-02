import time

def medir_tempo_execucao(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"O tempo total da funcao foi: {total_time}")
        return result
    return wrapper

@medir_tempo_execucao
def tarefa_1():
    print("Rodando a funcao...")
    time.sleep(2)
    print("Funcao finalizada")

tarefa_1()