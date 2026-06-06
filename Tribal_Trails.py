import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 1. PAGE SETUP & HELPERS ---
st.set_page_config(page_title="Tribal Trails", page_icon="🌿", layout="wide")

def b64(path):
    """Converts a file to base64 so it can be embedded directly into HTML."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

# --- 2. FILE LOADING (BULLETPROOF METHOD) ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

logo_b64 = b64(os.path.join(CURRENT_DIR, "logo.jpg"))
if not logo_b64:
    st.warning(f"⚠️ Could not find 'logo.jpg' in: {CURRENT_DIR}")

video_b64 = ""
for ext in ["mp4", "MP4", "mov", "MOV", "webm"]:
    p = os.path.join(CURRENT_DIR, f"hero.{ext}")
    if os.path.exists(p):
        video_b64 = b64(p)
        break
if not video_b64:
    st.warning(f"⚠️ Could not find a hero video in: {CURRENT_DIR}")
    
# --- HANUR VIDEO LOADING ---
hanur_b64 = ""
for ext in ["mp4", "MP4", "mov", "MOV", "webm"]:
    p = os.path.join(CURRENT_DIR, f"hanur.{ext}")
    if os.path.exists(p):
        hanur_b64 = b64(p)
        break
if not hanur_b64:
    st.warning(f"⚠️ Could not find a 'hanur' video in: {CURRENT_DIR}")

# --- IMAGE LOADING LOGIC ---
gallery = ""
gallery_dir = os.path.join(CURRENT_DIR, "gallery")

if os.path.exists(gallery_dir):
    for f in sorted(os.listdir(gallery_dir)):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            img_path = os.path.join(gallery_dir, f)
            img_b64 = b64(img_path)
            if img_b64:
                # Notice the class="slide" added here!
                gallery += f'<img class="slide" src="data:image/jpeg;base64,{img_b64}">'
else:
    st.warning(f"⚠️ Could not find a 'gallery' folder in: {CURRENT_DIR}")

# --- QR CODE LOADING ---
# Place this near the top of your Python script with the other file loaders
qr_b64 = ""
for ext in ["jpg", "jpeg", "png"]:
    p = os.path.join(CURRENT_DIR, f"qr.{ext}")
    if os.path.exists(p):
        qr_b64 = b64(p)
        break
if not qr_b64:
    st.warning(f"⚠️ Could not find a 'qr' image in: {CURRENT_DIR}")
    

# --- 3. COMPONENT: HEADER ---
header_css = """

.header {
    position: fixed;
    top: 0; 
    left: 0; 
    width: 100%;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    display: flex; 
    align-items: center;
    padding: 12px 5%; 
    z-index: 1000; 
    box-sizing: border-box;
}

.header img {
    height: 80px; 
    width: auto; 
    margin-right: 10px;
    margin-left:-55px;
    border-radius: 4px; 
}
.brand-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.brand-name {
    font-size: 48px; 
    color: #0B4F3A; 
    font-weight: 700; 
    font-family: 'Playfair Display', serif;
    margin: 0; 
    letter-spacing: 1.5px; 
    line-height: 1.1;
    margin-left:20px;
    
}
.brand-tagline {
    font-size: 20px;
    font-family: 'Lora', serif;
    color: #B58A42;
    margin: 2px 0 0 0;
    margin-left:53px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}
"""

header_html = f"""
<div class="header">
    <img src="data:image/jpeg;base64,{logo_b64}" alt="Tribal Trails Logo">
    <div class="brand-container">
        <p class="brand-name">TRIBAL TRAILS</p>
        <p class="brand-tagline">The Call of the Forest</p>
    </div>
</div>
"""


# --- 4. COMPONENT: HERO ---
hero_css = """
.hero {
    height: 15vh; 
    position: relative; 
    margin-top: 80px; /* Pushes hero below the fixed header */
    overflow: hidden; 
}
.hero video {
    width: 100%; 
    height: 100%; 
    object-fit: cover; 
}
.overlay {
    position: absolute; 
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7));
    display: flex; 
    flex-direction: column; 
    justify-content: center;
    align-items: center; 
    color: white; 
    text-align: center; 
    padding: 0 20px;
}
.overlay h1 {
    font-size: clamp(20px, 5vw, 56px); 
    font-weight: 700; 
    font-family: 'Lora', serif;
    text-transform: uppercase; 
    letter-spacing: 2px; 
    text-shadow: 2px 4px 8px rgba(0,0,0,0.5); 
    margin: 0;
}
.overlay p {
    font-size: clamp(18px, 3vw, 26px); 
    font-weight: 300; 
    font-family: 'Inter', sans-serif;
    margin-top: 15px; 
    max-width: 800px; 
    text-shadow: 1px 2px 4px rgba(0,0,0,0.5); 
}
"""

hero_html = f"""
<div class="hero">
    <video autoplay muted loop playsinline>
        <source src="data:video/mp4;base64,{video_b64}">
    </video>
    <div class="overlay">
        <h1>CULTIVATE YOUR LEGACY</h1>
        <p>A Premium, Self-Sustaining Agroforestry Investment.</p>
    </div>
