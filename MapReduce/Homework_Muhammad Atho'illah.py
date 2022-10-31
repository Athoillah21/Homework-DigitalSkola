from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRMostUsedWord(MRJob):

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            self.increment_counter('First Job', '1. Words', 1)
            yield (word.upper(), 1)

    def combiner_count_words(self, word, counts):
        self.increment_counter('First Job', '2. Word Counts in Combiners', 1)
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        self.increment_counter('First Job', '3. Word Counts', 1)
        yield None, (sum(counts), word)

    def reducer_find_max_word(self, _, word_count_pairs):
        self.increment_counter('Second Job', '1. Max Word', 1)
        yield max(word_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]


if __name__ == '__main__':
    MRMostUsedWord.run()