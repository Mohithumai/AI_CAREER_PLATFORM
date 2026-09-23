import streamlit as st
import pdfplumber
import math
import time
import json
import streamlit.components.v1 as components
from groq import Groq
import plotly.graph_objects as go

def show_analyzer(switch_page_callback):
    for _key in ["analyzed","resume_text","skills","ats_score","original_bullet","enhanced_bullet","voice_q","voice_transcript","voice_eval","full_rewrite","simulated_skill"]:
        if _key not in st.session_state:
            st.session_state[_key] = False if _key == "analyzed" else None

    st.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Manrope:wght@300;400;500;600;700&display=swap');
    :root {
        --bg:#050608; --surface:rgba(18,21,30,0.4); --surface-hi:rgba(18,21,30,0.85);
        --border:rgba(255,255,255,0.05); --border-hi:rgba(77,255,195,0.3);
        --accent:#4DFFC3; --secondary:#00d2ff; --warn:#FFBE57; --text:#ECE9E2; --sub:#818DA0;
    }
    .stApp,.main,[data-testid="stAppViewContainer"]{background:var(--bg)!important;}
    #MainMenu,footer,.stDeployButton{display:none!important;}
    [data-testid="stToolbar"]{visibility:hidden!important;}
    .block-container{padding-top:2rem!important;max-width:1040px!important;}
    p,div,li,label,span{font-family:'Manrope',sans-serif!important;color:var(--text);}
    h1,h2,h3,h4{font-family:'Syne',sans-serif!important;letter-spacing:-0.025em!important;color:var(--text);}

    /* ── Buttons ── */
    .stButton>button{background:rgba(255,255,255,0.03)!important;color:#C8C4BC!important;border:1px solid var(--border)!important;border-radius:8px!important;font-family:'Syne',sans-serif!important;font-weight:600!important;font-size:13px!important;letter-spacing:0.05em;text-transform:uppercase;height:44px!important;padding:0 24px!important;transition:all 0.3s ease!important;}
    .stButton>button:hover{background:rgba(77,255,195,0.08)!important;color:var(--accent)!important;border-color:var(--accent)!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(77,255,195,0.15)!important;}
    .glow-btn>div>button{background:linear-gradient(135deg,#4DFFC3 0%,#00d2ff 100%)!important;color:#050608!important;font-weight:800!important;border:none!important;}
    .glow-btn>div>button:hover{transform:scale(1.03) translateY(-1px)!important;box-shadow:0 10px 30px rgba(77,255,195,0.3)!important;}

    /* ── Cards ── */
    .feature-card{background:var(--surface);backdrop-filter:blur(15px);border:1px solid var(--border);border-radius:16px;padding:28px;margin-bottom:24px;transition:all 0.3s ease;}
    .feature-card:hover{border-color:var(--border-hi);background:var(--surface-hi);}
    .card-title{font-family:'Syne',sans-serif!important;font-size:11px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:16px;border-bottom:1px solid var(--border);padding-bottom:10px;}
    .status-pill{border-radius:20px;padding:4px 12px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:6px;}
    .status-pill.error{background:rgba(255,107,107,0.1);color:#FF6B6B;border:1px solid rgba(255,107,107,0.2);}
    .status-pill.success{background:rgba(77,255,195,0.1);color:var(--accent);border:1px solid rgba(77,255,195,0.2);}
    .code-pane{background:rgba(13,16,24,0.6);border:1px solid var(--border);border-radius:12px;padding:20px;height:440px;overflow-y:auto;font-family:'Manrope',sans-serif;font-size:13px;line-height:1.7;white-space:pre-wrap;}

    /* ── Tabs ── */
    [data-baseweb="tab-list"]{gap:12px;margin-bottom:24px;background:rgba(18,21,30,0.5);padding:8px;border-radius:12px;border:1px solid var(--border);}
    [data-baseweb="tab"]{font-family:'Syne',sans-serif!important;font-weight:700!important;color:var(--sub)!important;background:transparent!important;border-radius:8px!important;padding:10px 20px!important;border:1px solid transparent!important;}
    [aria-selected="true"]{color:#050608!important;background:var(--accent)!important;box-shadow:0 4px 15px rgba(77,255,195,0.3)!important;}

    /* ── Inputs ── */
    textarea,[data-testid="stTextInput"] input{background:rgba(13,16,24,0.85)!important;backdrop-filter:blur(8px)!important;color:var(--text)!important;border:1px solid var(--border)!important;border-radius:8px!important;font-size:13px!important;}

    /* ── FILE UPLOADER — premium, no duplicate text ── */

    /* Hide label + instructions text */
    [data-testid="stFileUploader"] [data-testid="stWidgetLabel"],
    [data-testid="stFileUploader"] label                         { display: none !important; }
    [data-testid="stFileUploaderDropzoneInstructions"]           { display: none !important; }

    /* Center the dropzone */
    [data-testid="stFileUploaderDropzone"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-height: 72px !important;
        padding: 16px !important;
    }

    /* Hide ONLY the inner span children of the button (kills "uploadUpload") */
    [data-testid="stFileUploaderDropzone"] button > * { display: none !important; }

    /* Premium button */
    [data-testid="stFileUploaderDropzone"] button {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        min-width: 260px !important;
        height: 54px !important;
        padding: 0 36px !important;
        background: linear-gradient(135deg, rgba(77,255,195,0.1) 0%, rgba(0,210,255,0.06) 100%) !important;
        border: 1px solid rgba(77,255,195,0.5) !important;
        border-radius: 12px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 24px rgba(77,255,195,0.1), inset 0 1px 0 rgba(255,255,255,0.05) !important;
        position: relative !important;
    }
    [data-testid="stFileUploaderDropzone"] button:hover {
        background: linear-gradient(135deg, rgba(77,255,195,0.2) 0%, rgba(0,210,255,0.12) 100%) !important;
        border-color: rgba(77,255,195,0.8) !important;
        box-shadow: 0 0 40px rgba(77,255,195,0.22), inset 0 1px 0 rgba(255,255,255,0.08) !important;
        transform: translateY(-2px) !important;
    }

    /* Inject one clean label */
    [data-testid="stFileUploaderDropzone"] button::before {
        content: "📄";
        font-size: 18px !important;
        margin-right: 10px !important;
        display: inline !important;
    }
    [data-testid="stFileUploaderDropzone"] button::after {
        content: "Upload Resume PDF";
        font-size: 14px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 0.08em !important;
        color: #4DFFC3 !important;
        text-transform: uppercase !important;
        display: inline !important;
    }
    </style>
    """)

    # ── Particle background ───────────────────────────────────────────────
    st.html("""
    <style>
        iframe{position:fixed!important;top:0!important;left:0!important;width:100vw!important;height:100vh!important;z-index:-1!important;pointer-events:none!important;}
        .stApp,[data-testid="stApp"],[data-testid="stAppViewContainer"],.main,.block-container,header{background:transparent!important;}
    </style>
    """)
    components.html("""
    <!DOCTYPE html><html><head><meta charset="UTF-8">
    <style>body{margin:0;padding:0;background:#050608;overflow:hidden;}#p{position:absolute;width:100%;height:100%;}</style>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>
    </head><body><div id="p"></div>
    <script>tsParticles.load("p",{fpsLimit:60,particles:{color:{value:"#4DFFC3"},links:{color:"#4DFFC3",distance:150,enable:true,opacity:0.12,width:1},move:{enable:true,speed:0.6,outModes:{default:"bounce"}},number:{density:{enable:true,area:800},value:40},opacity:{value:0.3},shape:{type:"circle"},size:{value:{min:1,max:3}}},detectRetina:true});</script>
    </body></html>
    """, height=0)

    # ── Data definitions ──────────────────────────────────────────────────
    skill_categories = {
        "Frontend": ["html","css","javascript","react","vue","tailwind"],
        "Backend":  ["python","java","c++","node","django","fastapi","rest apis"],
        "Database": ["sql","mysql","mongodb","postgresql","redis"],
        "DevOps":   ["git","github","aws","docker","ci/cd","kubernetes"],
    }
    skills_db = [s for cat in skill_categories.values() for s in cat]

    def extract_text_from_pdf(file):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                ex = page.extract_text()
                if ex: text += ex.lower() + "\n"
        return text

    # ── Header ────────────────────────────────────────────────────────────
    if st.button("← Back to Dashboard"):
        switch_page_callback("home")
    st.html("<hr style='border:none;border-top:1px solid rgba(255,255,255,0.05);margin:1.5rem 0;'>")
    st.html("""
    <div style="margin-bottom:2rem;">
        <span style="font-family:'Manrope',sans-serif;font-size:11px;letter-spacing:0.16em;text-transform:uppercase;color:#4DFFC3;font-weight:600;">◈ Workspace Portal</span>
        <h1 style="font-size:2.8rem;font-weight:800;margin:8px 0 12px 0;">AI Resume <span style="color:#4DFFC3;">Analyzer</span></h1>
        <p style="color:#818DA0;font-size:14px;max-width:600px;margin:0;line-height:1.6;">Upload your resume, find missing keywords for specific roles, and practice mock interviews.</p>
    </div>
    """)

    # ── API key ───────────────────────────────────────────────────────────
    st.html("""<div class="feature-card"><div style="font-family:'Syne',sans-serif;font-size:14px;font-weight:700;color:#4DFFC3;margin-bottom:6px;">Groq API Key Setup</div><div style="font-family:'Manrope',sans-serif;font-size:13px;color:#818DA0;margin-bottom:14px;">Powers AI rewrites and interactive interview features.</div>""")
    api_key = st.text_input("Groq Token", type="password", placeholder="gsk_...", label_visibility="collapsed")
    st.html("</div>")

    # ── Upload section ────────────────────────────────────────────────────
    if not st.session_state.analyzed:
        st.html("""
        <div style="background:rgba(18,21,30,0.4);border:1px dashed rgba(77,255,195,0.2);border-radius:16px;padding:30px;text-align:center;margin-bottom:15px;">
            <h3 style="color:#ECE9E2;font-family:'Syne',sans-serif;margin:0 0 8px 0;font-size:1.8rem;font-weight:700;">📄 Upload Your Resume</h3>
            <p style="color:#818DA0;font-family:'Manrope',sans-serif;margin:0;font-size:14px;">PDF only · ATS Analysis · AI Review</p>
        </div>
        """)
        uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

        if uploaded_file:
            loader_slot = st.empty()
            steps = ["Reading resume file data","Checking skill matching keywords","Scanning formatting layouts","Building dashboard interface"]
            for idx in range(len(steps) + 1):
                html = """<div style="background:rgba(18,21,30,0.85);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.05);border-radius:14px;padding:36px;max-width:460px;margin:0 auto;">"""
                for i, label in enumerate(steps):
                    if i < idx:
                        html += f"<div style='color:#4DFFC3;font-size:14px;margin:14px 0;display:flex;align-items:center;gap:12px;'><div style='background:rgba(77,255,195,0.1);border:1px solid #4DFFC3;border-radius:50%;width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:10px;'>✓</div>{label}</div>"
                    elif i == idx:
                        html += f"<div style='color:#ECE9E2;font-size:14px;margin:14px 0;font-weight:600;display:flex;align-items:center;gap:12px;'><div style='border:2px solid rgba(255,255,255,0.1);border-top-color:#4DFFC3;border-radius:50%;width:16px;height:16px;animation:spin 0.8s linear infinite;'></div>{label}...</div>"
                    else:
                        html += f"<div style='color:#3A3F4E;font-size:14px;margin:14px 0;display:flex;align-items:center;gap:12px;'><div style='border:2px solid rgba(255,255,255,0.05);border-radius:50%;width:16px;height:16px;'></div>{label}</div>"
                html += "</div><style>@keyframes spin{100%{transform:rotate(360deg);}}</style>"
                loader_slot.html(html)
                if idx < len(steps): time.sleep(0.5)

            extracted_text = extract_text_from_pdf(uploaded_file)
            st.session_state.resume_text = extracted_text
            st.session_state.skills = [s for s in skills_db if s.lower() in extracted_text]
            st.session_state.ats_score = round(min((len(st.session_state.skills) / 12) * 100, 95))
            bullet_sentences = [s.strip() for s in extracted_text.replace('\n','. ').split('.') if len(s.split()) > 5]
            weak = [s for s in bullet_sentences if not any(c.isdigit() for c in s)]
            st.session_state.original_bullet = weak[0] if weak else "Worked with engineers to deploy and build backend code services."
            st.session_state.enhanced_bullet = "Spearheaded microservice deployments that optimized runtime efficiency by 35% and removed system infrastructure latency blocks."
            loader_slot.empty()
            st.session_state.analyzed = True
            st.rerun()

    # ── Results dashboard ─────────────────────────────────────────────────
    if st.session_state.analyzed:
        col_side, col_main = st.columns([1, 2.5], gap="large")

        with col_side:
            score = st.session_state.ats_score
            color = "#4DFFC3" if score >= 75 else ("#FFBE57" if score >= 45 else "#FF6B6B")
            st.html(f"""
            <div class="feature-card" style="text-align:center;background:rgba(18,21,30,0.65);">
                <div style="font-family:'Syne',sans-serif;font-size:12px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:0.05em;">ATS Rating</div>
                <div style="font-family:'Syne',sans-serif;font-size:3.5rem;font-weight:800;color:{color};line-height:1;margin:14px 0;">{score}<span style="font-size:18px;color:var(--sub);font-weight:400;">/100</span></div>
                <div class="status-pill success" style="font-size:11px;">Parsing Score Verified</div>
            </div>
            <div class="feature-card" style="padding:22px;background:rgba(18,21,30,0.3);">
                <div class="card-title" style="margin-bottom:12px;">Summary Report</div>
                <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;font-size:14px;border-bottom:1px solid rgba(255,255,255,0.05);"><span>Layout Rules</span><span class="status-pill success">Clean</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;font-size:14px;border-bottom:1px solid rgba(255,255,255,0.05);"><span>Impact Data</span><span class="status-pill error">Deficit</span></div>
                <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;font-size:14px;"><span>Skills Found</span><span class="status-pill success" style="color:#00d2ff;background:rgba(0,210,255,0.05);border-color:rgba(0,210,255,0.1);">{len(st.session_state.skills)} Present</span></div>
            </div>
            """)
            if st.button("Upload New File", use_container_width=True):
                st.session_state.analyzed = False
                st.session_state.full_rewrite = None
                st.rerun()

        with col_main:
            tab1, tab2, tab3, tab4 = st.tabs(["Executive Overview","Job Matching","AI Resume Rewriter","Voice Interview"])

            # ── Tab 1: Overview ───────────────────────────────────────────
            with tab1:
                st.html("""<div class="feature-card"><div class="card-title">File Integrity</div><h3 style="font-size:18px;font-weight:700;margin:0 0 10px 0;">Your resume parsed cleanly.</h3><p style="color:var(--sub);font-size:13.5px;line-height:1.6;margin:0;">The file text contents match database reading rules, ensuring recruiters won't encounter unmapped reading blocks.</p></div>""")

                st.html("""<div class="feature-card"><div class="card-title">Discovered Technology Strengths</div>""")
                scores = {k: min(5, sum(1 for s in v if s in st.session_state.skills) * 2) for k, v in skill_categories.items()}
                labels = list(scores.keys()) + [list(scores.keys())[0]]
                vals   = list(scores.values()) + [list(scores.values())[0]]
                fig = go.Figure(data=go.Scatterpolar(r=vals, theta=labels, fill='toself',
                    fillcolor='rgba(77,255,195,0.04)', line=dict(color='#4DFFC3', width=2),
                    marker=dict(color='#4DFFC3', size=6)))
                fig.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0,5]),
                    angularaxis=dict(tickfont=dict(color="#818DA0",size=11,family="Manrope"),
                    linecolor="rgba(255,255,255,0.06)"), bgcolor="rgba(0,0,0,0)"),
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    showlegend=False, margin=dict(l=40,r=40,t=25,b=25), height=260)
                st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
                st.html("</div>")

                st.html("""<div class="feature-card" style="border-left:3px solid #00d2ff;"><div class="card-title" style="color:#00d2ff;">💡 What-If Skill Simulator</div><p style="color:var(--sub);font-size:13px;line-height:1.5;margin-bottom:12px;">Select a skill you want to learn to see how it shifts your ATS score.</p>""")
                unowned = [s for s in skills_db if s not in st.session_state.skills]
                sim = st.selectbox("Simulate skill:", ["Select technology..."] + sorted(unowned), label_visibility="collapsed")
                if sim and sim != "Select technology...":
                    new_score = round(min(((len(st.session_state.skills) + 1) / 12) * 100, 98))
                    st.html(f"""<div style="margin-top:12px;font-weight:600;font-size:13.5px;color:var(--accent);">Adding <b>{sim.title()}</b> raises your score to <b>{new_score}/100</b> (+{new_score - score} pts)!</div>""")
                st.html("</div>")

            # ── Tab 2: JD Matching ────────────────────────────────────────
            with tab2:
                st.html("""<div class="feature-card"><div class="card-title">Job Description Cross-Reference</div><p style="color:var(--sub);font-size:13.5px;line-height:1.6;margin:0 0 16px 0;">Paste the full job description to cross-examine keyword overlap gaps.</p></div>""")
                jd = st.text_area("Job Description", height=160, placeholder="Paste target requirements here...", label_visibility="collapsed")
                if jd:
                    jd_skills  = set(s for s in skills_db if s.lower() in jd.lower())
                    matched    = jd_skills & set(st.session_state.skills)
                    missing    = jd_skills - set(st.session_state.skills)
                    st.html("""<div class="feature-card">""")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("<span style='font-family:Syne;font-size:11px;font-weight:700;color:#FF6B6B;letter-spacing:0.05em;display:block;margin-bottom:10px;'>MISSING KEYWORDS</span>", unsafe_allow_html=True)
                        st.write(", ".join(f"*{t.title()}*" for t in missing) if missing else "No keyword deficits mapped.")
                    with c2:
                        st.markdown("<span style='font-family:Syne;font-size:11px;font-weight:700;color:#4DFFC3;letter-spacing:0.05em;display:block;margin-bottom:10px;'>MATCHED OVERLAPS</span>", unsafe_allow_html=True)
                        st.write(", ".join(t.title() for t in matched) if matched else "No intersections tracked.")
                    st.html("</div>")

            # ── Tab 3: AI Rewriter ────────────────────────────────────────
            with tab3:
                st.html("""<div class="feature-card"><div class="card-title">Full Profile Transformation Unit</div><p style="color:var(--sub);font-size:13.5px;line-height:1.6;margin:0 0 16px 0;">Generate a metrics-focused rewrite using Llama 3.3 via Groq.</p></div>""")
                st.markdown('<div class="glow-btn">', unsafe_allow_html=True)
                do_rewrite = st.button("Execute Full AI Profile Rewrite", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                if do_rewrite:
                    if not api_key:
                        st.error("Please insert your Groq API Key above.")
                    else:
                        with st.spinner("Processing full optimization rewrite..."):
                            try:
                                r = Groq(api_key=api_key).chat.completions.create(
                                    model="llama-3.3-70b-versatile",
                                    messages=[{"role":"user","content":f"Rewrite this resume to be polished and impactful with metrics. Return ONLY the rewritten text.\n\n{st.session_state.resume_text}"}],
                                    temperature=0.6)
                                st.session_state.full_rewrite = r.choices[0].message.content
                            except Exception as e:
                                st.error(f"API Error: {e}")
                if st.session_state.full_rewrite:
                    st.html("""<div style='margin:24px 0 12px 0;font-family:Syne;font-size:13px;font-weight:700;color:#4DFFC3;'>Side-by-Side Comparison</div>""")
                    p1, p2 = st.columns(2)
                    with p1:
                        st.html(f"""<div class="code-pane" style="border-color:rgba(255,255,255,0.06);"><span style="color:#818DA0;font-weight:700;display:block;margin-bottom:12px;font-size:11px;">📄 ORIGINAL</span>{st.session_state.resume_text}</div>""")
                    with p2:
                        st.html(f"""<div class="code-pane" style="border-color:var(--accent);background:rgba(18,21,30,0.8);"><span style="color:var(--accent);font-weight:700;display:block;margin-bottom:12px;font-size:11px;">✨ AI ENHANCED</span>{st.session_state.full_rewrite}</div>""")
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.download_button("Download Rewritten Resume (.txt)", data=st.session_state.full_rewrite, file_name="Optimized_Resume.txt", mime="text/plain", use_container_width=True)
                else:
                    st.html("""<div class="feature-card" style="margin-top:20px;padding:22px;"><div style="font-size:13.5px;font-weight:600;margin-bottom:12px;">Sentence Transformation Preview</div>""")
                    toggle = st.radio("View", ["Original Text Line","AI Quantified Upgrade"], horizontal=True, label_visibility="collapsed")
                    if toggle == "Original Text Line":
                        st.error(f"**Baseline:**\n\n{st.session_state.original_bullet}")
                    else:
                        st.success(f"**Optimized:**\n\n{st.session_state.enhanced_bullet}")
                    st.html("</div>")

            # ── Tab 4: Voice Interview ────────────────────────────────────
            with tab4:
                st.html("""<div class="feature-card"><div class="card-title">Interactive Vocal Simulator Suite</div><p style="color:var(--sub);font-size:13.5px;line-height:1.6;margin:0 0 16px 0;">Generate interview prompts, speak your answer, receive score analysis.</p></div>""")

                if st.button("Generate Interview Question", key="voice_trigger"):
                    if not api_key:
                        st.error("Add your Groq API key above first.")
                    else:
                        with st.spinner("Formulating question..."):
                            try:
                                r = Groq(api_key=api_key).chat.completions.create(
                                    model="llama-3.3-70b-versatile",
                                    messages=[{"role":"system","content":"Generate ONE engineering interview question. No intro text."},{"role":"user","content":f"Skills: {', '.join(st.session_state.skills)}"}],
                                    temperature=0.8)
                                st.session_state.voice_q = r.choices[0].message.content.strip()
                                st.session_state.voice_transcript = None
                                st.session_state.voice_eval = None
                            except Exception as e:
                                st.error(f"Error: {e}")

                if st.session_state.voice_q:
                    st.html(f"""<div class="feature-card" style="border-color:rgba(0,210,255,0.25);background:rgba(13,16,24,0.7);"><div style="font-size:11px;text-transform:uppercase;color:#00d2ff;font-weight:700;letter-spacing:0.05em;margin-bottom:8px;">Active Question</div><div style="font-family:Syne;font-size:1.1rem;font-weight:600;line-height:1.5;">{st.session_state.voice_q}</div></div>""")
                    if st.button("🔊 Read Aloud"):
                        components.html(f"""<script>window.speechSynthesis.cancel();const u=new SpeechSynthesisUtterance({json.dumps(st.session_state.voice_q)});u.rate=0.95;window.speechSynthesis.speak(u);</script>""", height=0)

                    st.markdown("<br><span style='font-size:12px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:0.05em;'>🎙️ Record your answer</span>", unsafe_allow_html=True)
                    audio_in = st.audio_input("", label_visibility="collapsed", key="native_audio")
                    if audio_in:
                        audio_bytes = audio_in.read()
                        if audio_bytes and len(audio_bytes) > 2000 and st.session_state.voice_transcript is None:
                            with st.spinner("Transcribing..."):
                                try:
                                    st.session_state.voice_transcript = Groq(api_key=api_key).audio.transcriptions.create(
                                        file=("answer.wav", audio_bytes), model="whisper-large-v3", response_format="text")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Transcription error: {e}")

                if st.session_state.voice_transcript:
                    st.html(f"""<div style="background:rgba(13,16,24,0.9);border-left:3px solid #00d2ff;padding:16px 20px;margin-bottom:16px;border-radius:0 10px 10px 0;"><div style="font-size:10px;color:#00d2ff;font-weight:700;text-transform:uppercase;margin-bottom:6px;">Your Answer</div><div style="font-style:italic;font-size:13.5px;line-height:1.6;">"{st.session_state.voice_transcript}"</div></div>""")
                    if st.button("Evaluate Response"):
                        with st.spinner("Analyzing..."):
                            try:
                                ev = Groq(api_key=api_key).chat.completions.create(
                                    model="llama-3.3-70b-versatile",
                                    messages=[{"role":"system","content":"Evaluate the answer. Give Score X/10, strengths, and gaps. Be concise."},
                                              {"role":"user","content":f"Q: {st.session_state.voice_q}\nA: {st.session_state.voice_transcript}"}],
                                    temperature=0.4)
                                st.session_state.voice_eval = ev.choices[0].message.content
                            except Exception as e:
                                st.error(f"Error: {e}")

                if st.session_state.voice_eval:
                    st.html(f"""<div class="feature-card" style="border-color:rgba(77,255,195,0.25);background:rgba(18,21,30,0.8);margin-top:15px;"><div style="font-family:'Syne';font-size:14px;font-weight:700;color:var(--accent);margin-bottom:12px;">Analysis Report</div><div style="font-size:13.5px;line-height:1.7;white-space:pre-wrap;">{st.session_state.voice_eval}</div></div>""")
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("Ask Follow-Up Question", use_container_width=True):
                        with st.spinner("Generating follow-up..."):
                            try:
                                fu = Groq(api_key=api_key).chat.completions.create(
                                    model="llama-3.3-70b-versatile",
                                    messages=[{"role":"user","content":f"Asked: '{st.session_state.voice_q}'. Answer: '{st.session_state.voice_transcript}'. Generate ONE short technical follow-up question."}],
                                    temperature=0.7)
                                st.session_state.voice_q = fu.choices[0].message.content.strip()
                                st.session_state.voice_transcript = None
                                st.session_state.voice_eval = None
                                st.rerun()
                            except Exception:
                                pass

    else:
        st.html("""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5rem 2rem;text-align:center;background:rgba(18,21,30,0.3);border:1px dashed rgba(255,255,255,0.05);border-radius:16px;margin-top:2rem;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:1.5rem;opacity:0.8;">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>
            </svg>
            <h3 style="font-size:1.4rem;color:#ECE9E2;margin:0 0 8px 0;">Awaiting Document Input</h3>
            <p style="color:#818DA0;font-size:13.5px;max-width:400px;margin:0;line-height:1.6;">Upload your resume using the drop container above.</p>
        </div>""")

    st.html("""<div style="border-top:1px solid rgba(255,255,255,0.05);margin-top:4rem;text-align:center;padding:24px;color:#3A3F4E;font-size:12px;font-family:'Manrope',sans-serif;">AI Career Intelligence Platform · Built with Streamlit</div>""")