</div>
"""
intro_css="""
.intro-section {
    padding: 100px 10%;
    background-color: #082f23; /* Premium Dark Green Background */
    text-align: center;
}
.intro-title {
    font-size: 42px;
    color: #FFFFFF; /* Changed to white for contrast */
    font-family: 'Lora', serif;
    margin-bottom: 25px;
}
.intro-text {
    font-size: 20px;
    line-height: 1.8;
    color: #E0E0E0; /* Soft light gray for readability */
    font-family: 'Inter', sans-serif;
    max-width: 900px;
    margin: 0 auto 60px auto;
}
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
}
.stat-card {
    background: rgba(255, 255, 255, 0.05); /* Sleek glass/translucent effect */
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 40px 20px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
    border-bottom: 4px solid #B58A42; /* Gold accent */
}
.stat-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.08); /* Slightly brighter on hover */
}
.stat-card h2 {
    color: #B58A42; /* Gold numbers to pop against the dark green */
    font-size: 48px;
    font-family: 'Lora', serif;
    margin-bottom: 10px;
}
.stat-card p {
    font-size: 16px;
    color: #FFFFFF;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 0;
}

/* Mobile Responsiveness for Intro */
@media (max-width: 900px) {
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .stats-grid { grid-template-columns: 1fr; }
    .intro-section { padding: 60px 5%; }
    .intro-title { font-size: 32px; }
}
"""

intro_html=f"""
<div class="intro-section">
    <h2 class="intro-title">Where Nature, Science & Value Grow Together</h2>
    <p class="intro-text">
        Step into a self-sustaining green sanctuary. Every sapling, water channel, and crop at Tribal Trails is strategically positioned using advanced agroforestry science. We are restoring biodiversity, enriching soil health, and building a living ecosystem that thrives for generations.
    </p>
    <div class="stats-grid">
        <div class="stat-card">
            <h2>15+</h2>
            <p>Native Species</p>
        </div>
        <div class="stat-card">
            <h2>5K+</h2>
            <p>Thriving Trees</p>
        </div>
        <div class="stat-card">
            <h2>100%</h2>
            <p>Organic Practices</p>
        </div>
        <div class="stat-card">
            <h2>Multi</h2>
            <p>Layered Ecosystem</p>
        </div>
    </div>
</div>
"""

hanur_css="""
.hanur-section {
    display: flex;
    align-items: center;
    padding: 100px 0%;
    background-color: #FFFFFF; /* Crisp white to contrast with the dark intro above it */
    gap: 60px;
}

.hanur-video-container {
    flex: 1;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(11, 79, 58, 0.15); /* Soft premium green shadow */
    position: relative;
}

.hanur-video-container video {
    width: 100%;
    height: auto;
    display: block; /* Removes weird spacing under videos */
    object-fit: cover;
}

.hanur-text-container {
    flex: 1;
}

.hanur-title {
    font-size: 42px;
    color: #0B4F3A;
    font-family: 'Lora', serif;
    margin-top: 0;
    text-align:center;
    margin-bottom: 20px;
    line-height: 1.2;
}

