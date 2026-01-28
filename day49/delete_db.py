import sqlite3

conexao = sqlite3.connect("exemplo.db")

cursor = conexao.cursor()

cursor.execute("DELETE FROM personagens WHERE nome = 'Superman'")

conexao.commit()

print("O personagem foi deletado com sucesso")

cursor.close()
conexao.close()