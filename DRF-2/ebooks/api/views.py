from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import isAdminUserOrReadOnly

class EbookListCreateAPIView(generics.ListCreateAPIView):
  queryset = Ebook.objects.all()
  serializer_class = EbookSerializer
  permission_classes = [isAdminUserOrReadOnly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Ebook.objects.all()
  serializer_class = EbookSerializer
  permission_classes = [isAdminUserOrReadOnly]
  
  
class ReviewCreateAPIView(generics.CreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def perform_create(self, serializer):
      ebook_pk = self.kwargs.get("ebook_pk")
      review_author = self.request.user
      ebook = get_object_or_404(Ebook, pk=ebook_pk)
      serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  
# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#   queryset = Ebook.objects.all()
#   serializer_class = EbookSerializer
  
#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)