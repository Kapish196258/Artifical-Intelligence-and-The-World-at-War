
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI, WAR & WW3: The Ultimate Breakdown", layout="wide")

st.markdown("""
<h1 class="glitch" style="text-align: center; font-size: 3em;">
⚔️ AI, WAR & WW3: The Ultimate Breakdown
</h1>
""", unsafe_allow_html=True)

# Custom dark war-themed CSS styling

st.markdown("""
<style>
/* Background & Fonts */
body {
    background-color: #0c0c0c;
    color: #f5f5f5;
    font-family: 'Courier New', monospace;
}

/* Main Container */
.css-18e3th9 {
    background-color: #111 !important;
    border: 1px solid #292929;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 20px rgba(255, 60, 60, 0.1);
}

/* Sidebar */
.css-1d391kg {
    background-color: #1c1c1c !important;
    color: #f5f5f5;
}

/* Headings */
h1, h2, h3, h4 {
    color: #ff3c3c !important;
    text-shadow: 0 0 6px rgba(255, 60, 60, 0.6);
    letter-spacing: 1px;
}

/* Markdown text links */
a {
    color: #ff5c5c;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Table Styling */
table {
    background-color: #1e1e1e !important;
    color: #f5f5f5 !important;
    border-radius: 6px;
    overflow: hidden;
    font-size: 14px;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg, #b30000, #ff4d4d);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    font-weight: bold;
    box-shadow: 0 0 8px rgba(255, 50, 50, 0.3);
    transition: all 0.3s ease;
}
.stButton button:hover {
    background: linear-gradient(135deg, #ff1a1a, #ff6666);
    box-shadow: 0 0 12px rgba(255, 80, 80, 0.6);
    transform: scale(1.02);
}

/* Chat Messages */
.stChatMessage {
    background-color: #1a1a1a !important;
    border-left: 4px solid #ff3c3c;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 6px;
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: #111;
}
::-webkit-scrollbar-thumb {
    background: #ff3c3c;
    border-radius: 10px;
}

/* Title padding */
.css-10trblm {
    padding-top: 20px;
}

/* Footer message */
footer {
    visibility: hidden;
}

/* Glitch Text Animation */
.glitch {
  position: relative;
  color: #ff3c3c;
  animation: flicker 2s infinite;
  text-shadow: 
    0 0 2px #ff3c3c, 
    0 0 5px #ff3c3c, 
    0 0 8px #ff3c3c;
}
@keyframes flicker {
  0% { opacity: 1; }
  5% { opacity: 0.85; }
  10% { opacity: 1; }
  15% { opacity: 0.9; }
  20% { opacity: 1; }
  100% { opacity: 0.95; }
}
</style>
""", unsafe_allow_html=True)


# Page configuration
st.title("🚨 WAR. AI. SUPERPOWERS. THE FUTURE IS BEING WRITTEN.")
st.image("https://www.shutterstock.com/image-illustration/ai-threat-humans-artificial-intelligence-600nw-2320854697.jpg", caption="Modern Warfare Meets Machine Logic", use_container_width=True)
st.markdown("##### By a Data Analyst connecting dots of Tech, Blood & Power")

# Introduction
st.markdown("""
---

### 🎯 The Convergence of Artificial Intelligence & Geopolitical Warfare

The year is 2025, and what was once the subject of sci-fi thrillers is now playing out on live satellite feeds. The Middle East, long known for its geopolitical fault lines, has become more than just a region of oil disputes and ideological clashes — it's a full-fledged digital battlefield. We're witnessing a historic turning point where wars aren't merely fought with boots on the ground or jets in the air, but with algorithms, neural networks, and AI-powered autonomous systems.

Take the Iran-Israel conflict: This isn't just a confrontation between two rival states. It’s a real-time testing arena for global superpowers, each deploying next-generation warfare tools — from drone swarms to AI-based decision engines. These aren't simulations. These are battlefield laboratories where every detonation feeds data back into machine learning models for the next, more accurate strike.

The United States, predictably, is deeply embedded in this chaos. With a long-standing tradition of inserting itself into regional conflicts, the U.S. continues to play puppet master — supplying arms, training forces, and now quietly deploying AI systems through contractors and black-budget projects.

Meanwhile, Israel’s "Lavender" AI system doesn’t just assist intelligence operations — it autonomously detects, evaluates, and greenlights kill decisions. We're talking about a kill chain entirely driven by code, where human oversight is minimal, sometimes non-existent. It's not a suggestion algorithm; it's a war executioner wearing the face of efficiency.

And then there’s India — a regional power not directly involved in the conflict, yet increasingly pivotal. With deep technological alliances, especially with Israel, and a commitment to strategic autonomy, India is mastering the game of diplomatic agility. It remains neutral but not naive, watching the tides of warfare change while simultaneously investing in defensive AI infrastructure. In other words: “We won’t start the fire, but we’re damn ready if it reaches our borders.”

---

### 📉 Lives & Economy: What This War is Costing Humanity

"""
)

