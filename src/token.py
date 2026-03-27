from pythainlp import word_tokenize

def thai_tokenizer(text):
    return word_tokenize(text, engine='newmm')