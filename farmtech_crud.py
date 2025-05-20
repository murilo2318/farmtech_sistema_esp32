
import sqlite3
from datetime import datetime

conn = sqlite3.connect('farmtech.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    umidade REAL,
    ph REAL,
    fosforo INTEGER,
    potassio INTEGER,
    status_bomba INTEGER
)
''')
conn.commit()

def inserir_leitura(umidade, ph, fosforo, potassio, status_bomba):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO leituras (timestamp, umidade, ph, fosforo, potassio, status_bomba)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (agora, umidade, ph, fosforo, potassio, status_bomba))
    conn.commit()
    print('Leitura inserida com sucesso!')

def consultar_todas_leituras():
    cursor.execute('SELECT * FROM leituras')
    return cursor.fetchall()

def consultar_leitura_por_id(id_leitura):
    cursor.execute('SELECT * FROM leituras WHERE id = ?', (id_leitura,))
    return cursor.fetchone()

def atualizar_leitura(id_leitura, umidade, ph, fosforo, potassio, status_bomba):
    cursor.execute('''
    UPDATE leituras SET
        umidade = ?,
        ph = ?,
        fosforo = ?,
        potassio = ?,
        status_bomba = ?
    WHERE id = ?
    ''', (umidade, ph, fosforo, potassio, status_bomba, id_leitura))
    conn.commit()
    print(f'Leitura {id_leitura} atualizada com sucesso!')

def deletar_leitura(id_leitura):
    cursor.execute('DELETE FROM leituras WHERE id = ?', (id_leitura,))
    conn.commit()
    print(f'Leitura {id_leitura} deletada com sucesso!')

if __name__ == '__main__':
    inserir_leitura(55.3, 7.2, 1, 0, 1)

    print('Todas as leituras:')
    for linha in consultar_todas_leituras():
        print(linha)

    print('\nConsulta leitura id=1:')
    print(consultar_leitura_por_id(1))

    atualizar_leitura(1, 60.5, 7.0, 0, 1, 0)

    deletar_leitura(1)

    conn.close()
