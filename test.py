from monkeylearn import MonkeyLearn
#
ml = MonkeyLearn('e9ccec8c0876f52ab36e13687017a3c40a010b50')
data = ["The movie was ok","The movie was bad"]

model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)
tweets_with_sentimet = {}
for result in result.body:
    tweet = result["text"]
    sentiment = result["classifications"][0]["tag_name"]
    confidence = result["classifications"][0]["confidence"]
    tweets_with_sentimet[tweet] = [sentiment,confidence]
print(tweets_with_sentimet)
# //////////////////////////
# #
# # {
# #  "cells": [
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "### IMPORTING PACKAGES"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 1,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stderr",
# #      "output_type": "stream",
# #      "text": [
# #       "[nltk_data] Downloading package punkt to /Users/ranivija/nltk_data...\n",
# #       "[nltk_data]   Package punkt is already up-to-date!\n",
# #       "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
# #       "[nltk_data]     /Users/ranivija/nltk_data...\n",
# #       "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
# #       "[nltk_data]       date!\n",
# #       "[nltk_data] Downloading package wordnet to\n",
# #       "[nltk_data]     /Users/ranivija/nltk_data...\n",
# #       "[nltk_data]   Package wordnet is already up-to-date!\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "import pandas as pd\n",
# #     "import numpy as np\n",
# #     "\n",
# #     "import seaborn as sns\n",
# #     "import matplotlib.pyplot as plt\n",
# #     "\n",
# #     "#for text pre-processing\n",
# #     "import re, string\n",
# #     "import nltk\n",
# #     "from nltk.tokenize import word_tokenize\n",
# #     "from nltk.corpus import stopwords\n",
# #     "from nltk.tokenize import word_tokenize\n",
# #     "from nltk.stem import SnowballStemmer\n",
# #     "from nltk.corpus import wordnet\n",
# #     "from nltk.stem import WordNetLemmatizer\n",
# #     "\n",
# #     "nltk.download('punkt')\n",
# #     "nltk.download('averaged_perceptron_tagger')\n",
# #     "nltk.download('wordnet')\n",
# #     "\n",
# #     "#for model-building\n",
# #     "from sklearn.model_selection import train_test_split\n",
# #     "from sklearn.linear_model import LogisticRegression\n",
# #     "from sklearn.linear_model import SGDClassifier\n",
# #     "from sklearn.naive_bayes import MultinomialNB\n",
# #     "from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix\n",
# #     "from sklearn.metrics import roc_curve, auc, roc_auc_score\n",
# #     "\n",
# #     "# bag of words\n",
# #     "from sklearn.feature_extraction.text import TfidfVectorizer\n",
# #     "from sklearn.feature_extraction.text import CountVectorizer\n",
# #     "\n",
# #     "#for word embedding\n",
# #     "import gensim\n",
# #     "from gensim.models import Word2Vec #Word2Vec is mostly used for huge datasets"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "## Loading Data"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 2,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "(7613, 5)\n"
# #      ]
# #     },
# #     {
# #      "data": {
# #       "text/html": [
# #        "<div>\n",
# #        "<style scoped>\n",
# #        "    .dataframe tbody tr th:only-of-type {\n",
# #        "        vertical-align: middle;\n",
# #        "    }\n",
# #        "\n",
# #        "    .dataframe tbody tr th {\n",
# #        "        vertical-align: top;\n",
# #        "    }\n",
# #        "\n",
# #        "    .dataframe thead th {\n",
# #        "        text-align: right;\n",
# #        "    }\n",
# #        "</style>\n",
# #        "<table border=\"1\" class=\"dataframe\">\n",
# #        "  <thead>\n",
# #        "    <tr style=\"text-align: right;\">\n",
# #        "      <th></th>\n",
# #        "      <th>id</th>\n",
# #        "      <th>keyword</th>\n",
# #        "      <th>location</th>\n",
# #        "      <th>text</th>\n",
# #        "      <th>target</th>\n",
# #        "    </tr>\n",
# #        "  </thead>\n",
# #        "  <tbody>\n",
# #        "    <tr>\n",
# #        "      <th>0</th>\n",
# #        "      <td>1</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Our Deeds are the Reason of this #earthquake M...</td>\n",
# #        "      <td>1</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>1</th>\n",
# #        "      <td>4</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Forest fire near La Ronge Sask. Canada</td>\n",
# #        "      <td>1</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>2</th>\n",
# #        "      <td>5</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>All residents asked to 'shelter in place' are ...</td>\n",
# #        "      <td>1</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>3</th>\n",
# #        "      <td>6</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>13,000 people receive #wildfires evacuation or...</td>\n",
# #        "      <td>1</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>4</th>\n",
# #        "      <td>7</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Just got sent this photo from Ruby #Alaska as ...</td>\n",
# #        "      <td>1</td>\n",
# #        "    </tr>\n",
# #        "  </tbody>\n",
# #        "</table>\n",
# #        "</div>"
# #       ],
# #       "text/plain": [
# #        "   id keyword location                                               text  \\\n",
# #        "0   1     NaN      NaN  Our Deeds are the Reason of this #earthquake M...   \n",
# #        "1   4     NaN      NaN             Forest fire near La Ronge Sask. Canada   \n",
# #        "2   5     NaN      NaN  All residents asked to 'shelter in place' are ...   \n",
# #        "3   6     NaN      NaN  13,000 people receive #wildfires evacuation or...   \n",
# #        "4   7     NaN      NaN  Just got sent this photo from Ruby #Alaska as ...   \n",
# #        "\n",
# #        "   target  \n",
# #        "0       1  \n",
# #        "1       1  \n",
# #        "2       1  \n",
# #        "3       1  \n",
# #        "4       1  "
# #       ]
# #      },
# #      "execution_count": 2,
# #      "metadata": {},
# #      "output_type": "execute_result"
# #     }
# #    ],
# #    "source": [
# #     "#you can download the data from https://www.kaggle.com/c/nlp-getting-started/data\n",
# #     "import os\n",
# #     "os.chdir('/Users/ranivija/Desktop/')\n",
# #     "df_train=pd.read_csv('train.csv')\n",
# #     "print(df_train.shape)\n",
# #     "df_train.head()"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "## EDA"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 3,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "0    4342\n",
# #       "1    3271\n",
# #       "Name: target, dtype: int64\n"
# #      ]
# #     },
# #     {
# #      "data": {
# #       "text/plain": [
# #        "<AxesSubplot:ylabel='target'>"
# #       ]
# #      },
# #      "execution_count": 3,
# #      "metadata": {},
# #      "output_type": "execute_result"
# #     },
# #     {
# #      "data": {
# #       "image/png": "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\n",
# #       "text/plain": [
# #        "<Figure size 432x288 with 1 Axes>"
# #       ]
# #      },
# #      "metadata": {
# #       "needs_background": "light"
# #      },
# #      "output_type": "display_data"
# #     }
# #    ],
# #    "source": [
# #     "# CLASS DISTRIBUTION\n",
# #     "#if dataset is balanced or not\n",
# #     "x=df_train['target'].value_counts()\n",
# #     "print(x)\n",
# #     "sns.barplot(x.index,x)"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 4,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "data": {
# #       "text/plain": [
# #        "id             0\n",
# #        "keyword       61\n",
# #        "location    2533\n",
# #        "text           0\n",
# #        "target         0\n",
# #        "dtype: int64"
# #       ]
# #      },
# #      "execution_count": 4,
# #      "metadata": {},
# #      "output_type": "execute_result"
# #     }
# #    ],
# #    "source": [
# #     "#Missing values\n",
# #     "df_train.isna().sum()"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 5,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "15.167532864567411\n",
# #       "14.704744357438969\n",
# #       "108.11342097217977\n",
# #       "95.70681713496084\n",
# #       "14.664934270865178\n",
# #       "14.09649930907416\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#1. WORD-COUNT\n",
# #     "df_train['word_count'] = df_train['text'].apply(lambda x: len(str(x).split()))\n",
# #     "print(df_train[df_train['target']==1]['word_count'].mean()) #Disaster tweets\n",
# #     "print(df_train[df_train['target']==0]['word_count'].mean()) #Non-Disaster tweets\n",
# #     "#Disaster tweets are more wordy than the non-disaster tweets\n",
# #     "\n",
# #     "#2. CHARACTER-COUNT\n",
# #     "df_train['char_count'] = df_train['text'].apply(lambda x: len(str(x)))\n",
# #     "print(df_train[df_train['target']==1]['char_count'].mean()) #Disaster tweets\n",
# #     "print(df_train[df_train['target']==0]['char_count'].mean()) #Non-Disaster tweets\n",
# #     "#Disaster tweets are longer than the non-disaster tweets\n",
# #     "\n",
# #     "#3. UNIQUE WORD-COUNT\n",
# #     "df_train['unique_word_count'] = df_train['text'].apply(lambda x: len(set(str(x).split())))\n",
# #     "print(df_train[df_train['target']==1]['unique_word_count'].mean()) #Disaster tweets\n",
# #     "print(df_train[df_train['target']==0]['unique_word_count'].mean()) #Non-Disaster tweets"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 6,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "data": {
# #       "image/png": "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\n",
# #       "text/plain": [
# #        "<Figure size 720x288 with 2 Axes>"
# #       ]
# #      },
# #      "metadata": {
# #       "needs_background": "light"
# #      },
# #      "output_type": "display_data"
# #     }
# #    ],
# #    "source": [
# #     "#Plotting word-count per tweet\n",
# #     "fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,4))\n",
# #     "train_words=df_train[df_train['target']==1]['word_count']\n",
# #     "ax1.hist(train_words,color='red')\n",
# #     "ax1.set_title('Disaster tweets')\n",
# #     "train_words=df_train[df_train['target']==0]['word_count']\n",
# #     "ax2.hist(train_words,color='green')\n",
# #     "ax2.set_title('Non-disaster tweets')\n",
# #     "fig.suptitle('Words per tweet')\n",
# #     "plt.show()"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "## PRE-PROCESSING"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 7,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "this is a message to be cleaned it may involve some things like adjacent spaces and tabs\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#1. Common text preprocessing\n",
# #     "text = \"   This is a message to be cleaned. It may involve some things like: <br>, ?, :, ''  adjacent spaces and tabs     .  \"\n",
# #     "\n",
# #     "#convert to lowercase and remove punctuations and characters and then strip\n",
# #     "def preprocess(text):\n",
# #     "    text = text.lower() #lowercase text\n",
# #     "    text=text.strip()  #get rid of leading/trailing whitespace \n",
# #     "    text=re.compile('<.*?>').sub('', text) #Remove HTML tags/markups\n",
# #     "    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  #Replace punctuation with space. Careful since punctuation can sometime be useful\n",
# #     "    text = re.sub('\\s+', ' ', text)  #Remove extra space and tabs\n",
# #     "    text = re.sub(r'\\[[0-9]*\\]',' ',text) #[0-9] matches any digit (0 to 10000...)\n",
# #     "    text=re.sub(r'[^\\w\\s]', '', str(text).lower().strip())\n",
# #     "    text = re.sub(r'\\d',' ',text) #matches any digit from 0 to 100000..., \\D matches non-digits\n",
# #     "    text = re.sub(r'\\s+',' ',text) #\\s matches any whitespace, \\s+ matches multiple whitespace, \\S matches non-whitespace \n",
# #     "    \n",
# #     "    return text\n",
# #     "\n",
# #     "text=preprocess(text)\n",
# #     "print(text)  #text is a string"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 8,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "message cleaned may involve things like adjacent spaces tabs\n",
# #       "messag clean may involv thing like adjac space tab\n",
# #       "messag clean may involv thing like adjac space tab\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#3. LEXICON-BASED TEXT PROCESSING EXAMPLES\n",
# #     " \n",
# #     "#1. STOPWORD REMOVAL\n",
# #     "def stopword(string):\n",
# #     "    a= [i for i in string.split() if i not in stopwords.words('english')]\n",
# #     "    return ' '.join(a)\n",
# #     "\n",
# #     "text=stopword(text)\n",
# #     "print(text)\n",
# #     "\n",
# #     "#2. STEMMING\n",
# #     " \n",
# #     "# Initialize the stemmer\n",
# #     "snow = SnowballStemmer('english')\n",
# #     "def stemming(string):\n",
# #     "    a=[snow.stem(i) for i in word_tokenize(string) ]\n",
# #     "    return \" \".join(a)\n",
# #     "text=stemming(text)\n",
# #     "print(text)\n",
# #     "\n",
# #     "#3. LEMMATIZATION\n",
# #     "# Initialize the lemmatizer\n",
# #     "wl = WordNetLemmatizer()\n",
# #     " \n",
# #     "# This is a helper function to map NTLK position tags\n",
# #     "# Full list is available here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html\n",
# #     "def get_wordnet_pos(tag):\n",
# #     "    if tag.startswith('J'):\n",
# #     "        return wordnet.ADJ\n",
# #     "    elif tag.startswith('V'):\n",
# #     "        return wordnet.VERB\n",
# #     "    elif tag.startswith('N'):\n",
# #     "        return wordnet.NOUN\n",
# #     "    elif tag.startswith('R'):\n",
# #     "        return wordnet.ADV\n",
# #     "    else:\n",
# #     "        return wordnet.NOUN\n",
# #     "\n",
# #     "# Tokenize the sentence\n",
# #     "def lemmatizer(string):\n",
# #     "    word_pos_tags = nltk.pos_tag(word_tokenize(string)) # Get position tags\n",
# #     "    a=[wl.lemmatize(tag[0], get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)] # Map the position tag and lemmatize the word/token\n",
# #     "    return \" \".join(a)\n",
# #     "\n",
# #     "text = lemmatizer(text)\n",
# #     "print(text)"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 9,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "data": {
# #       "text/html": [
# #        "<div>\n",
# #        "<style scoped>\n",
# #        "    .dataframe tbody tr th:only-of-type {\n",
# #        "        vertical-align: middle;\n",
# #        "    }\n",
# #        "\n",
# #        "    .dataframe tbody tr th {\n",
# #        "        vertical-align: top;\n",
# #        "    }\n",
# #        "\n",
# #        "    .dataframe thead th {\n",
# #        "        text-align: right;\n",
# #        "    }\n",
# #        "</style>\n",
# #        "<table border=\"1\" class=\"dataframe\">\n",
# #        "  <thead>\n",
# #        "    <tr style=\"text-align: right;\">\n",
# #        "      <th></th>\n",
# #        "      <th>id</th>\n",
# #        "      <th>keyword</th>\n",
# #        "      <th>location</th>\n",
# #        "      <th>text</th>\n",
# #        "      <th>target</th>\n",
# #        "      <th>clean_text</th>\n",
# #        "    </tr>\n",
# #        "  </thead>\n",
# #        "  <tbody>\n",
# #        "    <tr>\n",
# #        "      <th>0</th>\n",
# #        "      <td>1</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Our Deeds are the Reason of this #earthquake M...</td>\n",
# #        "      <td>1</td>\n",
# #        "      <td>deed reason earthquake may allah forgive u</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>1</th>\n",
# #        "      <td>4</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Forest fire near La Ronge Sask. Canada</td>\n",
# #        "      <td>1</td>\n",
# #        "      <td>forest fire near la ronge sask canada</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>2</th>\n",
# #        "      <td>5</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>All residents asked to 'shelter in place' are ...</td>\n",
# #        "      <td>1</td>\n",
# #        "      <td>resident ask shelter place notify officer evac...</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>3</th>\n",
# #        "      <td>6</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>13,000 people receive #wildfires evacuation or...</td>\n",
# #        "      <td>1</td>\n",
# #        "      <td>people receive wildfire evacuation order calif...</td>\n",
# #        "    </tr>\n",
# #        "    <tr>\n",
# #        "      <th>4</th>\n",
# #        "      <td>7</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>NaN</td>\n",
# #        "      <td>Just got sent this photo from Ruby #Alaska as ...</td>\n",
# #        "      <td>1</td>\n",
# #        "      <td>get sent photo ruby alaska smoke wildfires pou...</td>\n",
# #        "    </tr>\n",
# #        "  </tbody>\n",
# #        "</table>\n",
# #        "</div>"
# #       ],
# #       "text/plain": [
# #        "   id keyword location                                               text  \\\n",
# #        "0   1     NaN      NaN  Our Deeds are the Reason of this #earthquake M...   \n",
# #        "1   4     NaN      NaN             Forest fire near La Ronge Sask. Canada   \n",
# #        "2   5     NaN      NaN  All residents asked to 'shelter in place' are ...   \n",
# #        "3   6     NaN      NaN  13,000 people receive #wildfires evacuation or...   \n",
# #        "4   7     NaN      NaN  Just got sent this photo from Ruby #Alaska as ...   \n",
# #        "\n",
# #        "   target                                         clean_text  \n",
# #        "0       1         deed reason earthquake may allah forgive u  \n",
# #        "1       1              forest fire near la ronge sask canada  \n",
# #        "2       1  resident ask shelter place notify officer evac...  \n",
# #        "3       1  people receive wildfire evacuation order calif...  \n",
# #        "4       1  get sent photo ruby alaska smoke wildfires pou...  "
# #       ]
# #      },
# #      "execution_count": 9,
# #      "metadata": {},
# #      "output_type": "execute_result"
# #     }
# #    ],
# #    "source": [
# #     "#FINAL PREPROCESSING\n",
# #     "def finalpreprocess(string):\n",
# #     "    return lemmatizer(stopword(preprocess(string)))\n",
# #     "\n",
# #     "df_train['clean_text'] = df_train['text'].apply(lambda x: finalpreprocess(x))\n",
# #     "df_train=df_train.drop(columns=['word_count','char_count','unique_word_count'])\n",
# #     "df_train.head()"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "### Word2Vec model"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 10,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stderr",
# #      "output_type": "stream",
# #      "text": [
# #       "/Users/ranivija/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:9: DeprecationWarning: Call to deprecated `syn0` (Attribute will be removed in 4.0.0, use self.vectors instead).\n",
# #       "  if __name__ == '__main__':\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "# create Word2vec model\n",
# #     "#here words_f should be a list containing words from each document. say 1st row of the list is words from the 1st document/sentence\n",
# #     "#length of words_f is number of documents/sentences in your dataset\n",
# #     "df_train['clean_text_tok']=[nltk.word_tokenize(i) for i in df_train['clean_text']] #convert preprocessed sentence to tokenized sentence\n",
# #     "model = Word2Vec(df_train['clean_text_tok'],min_count=1)  #min_count=1 means word should be present at least across all documents,\n",
# #     "#if min_count=2 means if the word is present less than 2 times across all the documents then we shouldn't consider it\n",
# #     "\n",
# #     "\n",
# #     "w2v = dict(zip(model.wv.index2word, model.wv.syn0))  #combination of word and its vector\n",
# #     "\n",
# #     "#for converting sentence to vectors/numbers from word vectors result by Word2Vec\n",
# #     "class MeanEmbeddingVectorizer(object):\n",
# #     "    def __init__(self, word2vec):\n",
# #     "        self.word2vec = word2vec\n",
# #     "        # if a text is empty we should return a vector of zeros\n",
# #     "        # with the same dimensionality as all the other vectors\n",
# #     "        self.dim = len(next(iter(word2vec.values())))\n",
# #     "\n",
# #     "    def fit(self, X, y):\n",
# #     "        return self\n",
# #     "\n",
# #     "    def transform(self, X):\n",
# #     "        return np.array([\n",
# #     "            np.mean([self.word2vec[w] for w in words if w in self.word2vec]\n",
# #     "                    or [np.zeros(self.dim)], axis=0)\n",
# #     "            for words in X\n",
# #     "        ])\n"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "### TRAIN TEST SPLITTING OF LABELLED DATASET"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 11,
# #    "metadata": {},
# #    "outputs": [],
# #    "source": [
# #     "#SPLITTING THE TRAINING DATASET INTO TRAINING AND VALIDATION\n",
# #     " \n",
# #     "# Input: \"reviewText\", \"rating\" and \"time\"\n",
# #     "# Target: \"log_votes\"\n",
# #     "X_train, X_val, y_train, y_val = train_test_split(df_train[\"clean_text\"],\n",
# #     "                                                  df_train[\"target\"],\n",
# #     "                                                  test_size=0.2,\n",
# #     "                                                  shuffle=True)\n",
# #     "X_train_tok= [nltk.word_tokenize(i) for i in X_train]  #for word2vec\n",
# #     "X_val_tok= [nltk.word_tokenize(i) for i in X_val]      #for word2vec\n",
# #     "\n",
# #     "#TF-IDF\n",
# #     "# Convert x_train to vector since model can only run on numbers and not words- Fit and transform\n",
# #     "tfidf_vectorizer = TfidfVectorizer(use_idf=True)\n",
# #     "X_train_vectors_tfidf = tfidf_vectorizer.fit_transform(X_train) #tfidf runs on non-tokenized sentences unlike word2vec\n",
# #     "# Only transform x_test (not fit and transform)\n",
# #     "X_val_vectors_tfidf = tfidf_vectorizer.transform(X_val) #Don't fit() your TfidfVectorizer to your test data: it will \n",
# #     "#change the word-indexes & weights to match test data. Rather, fit on the training data, then use the same train-data-\n",
# #     "#fit model on the test data, to reflect the fact you're analyzing the test data only based on what was learned without \n",
# #     "#it, and the have compatible\n",
# #     "\n",
# #     "\n",
# #     "#Word2vec\n",
# #     "# Fit and transform\n",
# #     "modelw = MeanEmbeddingVectorizer(w2v)\n",
# #     "X_train_vectors_w2v = modelw.transform(X_train_tok)\n",
# #     "X_val_vectors_w2v = modelw.transform(X_val_tok)"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "### Building ML models (Text-classification)"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "#### LR (tf-idf)"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 12,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "              precision    recall  f1-score   support\n",
# #       "\n",
# #       "           0       0.82      0.84      0.83       857\n",
# #       "           1       0.79      0.76      0.77       666\n",
# #       "\n",
# #       "    accuracy                           0.81      1523\n",
# #       "   macro avg       0.80      0.80      0.80      1523\n",
# #       "weighted avg       0.81      0.81      0.81      1523\n",
# #       "\n",
# #       "Confusion Matrix: [[723 134]\n",
# #       " [160 506]]\n",
# #       "AUC: 0.8646537435919\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#FITTING THE CLASSIFICATION MODEL using Logistic Regression(tf-idf)\n",
# #     "\n",
# #     "lr_tfidf=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')\n",
# #     "lr_tfidf.fit(X_train_vectors_tfidf, y_train)  #model\n",
# #     "\n",
# #     "#Predict y value for test dataset\n",
# #     "y_predict = lr_tfidf.predict(X_val_vectors_tfidf)\n",
# #     "y_prob = lr_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]\n",
# #     " \n",
# #     "\n",
# #     "print(classification_report(y_val,y_predict))\n",
# #     "print('Confusion Matrix:',confusion_matrix(y_val, y_predict))\n",
# #     " \n",
# #     "fpr, tpr, thresholds = roc_curve(y_val, y_prob)\n",
# #     "roc_auc = auc(fpr, tpr)\n",
# #     "print('AUC:', roc_auc)  "
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "#### NB (tf-idf)"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 14,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "              precision    recall  f1-score   support\n",
# #       "\n",
# #       "           0       0.78      0.90      0.83       871\n",
# #       "           1       0.82      0.66      0.73       652\n",
# #       "\n",
# #       "    accuracy                           0.79      1523\n",
# #       "   macro avg       0.80      0.78      0.78      1523\n",
# #       "weighted avg       0.80      0.79      0.79      1523\n",
# #       "\n",
# #       "Confusion Matrix: [[780  91]\n",
# #       " [224 428]]\n",
# #       "AUC: 0.8445135694815211\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#FITTING THE CLASSIFICATION MODEL using Naive Bayes(tf-idf)\n",
# #     "#It's a probabilistic classifier that makes use of Bayes' Theorem, a rule that uses probability to make predictions based on prior knowledge of conditions that might be related. This algorithm is the most suitable for such large dataset as it considers each feature independently, calculates the probability of each category, and then predicts the category with the highest probability.\n",
# #     "\n",
# #     "nb_tfidf = MultinomialNB()\n",
# #     "nb_tfidf.fit(X_train_vectors_tfidf, y_train)  #model\n",
# #     "\n",
# #     "#Predict y value for test dataset\n",
# #     "y_predict = nb_tfidf.predict(X_val_vectors_tfidf)\n",
# #     "y_prob = nb_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]\n",
# #     " \n",
# #     "\n",
# #     "print(classification_report(y_val,y_predict))\n",
# #     "print('Confusion Matrix:',confusion_matrix(y_val, y_predict))\n",
# #     " \n",
# #     "fpr, tpr, thresholds = roc_curve(y_val, y_prob)\n",
# #     "roc_auc = auc(fpr, tpr)\n",
# #     "print('AUC:', roc_auc)  \n",
# #     "\n",
# #     "\n"
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "#### LR (w2v)"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 20,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "              precision    recall  f1-score   support\n",
# #       "\n",
# #       "           0       0.63      0.82      0.71       871\n",
# #       "           1       0.60      0.37      0.46       652\n",
# #       "\n",
# #       "    accuracy                           0.63      1523\n",
# #       "   macro avg       0.62      0.59      0.59      1523\n",
# #       "weighted avg       0.62      0.63      0.60      1523\n",
# #       "\n",
# #       "Confusion Matrix: [[712 159]\n",
# #       " [412 240]]\n",
# #       "AUC: 0.6552953730638924\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#FITTING THE CLASSIFICATION MODEL using Logistic Regression (W2v)\n",
# #     "lr_w2v=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')\n",
# #     "lr_w2v.fit(X_train_vectors_w2v, y_train)  #model\n",
# #     "\n",
# #     "#Predict y value for test dataset\n",
# #     "y_predict = lr_w2v.predict(X_val_vectors_w2v)\n",
# #     "y_prob = lr_w2v.predict_proba(X_val_vectors_w2v)[:,1]\n",
# #     " \n",
# #     "\n",
# #     "print(classification_report(y_val,y_predict))\n",
# #     "print('Confusion Matrix:',confusion_matrix(y_val, y_predict))\n",
# #     " \n",
# #     "fpr, tpr, thresholds = roc_curve(y_val, y_prob)\n",
# #     "roc_auc = auc(fpr, tpr)\n",
# #     "print('AUC:', roc_auc)  "
# #    ]
# #   },
# #   {
# #    "cell_type": "markdown",
# #    "metadata": {},
# #    "source": [
# #     "### TESTING THE MODEL ON UNLABELLED DATASET"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 26,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "   id keyword location                                               text  \\\n",
# #       "0   0     NaN      NaN                 Just happened a terrible car crash   \n",
# #       "1   2     NaN      NaN  Heard about #earthquake is different cities, s...   \n",
# #       "2   3     NaN      NaN  there is a forest fire at spot pond, geese are...   \n",
# #       "3   9     NaN      NaN           Apocalypse lighting. #Spokane #wildfires   \n",
# #       "4  11     NaN      NaN      Typhoon Soudelor kills 28 in China and Taiwan   \n",
# #       "\n",
# #       "                                          clean_text  predict_prob  target  \n",
# #       "0                          happen terrible car crash      0.703070       1  \n",
# #       "1  heard earthquake different city stay safe ever...      0.901061       1  \n",
# #       "2  forest fire spot pond geese flee across street...      0.870295       1  \n",
# #       "3                  apocalypse light spokane wildfire      0.634877       1  \n",
# #       "4                 typhoon soudelor kill china taiwan      0.995811       1  \n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "#Testing it on new dataset with the best model\n",
# #     "df_test=pd.read_csv('test.csv')  #reading the data\n",
# #     "df_test['clean_text'] = df_test['text'].apply(lambda x: finalpreprocess(x)) #preprocess the data\n",
# #     "X_test=df_test['clean_text'] \n",
# #     "X_vector=tfidf_vectorizer.transform(X_test) #converting X_test to vector\n",
# #     "y_predict = lr_tfidf.predict(X_vector)      #use the trained model on X_vector\n",
# #     "y_prob = lr_tfidf.predict_proba(X_vector)[:,1]\n",
# #     "df_test['predict_prob']= y_prob\n",
# #     "df_test['target']= y_predict\n",
# #     "print(df_test.head())\n",
# #     "final=df_test[['id','target']].reset_index(drop=True)\n",
# #     "final.to_csv('submission.csv')"
# #    ]
# #   }
# #  ],
# #  "metadata": {
# #   "kernelspec": {
# #    "display_name": "Python 3",
# #    "language": "python",
# #    "name": "python3"
# #   },
# #   "language_info": {
# #    "codemirror_mode": {
# #     "name": "ipython",
# #     "version": 3
# #    },
# #    "file_extension": ".py",
# #    "mimetype": "text/x-python",
# #    "name": "python",
# #    "nbconvert_exporter": "python",
# #    "pygments_lexer": "ipython3",
# #    "version": "3.7.3"
# #   }
# #  },
# #  "nbformat": 4,
# #  "nbformat_minor": 2
# # }

