import psycopg2
import requests

DB_PARAMS = {
    "host": "localhost",
    "port": 5432,
    "database": "ricknmorty",
    "user": "postgres",
    "password": "password" # ПРОВЕРЬ СВОЙ ПАРОЛЬ
}

# --- ДОБАВЛЕННЫЙ БЛОК: ОПИСАНИЕ ФУНКЦИИ ---
def create_table():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    
    create_script = '''
        CREATE TABLE IF NOT EXISTS raw_characters (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            status VARCHAR(50),
            species VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    '''
    
    cur.execute(create_script)
    conn.commit()
    print("✅ Таблица raw_characters создана или уже существует.")
    
    cur.close()
    conn.close()
# ------------------------------------------

def fetch_and_save():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        characters = data['results']
        
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        
        insert_query = "INSERT INTO raw_characters (name, status, species) VALUES (%s, %s, %s)"
        for char in characters:
            cur.execute(insert_query, (char['name'], char['status'], char['species']))
        
        conn.commit()
        print(f"✅ Успех! Загружено {len(characters)} персонажей в базу ricknmorty.")
        
        cur.close()
        conn.close()
    else:
        print(f"❌ Ошибка API: Код {response.status_code}")

if __name__ == "__main__":
    create_table() 
    fetch_and_save()
