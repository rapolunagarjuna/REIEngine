from src.models.User import User  # Import the User model

class UserService:

    @staticmethod
    def getAllUsers():

        users = User.objects().all()
        users_list = [{'username': user.username, 'age': user.age} for user in users]

        print("getAllUsers method called:", users_list)
        return users_list
    

    @staticmethod
    def addNewUser(userdata):
        try:
            new_user = User(username=userdata['username'], age=userdata['age'])
            new_user.save()  # Save the new user to the database

            # Return a success response with the user ID and a 201 status code
            return {"message": "User added successfully", "user_id": str(new_user.id), "status_code": 201}
        
        except Exception as e:
            # Log the exception for debugging and monitoring
            print(f"An error occurred while adding a user: {str(e)}")
            return {"error": "An error occurred while adding the user", "status_code": 500 }
