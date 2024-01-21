from flask_app.config.mysqlconnection import connectToMySQL




class user:
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

