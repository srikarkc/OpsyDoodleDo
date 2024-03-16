from concurrent import futures
import grpc
import string_service_pb2
import string_service_pb2_grpc

class StringCounterServicer(string_service_pb2_grpc.StringCounterServicer):
    def CountCharacters(self, request, context):
        count = len(request.user_string)
        return string_service_pb2.CharacterCountResponse(count=count)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    string_service_pb2_grpc.add_StringCounterServicer_to_server(StringCounterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()