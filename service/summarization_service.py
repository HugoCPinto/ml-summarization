import nltk.data

nltk.data.path.append('C:/Users/hugop/work/projects/ml-summarization/models/nltk_data/')  # fix me
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from string import punctuation
from heapq import nlargest


def collect_data():
    text = """
        Stephen Edwin King was born in Portland, Maine in 1947, the second son of Donald and Nellie Ruth Pillsbury King. 
        After his parents separated when Stephen was a toddler, he and his older brother, David, were raised by his mother. 
        Parts of his childhood were spent in Fort Wayne, Indiana, where his father's family was at the time, and in Stratford, Connecticut. 
        When Stephen was eleven, his mother brought her children back to Durham, Maine, for good. 
        Her parents, Guy and Nellie Pillsbury, had become incapacitated with old age, and Ruth King was persuaded by her sisters 
        to take over the physical care of the elderly couple. Other family members provided a small house in Durham and financial support. 
        After Stephen's grandparents passed away, Mrs. King found work in the kitchens of Pineland, a nearby residential facility for the mentally challenged.
        """
    return text

def tokenize_data(data):
    print(data)

    tokens = word_tokenize(data)
    stop_words = stopwords.words('english')

    #print(tokens)
    #print(stop_words)

    word_frequencies = {}
    for word in tokens:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

    #print(word_frequencies)

    max_frequency = max(word_frequencies.values())
    #print(max_frequency)

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    #print(word_frequencies)

    sent_token = sent_tokenize(data)
    sentence_scores = {}
    for sent in sent_token:
        sentence = sent.split(" ")
        for word in sentence:
            if word.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.lower()]

    #print(sentence_scores)

    select_length = int(len(sent_token)*0.75)
    #print(select_length)

    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    final_summary = [word for word in summary]
    summary = ' '.join(final_summary)

    print(summary)