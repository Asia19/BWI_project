SELECT first_gram,
	second_gram,
	first_tag,
	second_tag,
	log(tagged_bigram_count::float * (SELECT get_total_bigram_count()::float) / first_gram_count::float / second_gram_count::float) as max_likelihood
INTO TABLE bigram_max_likelihood
FROM table_for_collocation_criteria
ORDER BY max_likelihood DESC;

COPY bigram_max_likelihood TO 'C:\HSE\3_module\BWI_project\data\bigram_max_likelihood_table.csv' DELIMITER ' ' CSV HEADER;