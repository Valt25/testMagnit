CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY  AUTOINCREMENT,
    name VARCHAR,
    region_id INTEGER,

    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

INSERT INTO regions (region_id, name) VALUES (1, 'Краснодарский край');
INSERT INTO regions (region_id, name) VALUES (2, 'Ростовская область');
INSERT INTO regions (region_id, name) VALUES (3, 'Ставропольский край');

INSERT INTO cities (city_id, name, region_id) VALUES (1, 'Краснодар', 1);
INSERT INTO cities (city_id, name, region_id) VALUES (2, 'Кропоткин', 1);
INSERT INTO cities (city_id, name, region_id) VALUES (3, 'Славянск', 1);

INSERT INTO cities (city_id, name, region_id) VALUES (4, 'Ростов', 2);
INSERT INTO cities (city_id, name, region_id) VALUES (5, 'Шахты', 2);
INSERT INTO cities (city_id, name, region_id) VALUES (6, 'Батайск', 2);

INSERT INTO cities (city_id, name, region_id) VALUES (7, 'Ставрополь', 3);
INSERT INTO cities (city_id, name, region_id) VALUES (8, 'Пятигорск', 3);
INSERT INTO cities (city_id, name, region_id) VALUES (9, 'Кисловодск', 3);


CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    surname VARCHAR,
    father_name VARCHAR,
    city INTEGER,
    phone VARCHAR,
    email VARCHAR,
    comment VARCHAR,

    FOREIGN KEY (city) REFERENCES cities(city_id)
);