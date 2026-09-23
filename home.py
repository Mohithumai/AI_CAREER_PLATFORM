import streamlit as st

def show_home(switch_page_callback):
    # ── GLOBAL LANDING PAGE CSS ──
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Manrope:wght@300;400;500;600;700&display=swap');
    
    .main, [data-testid="stAppViewContainer"] { background: #050608 !important; }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* SaaS Glass Card */
    .feature-card {
        background: rgba(18, 21, 30, 0.4);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 30px;
        transition: all 0.4s cubic-bezier(0.2, 0.95, 0.4, 1.1);
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, rgba(77,255,195,0.6), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .feature-card:hover::before {
        opacity: 1;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        border-color: rgba(77, 255, 195, 0.4);
        box-shadow: 0 20px 40px rgba(77, 255, 195, 0.12);
        background: rgba(18, 21, 30, 0.85);
    }
    .feature-card:hover .icon-box {
        background: rgba(77, 255, 195, 0.15);
        box-shadow: 0 0 20px rgba(77, 255, 195, 0.3);
    }
    
    .icon-box {
        margin-bottom: 20px;
        background: rgba(77, 255, 195, 0.05);
        width: 56px;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 14px;
        border: 1px solid rgba(77, 255, 195, 0.2);
        transition: all 0.3s ease;
    }
    
    /* Text Gradients */
    .text-gradient {
        background: linear-gradient(90deg, #4DFFC3 0%, #00d2ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .text-gradient-gold {
        background: linear-gradient(90deg, #FFBE57 0%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Comparison Table */
    .comp-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    .comp-table th, .comp-table td { padding: 16px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05); font-family: 'Manrope', sans-serif; color: #ECE9E2; }
    .comp-table th { font-family: 'Syne', sans-serif; font-weight: 700; color: #818DA0; }
    .comp-table tr:hover { background: rgba(255,255,255,0.02); }
    
    button[kind="primary"] {
        background: linear-gradient(135deg, #4DFFC3 0%, #00d2ff 100%) !important;
        color: #050608 !important;
        border-radius: 50px !important;
        padding: 14px 36px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    button[kind="primary"]:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(77, 255, 195, 0.35) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    col_hero_left, col_hero_right = st.columns([1.3, 1], gap="large")
    
    with col_hero_left:
        st.markdown("""
        <div style="padding-top: 2rem;">
            <div style="font-family:'Manrope',sans-serif;font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#4DFFC3;font-weight:600;margin-bottom:16px; display: flex; align-items: center; gap: 8px;">
                <span style="width: 8px; height: 8px; background: #4DFFC3; border-radius: 50%; display: inline-block; box-shadow: 0 0 10px #4DFFC3;"></span>
                Next-Gen Career Copilot Matrix v3.0
            </div>
            <h1 style="font-family:'Syne',sans-serif;font-size:4.2rem;font-weight:800;color:#ECE9E2;line-height:1.05;margin:0 0 20px 0;letter-spacing:-0.03em;">
                AI Career <span class="text-gradient">Intelligence</span> Platform
            </h1>
            <p style="font-family:'Manrope',sans-serif;font-size:1.15rem;color:#818DA0;max-width:540px;margin:0 0 35px 0;line-height:1.7;">
                Analyze your resume text against modern ATS criteria. Uncover optimization gaps, execute instant AI modifications, and practice with real-time vocal mock interviews.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Analyzer Platform", type="primary"):
            switch_page_callback("analyzer")

    with col_hero_right:
        st.markdown("""
        <style>
        .orb-container { display: flex; justify-content: center; align-items: center; height: 100%; min-height: 380px; perspective: 1000px; }
        .ai-neural-core {
            width: 320px; height: 320px;
            background: radial-gradient(circle at 30% 30%, rgba(77, 255, 195, 0.15), rgba(0, 210, 255, 0.05) 60%, transparent 80%),
                        linear-gradient(135deg, rgba(18, 21, 30, 0.9), rgba(5, 6, 8, 0.95));
            border: 1px solid rgba(77, 255, 195, 0.3); border-radius: 30px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5), inset 0 0 40px rgba(77, 255, 195, 0.1), 0 0 30px rgba(0, 210, 255, 0.15);
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            position: relative; animation: float 6s ease-in-out infinite; backdrop-filter: blur(20px);
        }
        .ai-neural-core::before {
            content: ''; position: absolute; width: 360px; height: 360px;
            border: 1px dashed rgba(77, 255, 195, 0.2); border-radius: 50%; animation: core-spin 20s linear infinite;
        }
        .ai-neural-core::after {
            content: ''; position: absolute; width: 400px; height: 400px;
            border: 1px solid rgba(0, 210, 255, 0.1); border-radius: 50%; animation: core-spin-reverse 30s linear infinite;
        }
        .core-pulse-node {
            width: 90px; height: 90px; background: linear-gradient(135deg, #4DFFC3 0%, #00d2ff 100%);
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 0 40px rgba(77, 255, 195, 0.6); animation: pulse-node 3s ease-in-out infinite alternate;
            position: relative; z-index: 2;
        }
        .core-status-text { margin-top: 24px; font-family: 'Syne', sans-serif; font-size: 13px; letter-spacing: 0.15em; color: #4DFFC3; text-transform: uppercase; font-weight: 700; z-index: 2; }
        .core-sub-text { font-family: 'Manrope', sans-serif; font-size: 11px; color: #818DA0; margin-top: 4px; z-index: 2; }
        @keyframes core-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes core-spin-reverse { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }
        @keyframes pulse-node { 0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(77, 255, 195, 0.4); } 100% { transform: scale(1.05); box-shadow: 0 0 50px rgba(0, 210, 255, 0.8); } }
        </style>
        
        <div class="orb-container">
            <div class="ai-neural-core">
                <div class="core-pulse-node">
                    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#050608" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <div class="core-status-text">AI Core Online</div>
                <div class="core-sub-text">Active ATS & Voice Engine</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── SECTION 2: STATS ──
    st.markdown("<div style='height:3rem;'></div>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    def stat_card(col, num, label):
        col.markdown(f"""
        <div style="text-align:center;padding: 20px; background: rgba(18,21,30,0.3); border-radius: 12px; border: 1px solid rgba(255,255,255,0.03);">
            <div style="font-family:'Syne',sans-serif;font-size:2.8rem;font-weight:800;color:#ECE9E2;">{num}</div>
            <div style="font-family:'Manrope',sans-serif;font-size:12px;text-transform:uppercase;letter-spacing:0.1em;color:#4DFFC3;margin-top:4px;">{label}</div>
        </div>""", unsafe_allow_html=True)
    stat_card(s1, "25k+", "Resumes Analyzed")
    stat_card(s2, "95%", "ATS Accuracy")
    stat_card(s3, "5", "AI Modules")
    stat_card(s4, "100+", "Interview Scenarios")

    # ── SECTION 3: FEATURE CARDS WITH VIBRANT SVGS ──
    st.markdown("""<div style="text-align:center;margin:5rem 0 3rem;"><h2 style="font-family:'Syne',sans-serif;font-size:2.5rem;color:#ECE9E2;">Everything you need to <span class="text-gradient-gold">get hired.</span></h2><p style="font-family:'Manrope',sans-serif;color:#818DA0;margin-top:10px;">Enterprise-grade AI modules built for modern tech placements.</p></div>""", unsafe_allow_html=True)
    
    f1, f2, f3 = st.columns(3)
    def feature(col, svg_code, title, desc):
        col.markdown(f"""
        <div class="feature-card">
            <div class="icon-box">{svg_code}</div>
            <h3 style="font-family:'Syne',sans-serif;font-size:1.3rem;color:#ECE9E2;margin:0 0 10px 0;">{title}</h3>
            <p style="font-family:'Manrope',sans-serif;font-size:14px;color:#818DA0;line-height:1.6;margin:0;">{desc}</p>
        </div>""", unsafe_allow_html=True)
    
    svg_ats = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'
    svg_jd = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>'
    svg_rewrite = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83"></path></svg>'
    svg_prep = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
    svg_voice = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v1a7 7 0 0 1-14 0v-1"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>'
    svg_insights = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4DFFC3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>'

    feature(f1, svg_ats, "ATS Deep Analysis", "Deep-scan your PDF layout structure, text layers, and technical skill clusters to calculate an exact baseline ATS compatibility score.")
    feature(f2, svg_jd, "Target JD Matching", "Compare your personal profile directly against target Job Descriptions to uncover critical keyword gaps instantly.")
    feature(f3, svg_rewrite, "Generative Rewriter", "Our FAANG-trained AI transforms passive project descriptions into high-impact, metric-driven professional achievements.")
    
    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)
    f4, f5, f6 = st.columns(3)
    feature(f4, svg_prep, "Contextual Mock Prep", "Generate hyper-specific technical interview questions based on the exact overlap between your resume and the target role.")
    feature(f5, svg_voice, "Live Voice AI Practice", "Interactive voice module: The system questions you verbally, transcribes your spoken answers in real-time, and scores your confidence.")
    feature(f6, svg_insights, "Career Progression", "Track your technical readiness depth, interview success probability, and resume progression metrics in a single interface.")

    # ── SECTION 4: INTERACTIVE WORKFLOW TIMELINE ──
    st.markdown("""
    <div style="margin:6rem 0;padding:50px 30px;background:linear-gradient(135deg, rgba(18,21,30,0.6) 0%, rgba(5,6,8,0.8) 100%);border:1px solid rgba(255,255,255,0.05);border-radius:24px;">
        <h3 style="font-family:'Syne',sans-serif;text-align:center;color:#ECE9E2;font-size:2rem;margin-bottom:10px;">The Intelligence Pipeline</h3>
        <p style="font-family:'Manrope',sans-serif;text-align:center;color:#818DA0;margin-bottom:40px;font-size:14px;">How our platform transforms your career profile in seconds</p>
        <div style="display:flex;justify-content:space-between;align-items:center;font-family:'Manrope',sans-serif;color:#ECE9E2;text-align:center;font-weight:600;font-size:13px;flex-wrap:wrap;gap:20px;">
            <div style="flex:1;min-width:140px;">
                <div style="width:45px;height:45px;background:rgba(77,255,195,0.1);color:#4DFFC3;border:1px solid rgba(77,255,195,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-family:'Syne';font-weight:700;">01</div>
                Upload PDF Resume
            </div>
            <div style="color:rgba(77,255,195,0.4);">──────</div>
            <div style="flex:1;min-width:140px;">
                <div style="width:45px;height:45px;background:rgba(77,255,195,0.1);color:#4DFFC3;border:1px solid rgba(77,255,195,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-family:'Syne';font-weight:700;">02</div>
                ATS Matrix Scan
            </div>
            <div style="color:rgba(77,255,195,0.4);">──────</div>
            <div style="flex:1;min-width:140px;">
                <div style="width:45px;height:45px;background:rgba(77,255,195,0.1);color:#4DFFC3;border:1px solid rgba(77,255,195,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-family:'Syne';font-weight:700;">03</div>
                AI Content Rewrite
            </div>
            <div style="color:rgba(77,255,195,0.4);">──────</div>
            <div style="flex:1;min-width:140px;">
                <div style="width:45px;height:45px;background:rgba(255,190,87,0.1);color:#FFBE57;border:1px solid rgba(255,190,87,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-family:'Syne';font-weight:700;">04</div>
                Voice Mock Audit
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 5: COMPARISON TABLE ──
    st.markdown("""
    <div style="margin:6rem auto; max-width: 850px;">
        <h2 style="font-family:'Syne',sans-serif;font-size:2.3rem;color:#ECE9E2;text-align:center;margin-bottom:1rem;">Platform Competitiveness</h2>
        <p style="font-family:'Manrope',sans-serif;text-align:center;color:#818DA0;margin-bottom:2.5rem;font-size:14px;">See how our advanced AI agent architecture compares to legacy screening tools</p>
        <table class="comp-table">
            <tr>
                <th style="text-align:left;">Core Feature Matrix</th>
                <th style="color:#4DFFC3;">Our AI Platform</th>
                <th>Traditional ATS Filters</th>
            </tr>
            <tr><td style="text-align:left;">Real-Time Voice Mock Interviews</td><td>✅ Advanced (STT/TTS)</td><td>❌ None</td></tr>
            <tr><td style="text-align:left;">Contextual Job Description Matching</td><td>✅ Semantic Engine</td><td>❌ Exact String Match Only</td></tr>
            <tr><td style="text-align:left;">Generative Bullet-Point Rewrites</td><td>✅ Llama 3 Powered</td><td>❌ None</td></tr>
            <tr><td style="text-align:left;">Dynamic Interview Scenario Generation</td><td>✅ Custom Tailored</td><td>❌ Static Question Bank</td></tr>
            <tr><td style="text-align:left;">Automated PDF Text Extraction</td><td>✅ Multi-layer Parser</td><td>✅ Basic Parser</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 6: FINAL CTA ──
    st.markdown("""
    <div style="text-align:center;padding:5rem 2rem;background:linear-gradient(180deg, rgba(77,255,195,0.03) 0%, transparent 100%);border-top:1px solid rgba(77,255,195,0.1);margin-top:4rem;">
        <h3 style="font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:#ECE9E2;margin-bottom:1rem;">Ready to upgrade your career?</h3>
        <p style="font-family:'Manrope',sans-serif;color:#818DA0;margin-bottom:2rem;font-size:1.1rem;">Stop guessing what recruiters want. Let your personal AI copilot build your path.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns([1, 1.2, 1])
    with col5:
        if st.button("Get Started Now", type="primary", use_container_width=True):
            switch_page_callback("analyzer")