from mrjob.job import MRJob
from mrjob.step import MRStep
import re

word_re = re.compile(r"[\w']+")

class MRMostWordCount(MRJob):

    def mapper_words(self, _, line):
        for word in word_re.findall(line):
            yield word.upper(), 1

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_find_most_words(self, _, word_count_pairs):
        try:
            yield max(word_count_pairs)
        except ValueError:
            pass

def steps(self):
        return [
            MRStep(mapper=self.mapper_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words
                   ),
            MRStep(reducer = self.reducer_find_most_words)
        ]

if __name__ == '__main__':
    MRMostWordCount.run()