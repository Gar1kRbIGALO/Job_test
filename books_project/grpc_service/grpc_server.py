import sys
import grpc
from concurrent import futures
import books_pb2
import books_pb2_grpc
import django
import os
from kafka import KafkaConsumer
import json
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')

django.setup()

from books.models import Book


class BookServiceServicer(books_pb2_grpc.BookServiceServicer):
    def GetBookById(self, request, context):
        try:
            book = Book.objects.get(id=request.id)
            return books_pb2.BookResponse(
                id=book.id,
                title=book.title,
                author=book.author,
                publication_date=str(book.publication_date)
            )
        except Book.DoesNotExist:
            context.set_details('Book not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return books_pb2.BookResponse()

    def GetAllBooks(self, request, context):
        books = Book.objects.all()
        return books_pb2.BookListResponse(
            books=[
                books_pb2.Book(
                    id=book.id,
                    title=book.title,
                    author=book.author,
                    publication_date=str(book.publication_date)
                ) for book in books
            ]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()


def consume_messages():
    consumer = KafkaConsumer(
        'books_topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        group_id='grpc_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        print(f"Received message: {data}")



threading.Thread(target=consume_messages).start()

if __name__ == '__main__':
    serve()
