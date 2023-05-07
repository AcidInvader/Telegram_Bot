from model import Users, session

class ModelProcessor:

    def add_user(self, id):
        user = Users(user_id = id)
        session.add(user)
        session.commit()
    
    def delete_user(self):
        pass


    def check_subscription(self):
        pass

    def user_exists(self, el):
        user = session.query(Users).filter_by(user_id=el)
        if user:
            return True
        else:
            return False