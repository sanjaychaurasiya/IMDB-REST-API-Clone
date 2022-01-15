from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    # page_size limit the number of object to a single page in this case only 1 object
    page_size = 1
    # page_query_param is used to give any name to the query in this case it is p
    # page_query_param = 'p'
    # page_size_query_param is used to give client permission to get as many object
    # as they want by specifying size
    page_size_query_param = 'size'
    # this limit the number of object per page
    max_page_size = 10

    # last_page_strings = 'last'


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10


class WatchListCursorPagination(CursorPagination):
    page_size = 1
    ordering = '-created'
