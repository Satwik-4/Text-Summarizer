import nltk
from heapq import nlargest

# Step 1: Tokenize the text into sentences
def read_article(text):
    article = text.split(". ")
    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    return sentences

# Step 2: Calculate word frequencies
def calculate_word_frequencies(article):
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(article.lower()):
        if word not in stopwords:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/max_frequency)
    return word_frequencies

# Step 4: Calculate sentence scores
def calculate_sentence_scores(sentences, word_frequencies):
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
    return sentence_scores

# Step 5: Set summary length and generate summary
def generate_summary(article, top_n=5):
    # Tokenize the article into sentences
    sentences = nltk.sent_tokenize(article)
    
    # Calculate word frequency scores
    word_frequencies = calculate_word_frequencies(article)
    
    # Calculate the score for each sentence
    sentence_scores = calculate_sentence_scores(sentences, word_frequencies)
    
    # Select the top n sentences with highest scores
    summary_sentences = nlargest(top_n, sentence_scores, key=sentence_scores.get)
    
    # Join the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    
    return summary

# Example usage
text = "Natural language processing (NLP) is a subfield of computer science, " \
       "information engineering, and artificial intelligence concerned with " \
       "the interactions between computers and human (natural) languages. " \
       "As such, NLP is related to the area of human–computer interaction. " \
       "Many challenges in NLP involve: natural language understanding, " \
       "that is, enabling computers to derive meaning from human or natural " \
       "language input; and others involve natural language generation. " \
       "The history of NLP generally starts in the 1950s, although work can " \
       "be found from earlier periods. In 1950, Alan Turing published an " \
       "article titled 'Computing Machinery and Intelligence' which proposed " \
       "what is now called the Turing test as a criterion of intelligence."

text_1 = "NFTs are currently taking the digital art and collectibles world by storm. Digital artists are seeing their lives change thanks to huge sales to a new crypto-audience. And celebrities are joining in as they spot a new opportunity to connect with fans. But digital art is only one way to use NFTs. Really they can be used to represent ownership of any unique asset, like a deed for an item in the digital or physical realm.If Andy Warhol had been born in the late 90s, he probably would have minted Campbell's Soup as an NFT. It's only a matter of time before Nike puts a run of Jordans on Ethereum. And one day owning your car might be proved with an NFT. NFTs are tokens that we can use to represent ownership of unique items. They let us tokenize things like art, collectibles, even real estate. Ownership of an asset is secured by the Ethereum blockchain, no one can modify the record of ownership or copy/paste a new NFT into existence. NFT stands for non-fungible token. Non-fungible is an economic term that you could use to describe things like your furniture, a song file, or your computer. These things are not interchangeable for other items because they have unique properties. Fungible items, on the other hand, can be exchanged because their value defines them rather than their unique properties. For example, ETH or dollars are fungible because 1 ETH / $1 USD is exchangeable for another 1 ETH / $1 USD."

summary = generate_summary(text_1, 5)
print(summary)


