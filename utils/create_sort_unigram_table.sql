DROP TABLE IF EXISTS raw_tagged_unigram_counter;   
CREATE TABLE raw_tagged_unigram_counter(
	first_gram VARCHAR,
	first_tag VARCHAR,
	tagged_unigram_count int
);

DROP TABLE IF EXISTS tagged_unigram_counter;   
CREATE TABLE tagged_unigram_counter(
	first_gram VARCHAR,
	first_tag VARCHAR,
	tagged_unigram_count int
);

COPY raw_tagged_unigram_counter FROM 'C:/HSE/3_module/BWI_project/data/train_tagged_unigrams_counter.csv' DELIMITER ' ' CSV HEADER;

INSERT INTO tagged_unigram_counter
SELECT *
FROM raw_tagged_unigram_counter
ORDER BY tagged_unigram_count DESC;

COPY tagged_unigram_counter TO 'C:/HSE/3_module/BWI_project/data/train_tagged_unigrams_counter_sort.csv' DELIMITER ' ' CSV HEADER;
