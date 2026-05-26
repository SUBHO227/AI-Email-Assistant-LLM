import ollama

def predict_word(text):
  #promt engineering
  #These instructions guide Gemma to behave like # email autocomplete sentence instead of chatbot
    prompt = f"""
Complete the email sentence.
Maximum 8 words.

Do not generate paragraphs.
Do not explain.
Do not chat.

Examples:

Input: I would like to
Output: request leave for tomorrow.

Input: Please review the
Output: attached project report.

Input: Thank you for
Output: your valuable support.

Now complete this:

Input: {text}
Output:
"""
    
    #sending promt to Gemma model through ollama
    response = ollama.chat(
        #using Gemma 2b model
        model='gemma:2b',
        #message format used by LLMS
        messages=[
            {    #promt sent as user message
                'role': 'user',
                #Actual prompt content
                'content': prompt
            }
        ]
    )
    #Extracting generated response Text
    result = response['message']['content']
    ## Removing unnecessary chatbot style outputs
    result = result.replace("Sure, here's the completed sentence:", "")
    result = result.replace("I hope this helps!", "")
    result = result.replace("Let me know if you have any other questions.", "")
    # Removing unwanted * symbols
    result = result.replace("*", "")
     # Removing extra spaces/new lines
    result = result.strip()

     # Returning final cleaned output

    return result