.hanur-subtitle {
    font-size: 20px;
    color: #B58A42; /* Gold accent */
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    text-align:center;
    margin-bottom: 25px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.hanur-text {
    font-size: 18px;
    line-height: 1.8;
    color: #555;
    font-family: 'Inter', sans-serif;
    margin-bottom: 20px;
    text-align:center;
}

/* Mobile Responsiveness: Stack the video on top of the text */
@media (max-width: 950px) {
    .hanur-section { 
        flex-direction: column; 
        padding: 60px 5%;
        text-align: center;
        gap: 40px;
    }
    .hanur-title { font-size: 32px; }
}
"""
hanur_html=f"""
<div class="hanur-section">
    
    <!-- Left Side: The Video -->
    <div class="hanur-video-container">
        <video autoplay muted loop playsinline>
            <source src="data:video/mp4;base64,{hanur_b64}">
        </video>
    </div>

    <!-- Right Side: The Content -->
    <div class="hanur-text-container">
        <p class="hanur-subtitle">The Tribal Trails Advantage</p>
        <h2 class="hanur-title">Chosen by Science, Perfected by Nature.</h2>
        <p class="hanur-text">
            The specific terrain of our Hanur estate allows for the flawless execution of our master agroforestry plan. This topography enables absolute precision in farm management.
        </p>
        <p class="hanur-text">
            The landscape perfectly accommodates the strategic mapping of our 53 distinct farm plots. This ensures that the protective Forestry Shield and the inner multi-tiered canopy layers receive optimal sunlight, precise water distribution, and flawless daily management.
        </p>
    </div>
    
</div>
"""

cards_css="""
.cards-section {
    padding: 100px 10%;
    background-color: #F4FAF6; /* Soft green to contrast the white section above */
    text-align: center;
}
.section-title {
    font-size: 42px;
    color: #0B4F3A;
    font-family: 'Lora', serif;
    margin-bottom: 15px;
}
.section-subtitle {
    font-size: 20px;
    color: #555;
    font-family: 'Inter', sans-serif;
    margin-bottom: 60px;
}
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}
.value-card {
    background: #FFFFFF;
    padding: 40px 30px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
    text-align: left;
    border-top: 4px solid #0B4F3A; /* Premium dark green accent line */
}
.value-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(11,79,58,0.12);
}
.value-card h3 {
    color: #0B4F3A;
    font-size: 24px;
    font-family: 'Lora', serif;
    margin-bottom: 15px;
}
.value-card p {
    color: #666;
    font-size: 16px;
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    margin: 0;
}

/* Mobile Responsiveness for Cards */
@media (max-width: 1000px) {
    .cards-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 650px) {
    .cards-grid { grid-template-columns: 1fr; }
    .cards-section { padding: 60px 5%; }
    .section-title { font-size: 32px; }
}
"""
cards_html=f"""
<div class="cards-section">
    <h2 class="section-title">Engineered for Ecological Brilliance</h2>
    <p class="section-subtitle">A blueprint for harmonizing agricultural yield with environmental conservation.</p>
    
    <div class="cards-grid">
        <div class="value-card">
            <h3>Protective Forestry Shield</h3>
            <p>Natural windbreaks that build deep climatic resilience and safeguard the inner ecosystem.</p>
        </div>
        <div class="value-card">
            <h3>Biodiverse Fruit Zone</h3>
            <p>A thriving, multi-species habitat supporting local wildlife while delivering seasonal yields.</p>
        </div>
        <div class="value-card">
            <h3>Optimized Canopy Layout</h3>
            <p>Precision spacing calculated for maximum sunlight capture, airflow, and root health.</p>
        </div>
        <div class="value-card">
            <h3>Advanced Hydrology</h3>
            <p>Smart water retention and distribution systems designed for sustainable resource management.</p>
        </div>
        <div class="value-card">
            <h3>Organic Soil Enrichment</h3>
            <p>Continuous biomass layering engineered to regenerate and feed the earth's natural microbiome.</p>
        </div>
        <div class="value-card">
            <h3>Generational Wealth</h3>
            <p>A secure, appreciating asset yielding long-term value through timber and commercial crops.</p>
        </div>
    </div>
</div>
"""
qsn_css="""
.faq-section {
    padding: 100px 0; 
    background-color: #082f23; /* Deep premium forest green */
    text-align: center;
    overflow: hidden;
}

.faq-header {
    margin-bottom: 50px;
    padding: 0 10%;
}

.faq-title {
    font-size: 42px;
    color: #FFFFFF; /* Changed to white for the dark background */
    font-family: 'Lora', serif;
    margin-bottom: 15px;
}

.faq-subtitle {
    font-size: 20px;
    color: rgba(255, 255, 255, 0.7); /* Soft light grey */
    font-family: 'Lora', sans-serif;
    margin: 0;
}

/* Horizontal Scrolling Track */
.faq-carousel-wrapper {
    position: relative;
    width: 100%;
    overflow: hidden;
    display: flex;
}

