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
    PRIMARY KEY (user_id),
    user_avatar VARCHAR(255) NOT NULL
);


CREATE TABLE forms (
    form_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    is_active BOOLEAN NOT NULL,
    form_JSON TEXT NOT NULL,
    PRIMARY KEY (form_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE responses (
    response_id INT NOT NULL AUTO_INCREMENT,
    form_id INT NOT NULL,
    user_id INT NOT NULL,
    response_JSON TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (response_id),
    FOREIGN KEY (form_id) REFERENCES forms(form_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);