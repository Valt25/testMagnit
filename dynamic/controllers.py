from dynamic.db.models import Comment
import re


def create_comment(post_dict):
    comment = Comment()
    error = False
    message = ''

    name_field = 'name'
    if name_field in post_dict:
        name = post_dict[name_field]
        if name != '':
            comment.name = name
        else:
            error = True
            message += 'Name is required'
    else:
        error = True
        message += 'Name is required'

    surname_field = 'surname'
    if surname_field in post_dict:
        surname = post_dict[surname_field]
        if surname != '':
            comment.surname = surname
        else:
            error = True
            message += 'Surname is required'
    else:
        error = True
        message += 'Surname is required'

    comment_field = 'comment'
    if comment_field in post_dict:
        comment_text = post_dict[comment_field]
        if comment_text != '':
            comment.comment = comment_text
        else:
            error = True
            message += 'Comment is required'
    else:
        error = True
        message += 'Comment is required'

    father_name_field = 'father_name'
    if father_name_field in post_dict:
        father_name = post_dict[father_name_field]
        if father_name != '':
            comment.father_name = father_name

    town_field = 'town'
    if town_field in post_dict:
        town = post_dict[town_field]
        try:
            comment.city = int(town)
        except ValueError:
            error = True
            message += 'City id field have to be integer field\n'

    phone_field = 'phone'
    if phone_field in post_dict:
        phone = post_dict[phone_field]

        if phone != '':
            if re.match(r'\([0-9]{3}\) [0-9]*', phone):

                comment.phone = phone
            else:
                error = True
                message += 'Phone is invalid'

    email_field = 'email'
    if email_field in post_dict:
        email = post_dict[email_field]

        if email != '':
            if re.match(r'[^@]+@[^@]+\.[^@]+', email):

                comment.email = email
            else:
                error = True
                message += 'Email is invalid'

    if error:
        return False, message
    else:
        return comment, message
