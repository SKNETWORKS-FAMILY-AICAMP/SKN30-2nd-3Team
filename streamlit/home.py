import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="GRANDVISTA Hotel · Analytics",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 전역 CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500&display=swap');

.stApp { background:#0A1628; color:#F0EBE1; }

[data-testid="stSidebar"] { background:#060E1C !important; border-right:1px solid rgba(201,168,76,0.2); }
[data-testid="stSidebar"] * { color:#C9A84C !important; font-family:'Jost',sans-serif !important; letter-spacing:0.08em; }
[data-testid="stSidebarNav"] a { font-size:0.8rem !important; text-transform:uppercase; padding:0.6rem 1rem !important; border-radius:2px !important; }

.stButton > button { background:transparent; border:1px solid #C9A84C; color:#C9A84C; font-family:'Jost',sans-serif; letter-spacing:0.15em; text-transform:uppercase; font-size:0.75rem; padding:0.6rem 2rem; border-radius:0; transition:all 0.3s; }
.stButton > button:hover { background:#C9A84C; color:#0A1628; }

[data-testid="stMetric"] { background:#0F2040; border:1px solid rgba(201,168,76,0.13); padding:1.2rem 1.5rem; }
[data-testid="stMetricLabel"] { font-family:'Jost',sans-serif !important; letter-spacing:0.1em; text-transform:uppercase; font-size:0.7rem !important; color:#C9A84C !important; }
[data-testid="stMetricValue"] { font-family:'Cormorant Garamond',serif !important; font-size:2.2rem !important; color:#F0EBE1 !important; }

hr { border-color:rgba(201,168,76,0.2) !important; }
#MainMenu, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)


# ── 사이드바 ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div style='text-align:center;padding:2rem 0 1.5rem;'>
<div style='font-family:"Cormorant Garamond",serif;font-size:1.5rem;letter-spacing:0.3em;color:#C9A84C;text-transform:uppercase;'>GRANDVISTA</div>
<div style='font-family:"Jost",sans-serif;font-size:0.6rem;letter-spacing:0.4em;color:rgba(201,168,76,0.5);margin-top:4px;'>ANALYTICS SUITE</div>
</div>
<hr style='border-color:rgba(201,168,76,0.2);margin:0 1rem 1.5rem;'>
<div style='font-family:"Jost",sans-serif;font-size:0.65rem;letter-spacing:0.2em;color:rgba(201,168,76,0.4);padding:0 1rem 0.5rem;text-transform:uppercase;'>메뉴</div>
""", unsafe_allow_html=True)


# ── 히어로 섹션 ─────────────────────────────────────────────────────────
st.markdown("""
<div style='background:linear-gradient(135deg,#0F2040 0%,#0A1628 50%,#071020 100%);border:1px solid rgba(201,168,76,0.13);padding:5rem 4rem;'>
<div style='font-family:"Jost",sans-serif;font-size:0.65rem;letter-spacing:0.5em;color:#C9A84C;text-transform:uppercase;margin-bottom:1.2rem;'>&#8212; REVENUE &amp; OPERATIONS INTELLIGENCE &#8212;</div>
<h1 style='font-family:"Cormorant Garamond",serif;font-size:4.5rem;font-weight:300;line-height:1.1;color:#F0EBE1;margin:0 0 0.5rem 0;'>GRANDVISTA<br><span style='font-style:italic;color:#C9A84C;'>Hotel Analytics</span></h1>
<div style='width:60px;height:1px;background:#C9A84C;margin:1.5rem 0;'></div>
<p style='font-family:"Jost",sans-serif;font-size:1rem;font-weight:300;color:#B0A898;letter-spacing:0.05em;max-width:480px;line-height:1.8;margin:0;'>데이터 기반 예약 운영 인텔리전스.<br>취소 예측, 수익 보호, 객실 가동률 최적화.</p>
</div>
""", unsafe_allow_html=True)


# ── KPI 지표 ────────────────────────────────────────────────────────────
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "hotel_bookings_dummy.csv"   # home.py

@st.cache_data
def load_kpi():
    path = Path(DATA_PATH)
    if not path.exists():
        return None
    return pd.read_csv(path)

df = load_kpi()

st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

if df is not None:
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("총 예약 건수", f"{len(df):,}")
    c2.metric("전체 취소율", f"{df['is_canceled'].mean()*100:.1f}%")
    c3.metric("평균 ADR", f"${df['adr'].mean():.0f}")
    c4.metric("평균 리드타임", f"{df['lead_time'].mean():.0f}일")
    c5.metric("평균 주중 숙박", f"{df['stays_in_week_nights'].mean():.1f}박")
else:
    st.info(f"📂 `{DATA_PATH}` 파일을 앱 폴더에 넣으면 KPI 지표가 표시됩니다.")

st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
st.divider()

# ── 기능 카드 ─────────────────────────────────────────────────────────
st.markdown("""
<div style='margin:2rem 0 1rem;'>
<div style='font-family:"Jost",sans-serif;font-size:0.65rem;letter-spacing:0.4em;color:#C9A84C;text-transform:uppercase;margin-bottom:0.5rem;'>TOOLS</div>
<h2 style='font-family:"Cormorant Garamond",serif;font-size:2.2rem;font-weight:300;color:#F0EBE1;margin:0;'>분석 도구</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div style='background:#0F2040;border:1px solid rgba(201,168,76,0.13);padding:2rem;'>
<div style='font-size:2rem;margin-bottom:1rem;'>🔮</div>
<div style='font-family:"Jost",sans-serif;font-size:0.6rem;letter-spacing:0.35em;color:#C9A84C;text-transform:uppercase;margin-bottom:0.6rem;'>PREDICTION</div>
<div style='font-family:"Cormorant Garamond",serif;font-size:1.6rem;color:#F0EBE1;margin-bottom:0.8rem;'>예약 취소 예측</div>
<div style='font-family:"Jost",sans-serif;font-size:0.85rem;color:#8A8278;line-height:1.7;'>핵심 6개 피처 입력으로<br>취소 확률을 즉시 예측합니다.</div>
<div style='width:30px;height:1px;background:#C9A84C;margin-top:1.5rem;'></div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style='background:#0F2040;border:1px solid rgba(201,168,76,0.07);padding:2rem;'>
<div style='font-size:2rem;margin-bottom:1rem;'>📊</div>
<div style='font-family:"Jost",sans-serif;font-size:0.6rem;letter-spacing:0.35em;color:rgba(201,168,76,0.5);text-transform:uppercase;margin-bottom:0.6rem;'>ANALYTICS · SOON</div>
<div style='font-family:"Cormorant Garamond",serif;font-size:1.6rem;color:#6A6460;margin-bottom:0.8rem;'>수익 대시보드</div>
<div style='font-family:"Jost",sans-serif;font-size:0.85rem;color:#5A5450;line-height:1.7;'>ADR 트렌드, 채널별 수익,<br>시즌별 가동률 분석.</div>
<div style='width:30px;height:1px;background:rgba(201,168,76,0.2);margin-top:1.5rem;'></div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div style='background:#0F2040;border:1px solid rgba(201,168,76,0.07);padding:2rem;'>
<div style='font-size:2rem;margin-bottom:1rem;'>🎯</div>
<div style='font-family:"Jost",sans-serif;font-size:0.6rem;letter-spacing:0.35em;color:rgba(201,168,76,0.5);text-transform:uppercase;margin-bottom:0.6rem;'>INSIGHTS · SOON</div>
<div style='font-family:"Cormorant Garamond",serif;font-size:1.6rem;color:#6A6460;margin-bottom:0.8rem;'>피처 인사이트</div>
<div style='font-family:"Jost",sans-serif;font-size:0.85rem;color:#5A5450;line-height:1.7;'>취소에 영향을 주는<br>핵심 요인 심층 분석.</div>
<div style='width:30px;height:1px;background:rgba(201,168,76,0.2);margin-top:1.5rem;'></div>
</div>
""", unsafe_allow_html=True)

# ── 하단 ─────────────────────────────────────────────────────────────
st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style='text-align:center;font-family:"Jost",sans-serif;font-size:0.65rem;letter-spacing:0.2em;color:#3A3830;padding:1rem;'>
GRANDVISTA HOTEL · ANALYTICS SUITE · INTERNAL USE ONLY
</div>
""", unsafe_allow_html=True)
