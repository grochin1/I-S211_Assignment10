import sqlite3

schemas = [
    """ 
    CREATE TABLE person(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    ); """,
    """ 
    CREATE TABLE pet(
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    ); """,
    """ 
    CREATE TABLE person_pet(
        person_id INTEGER,
        pet_id INTEGER
    ); """
]


def main():
    conn = sqlite3.connect('pets.db')
    for schema in schemas:
        conn.execute(schema)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
