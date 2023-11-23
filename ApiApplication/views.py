from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookApiView(APIView):
    serializer_class = BookSerializer

    def get(self, request):
        all_books = Book.objects.all().values()
        return Response({"Message": "List Of Books", "Book List": all_books})

    def post(self, request):
        serializer_obj = BookSerializer(data=request.data)
        if serializer_obj.is_valid():
            book = Book.objects.create(
                id=serializer_obj.validated_data.get("id"),
                title=serializer_obj.validated_data.get("title"),
                author=serializer_obj.validated_data.get("author")
            )
            return Response({"Message": "New Book Added!", "Book": BookSerializer(book).data})
        else:
            return JsonResponse({"error": f"Invalid data: {serializer_obj.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return Response({"Message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return JsonResponse({"error": f"Book with id {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)
