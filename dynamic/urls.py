from dynamic.views import get_region_list, get_cities_list, create_comment, get_comment_list, delete_comment, \
    get_cities_with_comment_amount_list, get_popular_regions

urls = [
    ('comment', 'POST', create_comment),
    ('comment', 'GET', get_comment_list),
    ('comment', 'DELETE', delete_comment),

    ('regions', 'GET', get_region_list),
    ('regions/popular', 'GET', get_popular_regions),


    ('cities', 'GET', get_cities_list),
    ('cities/comment/amount', 'GET', get_cities_with_comment_amount_list),

    # ('cities', 'GET', get_cities_list)
]
