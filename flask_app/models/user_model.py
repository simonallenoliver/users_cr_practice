from flask_app.config.mysqlconnection import connectToMySQL




class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users
        """

        results = connectToMySQL('user_schema').query_db(query)

        user_row = []
        for row in results:
            new_user = cls(row)

            user_row.append(new_user)
        
        return user_row
    
    @classmethod
    def create_user(cls, form_data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES(%(first_name)s,%(last_name)s,%(email)s);
        """

        return connectToMySQL("user_schema").query_db(query, form_data)

    @classmethod
    def delete(cls, id):
        data = {
            "id":id
        }

        query = """
            DELETE FROM users WHERE id = %(id)s
        """
        return connectToMySQL("user_schema").query_db(query, data)
    
# form pre-population needs get_one class method. this selects a row of data from the db to use on the update page
    @classmethod
    def get_one(cls, id):
        data = {
            "id":id
        }

        query = """
            SELECT * FROM users WHERE id = %(id)s
        """
        results = connectToMySQL("user_schema").query_db(query, data)

        if results:
            row = results[0]
            new_user = cls(row)
            return new_user
    
    @classmethod
    def update(cls, data):

        query = """
            UPDATE users 
            SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE id = %(id)s
        """
        connectToMySQL("user_schema").query_db(query, data)
