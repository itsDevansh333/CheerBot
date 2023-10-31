import string
from collections import Counter
# import matplotlib
text=open('Thoughts.txt',encoding='utf-8').read()
lower_case=text.lower()
# print(lower_case)
# print(string.punctuation)
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)
tokenized_words=cleaned_text.split()
#print(tokenized_words)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words=[]
for token in tokenized_words:
    if token not in stop_words:
        final_words.append(token)
# print(final_words)
Emotions=[]
with open('Emotions.txt','r') as file:
    for line in file:
        clear_Line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion=clear_Line.split(':')
        if word in final_words:
            Emotions.append(emotion)
print(Emotions)
W=Counter(Emotions)
print(W)