.faq-track {
    display: flex;
    gap: 30px;
    padding-left: 30px; 
    width: max-content;
    animation: scroll-left 90s linear infinite; 
}

/* Pause on hover for readability */
.faq-track:hover {
    animation-play-state: paused;
}

@keyframes scroll-left {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } 
}

/* Individual FAQ Card Styling (Dark/Glass Theme) */
.faq-card {
    width: 380px; 
    background: rgba(255, 255, 255, 0.03); /* Sleek glass effect */
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    padding: 35px 30px;
    border-radius: 16px;
    text-align: left;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border-top: 4px solid #B58A42; /* Premium Gold accent */
    white-space: normal; 
    flex-shrink: 0; 
    transition: transform 0.3s ease, background 0.3s ease;
}

.faq-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.06); /* Slightly brighter on hover */
    box-shadow: 0 15px 40px rgba(0,0,0,0.5);
}

.faq-card h4 {
    color: #B58A42; /* Gold for the question */
    font-size: 18px;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 15px;
    line-height: 1.4;
}

.faq-card p {
    color: #E0E0E0; /* Light grey for the answer */
    font-size: 15px;
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    margin: 0;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .faq-section { padding: 60px 0; }
    .faq-title { font-size: 32px; }
    .faq-card { width: 300px; padding: 25px 20px; }
}
"""

qsn_html=f"""

