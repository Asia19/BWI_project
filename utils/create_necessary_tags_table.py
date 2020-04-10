import psycopg2


query20 = '''
    CREATE TABLE necessary_tags_of_bigram(
    first_tag VARCHAR,
    second_tag VARCHAR,
    PRIMARY KEY(first_tag,second_tag)
    );'''

query21 = "INSERT INTO necessary_tags_of_bigram VALUES (%s, %s)"

query30 = '''
    CREATE TABLE necessary_tags_of_trigram(
    first_tag VARCHAR,
    second_tag VARCHAR,
    third_tag VARCHAR,
    PRIMARY KEY(first_tag,second_tag,third_tag)
    );'''

query31 = "INSERT INTO necessary_tags_of_trigram VALUES (%s, %s, %s)"


if __name__=='__main__':
    n = 2
    # JJ - adjective or numeral, JJR  - adjective, JJS - adjective, superlative
    adjs = ['JJ', 'JJR', 'JJS']
    # NN noun, common; NNP - noun, proper, sing.; NNPS - noun, proper, plural; NNS - noun, common, plural
    nouns = ['NN', 'NNS', 'NNP', 'NNPS']
    tag_combs = []
    queries = {2:(query20,query21),3:(query30,query31)}
    if n == 2:
        for noun in nouns:
            tag_combs += [(adj, noun) for adj in adjs]  # A,N
            tag_combs += [(noun_, noun) for noun_ in nouns]  # N, N
    if n == 3:
        for noun in nouns:
            for adj in adjs:
                for noun_ in nouns:
                    tag_combs.append((adj, noun, noun_))  # A, N, N
                    tag_combs.append((noun, adj, noun_))  # N, A, N
                tag_combs += [(adj, adj_, noun) for adj_ in adjs]  # A, A, N
            for noun_ in nouns:
                tag_combs += [(noun, noun_, noun__) for noun__ in nouns]  # N, N, N
                tag_combs.append((noun, 'IN', noun_))  # N, P, N

    conn = psycopg2.connect(host="localhost",database="BWI", user="postgres", password="igsvemina1201")
    cur = conn.cursor()
    cur.execute(queries[n][0])
    for tag_comb in tag_combs:
        # cur.execute(*queries[n][1](tag_comb))
        cur.execute(queries[n][1],tag_comb)
    conn.commit()
