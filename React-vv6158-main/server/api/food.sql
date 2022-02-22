DROP table if EXISTS food CASCADE;

CREATE TABLE food (
    id          SERIAL PRIMARY KEY NOT NULL,
    name        VARCHAR(30),
    category    VARCHAR(30),
    calories    VARCHAR(10),
    total_fat   VARCHAR(10),
    sat_fat     VARCHAR(10),
    trans_fat   VARCHAR(10),
    protein     VARCHAR(10),
    total_carbs VARCHAR(10)
);
