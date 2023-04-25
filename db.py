import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.coursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            self.coursor.execute("INSERT INTO 'users' ('user_id') VALUE (?)", (user_id,))

    # check user
    def user_exists(self,user_id):
        with self.connection:
            result = self.coursor.execute("SELECT * FROM 'users' WHERE 'user_id = ?",
                                          (user_id,).fetchall())
            return bool(len(result))
    
    # setup nickname for user
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.coursor.execute("UPDATE 'users' SET 'nackname' = ? WHERE 'user_id' = ?",
                                        (nickname, user_id,))
    # get step of registration user
    def get_signup(self, user_id):
        with self.connection:
            result = self.coursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?",
                                          (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup
    
    # change signup
    def set_signup(self, user_id, signup):
        with self.connection:
            return self.coursor.execute("UPDATE 'users' SET 'signup' = ? WHERE 'user_id' = ?",
                                        (signup, user_id,))