<div class="faq-section">
    <div class="faq-header">
        <h2 class="faq-title">Investor Q&A</h2>
        <p class="faq-subtitle">Everything you need to know about owning a living ecosystem.</p>
    </div>
    
    <div class="faq-carousel-wrapper">
        <div class="faq-track">
            
            <!-- ORIGINAL SET OF 17 QUESTIONS -->
            <div class="faq-card"><h4>Q. Do I need agricultural experience to own a plot?</h4><p>Ans. Not at all. Our agronomists handle 100% of operations, from soil preparation to the final harvest.</p></div>
            <div class="faq-card"><h4>Q. How do I track the progress of my ecosystem?</h4><p>Ans. Through our automated digital ledger, giving you transparent, data-driven updates on your specific plot's growth and activities.</p></div>
            <div class="faq-card"><h4>Q. Who handles the daily labor and farm security?</h4><p>Ans. Nature's Cluster staffs, manages, and secures the entire estate. You simply own the appreciating asset.</p></div>
            <div class="faq-card"><h4>Q. What happens if a plant or tree requires medical attention?</h4><p>Ans. Our constant botanical monitoring ensures early detection and organic treatment, completely managed by our expert team.</p></div>
            <div class="faq-card"><h4>Q. Am I responsible for harvesting and selling the crops?</h4><p>Ans. No. We manage the entire commercial lifecycle, from planting the sapling to the final market sale.</p></div>
            <div class="faq-card"><h4>Q. When does this ecosystem start generating returns?</h4><p>Ans. The multi-storey model is engineered for phased yields: early financial returns from seasonal fruits and massive payouts from mature timber.</p></div>
            <div class="faq-card"><h4>Q. Why invest in timber over traditional real estate?</h4><p>Ans. Premium timber naturally appreciates in physical size and market value every single day, completely independent of housing market crashes.</p></div>
            <div class="faq-card"><h4>Q. Are there multiple streams of revenue?</h4><p>Ans. Absolutely. By layering tropical fruits alongside high-value woods like Sandalwood and Mahogany, your plot leverages diverse income streams.</p></div>
            <div class="faq-card"><h4>Q. Is there an expected holding period for the investment?</h4><p>Ans. Agroforestry is a generational wealth tool. While fruits yield sooner, the timber maximizes its premium valuation over a 10 to 15-year horizon.</p></div>
            <div class="faq-card"><h4>Q. How is my investment protected from extreme weather?</h4><p>Ans. The strategic Forestry Shield acts as a perimeter defense, breaking harsh winds and regulating the inner micro-climate.</p></div>
            <div class="faq-card"><h4>Q. What if there is a severe drought or water shortage?</h4><p>Ans. The Hanur estate utilizes advanced rainwater harvesting and gravity-assisted drip irrigation to ensure deep climatic resilience.</p></div>
            <div class="faq-card"><h4>Q. Is my ownership of the land legally secure?</h4><p>Ans. Yes. You receive complete, unencumbered legal ownership of the physical land and all the botanical assets growing upon it.</p></div>
            <div class="faq-card"><h4>Q. How does organic farming protect my financial asset?</h4><p>Ans. Chemical farming permanently depletes soil value. Our strict organic protocols ensure your land remains perpetually fertile and highly valued.</p></div>
            <div class="faq-card"><h4>Q. How does the "multi-storey" model maximize my plot's output?</h4><p>Ans. By vertically layering crops, we capture maximum sunlight and generate multiple revenue streams per square foot without exhausting the soil.</p></div>
            <div class="faq-card"><h4>Q. What role do bio-stimulants play in my investment?</h4><p>Ans. Organic inputs like Jeevamrutha accelerate root health, getting your timber and fruit assets to harvest maturity faster and healthier.</p></div>
            <div class="faq-card"><h4>Q. How does the integrated dairy model benefit my land?</h4><p>Ans. Through Gautraa by Nature's cluster, our on-site Gir cattle system provides premium organic manure, creating a self-sustaining nutrient loop that drastically lowers operational costs.</p></div>
            <div class="faq-card"><h4>Q. Why was the Hanur region chosen for this project?</h4><p>Ans. Its transitional forest climate and optimal soil composition create the ultimate biological engine for accelerating high-value timber growth.</p></div>

            <!-- DUPLICATED SET (Required for seamless infinite CSS scroll) -->
            <div class="faq-card"><h4>Q. Do I need agricultural experience to own a plot?</h4><p>Ans. Not at all. Our agronomists handle 100% of operations, from soil preparation to the final harvest.</p></div>
            <div class="faq-card"><h4>Q. How do I track the progress of my ecosystem?</h4><p>Ans. Through our automated digital ledger, giving you transparent, data-driven updates on your specific plot's growth and activities.</p></div>
            <div class="faq-card"><h4>Q. Who handles the daily labor and farm security?</h4><p>Ans. Nature's Cluster staffs, manages, and secures the entire estate. You simply own the appreciating asset.</p></div>
            <div class="faq-card"><h4>Q. What happens if a plant or tree requires medical attention?</h4><p>Ans. Our constant botanical monitoring ensures early detection and organic treatment, completely managed by our expert team.</p></div>
            <div class="faq-card"><h4>Q. Am I responsible for harvesting and selling the crops?</h4><p>Ans. No. We manage the entire commercial lifecycle, from planting the sapling to the final market sale.</p></div>
            <div class="faq-card"><h4>Q. When does this ecosystem start generating returns?</h4><p>Ans. The multi-storey model is engineered for phased yields: early financial returns from seasonal fruits and massive payouts from mature timber.</p></div>
            <div class="faq-card"><h4>Q. Why invest in timber over traditional real estate?</h4><p>Ans. Premium timber naturally appreciates in physical size and market value every single day, completely independent of housing market crashes.</p></div>
            <div class="faq-card"><h4>Q. Are there multiple streams of revenue?</h4><p>Ans. Absolutely. By layering tropical fruits alongside high-value woods like Sandalwood and Mahogany, your plot leverages diverse income streams.</p></div>
            <div class="faq-card"><h4>Q. Is there an expected holding period for the investment?</h4><p>Ans. Agroforestry is a generational wealth tool. While fruits yield sooner, the timber maximizes its premium valuation over a 10 to 15-year horizon.</p></div>
            <div class="faq-card"><h4>Q. How is my investment protected from extreme weather?</h4><p>Ans. The strategic Forestry Shield acts as a perimeter defense, breaking harsh winds and regulating the inner micro-climate.</p></div>
            <div class="faq-card"><h4>Q. What if there is a severe drought or water shortage?</h4><p>Ans. The Hanur estate utilizes advanced rainwater harvesting and gravity-assisted drip irrigation to ensure deep climatic resilience.</p></div>
            <div class="faq-card"><h4>Q. Is my ownership of the land legally secure?</h4><p>Ans. Yes. You receive complete, unencumbered legal ownership of the physical land and all the botanical assets growing upon it.</p></div>
            <div class="faq-card"><h4>Q. How does organic farming protect my financial asset?</h4><p>Ans. Chemical farming permanently depletes soil value. Our strict organic protocols ensure your land remains perpetually fertile and highly valued.</p></div>
            <div class="faq-card"><h4>Q. How does the "multi-storey" model maximize my plot's output?</h4><p>Ans. By vertically layering crops, we capture maximum sunlight and generate multiple revenue streams per square foot without exhausting the soil.</p></div>
            <div class="faq-card"><h4>Q. What role do bio-stimulants play in my investment?</h4><p>Ans. Organic inputs like Jeevamrutha accelerate root health, getting your timber and fruit assets to harvest maturity faster and healthier.</p></div>
            <div class="faq-card"><h4>Q. How does the integrated dairy model benefit my land?</h4><p>Ans. Through Gautraa by Nature's cluster, our on-site Gir cattle system provides premium organic manure, creating a self-sustaining nutrient loop that drastically lowers operational costs.</p></div>
            <div class="faq-card"><h4>Q. Why was the Hanur region chosen for this project?</h4><p>Ans. Its transitional forest climate and optimal soil composition create the ultimate biological engine for accelerating high-value timber growth.</p></div>

        </div>
    </div>
