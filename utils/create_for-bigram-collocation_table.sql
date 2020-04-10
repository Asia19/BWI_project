DROP TABLE IF EXISTS unigram_table1;
CREATE TABLE unigram_table1(
	bigram_fg VARCHAR,
	bigram_ft VARCHAR,
	first_gram_count int
);

DROP TABLE IF EXISTS unigram_table2;
CREATE TABLE unigram_table2(
	bigram_sg VARCHAR,
	bigram_st VARCHAR,
	second_gram_count int
);

INSERT INTO unigram_table1 SELECT * FROM tagged_unigram_counter;
INSERT INTO unigram_table2 SELECT * FROM tagged_unigram_counter;

SELECT T.first_gram,
	T.first_tag,
	T1.first_gram_count,
	T.second_gram,
	T.second_tag,
	T2.second_gram_count,
	T.tagged_bigram_count
INTO TABLE table_for_collocation_criteria
FROM tagged_bigram_counter as T
	JOIN unigram_table1 as T1 ON T.first_gram = T1.bigram_fg AND T.first_tag = T1.bigram_ft
	JOIN unigram_table2 as T2 ON T.second_gram = T2.bigram_sg AND T.second_tag = T2.bigram_st;

COPY table_for_collocation_criteria TO 'C:\HSE\3_module\BWI_project\data\raw_table_for_collocation' DELIMITER ' ' CSV HEADER;