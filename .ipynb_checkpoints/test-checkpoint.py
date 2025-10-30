import math
from collections import Counter, defaultdict

class TFIDFVectorizer:
    def __init__(self, v_max=None, lowercase=True):
        """
        Initializes the TF-IDF Vectorizer.

        Args:
            v_max (int, optional): Maximum size of the vocabulary. Keeps the most frequent v_max terms.
            lowercase (bool): Whether to lowercase documents before tokenization.
        """
        self.v_max = v_max
        self.lowercase = lowercase
        self.vocabulary = []
        self.idf = {}
        self.word_to_index = {}

    def _tokenize(self, document):
        """Splits a document into tokens."""
        if self.lowercase:
            document = document.lower()
        return document.split()

    def fit(self, corpus):
        """
        Learns the vocabulary and computes IDF values.

        Args:
            corpus (list of str): The collection of documents to fit on.
        """
        # Tokenize all documents
        tokenized_docs = [self._tokenize(doc) for doc in corpus]
        
        # Count word frequencies across entire corpus
        term_freq = Counter(word for doc in tokenized_docs for word in doc)

        # If vocabulary limit is set, keep top v_max most frequent terms
        if self.v_max:
            most_common = term_freq.most_common(self.v_max)
            self.vocabulary = [term for term, _ in most_common]
        else:
            self.vocabulary = sorted(term_freq.keys())

        # Create word-to-index mapping
        self.word_to_index = {word: i for i, word in enumerate(self.vocabulary)}

        # Compute document frequency for each term
        doc_freq = defaultdict(int)
        for word in self.vocabulary:
            for doc in tokenized_docs:
                if word in doc:
                    doc_freq[word] += 1

        # Compute IDF for each term
        N = len(corpus)
        for word in self.vocabulary:
            self.idf[word] = math.log(N / (1 + doc_freq[word])) + 1  # +1 smoothing

    def transform(self, corpus):
        """
        Transforms a list of documents into TF-IDF vectors.

        Args:
            corpus (list of str): Collection of documents to transform.

        Returns:
            list of lists: TF-IDF matrix representation of the corpus.
        """
        vectors = []
        for doc in corpus:
            tokens = self._tokenize(doc)
            tf_counts = Counter(tokens)
            doc_vector = [0.0] * len(self.vocabulary)
            for word, count in tf_counts.items():
                if word in self.word_to_index:
                    idx = self.word_to_index[word]
                    tf = count  # raw term frequency
                    idf = self.idf[word]
                    doc_vector[idx] = tf * idf
            vectors.append(doc_vector)
        return vectors

    def fit_transform(self, corpus):
      """
      Fits the model and transforms the corpus in one step.

      Args:
        corpus (list of str): Collection of documents to fit and transform.

      Returns:
        list of lists: TF-IDF matrix representation of the corpus.
      """
      self.fit(corpus)
      
      return self.transform(corpus)

corpus = [
    'The hotel and the stay were great',
    'This was a great stay',
    'Great stay in a great destination',
    'Great destination'
]

vectorizer = TFIDFVectorizer(lowercase=False)
tfidf_matrix = vectorizer.fit_transform(corpus)

print("Vocabulary:", vectorizer.vocabulary)
for row in tfidf_matrix:
    print(row)