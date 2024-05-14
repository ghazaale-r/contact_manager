-- user table --
CREATE TABLE users(
    user_id serial PRIMARY KEY,
    username varchar(255) unique NOT NULL,
    password varchar(255) NOT NULL,
);

-- contact table --
CREATE TABLE contacts(
    contact_id serial PRIMARY KEY,
    name varchar(255) NOT NULL,
    email varchar(255),
    user_id int not null,
    foreign key (user_id) references users(user_id)
);


-- address table --
CREATE TABLE Addresses(
    addr_id serial PRIMARY KEY,
    city varchar(255) ,
    state varchar(255) ,
    street varchar(255),
    zip_code varchar(255) not null,
    contact_id int not null,
    foreign key (contact_id) references contacts(contact_id)
);


-- phones table --
CREATE TABLE phones(
    phone_id serial PRIMARY KEY,
    label varchar(255) ,
    phone_number varchar(255) not null,
    contact_id int not null,
    foreign key (contact_id) references contacts(contact_id)
);
