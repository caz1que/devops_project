use db;

CREATE TABLE Users(
    UserID int not null AUTO_INCREMENT,
    Name varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (UserID)
);

INSERT INTO Users(Name, Surname)
VALUES("Mister", "Black"), ("Missis", "Green");  
