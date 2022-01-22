import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
import wolframalpha
import time
import subprocess
import random
import googletrans
from tkinter import *
from tkinter import ttk,messagebox
import textblob
import randfacts
from gtts import gTTS
from stemsim import *
from testing2 import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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

    speak("I am Assista! Your Educational and Therapist Bot!. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

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



        if 'simulation' in query:
            speak('Opening simulation...')
            time.sleep(1)
            simulate()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

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
            
            

        '''elif 'translator' in query:
            root = Tk()
            root.title('Assistas translator')
            root.iconbitmap(r'C:\Users\Sahil\Downloads\LOGO.png')
            root.geometry("880x300")


            def translate_it():
                # Delete Any Previous Translations
                translated_text.delete(1.0, END)
                try:
                    # Get Languages From Dictionary Keys
                    # Get the From Langauage Key
                    for key, value in languages.items():
                        if (value == original_combo.get()):
                            from_language_key = key

                        # Get the To Language Key
                        for key, value in languages.items():
                            if (value == translated_combo.get()):
                                to_language_key = key

                        # Turn Original Text into a TextBlob
                        words = textblob.TextBlob(original_text.get(1.0, END))

                        # Translate Text
                        words = words.translate(from_lang=from_language_key , to=to_language_key)

                        # Output translated text to screen
                        translated_text.insert(1.0, words)


                except Exception as e:
                    messagebox.showerror("Translator", e)





                    def clear():
                        # Clear the text boxes
                        original_text.delete(1.0, END)
                        translated_text.delete(1.0, END)

                        #language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)
                        # Grab Language List From GoogleTrans
                        languages = googletrans.LANGUAGES

                        # Convert to list
                        language_list = list(languages.values())



                        # Text Boxes
                        original_text = Text(root, height=10, width=40)
                        original_text.grid(row=0, column=0, pady=20, padx=10)

                        translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
                        translate_button.grid(row=0, column=1, padx=10)


                        translated_text = Text(root, height=10, width=40)
                        translated_text.grid(row=0, column=2, pady=20, padx=10)

                        # Combo boxes
                        original_combo = ttk.Combobox(root, width=50, value=language_list)
                        original_combo.current(21)
                        original_combo.grid(row=1, column=0)


                        translated_combo = ttk.Combobox(root, width=50, value=language_list)
                        translated_combo.current(26)
                        translated_combo.grid(row=1, column=2)

                        # Clear button
                        clear_button = Button(root, text="Clear", command=clear)
                        clear_button.grid(row=2, column=1)

                        root.mainloop()'''
        if 'translator' in query:
            translator()

            





                



            