</div>
"""
advantage_css="""
.advantage-section {
    padding: 100px 10%;
    background-color: #082f23; /* Deep premium forest green */
    color: white;
    text-align: center;
    overflow: hidden;
}
.adv-title {
    font-size: 42px;
    color: #FFFFFF;
    font-family: 'Lora', serif;
    margin-bottom: 15px;
}
.adv-subtitle {
    font-size: 20px;
    color: rgba(255, 255, 255, 0.7);
    font-family: 'Inter', sans-serif;
    margin-bottom: 60px;
}

/* Carousel Container with top/bottom fade effect */
.carousel-wrapper {
    display: flex;
    justify-content: center;
    height: 600px;
    position: relative;
    -webkit-mask-image: linear-gradient(to bottom, transparent, black 5%, black 95%, transparent);
    mask-image: linear-gradient(to bottom, transparent, black 5%, black 95%, transparent);
}

.carousel-column {
    width: 100%;
    max-width: 600px; /* Slightly wider since it's just one column now */
    overflow: hidden;
    position: relative;
}

/* The animated track */
.carousel-track {
    display: flex;
    flex-direction: column;
    gap: 20px;
    animation: scroll-up 60s linear infinite; /* Increased time since there are more cards */
}

/* Pause on hover so users can read */
.carousel-wrapper:hover .carousel-track {
    animation-play-state: paused;
}

@keyframes scroll-up {
    0% { transform: translateY(0); }
    /* Shifts exactly half the track height (the duplicated content) to loop seamlessly */
    100% { transform: translateY(-50%); } 
}

/* Card Styling */
.adv-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    padding: 35px 30px;
    border-radius: 16px;
    text-align: left;
    border-left: 4px solid #B58A42; /* Premium Gold Accent */
}
.adv-card h3 {
    color: #B58A42;
    font-size: 22px;
    font-family: 'Lora', serif;
    margin-bottom: 10px;
}
.adv-card p {
    color: #E0E0E0;
    font-size: 16px;
    font-family: 'Inter', sans-serif;
    margin: 0;
    line-height: 1.6;
}

