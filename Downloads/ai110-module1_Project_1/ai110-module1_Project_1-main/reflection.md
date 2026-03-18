# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? You have to enter what you think the number is and you have 8 attempts on the normal mode.
- List at least two concrete bugs you noticed at the start  
The hints were the opposite of what they were supposed to be, for example if the number was supposed to be 30 and I typed in 31 it would say go higher.
When I tried to restart the game withe the "new game" button it would restart the game with new attempts and a new number to guess but everytime I type in a new number in the new game the attempt count wouldn't go down and the hint section would say "Game over. Start a new game to try again." and wouldn't show any new hints.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). When it told me to put the fixes of thr 4 defined varables into logi_utils.py instead of app.py.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It made me fix the 4 def variables inside of app.py and put them inside the logic file.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I made revisions then launched the app.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I tested the "Higher" and "Lower" feature and I also tested the scoring feature
- Did AI help you design or understand any tests? How? It didn't help me design the tests because I already knew what I was looking for in terms of errors.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
