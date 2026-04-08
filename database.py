import config
from mysql.connector import Error

def get_available_dogs():
    conn = config.get_db_connection()
    if not conn: return []
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, age, breed FROM Dog WHERE adopted = 0")
        return cur.fetchall()
    except Error as e:
        print(f"Error al obtener perros: {e}")
        return []
    finally:
        cur.close()
        conn.close()

def get_dog_by_id(dog_id):
    conn = config.get_db_connection()
    if not conn: return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, age, breed FROM Dog WHERE id = %s", (dog_id,))
        return cur.fetchone()
    except Error as e:
        print(f"Error al obtener perro por ID: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def register_adoption_transactional(dog_id, name, lastname, address, id_card):
    conn = config.get_db_connection()
    if not conn: return False
    cur = conn.cursor()
    try:
        conn.start_transaction()
       
        sql_person = "INSERT INTO Person (name, lastName, id_card) VALUES (%s, %s, %s)"
        cur.execute(sql_person, (name, lastname, id_card))
        person_id = cur.lastrowid
        
        
        sql_adopter = "INSERT INTO Adopter (person_id, address) VALUES (%s, %s)"
        cur.execute(sql_adopter, (person_id, address))
        
        
        sql_adoption = "INSERT INTO Adoption (adopter_id, dog_id, adoption_date) VALUES (%s, %s, NOW())"
        cur.execute(sql_adoption, (person_id, int(dog_id)))
        
        
        cur.execute("UPDATE Dog SET adopted = 1 WHERE id = %s", (int(dog_id),))
        
        conn.commit()
        return True
    except Exception as e:
        print(f"--- ERROR REAL EN DB: {e} ---") 
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

def get_adoption_history():
    conn = config.get_db_connection()
    if not conn: return []
    cur = conn.cursor()
    try:
        query = """
            SELECT 
                P.name, 
                P.lastName, 
                D.name, 
                D.breed, 
                A.adoption_date 
            FROM Adoption A
            JOIN Person P ON A.adopter_id = P.id
            JOIN Dog D ON A.dog_id = D.id
            ORDER BY A.adoption_date DESC
        """
        cur.execute(query)
        return cur.fetchall()
    except Error as e:
        print(f"Error en historial: {e}")
        return []
    finally:
        cur.close()
        conn.close()