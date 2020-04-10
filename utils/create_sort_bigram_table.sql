DROP TABLE IF EXISTS raw_tagged_bigram_counter;
CREATE TABLE raw_tagged_bigram_counter(
	first_gram VARCHAR,
	second_gram VARCHAR,
	first_tag VARCHAR,
	second_tag VARCHAR,
	tagged_bigram_count int
);

DROP TABLE IF EXISTS tagged_bigram_counter;
CREATE TABLE tagged_bigram_counter(
	first_gram VARCHAR,
	second_gram VARCHAR,
	first_tag VARCHAR,
	second_tag VARCHAR,
	tagged_bigram_count int
);

COPY raw_tagged_bigram_counter FROM 'C:/HSE/3_module/BWI_project/data/train_tagged_bigrams_counter.csv' DELIMITER ' ' CSV HEADER;

INSERT INTO tagged_bigram_counter
SELECT *
FROM raw_tagged_bigram_counter
ORDER BY tagged_bigram_count DESC;

COPY tagged_bigram_counter TO 'C:/HSE/3_module/BWI_project/data/train_tagged_bigrams_counter_sort.csv' DELIMITER ' ' CSV HEADER;

DROP TABLE IF EXISTS filtered_tagged_bigram_counter;
SELECT *
INTO TABLE filtered_tagged_bigram_counter
FROM tagged_bigram_counter
WHERE (first_tag, second_tag) in (SELECT * FROM necessary_tags_of_bigram);