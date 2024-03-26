CREATE TABLE "episodes" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "original_airdate" date
);

CREATE TABLE "subjects" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "colors" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "episodes_subjects" (
  "episode_id" integer,
  "subject_id" integer
);

CREATE TABLE "episodes_colors" (
  "episode_id" integer,
  "color_id" integer
);

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("id");

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("subject_id") REFERENCES "subjects" ("id");

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("id");

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("id");