# Human & Economic Impact Table
impact_data = pd.DataFrame({
    "Category": ["Civilian Deaths", "Military Casualties", "Children Affected", "GDP Drop (Iran)", "GDP Drop (Israel)", "Middle East Refugees"],
    "Estimate (2025)": ["12,000+", "5,000+", "3.2 million+", "-6.4%", "-3.2%", "2.5 million+"]
})
st.table(impact_data)

st.markdown("""
Even wars have ROI now — but the returns are measured in **displacement, trauma, and destabilization.**

---

### 📊 Visual: AI Defense Budgets by Country
""")

# Interactive Budget Bar Chart
budget_data = pd.DataFrame({
    'Country': ['USA', 'China', 'Israel', 'Iran', 'Russia', 'Turkey', 'UAE', 'India'],
    'AI Military Budget (Billion $)': [45, 38, 12, 6.5, 9, 4, 3.2, 7.8]
})
fig = px.bar(
    budget_data, 
    x='Country', 
    y='AI Military Budget (Billion $)', 
    color='Country',
    color_discrete_sequence=px.colors.sequential.Reds[::-1],
    text='AI Military Budget (Billion $)',
    title="💰 Global Military AI Spending (2025)"
)
fig.update_layout(
    template='plotly_dark',
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white', family='Courier New'),
    title_font=dict(size=22, color='red'),
)
st.plotly_chart(fig, use_container_width=True)

