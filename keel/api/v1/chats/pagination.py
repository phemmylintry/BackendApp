
from rest_framework.pagination import LimitOffsetPagination

CHAT_PAGINATION_LIMIT = 20

class ChatsPagination(LimitOffsetPagination):

	default_limit = CHAT_PAGINATION_LIMIT
	max_limit = 1000000
	min_limit = 1
	min_offset = 0
	max_offset = 1000000

