import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser # pip install webbrowser
import os
import pyjokes #pip install pyjokes
import requests
import wolframalpha #pip install wolframalpha
import time
import subprocess 
import random
import googletrans #pip install googletrans==4.0.0rc1
from tkinter import *
from tkinter import ttk,messagebox
import textblob #pip install textblob
import randfacts #pip install randfacts
from gtts import gTTS #pip install gtts
import requests #pip install requests
from stemsim import *
from testing2 import *
from calculater2 import *





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


print('''Here  the list of  commands applicable:
*(Search Wikipedia for .............)-Searches Wikipedia for Your Query
*(tell me the news)- Opens BBC's official website
*(I have a doubt)- Gives an answer to your doubt
*(Tell me a story)-Tells you a story with options for different genres
*(trivia)-Gives a random trivia question
*(simulator)-Opens a Friction-Velocity Simulator
*(dictionary)-searches the dictionary for a word you want to find the meaning
*(weather)-Gives you the weather report of cities
*(city)-Gives you statistics about a city
*(translator)-directs you to a translation
*(tell me a joke)-Tells a random joke
*(tell me a fact)-tells a random facts
*(open.....)Open's a website. freecodecamp.org , stackoverflow.com and spotify''')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  

    else:
        speak("Good Evening!")  

    speak("I am Assista! Your Educational and Bore-Free Bot!. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.play_threshold = 4000
        r.adjust_for_ambient_noise(source)
        audio=r.listen (source,timeout=8,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()







        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'simulate' in query:
            speak("Opening the Simulator")
            simulate()

        elif 'calculator' in query:
            speak('which function will you use')
            qry=takeCommand().lower()
            speak('what number will you apply it on')
            no=takeCommand().lower()
            speak(calc(qry,no))

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://www.bbc.com/news")
            speak("here are some world headlines. Happy reading!")
            time.sleep(6)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            webbrowser.open("open.spotify.com")

        elif 'open freecodecamp' in query:
            webbrowser.open("freecodecamp.org")
        elif 'open simulator' in query:
            from stemsim import *
            stemsim()

        elif 'open Translator' in query:
            from testing 2 import *
            

        elif 'recommend me a good youtube channel to watch' in query:
            speak("Bright Side is a really good channel. It has various videos ranging from riddles to VR 360 roller coaster rides! Please check it out")
            webbrowser.open("https://www.youtube.com/channel/UC4rlAVgAK0SGk-yTfe48Qpw")

        elif 'trivia' in query:
            speak("Loading A random question .....")
            category = 'general'
            api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
            response = requests.get(api_url, headers={'X-Api-Key': 'OI+i5ZhAyyPAn1L+8ckpbQ==n9HQtFkWncwbYyTw'})
            if response.status_code == requests.codes.ok:
                speak(response.text)
                print(response.text)
            else:
                print("Error:", response.status_code, response.text)

        elif 'search the dictionary' in query:
            w=input("Enter the word you want to find the meaning of:")
            import requests
            word = w
            api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
            response = requests.get(api_url, headers={'X-Api-Key': 'OI+i5ZhAyyPAn1L+8ckpbQ==n9HQtFkWncwbYyTw'})
            if response.status_code == requests.codes.ok:
                print(response.text)
                speak(response.text)
            else:
                print("Error:", response.status_code, response.text)

        elif 'weather' in query:
            m=input("Enter the city you want to find the weather of:")
            city = m
            api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
            response = requests.get(api_url, headers={'X-Api-Key': 'OI+i5ZhAyyPAn1L+8ckpbQ==n9HQtFkWncwbYyTw'})
            if response.status_code == requests.codes.ok:
                print(response.text)
            else:
                print("Error:", response.status_code, response.text)

        elif 'cities' in query:
            qw=input("Enter the name of the city you want to find some data of:")
            name = qw
            api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(name)
            response = requests.get(api_url, headers={'X-Api-Key': 'OI+i5ZhAyyPAn1L+8ckpbQ==n9HQtFkWncwbYyTw'})
            if response.status_code == requests.codes.ok:
                print(response.text)
                speak(response.text)
            else:
                print("Error:", response.status_code, response.text)

        
            
            

                


        elif 'I have a doubt' in query:
            speak('I can answer to any question and what question do you want to ask now')
            question=takeCommand()
            app_id="5HY8K2-K7TLVXH9H6"
            client = wolframalpha.Client('5HY8K2-K7TLVXH9H6')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'tell me some facts' in query:
            facts = randfacts.get_fact()
            speak(facts)
            print(facts)

        
        elif 'tell me a story' in query:
            speak("I can tell you random stories from 4 genres. Fiction , Biography , Thriller or Science-Fiction. Please specify below:")
            genre=input("Enter the genre you want to listen your story from:")
            if genre=='Fiction':
                speak('When the Sea takes you I wont come with by Christian Jerome')
                speak('''“In my past life, I was a bird.”

“How’d you know?”

My little brother shrugged. “I just feel it.”

Piles of debris painted where the houses used to be, torn-down walls and foundations mere remains of the structures that were there. We must have scavenged through all of them, finding nothing but rubbish and mud. The blue comet streaked across the sky. Cold winds blew onto my back, smelling of sand and cement and something else. A tinge of something bitter, something revolting. The water took four people from around these parts, but the way they polluted the air was something I did not expect.

The people readied themselves for the rain and the wind, according to the news, but never for the swelling of the ocean and the subsequent taking. They all cried during the interviews, I remembered, their tears mixing with the drizzle and rain. Unfortunate, but I would have given a hand to have the leeway they had. They all blamed the blue comet which, if their word was to be believed, was a bad omen. I thought that rather stupid.

“You won’t find anything in here, Jo,” I shouted at him as he stooped down and grabbed something from the rubble. “The sea’s taken everything.”

“We’ve got nothing to lose, do we?”

“No, you’ve got nothing to lose. You’re dead, remember.”

His posture, upright and square, slackened. A small piece of plastic robot snuggled in his hand. It looked clean and undamaged, unlike the debris of the furniture and the houses around it. He dropped it back to the mud.

“Hey,” I said.

“It’s fine.” He stood up and gazed overhead, the blue comet dazzling over the dim late morning sky. He hopped over the remains of a destroyed TV set. “Let’s just go back home. Take my things for me, will you?”

-

“What were you in your past life?” he asked.

“I don’t know. I don’t think about it.”

“Come on. Anything.”

Jo pulled at a book underneath a pile of mess that once were the contents of our closet. The book’s pages had turned brown from the mud and water, its contents folded where the debris on top of it fell. I remember it being his favorite, some story about three fishermen finding and fighting over a tuna made of gold. He beamed like a crazed man when he brought the book home. He placed it inside one of the banged-up boxes we brought.

“What do you want to do with it?” I asked.

“I don’t know. Give it away, maybe?”

“I don’t know if anyone would want it.”

The sea gives and the sea takes, Father used to tell us over our meals when we were younger. Aside from our home, the sea took my textbooks and my pens, along with my uniforms and school bag. My little library was no more. Mud found a way inside my little make-up kit, three brushes, two lipsticks, and three other augments inside a tin cookie can. A few of my clothes still looked usable despite the muck seeping in on a few of them. I folded them neatly and placed them in my separate box.

Jo squealed, and I turned to see him holding a transparent plastic globe. Depicted inside was the ocean floor, small plastic cutouts shaped like fish floating on the bluish liquid inside. Glitters scattered inside the sphere as he shook it. The display seemed to swallow him whole. “This doesn’t belong here,” he said, and placed it inside the box that was his.

“You remember when I bought that for you?” I asked him.

“Christmas, two years ago now. I was eleven, I think.”

“I didn’t know it’s still working.”

“I kept it in its box under my bed. It looked too good to leave out in the open.”

The kitchen and the living room had disappeared. Two adjacent walls were all that was left, three wooden support columns supporting them. We scavenged for ten more minutes, finding nothing else worth taking in the leftovers of what used to be our little wooden one-story house. As we were leaving, a fire truck’s siren blared past, three trucks’ worth of relief packs following close. People scampered behind it. Jo and I ran alongside the crowd, both of our boxes in my arms.

-

“Father’s already on the other line,” Jo told me.

“And?”

“It says ‘One pack per family only’ on the tarp.”

“It’s fine. They won’t know.”

The relief trucks carrying Governor’s New Year Packs parked outside the school grounds, this time used as our temporary shelter. The line of people snaked thrice around the school building, hundreds of hungry and sweaty people filling the air with musk, mud, and saltwater. I fell in line after giving Mother our boxes.

A tarp hung on one of the trucks, “Jason Mesa for Reelection.” “Unconditional Service” it said on another. When they told me they only allowed one pack per family, I told them only I was available to get our packs, my mother currently taking care of a two-year old sister I didn’t have. Three hours I stayed on the line, bathed in the afternoon sun and the mindless chatter of hundreds of people. The only relief I had was looking up to see the blue streak in the sky.

We stayed on a classroom on the ground floor, with six other families. When I gave the packs to Mother, she didn’t look me in the eye, as when I gave her the boxes. I mostly looked at the floor, myself reluctant to ever look at her. Almost as if I didn’t deserve the respect. I wanted to insist that, again, it was not my fault, but knew my protestations, like before, would fall on deaf ears.

I went outside to escape what little New Year preparations we had. I did not feel any concern for it. Besides, I have my word to keep. Jo wanted to go to the playground, he said. “On that park near the intersection.”

“You know there’s probably nothing in there now, right?”

“It doesn’t matter. You promised we get to go wherever I wanted today, right?”

-

On the park grounds laid toppled trees, their roots exposed to the open air. Bushes and shrubberies looked dead, the lightbulbs on street lamps shattered. Trash and dead things scattered everywhere.

The playground itself was leveled. The slides and wooden supplements were either destroyed or lying upside down in the mud. There used to be a sandbox in here, I remembered, but I couldn’t find it. An upright swing set sat in the middle of the grounds, undamaged and dry under the faint late afternoon sun. Jo and I walked around and jumped over trees and debris. I took one seat, and when Jo sat on the other, he swung with his feet a little, the metal creaking every now and again.

“This was where they found Old Man Rudy, right?” Jo asked.

“Yeah, over there.” I pointed across a sizable shattered clay pot and its broken ornamental bamboo across the park. “He was drunk, they said.”

“Drunk and drowned by the sea. Not the best way to go.”

“That drunkard kind of deserved it, to be honest.”

Obscured by clouds, the comet was invisible for the first time since it appeared before the storm. Jo seemed like he was searching for it.

“You know it was an accident, right?”

“I know it was.”

His hand slipped from mine, I remembered, as we evacuated away from the sudden flooding on the streets. I saw the muddy water carry his body to the ocean, his head floating one moment and submerged the next. Debris floated around him. I could have reached out, that moment, but I didn’t. Maybe my hand could have gotten hold of his, but I didn’t want to try. I stood frozen, not wanting him to go, but not wanting to follow either. I wanted to take hold of him, but I didn’t want to get taken by the mud and by the sea.

Mother lunged at the water, but Father hooked his hand around her waist and pulled her back. He hugged the both of us as we gripped onto a lamppost, chin-high water craving to push us to the ocean a hundred meters away.

“We should have tightened our grips a bit more,” I said.

We stayed on the swings for quite some time.

-

“We’ve only got time for one more place. I can feel it.”

“Where do you want to go?” I asked.

“I want to go by the sea.”

I fetched out Jo’s box from Mother. The school grounds transformed into a massive camping site, dozens of charcoal grills and makeshift spitfires cooking New Year’s Eve dinners. Smoke blanketed all over the school, the smell unpleasant but appetizing. Father sat on his own grill, a pan over the charcoal cooking canned meat from the relief packs we received earlier. He kissed my forehead and hugged me, and I hugged him back.

Jo and I walked towards the opposite side of town. As we inched closer to the sea that took him, the devastation worsened. Houses went from damaged to outright flattened. We saw fewer people. The mud got thicker, squishing on our soles and slippers as we went. After a while it got darker, the street lamps either destroyed or devoid of power. Only the crescent moon and the blue streak of a comet up above led the way through the road full of muck and debris.

“Will they ever go back?” Jo asked.

“Who?”

“The people. Will they go back to their homes, near the sea?”

“I imagine they will.”

“We should move away. It’s too dangerous here.”

“If we had the money to move, we would have a long time ago.”

Debris still peppered the beach. Gentle waves rocked the surface of the sea, looking peaceful beneath the moonlight. The blue streak in the sky reflected off the water. Three days before, the typhoon made the ocean swell and, like a gigantic mouth, enveloped kilometers of land and pulled it back to its dark depths. Looking at it now, it seemed like no such event happened; that everything had been and will always be as peaceful as this.

I placed the box on the sand and Jo rummaged through what few items it contained. He picked up the plastic globe and gave it to me, the globe fitting snuggly in my hand. Remembrance, he said. I shook it, and the glitters and the fish floated up and sank back to the bottom again.

His box had his favorite book now caked with dry mud, his favorite shirt with an unrecognizable Superman logo covered in muck, and a Lego human figure with a broken arm. He lifted the box and we walked towards the sea. The water felt cold as I waded through, the sand tickling the places between my toes. Jo placed the box on the surface of the ocean. Its color darkened where the water licked on it. It rocked along with the gentle waves but kept its buoyancy, floating away from us, I supposed, towards the heart of the sea, or maybe where the moon met the horizon.

“Take them out of here, will you?”

I’ve heard the discussions late at night where Father insisted he knew nothing his whole life other than to fish. It brought so much frustration to Mother, having her whole life tethered to the dangerous sea. I imagined even more so now that it took her youngest. “You’re dead, Jonas. Why do you care so much?”

He thought for a second. “You’re alive, Marina. Why do you care so little?”

Jo’s ethereal body started disintegrating. The particles that broke off looked translucent and pale yellow, dissolving into nothingness after a second or two. I found myself wanting to sue for time, maybe a minute, or maybe two. My arms felt like reaching out again, grasping the material Jo was turning out to be.

“I was a bird, like you,” I said.

“Like me?”

“Yeah, like you. And when the weather’s bad, we’d fly off to another place.”

Jo’s box, now some ways into the sea, tipped over and was swallowed by the water, its contents dropping straight into the ocean floor. The blue comet streaking across the sky turned dim, fragmenting into hundreds of little particles too small and too dull to be seen. I was alone by the beach.

“I should have held on a little tighter,” I muttered. “I am so sorry.”

-

“We have rice, tomatoes, a can of meatloaf, and two cans of sardines.”

“Where are the others?” I asked.

“Why, I saved them up, of course. Take your pick.”

“I don’t want to eat, Father.”

“Come on, Rina. It’s New Year’s!”

Twenty-six people sat inside the classroom that doubled as our temporary home. Families huddled close together sporting the same food they received from the trucks earlier. The room smelled of sweat and sardines and brine. I didn’t understand the festiveness of Father and everyone else.

I sat beside Mother and Father and we prayed. Mother thanked the Lord for our little feast, and for giving us a roof beneath our heads this time of year. She asked to bless those people who, for the past three days, have been giving aid to us and everyone affected by the typhoon. She prayed for her youngest Jonas, that he was at peace, and that he was having fun in Heaven with the Creator up above. She sniffled as she said ‘Amen.’ Her eyes looked teary when she opened them. My eyes teared up too; she’d usually mention in her prayers a young woman named ‘Marina’ before.

Fireworks started going off outside. Everyone followed with cheers. People stood up and turned away from their food for a little while, greeting each other with amity whether they’re family or not. Men shook hands and women hugged each other. Kids jumped around in glee.

I worried about the birds.

I reached for the globe in my pocket and shook it, scattering the glitters and the fish. I whispered a greeting to it; I hope Jo would hear. From across the room, Father called out “Happy New Year!” as he marched closer and enveloped me and Mother in his arms.

I held the toy closer to my chest, hoping my little brother would also feel the embrace.''')
            elif genre=='Biography':
                speak("Zinedine Zidane")
                speak('''There is a famous person who I see as a good role model for me and he is a football player named Zine AL-dine Zidane. He may not be popular with many.

This player has very high morals and a great skill level, he is very humble, friendly with everyone. He has a wonderful smile and is not arrogant to any of the players or workers around him,

He also possesses many other qualities such as fair play and reliance on real skill and does not tend to exaggerate to get the penalty for deception.

I followed some of his famous matches on YouTube and watched him play for France. I also followed up when he participated in the training of Real Madrid, my favorite team.

What a wonderful addition to the team. I found it nice to implement his vision on the ground with such a great team. I really enjoyed watching him build those great moments and tight plans that helped the team so much to win.

I would very much like to be of such performance and skill not only in football but in life as well.''')

            elif genre=='Thriller':
                speak('The Heist by Alley Mejja')
                speak('''Sammy

My day started with a steaming cup of herbal tea and my to-do list that I was going to conquer. I came to the store for a few things I needed off of my list, but I never thought that my day would end like this. I never thought that today would be my last. I could hear my heart beating in my ears, I held my breath hoping it would slow my heart rate down. Can they hear my heart racing? The pounding in my head was overpowering, I couldn’t hear myself think. I scanned the room to make sure I hadn’t missed anything. To make sure that everybody was still alive. They took our cell phones as soon as they had us on the ground. I tried to protest, but before I could even utter a word, my face was plastered against the cold tile floor. My cheekbone ricochet off the floor and the pain washed over me for a split second, but then the shock kicked in and numbed every sensation in my body

I was able to lift my chin just enough to look towards the glass doors that led outside. The night sky lit up the parking lot, teasing me with the sight of my car in the distance. “How long had we been tied up? Why hasn’t anybody come for us?”  I thought. 

           We were lying face down, side by side in front of one of the register lanes. They had tied our hands behind our backs with some rope and gagged us with old musty washcloths that tasted like copper. I could tell right away that these people were amateurs; the man that took my phone out of my pocket earlier was stumbling over his words and had tremoring hands. There were a few of them, four to be exact. They were having a screaming match in the adjacent room, but they were keeping an eye on us the whole time. I could tell they weren’t prepared for what they had gotten themselves into. 

I was desperately trying to take my mind off everything that was going on, so I focused my energy on trying to eavesdrop on the conversation that was happening a few feet away. Inhale, exhale. Inhale, exhale. I needed to slow down the pounding in my ears if I was going to hear anything that they were saying. Inhale, exhale.

“...and you didn’t think to bring the gun?!” the bald one spat through clenched teeth. 

“ You said we were going to take the money and ditch! Nobody said anything about shooting these people!” the younger man yelled as he pointed to us. 

As he pointed toward us he stopped and stared at me straight in the eyes. Shit. I was focusing so hard on listening that I didn’t even realize how obvious I was being. The bald one followed his gaze and glared at me with his cold eyes. Shit. Shit. Shit. My heart was pounding more than it had been before, my eyes stung with pain from the tears that were flooding in them. I looked up at the ceiling and prayed to God that they would let it slide. I closed my eyes and felt the tears rolling down my cheeks. It was the first time I had cried since this whole ordeal started, and I couldn’t make them stop. Before I knew it, I felt someone yanking on my arm and dragging me to a standing position. 

“You enjoy the show?”  The man whispered in my ear. “ ‘cause that was nothing compared to what’s about to happen.”  

I stood there motionless, I was paralyzed with fear. My eyes were still closed, the darkness of my eyelids was my only safe haven. He was gripping my arm so tightly that I thought it was going to pop at any moment. The men that were arguing in the other room were now completely silent. 

“I’m on my feet….I could make a run for it if I can get him to let up on my arm.” I thought to myself. “They don’t even have a gun, I can do this.” 

I thought about my surroundings and what I could potentially use as a weapon. 

“The registers have dividing sticks, which could work with a hard enough blow in the right area… but there’s also the bottles of cleaner that would work. A few sprays to the eye and the second he let’s go of me to rub his eyes, I can make my run for it! Even if I only get to another room, that will give me more time and resources to come up with a plan! I could go to the utility closet and-”

In the midst of my scheming I hadn’t realized that the pressure on my arm was no longer there. I guess he had a change of heart? I couldn’t hear anybody talking, nobody was even breathing loud enough for me to hear. The only noise I could make out were cars in the far distance. I opened my eyes and saw that everything and everyone were in the same places they had been before. My three coworkers still face down on the dirty tile,  still gagged, but thankfully - still alive. 

Brian 

It was like I had forgotten how to breathe, my chest felt like someone had squeezed all the air out of it.

“Breathe Brian!” She quietly said as she gripped my chin in her cold hands. “We are going to get through this, but you need to talk to me about what you’re thinking.” She loosened her grip on me as I took a deep breath. 

Tell her what I'm thinking? I’m thinking that our lives are fucked! I looked deep into her eyes to try to gauge how she was feeling. Her eyes showed no tell tale signs of what she wanted to do.

 “Hell, maybe she doesn’t want this baby either.”  I wondered.

“I.… I really think I want to keep it,” She stuttered. “I love you and I know you’ll make an amazing daddy.”  

Shit. 

“I  just need to process this, okay?” I cautiously told her as I held her hands. They were so small, and fragile compared to mine. I never realized that until now, I had never stopped to just take in all her perfections. The waves in her golden hair were dancing in the wind, her nose had this little beauty mark just above her nostril. She looked at me with this perplexed look on her face, and god damn it - it was the cutest thing she’s ever done. I remember the stories my mother would tell me about raising a baby on her own. They all started off with hardships, tears, stress, and fear. In the end though, she wouldn’t have traded anything in the world for me. She made it through homelessness, abusive relationships, and shady jobs. If she was able to survive through all of that, I could raise a baby with the woman I love. We can do this. 

“I agree,” I said as I took a deep breath. “Let’s have ourselves a baby.” I pulled her into my arms. “I will figure this out, I promise.” I reassured her. She let out the sweetest sigh, like a weight had been lifted off of her shoulders. 

The walk home was quiet because we had so much going on in our heads. I had just gotten to a good place in my life. If someone had asked me five years ago if I ever wanted kids, I would have laughed. The thought of a child used to scare me because I couldn’t even take care of myself. To be fair, none of my exes were capable of mothering anything except their drug money. Kayla was different though, and she made me realize that there is so much more to life. She has dreams and she has been setting and achieving goals for herself these last few months. I made a promise to her that I was going to help her on her journey to become a singer. But, if her new dream is to have a baby - then that’s what  we're going to do. 

I collapsed on my bed as soon as I got home, laying there trying to figure out a plan. The ceiling fan had been spinning in a continuous loop, much like my mind. Today marked three years of my sobriety and yet all I could think about was how good a hit would feel right about now. I could almost feel the sweet sensation rushing through my veins, taking away all my stress and fears. I traced the scars on my arms, remembering the person I used to be. I did not want to become that man again. I was cruel and selfish to everybody around me - except my dealers. 

Wait. 

I paid my dealers a good chunk of money back in the day. If the going rate is what it used to be, this kid will have a college tuition paid for before he even turns eighteen. I sprung out of bed and called a few people until I found who I was looking for. 

“I need money.” I said sharply - even though I was terrified of the man. “What do you need sold?” 

“Oh, so you need something?” The deep voice chuckled. “I don’t mess around with drugs no more, but I could use a hand tonight. In exchange for your help, you’d get a cut of the money.” He offered. 

My mind started churning instantly, I was not expecting a damn job offer tonight. I closed my eyes and saw her face as I dropped her off home tonight. She was so happy we would be keeping the baby, all I want for the rest of my life is to see that girl happy. 

“Where do you want me to meet you?” I asked as my heart rate slowly started to increase. The realization of what I was about to do had just kicked in. 

“25th and Broad. Be there in 45 minutes.” He instructed and then hung up. 

Why the hell does he want to meet at a supermarket? 

Sammy 

The walls felt like they were closing in on me as each second went by. I looked down at the pale, bloody faces that were only a few inches from my feet. I wanted so badly to help them, but the only plan that came to mind was to save myself. I could feel the presence of the man nearby because the air was so tense and the sound of breathing had quieted, which meant everyone was holding their breath for what was about to happen next.  I heard footsteps approaching but I kept my head hung low. He circled around me slowly, stopping abruptly right behind me. 

“ What’s your name?” He asked me as he ran his skinny finger along my spine. I shuddered at his touch as I pulled myself together to speak. 

“Sammy.” I spit it out so fast I wasn’t even sure if he heard what I said. I closed my eyes and looked up at the ceiling silently praying for him to just leave me alone. Suddenly I felt a hand grab my ponytail and yanked me down to the floor. My lower spine collided with the polished concrete floor, sending a pain up and down my back. I cried out in pain just as my head whacked the floor and to my sheer disappointment, I was still conscious. 

“When you address me, you will speak in complete sentences. You understand?” He yelled down to me, sending goosebumps throughout my body. “Now, what is your name?” He asked again in a sing song tone, a demented smile plastered on his face. 

“My name is Sammy, and yours?” 

He looked at me quizzically, not expecting me to strike up a conversation. I came to the realization that if I do get out of here alive, I’m going to need all the information I can get on this man.  I felt somewhat in control now, so I picked myself up to a sitting position. I did my best to mask how much pain I was in while doing so. I propped myself up against the register terminal and looked right up at him waiting for my answer. 

“Z.” 

“Z?” I questioned. “What is that short for?” 

He started pacing the floor and made his way over to the front of the counter, he scanned the front area and locked eyes with Heather. She was laying maybe 2 feet from me, along with a few other employees. They all lifted their heads up by this point to watch what was about to take place. 

“It’s getting a little boring in here, wouldn’t you agree Sammy?” He asked rhetorically. 

During the split second that I had to process his question, I saw his steel toed boot collide with Heather’s face. She screamed out in agony as her nose turned into a faucet of blood. Her mouth was still stuffed with the wash cloth and she was choking on the blood that seeped through. 

“Take it out of her mouth!” I screamed. “She can’t breathe!” I was mentally debating if I should run over to her, but he might hurt her more out of spite. Z looked at me and mocked my words as a child would, then he nodded his head to one of his men as he nonchalantly walked back into the other room. 

Brian

There was so much blood, the stench of it was enough to make me sick to my stomach. This girl was lying face down in a pool of her blood, gagging on the remnants that got into her mouth. 

“Take it out of her mouth!” The girl screamed. She was fierce, which I think Z likes about her. Hell, maybe that’s the one thing keeping her and her friends alive right now. I gotta agree with her though, please let me take this fucking rag out of her mouth before I vomit.

Z looked over at me and nodded for me to remove it. Thank god. 

I knelt down and ripped it out of her mouth, her blood splattered on both of us. The girl started sobbing and grabbed the rag off the floor and held it to her nose. I wiped the blood from my hands onto my pants as I started to walk away.

“What the fuck is wrong with you people,” I turned around to see the feisty girl whispering through her teeth. “Why are you even still here?” 

“Listen, you think I wanna be here?” I spat at her. “I didn’t sign up for all this bullshit. I was here to get the money and to ditch, but Z is making a whole goddamn production out of it.” I didn’t want Z to get suspicious, so I walked back into the room to see what the plan was. The girl watched me leave, I could feel her eyes staring a hole into my back. 

“...we need to get out of here before their families call the cops and report them missing” Murphy angrily whispered, the vein on his forehead popping out ever so slightly. “The store closed an hour ago!”

“ I agree,” the shorter man stated. “Sorry boss, but i’m not going to jail on my first robbery.” He said in a calm manner, but the sweat pooling on his neck said otherwise. 

“Nice of you to join us,” Z said without looking at me. “Having some fun with the girls?” 

“No. In case you didn’t notice there was a lot of blood that I had to deal with.” I snapped. “When the hell are we getting out of here?” 

“Ah come on fellas, isn’t this fun!? We need to make our mark, what fun is it to just take money and leave?” Z boasted. “We gotta make it into the books!” 

None of us were amused by his theatrics. ''')
            elif 'Science-Fiction' in query:
                speak("The Counterparts, By Andrew hansen")
                speak('''They didn't arrive in spaceships, so it was hard to believe they weren't here to stay. They had no ride home, wherever home was. Some theorized Earth was home, that they'd always been here, among us. Somehow those same people kept calling them visitors. Merely visitors. As if saying it might make it true.
You didn't believe they were aliens--that fatigued, unreal word--but you never verbalized this. Didn't need to. When I first told you about them, you held me tight and knew exactly what to say, which was nothing. Maybe you understood what they were and were waiting for the rest of us to figure it out. You tended to know things. Strange things. My things. I once asked what color my thoughts were, and you said cosmic, that a cloud of sparkling nebulae haloed my head. This was a joke, of course, but sometimes I wondered.
"And if they're not aliens?" I asked when I could no longer swallow the idea.
"Aliens or not, it doesn't change what they are," you said.
I could have said no more, but I played along and gave shape to what everyone refused to say.
"They're us."

Encounters increased day by day, so much so the news stopped reporting them. Experts still gave televised talks and scripted interviews, but by then most people had made up their own minds. Anecdotes traveled faster than airwaves. I kept my ear to the ground when I made trips to town for coffee and sugar and other things the woods couldn't provide.
My sister had seen one. It had followed her out of the shower: a lithe, transparent copy of herself likened in water and steam. The floating droplets had composed themselves long enough for her to reach out and touch the fingertips, then forfeited shape and splatted onto the floor. Mike didn't believe her, but I did.
Another had manifested in a billow of bonfire smoke far side of the lumberyard. Duke Harley and Yoshiro's boys were witnesses. Same as my sister's, their visitor had mirrored them, ash and fumes coagulating into the exact contours of their cheeks and jawbones. A bas relief etched in smoke.
You wouldn't have recognized the town. Never quiet anymore. Always whispers. Rumors. Everyone had one. But once folks started uploading videos and the visitors went viral again and again, they were no longer rumors.
Like the Facebook clip of the two dust devils that took on boyish forms and joined a kids' soccer game. That was local. I knew the teacher who filmed it. When I tried showing you the clip, you just shook your head and smiled as though all couldn't be righter in the world. You said the kids didn't seem to mind. Now they had two more players.
You were right. The kiddos didn't mind. No one visited ever minded.

We didn't make love on the roof of the camper anymore. Collapsed in your arms, the glitter of stars and the plum-dark of night used to cloak us, a shield of privacy where the world slipped away and I was lost in you and you in me, but now the Milky Way wasn't so empty and I could never be intimate and vulnerable knowing we weren't alone, that they might be watching.
You didn't get mad. You never got mad. When you came in from the garden and I was busy sewing tomorrow's orders at the table, you unfurled on the couch and laid your head in my lap. I winnowed my fingers through your auburn curls and apologized for everything. You took the blame. It didn't matter if it were the visitors or our finances or appointments with the fertility doctor. You always took the blame. Chewed and swallowed it so I wouldn't have to.

The women and men the government hired to study the visitors talked a big talk about anti-particles and quantum projection. The visitors came from galactic distances so great no technology nor time could span the gulf. They could merely project themselves, like shadows on a wall, hijacking matter and energy from our corner of the cosmos to appear to us in comprehensible forms.
I didn't care for the scientific jargon. You tried explaining anti-particles to me, the theory that all things had a counterpart; for every atom there was another, though invisible, tied by unseen strings and balanced on unseen scales.
"Sounds like God," I said.
You shrugged. You knew.
Add up every atom in my body and there was another me. Another you. Counterparts.
I wanted to meet mine.

When tensions loosened and we felt safe going out, you took me roller skating like you used to when we first dated. Then like now, you braced to catch me before I fell, even before I tottered. Somehow you knew my imbalance before I did. I once thought this an excuse to put your hands on my hips. Maybe it was.
We were the only adults skating. The rest were teenagers. Kids with their friends and dates, but some came with their counterparts. These donned bodies of water or of mud and peat or leaf bits. Earthier bodies. These became more common. More tangible. They could emote. One day they might even speak.
If they could sing, I hoped they sang like angels.

I showered alone most evenings now. You didn't ask why. You probably already knew. I would run the water and steam the bathroom until I floated in a warm cloud. Breaths came thick and cozy, a coaxing pressure on my chest. I kept waiting for my likeness to materialize in the swirling moisture, for my counterpart to take shape, to crawl out of hiding. I was ready for her. The ancient Greek priestesses had done this--scaled mountaintops to conjure the Oracle out of the fog. I had tried meditating outside when you were away, inviting her to mimic a body from the dust of the earth, but she wouldn't have me.
Again, I wiped steam off the mirror and cried.
You couldn't take the blame this time.

The visitors lived up to their name. Just four months into visitation and they had permeated society, but already they were fading like snow out of season. Some hung around, vague apparitions of mist and shadow and wishful thinking. Others melted into heaps and scraps. Snowmen in late spring. The realest ones--those of bone and blood--stuck around longer, but they too retreated little by little into the unseen.
Folks sought therapists and hallucinogenics in their counterparts' absence, vying to fill a hole in themselves they had never named until recently. The news did a segment on this new mental health crisis. We didn't watch it.
I stopped asking if yours had appeared to you. I wouldn't get mad or jealous. I would be happy for you.
"What color are my thoughts now?" I asked on the last night of visitation. I knelt behind you, there in your garden, wiggled my fingers between yours, and pressed my forehead into your shoulder, as if to assure you were still solid, still here. "Are you going to fade away too?"
You didn't act surprised that I had figured it out. You knew. You had always known.
"Not if you'll keep me."
I smiled into your shoulder and saved my breath. We sat in your garden, holding each other, drinking unspoken words. If you were going to fade away, you'd have to take me with you.''')
            
            

        




                



            

