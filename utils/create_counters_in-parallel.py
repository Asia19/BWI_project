import nltk
import multiprocessing
import pickle
import io
import os
import sys
sys.path.append('..')
from utils.another import get_ngrams
from collections import Counter
from multiprocessing import Process
import time
from nltk.tag.perceptron import PerceptronTagger
nltk.download('averaged_perceptron_tagger')

n = 3
n_processes = 4
ngram_names = {1: 'unigrams', 2: 'bigrams', 3: 'trigrams'}
csv_headers = {1: 'gram,tag,tagged_gram_count\n', \
               2: 'first_gram,second_gram,first_tag,second_tag,tagged_bigram_count\n', \
               3: 'first_gram,second_gram,third_gram,first_tag,second_tag,third_tag,tagged_trigram_count\n'}

def pos_tagger(infile, outfile):
    start = time.time()
    tagged_ngrams_counter = Counter()
    tagger = PerceptronTagger()
    with io.open(infile, encoding='utf-8', mode='rt') as text_file:
        for i, line in enumerate(text_file):
            if i % 100000 == 0:
                print(f'{os.getpid()} process, {i} lines, {time.time()-start:.1f} time')
            if n==1:
                tagged_ngrams = tagger.tag(line.rstrip().split(' '))
            else:
                tagged_ngrams = [tuple(tagger.tag(ngram)) for ngram in get_ngrams(line.rstrip().split(' '), n)]
            tagged_ngrams_counter.update(tagged_ngrams)
        with open(outfile, mode='wb') as counter_pickle, \
            open(outfile[:-6]+'csv', 'w', encoding='utf-8') as counter_csv:
            pickle.dump(tagged_ngrams_counter, counter_pickle)
            counter_csv.write(csv_headers[n])
            if n==1:
                for tagged_ngram, count in tagged_ngrams_counter.items():
                    counter_csv.write('{} {} {}\n'.format(*tagged_ngram, count))
            else:
                for tagged_ngram, count in tagged_ngrams_counter.items():
                    ngram, tags = zip(*tagged_ngram)
                    counter_csv.write('{} {} {}\n'.format(' '.join(ngram), ' '.join(tags), count))


if __name__ == '__main__':

    # n_processes = int(os.environ["NUMBER_OF_PROCESSORS"])
    args = []
    file_names = []

    for i in range(n_processes):
        file_names.append(f'../delete/train_tagged_{ngram_names[n]}_counter-{i+1}.pickle')
        args.append((f'../delete/train_v2-preprocessed-{i+1}.txt', file_names[i]))


    processes = []
    for rank in range(n_processes):
        p = Process(target=pos_tagger, args=args[rank])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


    tagged_ngrams_counter = Counter()
    with open(f'../delete/train_tagged_{ngram_names[n]}_counter.pickle', mode='wb') as file, \
        open(f'../delete/train_tagged_{ngram_names[n]}_counter.csv', 'w', encoding='utf-8') as file_csv:
        for file_name in file_names:
            f = open(file_name, mode='rb')
            try:
                tagged_ngrams_counter.update(pickle.load(f))
            finally:
                f.close()
        pickle.dump(tagged_ngrams_counter, file)
        # csv
        file_csv.write(csv_headers[n])
        if n == 1:
            for tagged_ngram, count in tagged_ngrams_counter.items():
                file_csv.write('{} {} {}\n'.format(*tagged_ngram, count))
        else:
            for tagged_ngram, count in tagged_ngrams_counter.items():
                ngram, tags = zip(*tagged_ngram)
                file_csv.write('{} {} {}\n'.format(' '.join(ngram), ' '.join(tags), count))


    # print('lets check')
    # check_counter = Counter()
    # tagger = PerceptronTagger()
    # with io.open(f'../delete/train_v2-preprocessed.txt', encoding='utf-8', mode='rt') as text_file:
    #     for line in text_file:
    #         if n == 1:
    #             tagged_ngrams = tagger.tag(line.rstrip().split(' '))
    #         else:
    #             tagged_ngrams = [tuple(tagger.tag(ngram)) for ngram in get_ngrams(line.rstrip().split(' '), n)]
    #         check_counter.update(tagged_ngrams)
    #
    # for tagged_ngram, count in check_counter.items():
    #     if tagged_ngrams_counter[tagged_ngram]!=count:
    #         print('ooops!')
