#encoding=utf-8

#http://joshbohde.com/blog/document-summarization

import networkx as nx
import numpy as np

from collections import Counter
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


document = """To Sherlock Holmes she is always the woman. I have
seldom heard him mention her under any other name. In his eyes she
eclipses and predominates the whole of her sex. It was not that he
felt any emotion akin to love for Irene Adler. All emotions, and that
one particularly, were abhorrent to his cold, precise but admirably
balanced mind. He was, I take it, the most perfect reasoning and
observing machine that the world has seen, but as a lover he would
have placed himself in a false position. He never spoke of the softer
passions, save with a gibe and a sneer. They were admirable things for
the observer-excellent for drawing the veil from men’s motives and
actions. But for the trained reasoner to admit such intrusions into
his own delicate and finely adjusted temperament was to introduce a
distracting factor which might throw a doubt upon all his mental
results. Grit in a sensitive instrument, or a crack in one of his own
high-power lenses, would not be more disturbing than a strong emotion
in a nature such as his. And yet there was but one woman to him, and
that woman was the late Irene Adler, of dubious and questionable
memory.
"""

document = ' '.join(document.strip().split('\n'))

def bag_of_words(sentence):
	return Counter(word.lower().strip('.,') for word in sentence.split(' '))

def textrank(document):
	sentence_tokenizer = PunktSentenceTokenizer()
	sentences = sentence_tokenizer.tokenize(document)

	c = CountVectorizer()
	#bow_array = c.fit_transform([sentences[0]])
	#bow_array.toarray()
	bow_matrix = c.fit_transform(sentences)

	normalized_matrix = TfidfTransformer().fit_transform(bow_matrix)

	similarity_graph = normalized_matrix * normalized_matrix.T
	similarity_graph.toarray()

	nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
	scores = nx.pagerank(nx_graph)

	return sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

print textrank(document)
