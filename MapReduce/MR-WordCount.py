from mrjob.job import MRJob
import re

word_re = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in word_re.findall(line):
            yield word.upper(), 1

    def reducer(self, key, values):
        yield sum(values), key

if __name__ == '__main__':
    MRWordCount.run()
