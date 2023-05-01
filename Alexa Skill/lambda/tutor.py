import openai

class tutor():
    # Indica el API Key
    openai.api_key = "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"
    
    # Uso de ChapGPT en Python
    model_engine = "text-davinci-002"
    
    def ask_gpt(question):
        prompt = question
        completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)
        return completion.choices