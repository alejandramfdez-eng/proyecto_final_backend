CREATE TABLE "record" (
	"id"	INTEGER,
	"id_movies"	TEXT NOT NULL,
	"title"	TEXT NOT NULL,
	"year"	TEXT NOT NULL,
	"gender"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "comments" (
	"id"	INTEGER,
	"id_movies"	TEXT NOT NULL,
	"person"	TEXT NOT NULL,
	"comment"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "qualification" (
	"id"	INTEGER,
	"id_movies"	TEXT NOT NULL,
	"person"	TEXT NOT NULL,
	"qualification"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

