import newspaper
from newspaper import Article
from textblob import TextBlob


bbc_paper = newspaper.build("https://m.bbc.co.uk", memoize_articles=False)
cnn_paper=newspaper.build("http://cnn.com", memoize_articles=False)
telegraph_paper = newspaper.build("https://www.telegraph.co.uk/", memoize_articles=False)
ft_paper = newspaper.build("https://www.ft.com", memoize_articles=False)
guardian_paper = newspaper.build("https://www.theguardian.com", memoize_articles=False)


bbc_output = []

def sentimentfinder(sentiment):
	if sentiment < -0.8:
		return "Appalled"
	if sentiment < -0.5:
		return "Negative"
	if sentiment < -0.2:
		return "Midly Negative"
	if sentiment == 0:
		return "Neutral"
	if sentiment < 0.2:
		return "Somewhat Positive"
	if sentiment < 0.5:
		return "Positive"
	if sentiment < 0.8:
		return "Overjoyed"
	else:
		return "Not clear"

def articleprinter(paper_variable):
	x = 0
	for article in paper_variable.articles:
		article.download()
		article.parse()
		article.nlp()
		text = article.summary
		blob = TextBlob(text)
		sentiment = blob.sentiment.polarity
		attitude = sentimentfinder(sentiment)
		articlelist = [article.title, article.summary, article.keywords, attitude]
		if x == 50:
            		break
		bbc_output.append(articlelist)

articleprinter(bbc_paper)

for x in range(len(bbc_output)):   ##use if statement here to filter results e.g if "Boris" in bbc_output[x][1]:
	print("Article title"+bbc_output[x][0])
	print("Language used: "+bbc_output[x][3])














