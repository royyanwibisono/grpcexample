import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures
import time

class MyServiceServicer(example_pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        message = f"Hello, {request.name}!"
        return example_pb2.HelloResponse(message=message)
    def GetUser(self, request, context):
        # Assuming we have a function to retrieve user information based on the ID
        user = get_user_by_id(request.id)
        user_response = example_pb2.UserResponse()
        user_response.name = user.name
        for email in user.email:
            email_proto = user_response.email.add()
            email_proto.address = email.address
            email_proto.is_primary = email.is_primary
        return user_response

def get_user_by_id(user_id):
    # Assuming implementation to retrieve user information
    # based on the provided ID
    
    # Dummy user data for demonstration purposes
    dummy_users = {
        1: {
            "name": "John Doe",
            "email": [
                {"address": "john.doe@example.com", "is_primary": True},
                {"address": "johndoe@gmail.com", "is_primary": False}
            ]
        },
        2: {
            "name": "Jane Smith",
            "email": [
                {"address": "jane.smith@example.com", "is_primary": True},
                {"address": "janesmith@gmail.com", "is_primary": False}
            ]
        }
    }

    # Retrieve the user data based on the provided ID
    if user_id in dummy_users:
        user_data = dummy_users[user_id]
        user = example_pb2.UserResponse()
        user.name = user_data["name"]
        for email_data in user_data["email"]:
            email = user.email.add()
            email.address = email_data["address"]
            email.is_primary = email_data["is_primary"]
        return user
    else:
        raise Exception("User not found")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
