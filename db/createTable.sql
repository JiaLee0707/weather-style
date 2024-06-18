CREATE TABLE clothes_top (  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(100) NOT NULL,  
    link VARCHAR(5000) NOT NULL,  
    image_path VARCHAR(200) NOT NULL,  
    temperature_start INT(3) NOT NULL,
    temperature_end INT(3) NOT NULL,
    tag VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE clothes_bottom (  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(100) NOT NULL,  
    link VARCHAR(5000) NOT NULL,  
    image_path VARCHAR(200) NOT NULL,  
    temperature_start INT(3) NOT NULL,
    temperature_end INT(3) NOT NULL,
    tag VARCHAR(50) NOT NULL,
    clothes_top_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (clothes_top_id) REFERENCES clothes_top(id)
);

CREATE TABLE style_list (  
    id INT NOT NULL AUTO_INCREMENT,  
    matching_date DATETIME NOT NULL,
    temperature INT(3) NOT NULL,
    clothes_top_id INT NOT NULL,
    clothes_bottom_id INT NOT NULL,
    created_date DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (clothes_top_id) REFERENCES clothes_top(id),
    FOREIGN KEY (clothes_bottom_id) REFERENCES clothes_bottom(id)
);