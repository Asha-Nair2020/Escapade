import mysql.connector
from config import HOST, USER, PASSWORD


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection

def get_all_records():
    try:
        db_name = 'Project'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print('Connected to DB:', db_name)

        query = """SELECT *
                    FROM Saved_Recommendations"""
        cur.execute(query)
        results = cur.fetchall() # list of tuples. Where each tuple is a record

        return results
        #for i in results:
        #    print(i)

    except Exception:
        raise DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


def get_recent_recommendations(user_id):
    records = get_all_records()
    recommendations = [x for x in records if x[1] == user_id]
    last_recommendation=' '
    for i in recommendations:
        last_recommendation=i[2]
        # print(i[2])
    print(last_recommendation)
    return last_recommendation




def insert_record(record):
    db_name = 'Project'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    print('Connected to DB:', db_name)

    query = """
            INSERT INTO Review ({})
            VALUES ('{}', '{}')
            """.format(','.join(record.keys()),
                       record['recommended_place'],
                       record['review'])
    cur.execute(query)
    db_connection.commit()
    cur.close()

    db_connection.close()


if __name__ == '__main__':
    get_recent_recommendations(3)
    # insert_record(record)
    # print(get_all_records())


