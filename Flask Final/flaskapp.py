# Importing flask and transformers 
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer

# Import the necessary libraries
import nltk
import sentencepiece as spm
from nltk import sent_tokenize
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import PyPDF2
import os
import torch

app = Flask(__name__) # Initializing the flask app

#### Summarizer model ####

# Load the summarizer model and tokenizer
model_name = "DaviadiAF/T5-Small_AbsSumm_XSumCNN"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize a variable to store the summary
generated_summary = ""

# Configuring the upload folder for all uploaded papers to summarize
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = '' 
    pdf_reader = PyPDF2.PdfReader(pdf_file) # Reading the pdf
    num_pages = len(pdf_reader.pages) # obtaining number of pages in pdf
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num] # Extract each page in the pdf
        text += page.extract_text() # Extracting the text from the pdf
    return text

### Common words Model ###

def find_common_words(sentence1, sentence2): # Common words 
    # Tokenize the sentences and remove stopwords
    stop_words = set(stopwords.words('english')) 
    tokenizer = RegexpTokenizer(r'\w+\'?\w*')  # Modified regular expression
    
    # Getting each tokenized work in each sentence if it is not a stopword
    words1 = [word.lower() for word in tokenizer.tokenize(sentence1) if word.lower() not in stop_words]
    words2 = [word.lower() for word in tokenizer.tokenize(sentence2) if word.lower() not in stop_words]

    # Find common words
    common_words = set(words1) & set(words2)

    return common_words

def find_common_phrases(text1, text2, min_phrase_length): # Common phrases 
    # Tokenize the texts into sentences
    tokenizer = RegexpTokenizer(r'\w+\'?\w*')  # Modified regular expression
    tokens1 = tokenizer.tokenize(text1)
    tokens2 = tokenizer.tokenize(text2)

    common_phrases = set() # Initializing common_phrases variable
    
    # Joining the tokens from each sentence together.    
    for phrase_length in range(min(len(tokens1), len(tokens2)), min_phrase_length - 1, -1):
        ngrams1 = [' '.join(tokens1[i:i+phrase_length]) for i in range(len(tokens1) - phrase_length + 1)]
        ngrams2 = [' '.join(tokens2[i:i+phrase_length]) for i in range(len(tokens2) - phrase_length + 1)]

        common_phrases.update(set(ngrams1) & set(ngrams2))

    # Return the common phrases that meet the minimum length criteria
    common_phrases = [phrase for phrase in common_phrases if len(phrase.split()) >= min_phrase_length]

    return common_phrases


### Translation model ###

# Importing the translation model 
name_of_model = "Helsinki-NLP/opus-mt-en-nl"
translation_model = AutoModelForSeq2SeqLM.from_pretrained(name_of_model)
translation_tokenizer = AutoTokenizer.from_pretrained(name_of_model)

### Flask application ###

## Home page
@app.route('/') 
def home():
    return render_template('indexv3.html')

## Summarizer section
@app.route('/summarize', methods=['POST'])
def summarize():
# Uploading pdf file and retreiving its path to the "uploads" folder
    # If file is not a pdf, redirect to a different webpage
    if 'pdf_file' not in request.files:
        return redirect(request.url)

    # Requesting a PDF file 
    pdf_file = request.files['pdf_file']
    
    #If there is no pdf file, redirect to a different webpage
    if pdf_file.filename == '':
        return redirect(request.url)

    if pdf_file:
        # Save the uploaded file to the upload folder
        pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(pdf_file_path)

        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(open(pdf_file_path, 'rb'))#

    global generated_summary  # Store the generated summary in a global variable

    # Process and summarize the text
    inputs = tokenizer(text, return_tensors='pt', max_length=2000, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=800, min_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    generated_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return f'Summary: {generated_summary}'

## Common words section
@app.route("/summarize/commonwords", methods = ["POST"])
def common_words():
    # Function to find common phrases in two texts
    text = request.form['text']

    # Use the generated summary for comparison
    summary = generated_summary

    # Find common words
    common_words = find_common_words(text, summary)

    # Find common phrases with a minimum phrase length of 3 words
    common_phrases = find_common_phrases(text, summary, 3)

    return f'Common Words: {common_words}\n Common Phrases: {common_phrases}'

## Translation section 
@app.route("/summarize/translate", methods = ["POST"])
def translate():
    text_to_translate = generated_summary

    # Perform the translation
    inputs = translation_tokenizer(text_to_translate, return_tensors="pt")
    translation = translation_model.generate(**inputs)
    translated_text = translation_tokenizer.decode(translation[0], skip_special_tokens=True)

    return f"Translated text: {translated_text}"

## Running the Flask application 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 

