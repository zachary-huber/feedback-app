-- write a query to create a table named "users" with the following columns: user_id, first_name, last_name, email, password, created_at, updated_at, last_login, and is_admin. Make sure to set the appropriate data types, set user_id as the primary key, and set created_at and updated_at as NOT NULL
CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    last_login DATETIME,
    is_admin BOOLEAN NOT NULL,
    PRIMARY KEY (user_id)
);


-- write a query to create a table named forms with the following columns: form_id, user_id, title, description, created_at, updated_at, and is_active, form_html. Make sure to set the appropriate data types, set form_id as the primary key, set created_at and updated_at as NOT NULL, and set user_id as a foreign key that references the user_id column in the users table
CREATE TABLE forms (
    form_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    is_active BOOLEAN NOT NULL,
    form_html TEXT NOT NULL,
    PRIMARY KEY (form_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- write a query to create a table named "responses" with the following columns: response_id, form_id, user_id, response_html, created_at, and updated_at. Make sure to set the appropriate data types, set response_id as the primary key, set created_at and updated_at as NOT NULL, and set form_id and user_id as foreign keys that reference the form_id and user_id columns in the forms and users tables, respectively
CREATE TABLE responses (
    response_id INT NOT NULL AUTO_INCREMENT,
    form_id INT NOT NULL,
    user_id INT NOT NULL,
    response_html TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (response_id),
    FOREIGN KEY (form_id) REFERENCES forms(form_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);