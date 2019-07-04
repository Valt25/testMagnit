from dynamic.db.models import Region, City, Comment, RegionWithCommentAmount, CityWithCommentAmount
from dynamic.utils import jsonify, Response, get_params_in_dict, parse_post_in_dict
from dynamic.controllers import create_comment as create_comment_controller

@jsonify
def get_region_list(environ):
    regions = Region.all()
    result = []
    for region in regions:
        result.append(region.__dict__)
    return Response(200, result)


@get_params_in_dict
@jsonify
def get_cities_list(environ):
    region_id = environ['QUERY_DICT']['region_id']
    cities = City.all_cities_in_region(region_id)
    result = []
    for city in cities:
        result.append(city.__dict__)
    return Response(200, result)


@parse_post_in_dict
def create_comment(environ):
    post_dict = environ['POST_DICT']
    comment, message = create_comment_controller(post_dict)
    if comment:
        comment.save()
        headers = [('Location', '/view/')]
        return Response(301, '', headers)
    else:
        return Response(400, message)


@jsonify
def get_comment_list(environ):
    comments = Comment.all()
    result = []
    for comment in comments:
        result.append(comment.__dict__)
    return Response(200, result)


@parse_post_in_dict
def delete_comment(environ):
    post_dict = environ['POST_DICT']
    comment_id = post_dict['comment_id']
    Comment.delete(comment_id)
    return Response(200)


@get_params_in_dict
@jsonify
def get_popular_regions(environ):
    query = environ['QUERY_DICT']
    if 'amount' in query:
        amount = query['amount']
    else:
        amount = -1
    regions = RegionWithCommentAmount.get_related_comments_more_than(amount)
    result = []
    for region in regions:
        result.append(region.__dict__)
    return Response(200, result)


@get_params_in_dict
@jsonify
def get_cities_with_comment_amount_list(environ):
    region_id = environ['QUERY_DICT']['region_id']
    cities = CityWithCommentAmount.get_related_comments_more_than(region_id)
    result = []
    for city in cities:
        result.append(city.__dict__)
    return Response(200, result)