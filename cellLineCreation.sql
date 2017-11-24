CREATE DATABASE conpendium;

CREATE TABLE mammalianCells(
    cellname VARCHAR(20),
    origin VARCHAR(50),
    sizes FLOAT,
    morph VARCHAR(25),
    gType VARCHAR(25),
    PRIMARY KEY (cellname))

CREATE TABLE materials(
    cellname VARCHAR(20),
    productSheet URL,
    mediaType VARCHAR(40),
    FOREIGN KEY (cellname) REFERENCES mammalianCells(cellname))

CREATE TABLE applications(
    cellname VARCHAR(20),
    toppubs  URL,
    ranks INTEGER
    FOREIGN KEY (cellname) REFERENCES mammalianCells(cellname))
