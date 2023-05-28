import grpc
import example_pb2
import example_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = example_pb2_grpc.MyServiceStub(channel)
    response = stub.SayHello(example_pb2.HelloRequest(name='Royyan'))
    print(response.message)
    
    # Call the getUser method
    user_request = example_pb2.UserRequest(id=1)
    user_response = stub.GetUser(user_request)
    print("User Name:", user_response.name)
    for email in user_response.email:
        print("Email Address:", email.address)
        print("Is Primary:", email.is_primary)
    if user_response.HasField("contact"):
        if user_response.contact.HasField("phone_number"):
            print("Phone Number:", user_response.contact.phone_number)
        elif user_response.contact.HasField("social_media"):
            print("Social Media:", user_response.contact.social_media)

if __name__ == '__main__':
    run()
