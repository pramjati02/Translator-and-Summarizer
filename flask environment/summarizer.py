from flask import Flask, request, render_template
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

# Load the summarizer model and tokenizer
model_name = "DaviadiAF/T5-Small_AbsSumm_XSumCNN"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('new_index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']

    # Process and summarize the text
    inputs = tokenizer(text, return_tensors='pt', max_length=2000, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=800, min_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return f'Summary: {summary}'

#@app.route("/summarize/commonwords", methods=["POST"])


if __name__ == '__main__':
    app.run(debug=True)