/* Mobile Responsiveness: Disable animation for readability */
@media (max-width: 900px) {
    .carousel-wrapper { height: auto; -webkit-mask-image: none; mask-image: none; }
    .carousel-column { overflow: visible; }
    .carousel-track { animation: none !important; }
    /* Hide the duplicated cards on mobile so the list isn't twice as long */
    .duplicate { display: none; } 
    .advantage-section { padding: 60px 5%; }
}
"""

advantage_html=f"""
<div class="advantage-section">
    <h2 class="adv-title">Redefining Land Ownership</h2>
    <p class="adv-subtitle">We don’t just sell plots; we engineer living, appreciating ecosystems.</p>
    
    <div class="carousel-wrapper">
        <div class="carousel-column">
            <div class="carousel-track">
                <!-- Original Set of 10 Cards -->
                <div class="adv-card"><h3>100% Managed Ecosystem</h3><p>Expert botanists and agriculturists handle the entire lifecycle of your land.</p></div>
                <div class="adv-card"><h3>Generational Wealth</h3><p>A secure, tangible asset designed to appreciate naturally over decades.</p></div>
                <div class="adv-card"><h3>Zero Monoculture</h3><p>Over 15 diverse native species planted to ensure deep ecological resilience.</p></div>
                <div class="adv-card"><h3>Zero-Effort Ownership</h3><p>Enjoy the financial benefits of agricultural land without any of the daily labor.</p></div>
                <div class="adv-card"><h3>Precision Agroforestry</h3><p>Scientific spacing and layering to maximize sunlight, airflow, and growth.</p></div>
                <div class="adv-card"><h3>Appreciating Value</h3><p>As the forest canopy matures, the intrinsic value of the underlying land grows.</p></div>
                <div class="adv-card"><h3>Advanced Hydrology</h3><p>Smart rainwater harvesting and drip systems that conserve every drop.</p></div>
                <div class="adv-card"><h3>Diverse Revenue</h3><p>Multiple income streams from seasonal cash crops and long-term timber yields.</p></div>
                <div class="adv-card"><h3>Regenerative Soil</h3><p>Organic biomass integration that actively repairs and feeds the earth.</p></div>
                <div class="adv-card"><h3>Transparent Tracking</h3><p>Clear, consistent updates on your ecosystem's growth and agricultural output.</p></div>
                
                <!-- Duplicated Set (Required for seamless infinite scroll) -->
                <div class="adv-card duplicate"><h3>100% Managed Ecosystem</h3><p>Expert botanists and agriculturists handle the entire lifecycle of your land.</p></div>
                <div class="adv-card duplicate"><h3>Generational Wealth</h3><p>A secure, tangible asset designed to appreciate naturally over decades.</p></div>
                <div class="adv-card duplicate"><h3>Zero Monoculture</h3><p>Over 15 diverse native species planted to ensure deep ecological resilience.</p></div>
                <div class="adv-card duplicate"><h3>Zero-Effort Ownership</h3><p>Enjoy the financial benefits of agricultural land without any of the daily labor.</p></div>
                <div class="adv-card duplicate"><h3>Precision Agroforestry</h3><p>Scientific spacing and layering to maximize sunlight, airflow, and growth.</p></div>
                <div class="adv-card duplicate"><h3>Appreciating Value</h3><p>As the forest canopy matures, the intrinsic value of the underlying land grows.</p></div>
                <div class="adv-card duplicate"><h3>Advanced Hydrology</h3><p>Smart rainwater harvesting and drip systems that conserve every drop.</p></div>
                <div class="adv-card duplicate"><h3>Diverse Revenue</h3><p>Multiple income streams from seasonal cash crops and long-term timber yields.</p></div>
                <div class="adv-card duplicate"><h3>Regenerative Soil</h3><p>Organic biomass integration that actively repairs and feeds the earth.</p></div>
                <div class="adv-card duplicate"><h3>Transparent Tracking</h3><p>Clear, consistent updates on your ecosystem's growth and agricultural output.</p></div>
            </div>
        </div>
    </div>
</div>
"""

gallery_css="""
.gallery-section {
    padding: 100px 10%;
    background-color: #FFFFFF; 
    text-align: center;
}
.gallery-title {
    font-size: 42px;
    color: #0B4F3A;
    font-family: 'Lora', serif;
    margin-bottom: 15px;
}
.gallery-subtitle {
    font-size: 20px;
    color: #555;
    font-family: 'Inter', sans-serif;
    margin-bottom: 60px;
}

/* Slider Container */
.slider-container {
    width: 100%;
    max-width: 1000px; /* Prevents the slider from becoming too wide on huge screens */
    margin: 0 auto;
    overflow: hidden; /* Hides the images that are "off-screen" */
    border-radius: 16px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    position: relative;
    background: #000; /* Dark background behind images if they have different aspect ratios */
}

/* The track that moves left and right */
.slider-track {
    display: flex;
    transition: transform 0.8s ease-in-out; /* Smooth sliding animation */
    width: 100%;
}

/* Individual Images */
.slide {
    min-width: 100%; /* Forces every image to take up exactly 100% of the container width */
    height: 600px; /* Fixed height so the slider doesn't jump up and down */
    object-fit: cover; /* Ensures images fill the space beautifully without stretching */
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .slide { height: 400px; }
    .gallery-section { padding: 60px 5%; }
    .gallery-title { font-size: 32px; }
}
"""

gallery_html=f"""
<div class="gallery-section">
    <h2 class="gallery-title">Experience Tribal Trails</h2>
    <p class="gallery-subtitle">A visual journey through our living ecosystem and agricultural developments.</p>
    
    <div class="slider-container">
        <div class="slider-track" id="galleryTrack">
            <!-- Python injects the images here -->
            {gallery}
        </div>
    </div>
</div>

