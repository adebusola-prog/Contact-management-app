from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ResponsePagination(PageNumberPagination):
   page_size = 2