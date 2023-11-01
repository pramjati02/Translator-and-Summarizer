# Translator-and-Summarizer:
Program that will both translate and summarize papers on demand.
Codes can be run through the Jupyter notebooks with Jupyterlab and Google Colab, or can be copy and pasted manually to your IDE. 

# Summarizer 
Can be accessed through summarizer.ipynb

Summarizes texts that are inputted by the user. 

Article used to build the summarizer: https://www.analyticsvidhya.com/blog/2023/07/build-a-text-summariser-using-llms-with-hugging-face/ 

Git link for summarizer:

# Common Words Model
Can be accessed through Words and phrases in common.ipynb

Outputs both the words (not including stopwords) and phrases in common of two articles. At the moment, the model relies on user input in order to infer the maximum length of common phrases in the output.



Git link for translator:

Git link for subword tokenizer:

# Flask Environment
The incorporated summarizer model in the flask environment can be found in the folder ***flask environment*** under the branch ***Flask_environments***. 

To run this environment, you will need to navigate to the folder and download the two files ***summarizer.py*** and ***new_index.html***. Alternatively, you can use **git clone** if you are using a terminal. A terminal with python3 was used to make this environment, therefore we recommend using one to run it. We recommend using **Windows Subsystem for Linux (WSL)** to install the required packages and run the environment. 

Instructions for installing WSL can be found here: https://learn.microsoft.com/en-us/windows/wsl/install

Instructions for installing python3 into WSL: write in your terminal **sudo apt install python3 python3-pip**

In the terminal, you will need to install The packages ***flask***, ***transformers***, ***torch***, ***torchaudio*** and ***torchvision*** using the command **pip3** eg. **pip3 install flask**. After installing these packages, navigate to the folder with your downloaded ***summarizer.py*** and ***new_index.html*** files in your terminal using **cd (file path location)**, and run it using **python3 summarizer.py**.
