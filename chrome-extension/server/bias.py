import sys
import google.generativeai as genai
import os
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
sys.stderr = open(os.devnull, 'w')

# text = sys.stdin.read()

genai.configure(api_key=os.environ.get("API_KEY"))
genai.configure(api_key="AIzaSyDzecibA6w_72JMv7VrOq0NFVZLhyRYZSE")

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
    system_instruction="For each of the texts you receive, your response will be a JSON object containing 4 topics. A topic object has the following schema:\n- name: The name of the topic. This should be no longer than 4 words. \n- score: A number between 1 and 100 with 100 being the most positive and 1 being the most negative. This score will represent the author's attitude towards that topic. \n- explanation: The explanation for the score. This explanation should be no longer than 1 sentence.\n\nThe first three topic objects will contain the topics of three attitudes that the author of the input text possesses that would most likely affect the impartiality of the text. The topic should be a concept or entity that the author may feel positively or negatively toward. An example of a topic would be the author's attitude towards the LGBTQ+ community.  \n\nThe last topic object will have a name of \"Impartiality Score\" and the score will represent the author's overall impartiality with 100 being the most impartial. ",
)

# response = model.generate_content(text)
response = model.generate_content("Chinas Olympic Swimming Success Deserves All of Your Doubts. After Pan Zhanles world-record performance in the 100-meter freestyle final, the countrys triumphs in the pool should come under scrutiny due to its recent doping scandals. PARIS — It would be nice to believe that Chinese swimmer Pan Zhanles scorching obliteration of the Olympic field and world record in the mens 100-meter freestyle Wednesday night was a completely fair and honest athletic accomplishment. Nice, but also naive. China forfeited the benefit of the doubt, as did the World Anti-Doping Association (WADA) and World Aquatics. That’s the cloud it has created and has to live under. Every great Chinese swimming feat here—and there have been few so far—will be greeted by suspicion more than celebration. Oh well. When one country has 23 swimmers test positive for a prohibited heart medication—trimetazidine, or TMZ—in 2021 and it goes both unannounced for three years and unpunished ever, thats a problem. When those positive tests are written off by China, WADA and World Aquatics as accidental hotel kitchen contamination, without any credible theory on how it happened, thats a problem. When The New York Times later revealed that three of those 23 swimmers also tested positive in 2016 and 17 for the anabolic agent clenbuterol, and those tests were neither publicized nor punished, thats a problem. And when The Times again reported on other dismissed and unpublished positive tests for two swimmers in 2022—attributed to bad beef at McDonalds—thats a problem. So much tainted food. So little credibility.With all those positive tests as a pre-Olympic backdrop, and with 11 of the original TMZ 23 athletes on the Chinese roster for Paris, scrutiny and suspicion were high. So were expectations, after China hauled in 16 medals (five gold, three silver, eight bronze) at the 2023 world championships. Through the first four days of competition here, China swam unspectacularly. With just two silver medals and two bronze—and several surprising disappointments—there were some tart remarks in La Défense Arena about what might have been missing from Chinas pre-meet preparation. The last re-writing of the record book was in February by Pan himself, taking .06 off the mark set by David Popovici in 2022. Then here came Pan to take a giant bite out of it in Paris, at a time when doubt in China—and WADA, and World Aquatics—is at an all-time high. It was a stunning swim, both visually and contextually. To be a full body length clear of the field in an Olympic sprint final—leaving Chalmers and Popovici and five others in his wake—was unusual. The margin of victory, .92 of a second, is the largest in the Olympics in that event since 1928. Yep, this was a once-every-96-year beatdown.")

result = json.dumps(response.text)
print(result)