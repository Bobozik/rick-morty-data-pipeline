import psycopg2  # Библиотека-драйвер для работы с Postgres

# Параметры подключения
DB_PARAMS = {
    "host": "localhost",
    "port": 5432,
    "database": "ricknmorty",
    "user": "postgres",
    "password": "postgres" 
}

def check_db_connection():
    try:
        # 1. Пробуем «постучаться» в базу
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        
        # 2. Выполняем простой SQL-запрос через Python
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        
        print(f"✅ Успех! Подключено к: {db_version}")
        
        # 3. Закрываем соединение
        cur.close()
        conn.close()
        
    except Exception as error:
        print(f"❌ Ошибка подключения: {error}")

if __name__ == "__main__":
    check_db_connection()
