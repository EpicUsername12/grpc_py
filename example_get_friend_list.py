import grpc
from friends import friends_service_pb2_grpc
from friends import get_user_friend_pids_rpc_pb2

HOST = "localhost"
PORT = 50051

PID = 1544386850
API_KEY = "7c...."

grpc_client = grpc.insecure_channel('%s:%d' % (HOST, PORT))
friends_service = friends_service_pb2_grpc.FriendsStub(grpc_client)

response = friends_service.GetUserFriendPIDs(get_user_friend_pids_rpc_pb2.GetUserFriendPIDsRequest(pid=PID), metadata=[("x-api-key", API_KEY)])

print("Friend list: ", response.pids)
