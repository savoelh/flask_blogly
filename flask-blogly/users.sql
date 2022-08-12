DROP DATABASE IF EXISTS users;

CREATE DATABASE users;

 \c users

CREATE TABLE users
   (
      id SERIAL PRIMARY KEY,
      first_name VARCHAR (10) NOT NULL,
      last_name VARCHAR (10) NOT NULL,
      image_url VARCHAR (200)
   );

INSERT INTO users
   (first_name, last_name, image_url)

VALUES 
   ('Yui', 'Hirasawa', 'https://static.wikia.nocookie.net/k-on/images/4/45/Yui_Character_.jpg'),
   ('Mio', 'Akiyama', 'https://static.wikia.nocookie.net/k-on/images/5/56/Mio_Character.jpg'),
   ('Ritsu', 'Tainaka', 'https://static.wikia.nocookie.net/k-on/images/7/74/Ritsu_Character_.jpg'),
   ('Tsumigu', 'kotobuki', 'https://static.wikia.nocookie.net/k-on/images/9/9e/Mugi_Character_.jpg'),
   ('Azusa', 'Nakano', 'https://static.wikia.nocookie.net/k-on/images/3/35/Azusa_Character.jpg');

CREATE TABLE posts
   (
      id SERIAL PRIMARY KEY,
      title VARCHAR (20) NOT NULL,
      content VARCHAR (500) NOT NULL,
      created_at TIMESTAMP DEFAULT NOW(),
      users_id INTEGER REFERENCES users
   );


INSERT INTO posts
   (title, content, users_id)

VALUES
   ('My Post!', 'This is a test example of a post', 1);


CREATE TABLE tags
   (
      id SERIAL PRIMARY KEY,
      name TEXT UNIQUE 
   );

INSERT INTO tags
   (name)

VALUES
   ('Turtle'),
   ('Hare'),
   ('Guitar'),
   ('Bass'),
   ('Drums'),
   ('Piano');

CREATE TABLE posttags
   (
        id SERIAL PRIMARY KEY,
        post_id INTEGER REFERENCES posts,
        tag_id INTEGER REFERENCES tags
   );