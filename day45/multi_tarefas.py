import threading
import time

def tarefa(nome, tempo_execucao):
    print(f"Tarefa {nome} iniciada...")
    time.sleep(tempo_execucao)
    print("Tarefa {nome} finalizada")

thread1 = threading.Thread(target=tarefa, args=("Download tarefa 1", 3))
thread2 = threading.Thread(target=tarefa, args=("Download tarefa 2", 4))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Todas as tarefas foram finalizadas")