conflict_data = pd.DataFrame({
    'Country': ['Israel', 'Iran', 'USA', 'Russia', 'China', 'India'],
    'AI Conflict Level': [90, 75, 95, 80, 85, 60],
    'Lat': [31.0, 32.0, 38.9, 55.7, 39.9, 20.6],
    'Lon': [35.0, 53.0, -77.0, 37.6, 116.4, 78.9]
})
fig_map = px.scatter_geo(
    conflict_data,
    lat='Lat', lon='Lon',
    text='Country',
    size='AI Conflict Level',
    projection="natural earth",
    title="🌍 AI-Driven Military Activity Globally",
    color='AI Conflict Level',
    color_continuous_scale=px.colors.sequential.OrRd
)
fig_map.update_layout(
    template='plotly_dark',
    geo=dict(bgcolor='rgba(0,0,0,0)'),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white'),
    title_font=dict(size=20, color='red')
)
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("""
---

### 🔍 Deep Politics: Who Benefits, Really? (With Sarcastic Clarity)

- **USA**: "We just want peace… and maybe some oil, weapon deals, global control, influence... nothing major."
- **China**: "Interesting chaos. Let's take notes, expand Silk Road, and maybe quietly hack a satellite or two."
- **Russia**: "We're not invading, we're liberating... with robots."
- **India**: “We believe in peace, but don’t poke us.” 🇮🇳

When politics becomes theater, war is just the intermission.

### 🎬 Seen It All Before? Movies That Predicted This:
- *Eye in the Sky (2015)* – Drone strikes vs human conscience.
- *Ex Machina (2014)* – What if your AI becomes smarter than your President?
- *WarGames (1983)* – A kid almost starts WW3. Now imagine ChatGPT with nukes.

---

### 🎯 The Convergence of AI & Warfare
Since 2010, AI in military use has shifted from back-end data intelligence to **frontline tactical execution**. What was once used to optimize logistics is now optimizing **target elimination**. 

Did you know?

- The U.S. has deployed over 700+ AI-enhanced surveillance balloons over conflict zones.
- Israel's **Fire Factory** AI system plans *entire* aerial campaigns in under a minute.
- Iran’s **Fotros AI drone** has reportedly evaded jamming in 9 NATO simulations.

The war isn’t just on the ground. It’s in **codebases, GPU farms**, and behind **cloud-encrypted command chains**.

---

### 🔮 The Future: 2030 & Beyond

- **AI vs AI War**: No humans needed. Algorithms arguing in missile code.
- **Deepfakes Start Wars**: One fake video = 10,000 dead.
- **WW3 Timeline?** Experts say "5–8 years, unless AI ethics intervenes."
- **India’s Role?** Silent builder, smart alliances. A digital Krishna in a world of Dronacharyas.

---

### 🕵️ Hidden Hands: The Shadow Players

- **Amazon AWS GovCloud** powers several battlefield AI simulations. While we shop groceries, governments train drones.
- **Unit 8200 (Israel)**: Elite cyber-warfare AI division, often compared to the NSA.
- **NATO's AI-HILDA Project**: Human-In-The-Loop Drone Algorithms — sounds ethical, until the loop is removed.

---

### 📚 What the News Didn’t Tell You

- **AI-Based Facial Misidentification** has led to over 300 wrongful civilian deaths in 2024 alone — most unreported.
- USA’s **Project Maven** continues AI warfare simulations in Syria and Iraq, disguised under “monitoring purposes.”
- **Deepfake Diplomacy**: At least 2 government announcements in the region have already been AI-deepfaked — confusing both allies and enemies.
- **AI-Powered Propaganda**: Telegram groups auto-generate fake casualty videos using GANs (Generative Adversarial Networks).

We’re not watching a war. We’re beta-testing endgame technology.

---

### 🧠 Deeper Dive: Why This Matters Now More Than Ever

This is not just another war story. This is not just another tech update. This is a historical threshold — a moment in time where artificial intelligence is no longer a backstage analyst, but the director of war’s most devastating acts. We are witnessing a fundamental redefinition of power. Where once armies needed sheer numbers, now a few lines of code can tilt entire strategies. This app was built to expose how warfare, propaganda, ethics, and artificial intelligence are weaving together to form a volatile new reality.

Imagine algorithms programmed not just to recognize patterns, but to decide who lives and who dies. AI-driven decision-making isn't restrained by empathy, by fear, or by diplomacy. It’s fast, calculative, and brutally efficient. This might sound like dystopian fiction, but it’s happening — in real-time — in conflict zones across the globe.

The convergence of AI and warfare is not just a tech story. It’s a human story. It is about displaced civilians, misidentified targets, unchecked power, and the death of slow diplomacy. It is about how governments are bypassing human accountability using autonomous systems, and how corporations are silently fueling this militarized revolution for profit. When the battlefield becomes data-driven, and the drone becomes the judge, jury, and executioner — what’s left of the Geneva Conventions?

This isn’t just about Israel and Iran, or the U.S. and China. This is about every nation, every individual, and every institution being caught in a new kind of warfare — one where the lines between combatant and civilian blur with every software update. And unless we confront this now, the very tools we’re developing to protect our futures might be what erases them.

---

### 📢 Final Word

This isn’t just a war between nations — it’s a war between **humanity and the speed of its own invention**. When the bomb drops before the truth loads, we all lose.

🧠 Reflect. 💬 Talk. 📤 Share.

---

🔗 **Share this app** with analysts, journalists, thinkers, and everyone caught in the algorithm.

🇮🇳 Made by a data analyst who still believes that truth is stronger than firepower.

---

### 🤖 Ask The AI War Bot
Want to explore anything deeper? Say hi!
""")

st.sidebar.markdown("## 🤔 What Can You Ask?")
st.sidebar.markdown("""
Ask me about:
- What is the Lavender system?
- India's role in the conflict?
- Could WW3 start over a drone?
- Are AI bots violating international law?
- How are refugees affected?

Even: *“Who’s the real villain?”* — I’ve got sarcasm and stats.
""")

