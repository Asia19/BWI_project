CREATE FUNCTION get_chi_squared_value(tagged_bigram_count int, first_gram_count int, second_gram_count int)
RETURNS real as $$
DECLARE
	total_bigram_count real := (SELECT get_total_bigram_count());
	o11 int := tagged_bigram_count;
	o12 int := second_gram_count - o11;
	o21 int := first_gram_count - o11;
	o22 real :=  total_bigram_count - o11 - o12 - o21;
BEGIN
   RETURN total_bigram_count * (o11 * o22 - o12 * o21)^2 / ((o11 + o12)*(o11 + o21)*(o12 + o22)*(o21 + o22))::float;
END;
$$ LANGUAGE plpgsql;

SELECT first_gram,
	second_gram,
	first_tag,
	second_tag,
	--get_chi_squared_value(tagged_bigram_count, first_gram_count, second_gram_count) as chi_squared
	(SELECT get_total_bigram_count())::float * ((tagged_bigram_count*((SELECT get_total_bigram_count()) - second_gram_count - first_gram_count + tagged_bigram_count)-(second_gram_count - tagged_bigram_count)*(first_gram_count - tagged_bigram_count))::float)^2 / (second_gram_count*first_gram_count*((SELECT get_total_bigram_count()) - first_gram_count)*((SELECT get_total_bigram_count()) - second_gram_count))::float  as chi_squared
INTO TABLE bigram_chi_squared
FROM table_for_collocation_criteria
ORDER BY chi_squared DESC;

COPY bigram_chi_squared TO 'C:\HSE\3_module\BWI_project\data\bigram_chi-squared_table.csv' DELIMITER ' ' CSV HEADER;