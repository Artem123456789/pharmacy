from rest_framework.pagination import PageNumberPagination


class MedicinesListPaginator(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 9
    max_page_size = 100
