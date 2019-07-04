import sqlite3

from dynamic.db import db_file_name


class Region:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def all(cls):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM regions;')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in data:
            result.append(cls(row[0], row[1]))
        return result


class RegionWithCommentAmount:

    def __init__(self, id, name, comment_amount):
        self.id = id
        self.name = name
        self.comment_amount = comment_amount

    @classmethod
    def get_related_comments_more_than(cls, comments_count):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT regions.region_id, regions.name, COUNT(comment_id) as comment_count FROM regions LEFT OUTER JOIN cities ON (regions.region_id = cities.region_id) LEFT OUTER JOIN comments ON (cities.city_id = comments.city) GROUP BY  regions.region_id HAVING comment_count > ?;',
            [int(comments_count)])
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in data:
            result.append(cls(row[0], row[1], row[2]))
        return result


class City:
    def __init__(self, id, name, region_id):
        self.id = id
        self.name = name
        self.region_id = region_id

    @classmethod
    def all_cities_in_region(cls, region_id):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cities WHERE region_id=?;', [region_id])
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in data:
            result.append(cls(row[0], row[1], row[2]))
        return result


class CityWithCommentAmount:
    def __init__(self, id, name, comment_amout):
        self.id = id
        self.name = name
        self.comment_amount = comment_amout

    @classmethod
    def get_related_comments_more_than(cls, region_id):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT cities.city_id, cities.name, COUNT(comment_id) as comment_count FROM cities LEFT OUTER JOIN comments ON (cities.city_id = comments.city) WHERE region_id=? GROUP BY  cities.city_id;',
            [region_id])
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in data:
            result.append(cls(row[0], row[1], row[2]))
        return result


class Comment:

    def __init__(self, id=None, name='', surname=None, father_name=None, city=None, phone=None, email=None,
                 comment=''):
        self.id = id
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.city = city
        self.phone = phone
        self.email = email
        self.comment = comment

    def save(self):
        print(self.__dict__)
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO comments (name, surname, father_name, city, phone, email, comment) VALUES (?, ?, ?, ?, ?, ?, ?);',
            [self.name,
             self.surname,
             self.father_name,
             self.city,
             self.phone,
             self.email,
             self.comment])
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def all(cls):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM comments;')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        result = []
        for row in data:
            result.append(cls(*row))
        return result

    @classmethod
    def delete(cls, id):
        conn = sqlite3.connect(db_file_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM comments WHERE comment_id=?;', [id])
        conn.commit()
        cursor.close()
        conn.close()