<!-- JavaScript to power the automatic sliding -->
<script>
    const track = document.getElementById('galleryTrack');
    const slides = track.querySelectorAll('.slide');
    let currentIndex = 0;

    // Only run the slider if there is more than 1 image
    if (slides.length > 1) {{
        setInterval(() => {{
            currentIndex++;
            // If we reach the end, instantly reset back to the first image
            if (currentIndex >= slides.length) {{
                currentIndex = 0;
            }}
            // Move the track to the left by 100% for each slide index
            track.style.transform = `translateX(-${{currentIndex * 100}}%)`;
        }}, 2000); // 2000 milliseconds = 2 seconds
    }}
</script>
"""

footer_css="""
.footer-section {
    background-color: #082f23; 
    color: rgba(255, 255, 255, 0.7);
    padding: 80px 10%; /* Even padding */
    font-family: 'Lora', sans-serif;
    text-align: center;
}

.footer-quote {
    color: #B58A42;
    font-family: 'Lora', serif;
    font-size: 32px;
    font-style: italic;
    margin-bottom: 60px;
    font-weight: 500;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    text-align: center; /* Centers the text inside each grid cell */
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 50px;
    margin-bottom: 40px;
    align-items: start;
}

.footer-column {
    display: flex;
    flex-direction: column;
    align-items: center; /* This centers the content horizontally in every column */
}

.footer-column h4 {
    color: #FFFFFF;
    font-size: 20px;
    font-family: 'Lora', serif;
    margin-top: 0;
    margin-bottom: 25px;
    letter-spacing: 1px;
}

/* This fixes your contact list to align left but stay centered in the column */
.contact-list {
    text-align: left;
    display: inline-block;
}

.footer-social-wrapper {
    display: flex;
    gap: 25px;
    justify-content: center; /* Forces the icons to sit in the middle */
}

.social-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: rgba(255, 255, 255, 0.7);
    font-size: 13px;
    transition: color 0.3s ease;
}

.social-item:hover {
    color: #B58A42;
}

.social-item img {
    width: 32px;
    height: 32px;
    margin-bottom: 10px;
    transition: transform 0.3s ease;
}

.social-item:hover img {
    transform: scale(1.15);
}

.footer-qr {
    width: 120px;
    height: 120px;
    border-radius: 8px;
    border: 2px solid rgba(255,255,255,0.2);
}
"""
footer_html=f"""

<div class="footer-section">
    
    <h2 class="footer-quote">"The greatest investment is the one that grows with nature."</h2>
    
    <div class="footer-grid">
        
        <div class="footer-column">
            <h4>Contact Us</h4>
            <p>📞 +91 9591597415</p>
            <p>✉️ naturescluster@gmail.com</p>
        </div>
        
        <div class="footer-column">
            <h4>Connect With Us</h4>
            <div class="footer-social-wrapper">
                <a href="https://wa.me/919591597415" target="_blank" class="social-item">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
                    <span>WhatsApp</span>
                </a>
                
                <a href="https://instagram.com/naturescluster" target="_blank" class="social-item">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram">
                    <span>Instagram</span>
                </a>
                
                <a href="https://facebook.com/naturescluster" target="_blank" class="social-item">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/2021_Facebook_icon.svg" alt="Facebook">
                    <span>Facebook</span>
                </a>
                
                <a href="https://youtube.com/@naturescluster" target="_blank" class="social-item">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" alt="YouTube">
                    <span>YouTube</span>
                </a>
            </div>
        </div>
        
        <div class="footer-column">
            <h4>Scan for Location</h4>
            <img src="data:image/jpeg;base64,{qr_b64}" class="footer-qr" alt="Location QR Code">
        </div>
        
    </div>
    
    
</div>
"""


# --- 5. ASSEMBLE AND RENDER ---
final_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        /* Base Global Styles */
        body {{
            margin: 0; 
            background: #F4FAF6; 
            font-family: 'Lora', system-ui, sans-serif; 
            color: #333;
            
        }}
        
        /* Segregated CSS Injections */
        {header_css}
        {hero_css}
        {intro_css}
        {hanur_css}
        {qsn_css}
        {cards_css}
        {advantage_css}
        {gallery_css}
        {footer_css}
    </style>
</head>
<body>
    
    {header_html}
    {hero_html}
    {intro_html}
    {hanur_html}
    {qsn_html}
    {cards_html}
    {advantage_html}
    {gallery_html}
    {footer_html}

</body>
</html>
"""

components.html(final_html, height=6700, scrolling=False)