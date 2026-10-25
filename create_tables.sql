CREATE TABLE "comments" (
	"id"	INTEGER,
	"id_movies"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"comment"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "qualifications" (
	"id"	INTEGER,
	"id_movies"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"qualification"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

