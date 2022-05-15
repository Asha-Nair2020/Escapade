import mysql.connector
from config import HOST, USER, PASSWORD
import utils



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


# 1 RECOMMENDATIONS
# this is what we are adding, as a Dict in key value pairs (here is where saved recommendation function will go)
# this is just an example
recommendation = {
    'userID': '123',
    'recsID': '456',
    'recsNames': 'abc'
}

def insert_new_recommendation(recommendation):
    try:
        db_name = 'try'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
        # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
        # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)
        query = """INSERT INTO saved_recs ({}) VALUES ('{}', '{}', '{}')""".format(
            ', '.join(recommendation.keys()),
            recommendation['userID'],
            recommendation['recsID'],
            recommendation['recsNames'],
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


#
# 2 REVIEWS

# this is what we are adding, as a Dict in key value pairs (where the users review function will go/imported in)
# this is just an example
reviews = {
    'userID': '123',
    'RecsID': '456',
    'RecsNames': 'abc',
    'Review': '123'
}


# def insert_new_review(reviews):
#    try:
#       db_name = 'try'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print("Connected to DB: %s" % db_name)
#
#         # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
#         # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
#         # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)
#         query = """INSERT INTO reviews ({}) VALUES ('{}', '{}', '{}', '{}')""".format(
#             ', '.join(reviews.keys()),
#             reviews['userID'],
#             reviews['RecsID'],
#             reviews['RecsNames'],
#             reviews['Review']
#         )
#         cur.execute(query)
#         db_connection.commit()
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#
#     print("Record added to DB")
#
#





# # 3 ESCAPADE USERS
#
# # this is what we are adding, as a Dict in key value pairs (here is where users info function will go)
# # this is just an example - will most likely change into methods/inputs


# users = {
#     'userID': '123',
#     'UsersNames': '456',
#     'UsersPasswords': 'abc'
# }

def insert_new_users():
    user = utils.register()
    saved = {
        user['name'],
        user['email_address'],
        user['password']
    }
    try:
        db_name = 'Escapade'

        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
        # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
        # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)


def get_all_records():
    try:
        db_name = "project"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM escapade_users"""
        cur.execute(query)
        results = cur.fetchall()

        return results #this is needed or it gives none data type


    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


#if using check1 to check if username is already present, need to enter username as input
def insert_new_users(record):
    try:
        db_name = "try"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("connected to DB: ", db_name)

        # cur.execute("Select * from escapade_users where USER_NAME = ?", (username))
        # check1 = cur.fetchone()
        
        # query = """INSERT INTO escapade_users ({}) VALUES ('{}', '{}', '{}')""".format(
        #   ', '.join(saved.values()),
        #    user['name'],
        #   user['email_password'],
         #   user['password'],
        
        query = """ INSERT INTO escapade_users ({})
        VALUES ("{}", "{}")
        """.format(",".join(record.keys()), record['USER_NAME'], record['USER_PASSWORD'])
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Sign up failed")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


def password_from_inputted_username(username, password):
    records = get_all_records()
    password_based_on_user = [x for x in records if x[1] == username]
    print(password_based_on_user)   ##remove later
    for i in password_based_on_user:
        print(i[2])    ## remove latez
    if password == i[2]:
        print("congratulations!")
    else:
        print("try again")


if __name__ == '__main__':
    _connect_to_db('Escapade')
    # insert_new_users()
    # insert_new_recommendation(recommendation)
    # insert_new_review(reviews)