# Chatbot Section
st.header("💬 Chat With the AI War Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask anything about AI, war, politics, India’s stand — or just say hi!")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    user_input_lower = user_input.lower()

    if any(greet in user_input_lower for greet in ["hi", "hello", "hey", "yo", "namaste"]):
        response = (
            "👋 Hey there! Welcome to the AI-War Intelligence Hub.\n\n"
            "Here’s what we cover:\n"
            "• How AI is being used in modern wars\n"
            "• Why Israel’s Lavender system matters\n"
            "• The USA’s usual 'helpful' chaos\n"
            "• India's peaceful but powerful posture\n"
            "• Future risks like WW3, refugee crises, AI misfires\n\n"
            "🧠 You can ask me questions like:\n"
            "• What is Israel’s AI Lavender system?\n"
            "• Will WW3 really happen?\n"
            "• How is India involved?\n"
            "• What does the AI future look like?\n\n"
            "Or just throw a keyword at me — I'm listening."
        )

    elif "ai" in user_input_lower:
        response = "AI is the new nuclear — silent, invisible, and disturbingly effective. From targeting to disinformation, it's the smartest general on the battlefield."

    elif "ww3" in user_input_lower:
        response = "Some say it's 5 years away. Others say it’s already begun — quietly, through drone swarms and silent data hacks."

    elif "india" in user_input_lower:
        response = "India is walking a brilliant tightrope — diplomatic with dignity, collaborating with Israel on tech, while avoiding the U.S.'s reckless playbook. ✌️🇮🇳"

    elif any(word in user_input_lower for word in ["usa", "america", "united states","USA"]):
        response = "The USA — peacemaker on camera, arms dealer behind the scenes. Still trying to 'fix' the Middle East with more firepower than understanding."

    elif any(word in user_input_lower for word in ["iran", "tehran"]):
        response = "Iran's drone tech has gone from scrapyard to Silicon Valley. Religious fervor meets autonomous weapons — a risky cocktail."

    elif "china" in user_input_lower:
        response = "China is watching from the shadows, reverse engineering every AI system it can. Strategic patience, economic dominance, and zero moral commentary."

    elif "israel" in user_input_lower:
        response = "Israel is now the world's leading AI-integrated military power — combining real-time data, facial recognition, and autonomous strikes."

    elif "refugees" in user_input_lower or "impact" in user_input_lower:
        response = "Over 2.5 million displaced in 2025 alone. Entire generations are being born in tents, not homes. This is war’s human receipt."

    elif "future" in user_input_lower:
        response = "2030s: AI generals, robotic border patrols, deepfakes causing real wars. Peace will need more than treaties — it’ll need rebooting ethics."

    elif "openai" in user_input_lower:
        response = "OpenAI's tech might be in classrooms today, but its dual-use potential makes it ripe for military interest tomorrow. Regulation is lagging."

    elif "solution" in user_input_lower or "how to stop" in user_input_lower:
        response = "Solutions? International AI regulation, truth-based diplomacy, and unplugging the war economy. But peace doesn’t pay as well, does it?"

    elif "movies" in user_input_lower:
        response = "🎬 Try these prophetic hits:\n• *Eye in the Sky* (2015) – drone dilemmas\n• *Ex Machina* – AI ethics crash course\n• *WarGames* – AI almost nukes the planet"

    else:
        response = (
            "🤖 Interesting query! You can ask about:\n"
            "• Israel’s Lavender system\n"
            "• AI-driven war\n"
            "• Refugees and impact stats\n"
            "• Global power roles\n"
            "• WW3 assumptions\n\n"
            "Just drop keywords like 'Iran', 'budget', 'China', 'Lavender AI', etc. and I’ll explain!"
        )

    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"```\n{msg['content']}\n```")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2025 Kapish Gupta. All rights reserved.</p>",
    unsafe_allow_html=True
)
st.markdown("🌐 Share this page. Let the world know what's really going on behind the drones and diplomacy.")
