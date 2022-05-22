import mysql.connector
from config import HOST, USER, PASSWORD
import utils

DATABASE_NAME='Escapade'

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE_NAME
    )
    return connection


# 1 RECOMMENDATIONS

def insert_new_recommendation(user_id,selected_spot):
    try:
      db_connection = _connect_to_db()
      cur = db_connection.cursor()
      #print("Connected to DB: %s" % db_name)
      query = """INSERT INTO saved_recommendations
      (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
      VALUES ("{}", "{}", "{}", "{}", "{}")
      """.format(

          user_id,
          selected_spot["NAME"],
          selected_spot["ADDRESS"],
          selected_spot["CATEGORY"],
          selected_spot["PHONE"]
      )
      cur.execute(query)
      db_connection.commit()
      cur.close()

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()


def get_all_recommendations():
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM saved_recommendations"""
        cur.execute(query)
        results = cur.fetchall()

        return results  # this is needed or it gives none data type

    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


# 2 APPLICATION RAITING

def insert_application_rating(user_id,given_rating):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        query = """INSERT INTO application_rating 
            (USER_ID,APPLICATION_RATING) 
            VALUES ("{}", "{}")""".format(
            user_id,
            given_rating,
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()

def get_all_ratings():
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM application_rating"""
        cur.execute(query)
        results = cur.fetchall()

        return results  # this is needed or it gives none data type

    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()

# 3 REVIEWS OF RECOMMENDATIONS

def get_recent_recommendations(user_id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        query="""SELECT * FROM saved_recommendations WHERE user_id='"""+ str(user_id) + \
              "' AND RECOMMENDATION_ID NOT IN (SELECT RECOMMENDATION_ID FROM reviews_recommendations )" \
              " ORDER BY recommendation_id DESC LIMIT 1"

        cur.execute(query)
        last_recommendation=cur.fetchall()
        cur.close()
        return last_recommendation
    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()


def insert_review(user_id,recommendation_id,name,review):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        query = """
                INSERT INTO reviews_recommendations 
                (USER_ID,RECOMMENDATION_ID,NAME,REVIEW)
                VALUES ("{}", "{}","{}","{}")
                """.format(user_id,recommendation_id,
                           name,review)
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()


def get_all_reviews():
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM reviews_recommendations"""
        cur.execute(query)
        results = cur.fetchall()

        return results  # this is needed or it gives none data type

    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()

# 3 ESCAPADE USERS

def get_all_records(email):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        query = """SELECT * FROM escapade_users WHERE EMAIL_ADDRESS='"""+ email + "'"
        cur.execute(query)
        results = cur.fetchall()
        return results

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()




def insert_new_users(name,email_address,password):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        query = """ INSERT INTO escapade_users (USER_NAME,EMAIL_ADDRESS,USER_PASSWORD)
        VALUES (%s,%s,%s)"""
        record = (name,email_address,password)
        cur.execute(query,record)
        db_connection.commit()
        cur.close()

    except Exception as e:
        print(e)
        raise DbConnectionError("Sign up failed")

    finally:
        if db_connection:
            db_connection.close()

def get_all_users():
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM escapade_users """
        cur.execute(query)
        results = cur.fetchall()

        return results  # this is needed or it gives none data type


    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


def check_user_exists(value,type):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute("Select * from escapade_users where " + type  +"= '"+ value+"'")
        check1 = cur.fetchone()
        if check1==None:
            return False
        else:
            return True
        cur.close()

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()


def check_rating_exists(user_id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute("Select * from application_rating where USER_ID=" + "'"+ str(user_id)+"'")
        check1 = cur.fetchone()
        cur.close()
        if check1 is None:
            return False
        else:
            return True

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()



def password_from_inputted_username(username, password):
    try:
        records = get_all_records(username)
        if len(records)==0:
            return 0
        else:
            if records[0][3]==password:
                usr=utils.user(records[0][0],records[0][1],records[0][2],records[0][3])
                return usr
            else:
                return 0
    except Exception as e:
        print(e)

def get_password_from_user(username):
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM escapade_users WHERE USER_NAME='""" + username + "'"
        cur.execute(query)
        results = cur.fetchall()

        return results  # this is needed or it gives none data type

    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()







if __name__ == '__main__':
    _connect_to_db('Escapade')
