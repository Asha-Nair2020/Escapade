import mysql.connector
from config import HOST, USER, PASSWORD


def _connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


def insert_new_recommendation(selected_spot):
    db_name = 'Escapade'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    print("Connected to DB: %s" % db_name)
    query = """INSERT INTO saved_recommendations s 
    (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
    VALUES ("{}", "{}", "{}", "{}", "{}")
    INNER JOIN escapade_users e ON s.USER_ID = e.USER_ID"
    """.format(

        2,
        selected_spot["NAME"],
        selected_spot["ADDRESS"],
        selected_spot["CATEGORY"],
        selected_spot["PHONE"]
    )
    cur.execute(query)
    db_connection.commit()
    cur.close()




def insert_application_rating(given_rating):
    db_name = 'Escapade'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    print("Connected to DB: %s" % db_name)
    query = """INSERT INTO application_rating 
    (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
    VALUES ("{}", "{}")""".format(

        2,
        given_rating["APPLICATION_RATING"],
    )
    cur.execute(query)
    db_connection.commit()
    cur.close()



# uncomment to use - will most likely be a for loop
if __name__ == '__main__':
    _connect_to_db('Escapade')
    # insert_new_recommendation(recommendation)
    # insert_new_review(reviews)
    # insert_new_users(users)
