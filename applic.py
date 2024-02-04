from flask import Flask, jsonify, request
from stanza import Pipeline

app = Flask(__name__)
app.config.from_object(__name__)

nlp = Pipeline('en')
content= "These are simple sentences. And that's another one"

@app.route('/lemmatizza', methods=['POST'])
def lemmatizza():
   inpost = request.get_json
   print(type(inpost))
   text = inpost.get('text')
   out = []
   doc = nlp(text)  # applicato nlp a variabile content -> oggetto di tipo doc processato da stanza
   for sent in doc.sentences: # forloop addestrata per ottenere contenuto frasi
       for word in sent.words:
           out.append(word.lemma) # per ogni parola restituisco lemma e inserisco dentro lista out
   return out

@app.route('/sentiment_simple', methods=['GET'])
def sentiment_analysis():
   sentiment = {0: 'negativo',
                1: 'neutro',
                2: 'positivo'} # dizionario x convertire numero in sentimento
   out = []
   doc = nlp(content)
   for sent in doc.sentences:
      convertito = sentiment.get(sent.sentiment)
      out.append(f"La frase: {sent.text} ha il sentimento: {convertito}")
   return out


@app.route('/sentiment_post', methods=['POST'])
def sentiment_analysis_post():
   inpost = request.get_json()
   text = inpost.get('text')
   sentiment = {0: 'negativo',
                1: 'neutro',
                2: 'positivo'}
   out = []
   doc = nlp(text)
   for sent in doc.sentences:
      convertito = sentiment.get(sent.sentiment)
      out.append(f"La frase: {sent.text} ha il sentimento: {convertito}")
   return out


if __name__ == '__main__':
   app.run()
