from src.services.UserService import UserService

class DefaultService:

    @staticmethod
    def signup(data):
        return UserService.addNewUser(data)
    
    @staticmethod
    def login(data):
        try: 
            email = data.get("email")
            password = data.get("password")
            user =  UserService.getUserByEmail(email)
            if user.get("password") == password:
                return {"success": True, "user": {"email": email, "userName": user.get("username")}}
            return {"success": False, "message": "Email / Password is incorrect, please retry!"}
        except Exception as e:
            print(f"An error occurred while logging in an user: {str(e)}")
            return {"success": False, "message": "Unable to log you in at the moment, please try again later!"}
