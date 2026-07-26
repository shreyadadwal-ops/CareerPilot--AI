import streamlit as st
import streamlit.components.v1 as components


def add_bg_and_css():

    st.markdown(
        """
        <style>

        iframe[title="st.iframe"] {
            position: fixed !important;
            top: 0;
            left: 0;
            width: 100vw !important;
            height: 100vh !important;
            z-index: -1;
            border: none;
        }

        .stApp {
            background: transparent;
        }

        /* ---------- HEADINGS ---------- */

        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }

        p {
            color: white !important;
        }

        label,
        label p {
            color: white !important;
            font-weight: bold !important;
        }

        /* ---------- SIDEBAR ---------- */

        section[data-testid="stSidebar"] {
            background: rgba(8,15,30,0.90);
        }

        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* ---------- INPUT BOXES ---------- */

        .stTextInput input,
        .stTextArea textarea {
            background-color: rgba(255,255,255,0.95) !important;
            color: black !important;
            border-radius: 8px;
        }

        /* ---------- FILE UPLOADER ---------- */

        [data-testid="stFileUploader"] {
            color: white !important;
        }

        [data-testid="stFileUploader"] small {
            color: white !important;
        }

        /* ---------- METRIC CARDS ---------- */

        [data-testid="stMetric"] {
            background: rgba(18,25,40,0.60);
            border-radius: 12px;
            padding: 15px;
        }

        [data-testid="stMetricLabel"] {
            color: white !important;
        }

        [data-testid="stMetricValue"] {
            color: #00E5FF !important;
            font-weight: bold;
        }

        /* ---------- BUTTON ---------- */

        .stButton button {
            background-color: #00BFFF !important;
            color: white !important;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }

        /* ---------- ALERTS ---------- */

        [data-testid="stAlert"] {
            color: white !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    components.html(
        """
        <style>
        html, body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: #030815;
        }

        #network-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        </style>

        <canvas id="network-bg"></canvas>

        <script>

        const canvas = document.getElementById('network-bg');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particles = [];

        const numParticles = 110;

        for (let i = 0; i < numParticles; i++) {

            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.4,
                vy: (Math.random() - 0.5) * 0.4,
                r: Math.random() * 1.5 + 1
            });

        }

        function draw() {

            ctx.fillStyle = "#030815";
            ctx.fillRect(0,0,canvas.width,canvas.height);

            for (let i=0;i<particles.length;i++) {

                let p = particles[i];

                p.x += p.vx;
                p.y += p.vy;

                if (p.x < 0 || p.x > canvas.width)
                    p.vx *= -1;

                if (p.y < 0 || p.y > canvas.height)
                    p.vy *= -1;

                ctx.beginPath();
                ctx.arc(p.x,p.y,p.r,0,Math.PI*2);

                ctx.fillStyle="#3fd0ff";
                ctx.shadowColor="#3fd0ff";
                ctx.shadowBlur=8;

                ctx.fill();

                ctx.shadowBlur=0;

                for (let j=i+1;j<particles.length;j++) {

                    let p2 = particles[j];

                    let dist = Math.hypot(
                        p.x-p2.x,
                        p.y-p2.y
                    );

                    if (dist < 140) {

                        ctx.beginPath();

                        ctx.moveTo(p.x,p.y);

                        ctx.lineTo(p2.x,p2.y);

                        ctx.strokeStyle=`rgba(63,208,255,${
                            1-dist/140
                        })`;

                        ctx.lineWidth=0.6;

                        ctx.stroke();

                    }

                }

            }

            requestAnimationFrame(draw);

        }

        draw();

        window.addEventListener('resize',()=>{

            canvas.width=window.innerWidth;
            canvas.height=window.innerHeight;

        });

        </script>
        """,
        height=0,
    )