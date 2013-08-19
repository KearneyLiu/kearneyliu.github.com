Title: Some papers I read about Opinion Mining and Sentiment Analysis and my notes
Date: 2013-08-19
Category: Research
Tags: Sentiment Analysis, Twitter, Paper 

My research interest is **Opinion Mining and Sentiment Analysis**. These days I read a lot of papers. Here are some of them. Share with you.

###Sentiment Analysis of Twitter Data###
*Apoorv Agarwal, ACL 2011*

####Main Approaches
- POS-specific prior polarity feature
- tree kernel to obviate the need for tedious feature engineering 

####Notes
In all, the author just care more about the polarity of English word(non-stop) and its POS features. Besides, he proposes two models compared with baseline(unigram), and proves his methods are greater than the baseline. However, I think there may be some improvements, for instance, to use Standford NLP implement and achieve more info about the tree.


********

###Merging SenticNet and WordNet-Affect Emotion Lists for Sentiment Analysis###
*Soujanya Porial, ICSP2012*
####Main motivation
- adding new useful information to SenticNet entries
- Expanding WordNet-Affect emotion lists with the SenticNet concepts

####Main approach
- For classification, the author used two kinds of features of the concepts 
- ISEAR data-based features
- Features based on similarity measures

####Notes
This paper tells us how to expand a exiting sentiment lexicon to involve more words. The method he uses is excellent, and enlightens me how to expand the SenticNet lexicon.


********

###Semantic Sentiment Analysis of Twitter
*Hassan Saif, Iswc2012*

####Main Approach
Introduce and implement a new set of semantic features for training a model for sentiment analysis of tweets.

a new type of features for sentiment analysis, called semantic features, where for each entity in a tweet (e.g. iPhone, iPad, MacBook), the abstract concept that represents it will be added as a new feature (e.g. Apple product)

####Notes
In this paper, the author extracts each entity in a tweet, and make up the concept. But I think it may be too sparse, if some tweets does not involve these words, the results could not be good. 



