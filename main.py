import psycopg2
import requests

DB_PARAMS = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "password" # ТВОЙ ПАРОЛЬ
}

def fetch_and_save():
    url = "https://rickandmortyapi.com/api/character"
    
    # 1. Проверяем ответ сервера
    response = requests.get(url)
    
    if response.status_code == 200:
            data = response.json()
            characters = data['results']
            
            # 2. Подключаемся
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            
            # 3. Сохраняем
            insert_query = "INSERT INTO raw_characters (name, status, species) VALUES (%s, %s, %s)"
            for char in characters:
                cur.execute(insert_query, (char['name'], char['status'], char['species']))
            
            conn.commit()
            print(f"✅ Успех! Загружено {len(characters)} персонажей.")
            
            cur.close()
            conn.close()
    else:
        print(f"❌ Ошибка API: Код {response.status_code}. Сервер прислал не JSON.")

if __name__ == "__main__":
    fetch_and_save()
