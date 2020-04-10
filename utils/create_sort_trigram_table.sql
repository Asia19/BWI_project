DROP TABLE IF EXISTS raw_tagged_trigram_counter;
CREATE TABLE raw_tagged_trigram_counter(
	first_gram VARCHAR,
	second_gram VARCHAR,
	third_gram VARCHAR,
	first_tag VARCHAR,
	second_tag VARCHAR,
	third_tag VARCHAR,
	tagged_trigram_count int
);

DROP TABLE IF EXISTS tagged_trigram_counter;
CREATE TABLE tagged_trigram_counter(
	first_gram VARCHAR,
	second_gram VARCHAR,
	third_gram VARCHAR,
	first_tag VARCHAR,
	second_tag VARCHAR,
	third_tag VARCHAR,
	tagged_trigram_count int
);

COPY raw_tagged_trigram_counter FROM 'C:/HSE/3_module/BWI_project/data/train_tagged_trigrams_counter.csv' DELIMITER ' ' CSV HEADER;

INSERT INTO tagged_trigram_counter
SELECT *
FROM raw_tagged_trigram_counter
ORDER BY tagged_trigram_count DESC;

COPY tagged_trigram_counter TO 'C:/HSE/3_module/BWI_project/data/train_tagged_trigrams_counter_sort.csv' DELIMITER ' ' CSV HEADER;

DROP TABLE IF EXISTS filtered_tagged_trigram_counter;
SELECT *
INTO TABLE filtered_tagged_trigram_counter
FROM tagged_trigram_counter
WHERE (first_tag, second_tag, third_tag) in (SELECT * FROM necessary_tags_of_trigram);