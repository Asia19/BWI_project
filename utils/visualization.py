from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_counter(counter, n=30):
    top = counter.most_common(n)
    x, y = map(list,zip(*top))
    if not isinstance(x[0], str):
        x = list(map(repr, x))
    plt.figure(figsize=[15,15])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    sns.barplot(x=y,y=x)


# def plot_top_counter_train(top):
#     x, y = map(list,zip(*top))
#     if not isinstance(x[0], str):
#         x = list(map(repr, x))
#     plt.figure(figsize=[10,10])
#     plt.xticks(fontsize=13)
#     plt.yticks(fontsize=13)
#     sns.barplot(x=y,y=x)


def plot_top_counter_train(top, n=1):
    x, y = zip(*map(lambda x: (', '.join(x[:-1]),x[-1]), top))
    plt.figure(figsize=[10,10])
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    sns.barplot(x=list(y),y=list(x))


def plot_top_pos_instances(tagged_ngrams_counter, pos, m=30):
    instances_counter = Counter()
    for tagged_ngram, count in tagged_ngrams_counter.items():
        ngram, tags = tagged_ngram
        if tags == pos:
            instances_counter.update({ngram:count})
    top = instances_counter.most_common(m)
    x, y = zip(*top)
    x, y = list(x),list(y)
    plt.figure(figsize=[10,10])
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.title(f'top instances for tags {pos}',fontsize=13)
    sns.barplot(x=y,y=x)