import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Descargar recursos de NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Paso 1: Cargar el conjunto de datos
data = pd.read_csv('reviews.csv')  # Reemplaza con el archivo real si tienes uno
data['review'] = data['review'].astype(str)  # Asegurarse de que sean strings

# Paso 2: Análisis de sentimientos
def analyze_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity

data['polarity'] = data['review'].apply(analyze_sentiment)
data['sentiment'] = data['polarity'].apply(lambda x: 'positive' if x > 0 else 'negative')

# Paso 3: Procesamiento del lenguaje
stop_words = set(stopwords.words('english'))

def preprocess_text(review):
    tokens = nltk.word_tokenize(review.lower())
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

data['cleaned_review'] = data['review'].apply(preprocess_text)

# Filtrar por sentimientos
positive_reviews = ' '.join(data[data['sentiment'] == 'positive']['cleaned_review'])
negative_reviews = ' '.join(data[data['sentiment'] == 'negative']['cleaned_review'])

# Paso 4: Crear nubes de palabras
def create_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16)
    plt.show()

create_wordcloud(positive_reviews, 'Nube de Palabras: Reseñas Positivas')
create_wordcloud(negative_reviews, 'Nube de Palabras: Reseñas Negativas')
