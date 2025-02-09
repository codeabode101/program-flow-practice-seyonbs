# **🌟 Monday: Tavern Beginnings**  
**Prompt:**  
Create your tavern adventurer!  
1. Use `input()` for:  
   - Hero's name: `"What's your warrior's name? "`  
   - Starting town: `"Where does your adventure begin? (Misty Vale/Stonehaven) "`  
   - Store health as 100  

2. Print using f-string:  
   `⚔️ [Name] enters [Town] Tavern, ready for adventure!`  

3. Use `if` to check health:  
   - If 100: `✨ [Name] is at full health! Let's roll dice!`  
   - Else: `🧪 [Name] should visit the alchemist first!`

---

# **🌳 Tuesday: Forest Encounter**  
**Prompt:**  
You explore the Whispering Woods!  
1. Use `input()` for:  
   `"What do you see? (owl/troll/fairy) "`  

2. Use `if`/`elif`/`else`:  
   - Owl: `🦉 [Name] gets wise advice! Health +10`  
   - Troll: `👹 ROAR! [Name] loses 25 health!`  
   - Fairy: `🧚 [Name] dances with fairies! Health +20`  

3. Print using f-string:  
   `[Name]'s current health: [health]`

---

# **🧌 Wednesday: Bridge Showdown**  
**Prompt:**  
A bridge collapses over rapids!  
1. Use `input()`:  
   `"Swim across or climb rocks? (swim/climb) "`  

2. Use `if`/`elif`:  
   - Swim: `🌊 Cold water! -30 HP | Remaining: [health]`  
   - Climb: `🧗 Risky climb! -15 HP | Remaining: [health]`  

3. Use `and` to check if health is less than or equal to 30 **AND** greater than 0:  
   `🚨 WARNING: [Name] is shaking with fatigue!`

---

# **🏺 Thursday: Ancient Temple**  
**Prompt:**  
You find a glowing artifact!  
1. Use `input()`:  
   `"Touch it or leave it? "`  

2. Use `if`/`else`:  
   - Touch: `💥 CURSED! [Name] loses 40 health!`  
   - Leave: `🔮 Wise choice! Find healing spring +25 HP`  

3. Use `or` to check if health is greater than 80 **OR** choice was "leave":  
   `✨ Mystical energy surrounds you!`

---

# **🎪 Friday: Festival Finale**  
**Prompt:**  
Return to town for the harvest festival!  
1. Use `if`/`else`:  
   - If health is greater than or equal to 60: `🎉 [Name] leads the parade! Crowd cheers!`  
   - Else: `🩹 [Name] rests at healers' tent`  

2. Print using f-string:  
   `Final Health: [health] | Fame: [fame_level]`  

3. Check if town is "Misty Vale" **AND** health is greater than 50:  
   `🏆 Local hero achievement unlocked!`

**Next Steps:**  
Add more input choices! What if:  
- Player can choose weapon type?  
- Add tavern minigames with dice rolls?  
- Let players name their pet companion?  
