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
The incorporated summarizer model in the flask environment can be found in the folder ***Flask Final*** under the branch ***main***. 

To run this environment, you will need to navigate to the folder and download the files in that folder. Alternatively, you can use **git clone** if you are using a terminal. A terminal with python3 was used to make this environment, therefore we recommend using one to run it. We recommend using **Windows Subsystem for Linux (WSL)** to install the required packages and run the environment. 

Instructions for installing WSL can be found here: https://learn.microsoft.com/en-us/windows/wsl/install

Instructions for installing python3 into WSL: write in your terminal **sudo apt install python3 python3-pip**

In the terminal, you will need to install the packages in ***requirements.txt*** using the command ***pip3 install -r requirements.txt*** 

After installing these packages, navigate to the folder with your downloaded github repository files in your terminal using **cd (file path location)**, and run it using **python3 flaskapp.py**.
# High level overview user end
![photoshopdiagram](https://github.com/pramjati02/Translator-and-Summarizer/assets/139998943/2aa925ef-21f7-4442-80fe-bb260abb8c93)
