CREATE FUNCTION get_total_bigram_count()
RETURNS integer as $total_count$
declare
	total_count integer;
BEGIN
   SELECT sum(tagged_bigram_count) into total_count FROM tagged_bigram_counter;
   RETURN total_count;
END;
$total_count$ LANGUAGE plpgsql;

SELECT first_gram,
	second_gram,
	first_tag,
	second_tag,
	(sqrt(tagged_bigram_count::float) - first_gram_count::float * second_gram_count::float / (SELECT get_total_bigram_count())::float / sqrt(tagged_bigram_count::float)) as student_t
INTO TABLE bigram_student_t
FROM table_for_collocation_criteria
ORDER BY student_t DESC;

COPY bigram_student_t TO 'C:\HSE\3_module\BWI_project\data\bigram_student-t_table.csv' DELIMITER ' ' CSV HEADER;