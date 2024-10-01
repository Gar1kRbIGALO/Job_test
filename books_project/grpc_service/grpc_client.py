import grpc
import books_pb2
import books_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = books_pb2_grpc.BookServiceStub(channel)

        response = stub.GetBookById(books_pb2.BookRequest(id=1))
        print(f'Book with ID 1: {response.title}, {response.author}, {response.publication_date}')

        response = stub.GetAllBooks(books_pb2.EmptyRequest())
        for book in response.books:
            print(f'{book.id}: {book.title} by {book.author}')


if __name__ == '__main__':
    run()
