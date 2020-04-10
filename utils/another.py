import nltk


def get_ngrams(sentence, n):
    for i in range(len(sentence) - n + 1):
        yield sentence[i:i+n]


def get_ngrams_str(sentence, n):
    for i in range(len(sentence) - n + 1):
        yield ' '.join(sentence[i:i+n])


def get_decoding(tags):
    pos_dict = { 'CC':'Coordinating conjunction', \
        'CD':'Cardinal number', \
        'DT':'Determiner', \
        'EX':'Existential there', \
        'FW':'Foreign word', \
        'IN':'Preposition or subordinating conjunction', \
        'JJ':'Adjective', \
        'JJR':'Adjective, comparative', \
        'JJS':'Adjective, superlative', \
        'LS':'List item marker', \
        'MD':'Modal', \
        'NN':'Noun, singular or mass', \
        'NNS':'Noun, plural', \
        'NNP':'Proper noun, singular', \
        'NNPS':'Proper noun, plural', \
        'PDT':'Predeterminer', \
        'POS':'Possessive ending', \
        'PRP':'Personal pronoun', \
        'PRP$':'Possessive pronoun', \
        'RB':'Adverb', \
        'RBR':'Adverb, comparative', \
        'RBS':'Adverb, superlative', \
        'RP':'Particle', \
        'SYM':'Symbol', \
        'TO':'to', \
        'UH':'Interjection',\
        'VB':'Verb, base form', \
        'VBD':'Verb, past tense', \
        'VBG':'Verb, gerund or present participle', \
        'VBN':'Verb, past participle', \
        'VBP':'Verb, non-3rd person singular present', \
        'VBZ':'Verb, 3rd person singular present', \
        'WDT':'Wh-determiner', \
        'WP':'Wh-pronoun', \
        'WP$':'Possessive wh-pronoun', \
        'WRB':'Wh-adverb'}
    return list(map(lambda x: x+', '+pos_dict.get(x,x),tags))


# def get_ngrams_and_tags(sentence, ngram_tags, n):
#     for i in range(len(sentence) - n + 1):
#         ngram = tuple(sentence[i:i+n])
#         if not (ngram in ngram_tags):
#             _, ngram_tags[ngram] = zip(*nltk.pos_tag(ngram))
#         yield ' '.join(ngram), ngram_tags[ngram]


def get_ngrams_and_tags(sentence, n):
    for i in range(len(sentence) - n + 1):
        ngram = tuple(sentence[i:i+n])
        _, tags = zip(*nltk.pos_tag(ngram))
        yield ' '.join(ngram), tags
