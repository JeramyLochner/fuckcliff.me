#!/usr/bin/env python

import markovify
import html2text
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getModel(url):
	soup = BeautifulSoup(urlopen(url), 'lxml')
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out
	text = html2text.html2text(soup.get_text())

	# lines = (line.strip() for line in text.splitlines())
	# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# text = '\n'.join(chunk for chunk in chunks if chunk)

	#print(text)

	model = markovify.Text(text)
	return model

cliff_url = 'http://fuckcliff.me'
cliff_model = getModel(cliff_url)

# for i in range(3):
#     print(cliff_model.make_sentence())


wiki_url = "https://en.wikipedia.org/wiki/1960_Valdivia_earthquake"
wiki_model = getModel(wiki_url)

# for i in range(3):
#     print(wiki_model.make_sentence())

wombo_combo = markovify.combine([ cliff_model, wiki_model ], [ 1, 1.5 ])

for i in range(25):
    print(wombo_combo.make_sentence())

#"https://en.wikipedia.org/wiki/1989_Tiananmen_Square_protests"

#All I want to say is that students are getting very weak, it is a shame that after being born on this planet, you were born.

#So, either accept the truth or Hitler.

#Area 51 Area 51 Area 51 is a registered trademark of the Pentagon by the war were explained away by politicians as the result of the Beijing student protests and called for the Premier to emerge.


#https://en.wikipedia.org/wiki/Fukushima_Daiichi_nuclear_disaster

#Cliff 101: The Basics For those of the city formerly known as Mexico City.

#In the 4th century, Cliffists faced persecution from Roman Christians and the National Center for International Security and Cooperation.

#With this new cash flow, Trotsky was able to deny anything, such as fossil gas and coal power expansion in any developed nation.

#Each man killed himself.


#https://en.wikipedia.org/wiki/1960_Valdivia_earthquake

#Hundreds of people were already reported dead by the ruling elite long before you were born.

#Won from Saddam Hussein in a severely deteriorated state and had developed a contingency plan.

#However, Cliff is unknown, but it is worth pointing out that Carl Marx was the inspiration for Lenin and Communism.

#In return, Cliff was known to participate in the slave trade, slaves and human sacrifice became crucial aspects of the Earth and Planetary Interiors.

#By using this site, you agree to the chronicle of Mariño de Lobera, corregidor of Valdivia was totally destroyed.
