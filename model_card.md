# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Find Your Tunes

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

---

## Appendix: Edge-Case Profile Outputs

The five most revealing adversarial profiles, run through `recommend_songs` (k=5) and printed with the CLI's `print_recommendations`.

### 1. High-energy sad

Genre + mood (3.0 pts) outweigh energy (max 1.5), so a 0.40-energy song wins for a user who asked for 0.90.

```text
============================================================
  Top 5 Recommendations
  Profile: genre=blues, mood=sad, energy=0.9
============================================================

1. Empty Station Blues by Hank Delaney
   Score: 3.75
   Why:
     - genre matches blues (+2.0)
     - mood matches sad (+1.0)
     - energy 0.40 vs target 0.90 (+0.75)

2. Dusty Backroads by Carter Hollow
   Score: 2.52
   Why:
     - country is similar to blues (+1.0)
     - nostalgic mood is similar to sad (+0.5)
     - energy 0.58 vs target 0.90 (+1.02)

3. Night Drive Loop by Neon Echo
   Score: 1.77
   Why:
     - moody mood is similar to sad (+0.5)
     - energy 0.75 vs target 0.90 (+1.27)

4. Pine Cabin Letters by Willow & Wren
   Score: 1.60
   Why:
     - folk is similar to blues (+1.0)
     - energy 0.30 vs target 0.90 (+0.60)

5. Storm Runner by Voltline
   Score: 1.48
   Why:
     - energy 0.91 vs target 0.90 (+1.48)

============================================================
```

### 2. Sad pop

Genre (2.0) outweighs mood (1.0), so a sad listener gets happy and intense pop songs at the top.

```text
============================================================
  Top 5 Recommendations
  Profile: genre=pop, mood=sad, energy=0.8
============================================================

1. Sunrise City by Neon Echo
   Score: 3.47
   Why:
     - genre matches pop (+2.0)
     - energy 0.82 vs target 0.80 (+1.47)

2. Gym Hero by Max Pulse
   Score: 3.30
   Why:
     - genre matches pop (+2.0)
     - energy 0.93 vs target 0.80 (+1.30)

3. Night Drive Loop by Neon Echo
   Score: 2.92
   Why:
     - synthwave is similar to pop (+1.0)
     - moody mood is similar to sad (+0.5)
     - energy 0.75 vs target 0.80 (+1.42)

4. Rooftop Lights by Indigo Parade
   Score: 2.44
   Why:
     - indie pop is similar to pop (+1.0)
     - energy 0.76 vs target 0.80 (+1.44)

5. Laser Cathedral by Pulse Vector
   Score: 2.28
   Why:
     - edm is similar to pop (+1.0)
     - energy 0.95 vs target 0.80 (+1.28)

============================================================
```

### 3. Conflicting tastes (metal + peaceful + acoustic)

A genre match alone puts Iron Tempest (angry, 0.97 energy, not acoustic) at #2, the opposite of every other preference.

```text
============================================================
  Top 5 Recommendations
  Profile: genre=metal, mood=peaceful, energy=0.2, likes_acoustic=True
============================================================

1. Pine Cabin Letters by Willow & Wren
   Score: 2.81
   Why:
     - mood matches peaceful (+1.0)
     - energy 0.30 vs target 0.20 (+1.35)
     - acousticness 0.93 (+0.47)

2. Iron Tempest by Graveforge
   Score: 2.36
   Why:
     - genre matches metal (+2.0)
     - energy 0.97 vs target 0.20 (+0.34)
     - acousticness 0.03 (+0.01)

3. Spacewalk Thoughts by Orbit Bloom
   Score: 2.34
   Why:
     - chill mood is similar to peaceful (+0.5)
     - energy 0.28 vs target 0.20 (+1.38)
     - acousticness 0.92 (+0.46)

4. Library Rain by Paper Lanterns
   Score: 2.21
   Why:
     - chill mood is similar to peaceful (+0.5)
     - energy 0.35 vs target 0.20 (+1.28)
     - acousticness 0.86 (+0.43)

5. Coffee Shop Stories by Slow Stereo
   Score: 2.19
   Why:
     - relaxed mood is similar to peaceful (+0.5)
     - energy 0.37 vs target 0.20 (+1.25)
     - acousticness 0.89 (+0.45)

============================================================
```

### 4. Acoustic-loving EDM

The acoustic preference is worth at most 0.5 points, so it is effectively ignored: the top pick has acousticness 0.02.

```text
============================================================
  Top 5 Recommendations
  Profile: genre=edm, mood=euphoric, energy=0.95, likes_acoustic=True
============================================================

1. Laser Cathedral by Pulse Vector
   Score: 4.51
   Why:
     - genre matches edm (+2.0)
     - mood matches euphoric (+1.0)
     - energy 0.95 vs target 0.95 (+1.50)
     - acousticness 0.02 (+0.01)

2. Sunrise City by Neon Echo
   Score: 2.89
   Why:
     - pop is similar to edm (+1.0)
     - happy mood is similar to euphoric (+0.5)
     - energy 0.82 vs target 0.95 (+1.30)
     - acousticness 0.18 (+0.09)

3. Rooftop Lights by Indigo Parade
   Score: 2.89
   Why:
     - indie pop is similar to edm (+1.0)
     - happy mood is similar to euphoric (+0.5)
     - energy 0.76 vs target 0.95 (+1.22)
     - acousticness 0.35 (+0.17)

4. Gym Hero by Max Pulse
   Score: 2.50
   Why:
     - pop is similar to edm (+1.0)
     - energy 0.93 vs target 0.95 (+1.47)
     - acousticness 0.05 (+0.03)

5. Night Drive Loop by Neon Echo
   Score: 2.31
   Why:
     - synthwave is similar to edm (+1.0)
     - energy 0.75 vs target 0.95 (+1.20)
     - acousticness 0.22 (+0.11)

============================================================
```

### 5. Energy above range

Energy is never validated to 0–1, so every score goes negative and the explanation prints `+-5.37`.

```text
============================================================
  Top 5 Recommendations
  Profile: genre=lofi, mood=chill, energy=5.0
============================================================

1. Midnight Coding by LoRoom
   Score: -2.37
   Why:
     - genre matches lofi (+2.0)
     - mood matches chill (+1.0)
     - energy 0.42 vs target 5.00 (+-5.37)

2. Library Rain by Paper Lanterns
   Score: -2.48
   Why:
     - genre matches lofi (+2.0)
     - mood matches chill (+1.0)
     - energy 0.35 vs target 5.00 (+-5.48)

3. Focus Flow by LoRoom
   Score: -2.90
   Why:
     - genre matches lofi (+2.0)
     - focused mood is similar to chill (+0.5)
     - energy 0.40 vs target 5.00 (+-5.40)

4. Spacewalk Thoughts by Orbit Bloom
   Score: -3.58
   Why:
     - ambient is similar to lofi (+1.0)
     - mood matches chill (+1.0)
     - energy 0.28 vs target 5.00 (+-5.58)

5. Coffee Shop Stories by Slow Stereo
   Score: -3.95
   Why:
     - jazz is similar to lofi (+1.0)
     - relaxed mood is similar to chill (+0.5)
     - energy 0.37 vs target 5.00 (+-5.45)

============================================================
```
