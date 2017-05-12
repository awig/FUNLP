import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import brown, treebank

# Setup Training and Test Sentences
dataset = brown.tagged_sents(categories='science_fiction')
# untagged_dataset = brown.sents(categories='science_fiction')
# dataset = treebank.tagged_sents()
train_n = round(len(dataset)*0.7)
valid_n = train_n + round(len(dataset)*0.2)
train_set = dataset[:train_n]
valid_set = dataset[train_n+1:valid_n]
test_set = dataset[valid_n+1:]
# train_untagged = untagged_dataset[:train_n]

# should just make a list and have these in a for loop?

# Train Taggers
# Unigram Tagger (add a DefaultTagger 'NN' backoff?)
from nltk.tag import UnigramTagger
uni_tagger = UnigramTagger(train=train_set)

# Bigram Tagger
from nltk.tag import NgramTagger
bi_tagger = NgramTagger(2, train=train_set)

# Bi-Uni Backoff Tagger
biuni_tagger = NgramTagger(2, train=train_set, backoff=uni_tagger)

# Brill (tranformational) Tagger
from nltk.tag import BrillTaggerTrainer, DefaultTagger
from nltk.tbl.template import Template
from nltk.tag.brill import Pos, Word
templates = [Template(Pos([-1])), Template(Pos([-1]), Word([0]))]
# initial tagger to use? Default Tagger
brill_trainer = BrillTaggerTrainer(initial_tagger=uni_tagger,
                             templates=templates)
brill_tagger = brill_trainer.train(train_set, max_rules=100)

# Stanford Tagger
# from nltk.tag import StanfordPOSTagger
# leave for now need to install CoreNLP for it I think

# HunPos perceptron Tagger
# from nltk.tag import HunposTagger
# en_wsj_file = '/Users/ajwigington/projects/nltk_data/taggers/en_wsj.model'
# hunpos_tagger = HunposTagger()
# untrained

# HMM Supervised  Tagger
from nltk.tag import HiddenMarkovModelTrainer
hmmsup_tagger = HiddenMarkovModelTrainer().train_supervised(train_set)
# hmmunsup_trainer = HiddenMarkovModelTrainer().train_unsupervised([w for (w,t) in train_set])

# perceptron Tagger
from nltk.tag import PerceptronTagger
percep_tagger = PerceptronTagger(load=False)
percep_tagger.train(list(train_set))  # workaround the Lazy Subsequencer


# Test Taggers
print("Validation Accuracy")
print("-------------------")
print("Unigram Tagger: {}".format(uni_tagger.evaluate(valid_set)))
print("Bigram Tagger:  {}".format(bi_tagger.evaluate(valid_set)))
print("Bi-Uni Tagger:  {}".format(biuni_tagger.evaluate(valid_set)))
print("Brill Tagger:   {}".format(brill_tagger.evaluate(valid_set)))
print("HMM Tagger:     {}".format(hmmsup_tagger.evaluate(valid_set)))
print("Percep Tagger:  {}".format(percep_tagger.evaluate(valid_set)))
print("\n\n")


# now try my input

SENTENCE = "Flies love the smell."

# Tokenize my sentence using the treebankword tokenizer
tokenizer = TreebankWordTokenizer()
sent_tokens = tokenizer.tokenize(SENTENCE)

print("Tag My Sentence: \'{}\'".format(SENTENCE))
print("----------------------------------------------------------------")
print("Unigram Tagger: {}".format(uni_tagger.tag(sent_tokens)))
print("Bigram Tagger:  {}".format(bi_tagger.tag(sent_tokens)))
print("Bi-Uni Tagger:  {}".format(biuni_tagger.tag(sent_tokens)))
print("Brill Tagger:   {}".format(brill_tagger.tag(sent_tokens)))
print("HMM Tagger:     {}".format(hmmsup_tagger.tag(sent_tokens)))
print("Percep Tagger:  {}".format(percep_tagger.tag(sent_tokens)))
