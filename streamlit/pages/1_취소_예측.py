import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="취소 예측 · GRANDVISTA",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 전역 CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500&display=swap');

.stApp { background: #0A1628; color: #F0EBE1; }

[data-testid="stSidebar"] {
    background: #060E1C !important;
    border-right: 1px solid #C9A84C33;
}
[data-testid="stSidebar"] * {
    color: #C9A84C !important;
    font-family: 'Jost', sans-serif !important;
    letter-spacing: 0.08em;
}
[data-testid="stSidebarNav"] a {
    font-size: 0.8rem !important;
    text-transform: uppercase;
    padding: 0.6rem 1rem !important;
    border-radius: 2px !important;
}

/* 셀렉트박스 */
[data-testid="stSelectbox"] label,
[data-testid="stSlider"] label,
[data-testid="stNumberInput"] label {
    font-family: 'Jost', sans-serif !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: #C9A84C !important;
}
.stSelectbox > div > div {
    background: #0F2040 !important;
    border: 1px solid #C9A84C33 !important;
    border-radius: 0 !important;
    color: #F0EBE1 !important;
}
.stNumberInput > div > div > input {
    background: #0F2040 !important;
    border: 1px solid #C9A84C33 !important;
    border-radius: 0 !important;
    color: #F0EBE1 !important;
}
/* 슬라이더 트랙 */
[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    background: #C9A84C !important;
    border-color: #C9A84C !important;
}

/* 예측 버튼 */
.stButton > button {
    background: #C9A84C !important;
    border: none !important;
    color: #0A1628 !important;
    font-family: 'Jost', sans-serif !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.75rem 3rem !important;
    border-radius: 0 !important;
    width: 100% !important;
    transition: all 0.3s !important;
}
.stButton > button:hover {
    background: #E8C86A !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px #C9A84C44 !important;
}

hr { border-color: #C9A84C22 !important; }
#MainMenu, footer, header { visibility: hidden; }

/* 결과 카드 */
.result-high {
    background: linear-gradient(135deg, #2D0A0A, #1A0606);
    border: 1px solid #EF4444;
    padding: 2rem 2.5rem;
}
.result-low {
    background: linear-gradient(135deg, #0A2D15, #061A0C);
    border: 1px solid #22C55E;
    padding: 2rem 2.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 2rem 0 1.5rem;'>
        <div style='font-family:"Cormorant Garamond",serif; font-size:1.5rem;
                    letter-spacing:0.3em; color:#C9A84C; text-transform:uppercase;'>
            GRANDVISTA
        </div>
        <div style='font-family:"Jost",sans-serif; font-size:0.6rem;
                    letter-spacing:0.4em; color:#C9A84C88; margin-top:4px;'>
            ANALYTICS SUITE
        </div>
    </div>
    <hr style='border-color:#C9A84C33; margin: 0 1rem 1.5rem;'>
    <div style='font-family:"Jost",sans-serif; font-size:0.65rem;
                letter-spacing:0.2em; color:#C9A84C66; padding: 0 1rem 0.5rem;
                text-transform:uppercase;'>
        메뉴
    </div>
    """, unsafe_allow_html=True)

# ── 경로 설정 ─────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT_DIR / "modeling" / "saved" / "best_mlp.pkl"
DATA_PATH = ROOT_DIR / "dataset" / "preprocessed" / "hotel_bookings_dummy.csv"

# ── 학습 데이터 기반 51개 피처 기본값 ──────────────────────────────────
DEFAULT_VALUES = {
    'lead_time': 104,
    'stays_in_weekend_nights': 1,
    'stays_in_week_nights': 3,
    'is_repeated_guest': 0,
    'previous_cancellations': 0,
    'previous_bookings_not_canceled': 0,
    'booking_changes': 0,
    'days_in_waiting_list': 0,
    'adr': 102.0,
    'required_car_parking_spaces': 0,
    'total_of_special_requests': 1,
    'diff_reserved_room_type': 0,
    'is_agent': 1,
    'is_company': 0,
    'is_city_hotel': 1,
    'arrival_date_month_August': 0,
    'arrival_date_month_December': 0,
    'arrival_date_month_February': 0,
    'arrival_date_month_January': 0,
    'arrival_date_month_July': 0,
    'arrival_date_month_June': 0,
    'arrival_date_month_March': 0,
    'arrival_date_month_May': 0,
    'arrival_date_month_November': 0,
    'arrival_date_month_October': 0,
    'arrival_date_month_September': 0,
    'meal_FB': 0,
    'meal_HB': 0,
    'meal_SC': 0,
    'meal_Undefined': 0,
    'market_segment_Complementary': 0,
    'market_segment_Corporate': 0,
    'market_segment_Direct': 0,
    'market_segment_Groups': 0,
    'market_segment_Offline TA/TO': 0,
    'market_segment_Online TA': 0,
    'market_segment_Undefined': 0,
    'distribution_channel_Direct': 0,
    'distribution_channel_GDS': 0,
    'distribution_channel_TA/TO': 1,
    'distribution_channel_Undefined': 0,
    'deposit_type_Non Refund': 0,
    'deposit_type_Refundable': 0,
    'customer_type_Group': 0,
    'customer_type_Transient': 1,
    'customer_type_Transient-Party': 0,
    'guest_type_Group': 1,
    'guest_type_Single': 0,
    'guest_type_Undefined': 0,
    'country_region_OTH': 0,
    'country_region_PRT': 0,
}
FEATURE_ORDER = list(DEFAULT_VALUES.keys())

# ── 모델 로드 ──────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    path = Path(MODEL_PATH)
    if not path.exists():
        return None, "no_file"
    try:
        return joblib.load(path), "ok"
    except ModuleNotFoundError:
        return None, "no_torch"
    except Exception as e:
        return None, str(e)

@st.cache_resource
def load_scaler():
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["is_canceled"])
    y = df["is_canceled"]
    X_train, _, _, _ = train_test_split(X, y, test_size=0.3, random_state=1004)
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    return scaler

def build_input_df(user: dict) -> pd.DataFrame:
    row = DEFAULT_VALUES.copy()
    row.update(user)
    return pd.DataFrame([row])[FEATURE_ORDER]

# ── 페이지 헤더 ──────────────────────────────────────────────────────
st.markdown("""
<div style='
    border-bottom: 1px solid #C9A84C22;
    padding: 2.5rem 0 2rem;
    margin-bottom: 2.5rem;
'>
    <div style='
        font-family: "Jost", sans-serif;
        font-size: 0.6rem; letter-spacing: 0.45em;
        color: #C9A84C; text-transform: uppercase;
        margin-bottom: 0.6rem;
    '>PREDICTION TOOL · INTERNAL</div>
    <h1 style='
        font-family: "Cormorant Garamond", serif;
        font-size: 3rem; font-weight: 300;
        color: #F0EBE1; margin: 0;
        line-height: 1.2;
    '>예약 취소 <span style='font-style:italic; color:#C9A84C;'>예측</span></h1>
    <p style='
        font-family: "Jost", sans-serif;
        font-size: 0.85rem; font-weight: 300;
        color: #6A6460; letter-spacing: 0.05em;
        margin: 0.8rem 0 0;
    '>6가지 핵심 지표 입력 → 취소 확률 즉시 산출</p>
</div>
""", unsafe_allow_html=True)

model, model_status = load_model()

# ── 2단 레이아웃: 입력 폼 | 결과 ─────────────────────────────────────
left, gap, right = st.columns([5, 1, 6])

with left:
    st.markdown("""
    <div style='
        font-family: "Jost", sans-serif;
        font-size: 0.6rem; letter-spacing: 0.35em;
        color: #C9A84C88; text-transform: uppercase;
        margin-bottom: 1.5rem;
    '>── 예약 정보 입력</div>
    """, unsafe_allow_html=True)

    # 1. 보증금 유형
    deposit = st.selectbox(
        "보증금 유형 (Deposit Type)",
        ["No Deposit", "Non Refund", "Refundable"],
        help="Non Refund일수록 취소 위험이 높은 경향이 있습니다."
    )

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # 2. 리드타임
    lead_time = st.slider(
        "예약 리드타임 (Lead Time, 일)",
        min_value=0, max_value=500, value=60,
        help="체크인 날짜까지 남은 일수"
    )

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # 3. ADR
    adr = st.number_input(
        "일평균 객실 요금 (ADR, USD)",
        min_value=0.0, max_value=2000.0, value=100.0, step=5.0,
        help="Average Daily Rate — 할인 및 부가 서비스 제외한 순 객실 요금"
    )

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # 4. 특별 요청 수
    special_requests = st.slider(
        "특별 요청 수 (Special Requests)",
        min_value=0, max_value=5, value=1,
        help="베개 종류, 층 선택, 침대 배치 등 고객 요청 건수"
    )

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # 5. 마케팅 채널
    segment_options = [
        "Online TA", "Offline TA/TO", "Direct",
        "Corporate", "Groups", "Complementary"
    ]
    segment = st.selectbox("마케팅 채널 (Market Segment)", segment_options)

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # 6. 주중 숙박 일수
    week_nights = st.slider(
        "주중 숙박 일수 (Week Nights)",
        min_value=0, max_value=20, value=2,
        help="월~목 숙박 일수"
    )

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    predict_btn = st.button("✦ 취소 확률 예측", type="primary")


# ── 결과 패널 ─────────────────────────────────────────────────────────
with right:
    st.markdown("""
    <div style='
        font-family: "Jost", sans-serif;
        font-size: 0.6rem; letter-spacing: 0.35em;
        color: #C9A84C88; text-transform: uppercase;
        margin-bottom: 1.5rem;
    '>── 예측 결과</div>
    """, unsafe_allow_html=True)

    if not predict_btn:
        st.markdown("""
        <div style='
            background: #0F2040;
            border: 1px dashed #C9A84C22;
            padding: 4rem 2.5rem;
            text-align: center;
        '>
            <div style='font-size: 3rem; margin-bottom: 1rem; opacity: 0.3;'>🔮</div>
            <div style='
                font-family: "Jost", sans-serif;
                font-size: 0.75rem; letter-spacing: 0.2em;
                color: #3A3830; text-transform: uppercase;
            '>좌측 정보 입력 후<br>예측 버튼을 눌러주세요</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        # 입력값 조립
        user = {
            "lead_time": lead_time,
            "adr": float(adr),
            "stays_in_week_nights": week_nights,
            "total_of_special_requests": special_requests,
            "deposit_type_Non Refund": 1 if deposit == "Non Refund" else 0,
            "deposit_type_Refundable": 1 if deposit == "Refundable" else 0,
            "market_segment_Online TA":   1 if segment == "Online TA" else 0,
            "market_segment_Offline TA/TO": 1 if segment == "Offline TA/TO" else 0,
            "market_segment_Direct":       1 if segment == "Direct" else 0,
            "market_segment_Corporate":    1 if segment == "Corporate" else 0,
            "market_segment_Groups":       1 if segment == "Groups" else 0,
            "market_segment_Complementary":1 if segment == "Complementary" else 0,
        }
        input_df = build_input_df(user)

        if model is None:
            if model_status == "no_file":
                st.markdown(f"""
                <div style='background:#0F2040; border:1px solid #C9A84C33; padding:2rem;'>
                    <div style='font-family:"Jost",sans-serif; font-size:0.75rem;
                                color:#C9A84C; letter-spacing:0.1em;'>
                        ⚠ 모델 파일 없음
                    </div>
                    <div style='font-family:"Jost",sans-serif; font-size:0.85rem;
                                color:#8A8278; margin-top:0.5rem;'>
                        <code style='color:#C9A84C;'>{MODEL_PATH}</code> 파일을<br>
                        앱 폴더에 넣어주세요.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif model_status == "no_torch":
                st.markdown("""
                <div style='background:#0F2040; border:1px solid #C9A84C33; padding:2rem;'>
                    <div style='font-family:"Jost",sans-serif; font-size:0.75rem;
                                color:#C9A84C; letter-spacing:0.1em;'>
                        ⚠ PyTorch 설치 필요
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.code("pip install torch", language="bash")
        else:
            with st.spinner(""):
                try:
                    import torch
                    import torch.nn.functional as F

                    scaler = load_scaler()
                    x_scaled = scaler.transform(input_df)
                    x = torch.tensor(x_scaled, dtype=torch.float32)
                    model.eval()
                    with torch.no_grad():
                        logits = model(x)
                        if logits.shape[1] == 1:
                            cancel_prob = torch.sigmoid(logits)[0, 0].item() * 100
                        else:
                            cancel_prob = F.softmax(logits, dim=1)[0, 1].item() * 100
                    stay_prob = 100 - cancel_prob
                    pred = 1 if cancel_prob >= 50 else 0

                    # 결과 카드
                    if pred == 1:
                        result_class = "result-high"
                        verdict_icon = "✕"
                        verdict_text = "취소 가능성 높음"
                        verdict_color = "#EF4444"
                        main_prob = cancel_prob
                        main_label = "취소 확률"
                    else:
                        result_class = "result-low"
                        verdict_icon = "✓"
                        verdict_text = "취소 가능성 낮음"
                        verdict_color = "#22C55E"
                        main_prob = stay_prob
                        main_label = "유지 확률"

                    st.markdown(f"""
                    <div class='{result_class}'>
                        <div style='display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem;'>
                            <div style='
                                width: 48px; height: 48px;
                                border: 2px solid {verdict_color};
                                border-radius: 50%;
                                display: flex; align-items: center; justify-content: center;
                                font-size: 1.3rem; color: {verdict_color};
                                font-family: "Jost", sans-serif;
                            '>{verdict_icon}</div>
                            <div>
                                <div style='
                                    font-family: "Jost", sans-serif;
                                    font-size: 0.6rem; letter-spacing: 0.35em;
                                    color: {verdict_color}88; text-transform: uppercase;
                                '>PREDICTION RESULT</div>
                                <div style='
                                    font-family: "Cormorant Garamond", serif;
                                    font-size: 1.5rem; color: {verdict_color};
                                    margin-top: 2px;
                                '>{verdict_text}</div>
                            </div>
                        </div>
                        <div style='
                            font-family: "Cormorant Garamond", serif;
                            font-size: 5rem; font-weight: 300;
                            color: {verdict_color}; line-height: 1;
                            margin-bottom: 0.3rem;
                        '>{main_prob:.1f}<span style='font-size:2rem;'>%</span></div>
                        <div style='
                            font-family: "Jost", sans-serif;
                            font-size: 0.65rem; letter-spacing: 0.2em;
                            color: {verdict_color}88; text-transform: uppercase;
                        '>{main_label}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # 확률 바
                    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div style='margin: 0;'>
                        <div style='
                            font-family: "Jost", sans-serif;
                            font-size: 0.6rem; letter-spacing: 0.25em;
                            color: #C9A84C88; text-transform: uppercase;
                            margin-bottom: 0.5rem;
                        '>확률 분포</div>
                        <div style='
                            display: flex; height: 8px;
                            background: #0A1628;
                            border: 1px solid #C9A84C22;
                        '>
                            <div style='
                                width: {cancel_prob:.1f}%;
                                background: #EF4444;
                                transition: width 0.5s;
                            '></div>
                            <div style='
                                width: {stay_prob:.1f}%;
                                background: #22C55E;
                            '></div>
                        </div>
                        <div style='
                            display: flex; justify-content: space-between;
                            font-family: "Jost", sans-serif;
                            font-size: 0.7rem; color: #8A8278;
                            margin-top: 0.4rem;
                        '>
                            <span>취소 {cancel_prob:.1f}%</span>
                            <span>유지 {stay_prob:.1f}%</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # 입력 요약
                    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
                    st.markdown("""
                    <div style='
                        font-family: "Jost", sans-serif;
                        font-size: 0.6rem; letter-spacing: 0.3em;
                        color: #C9A84C88; text-transform: uppercase;
                        border-top: 1px solid #C9A84C22;
                        padding-top: 1.2rem; margin-bottom: 0.8rem;
                    '>입력 요약</div>
                    """, unsafe_allow_html=True)

                    summary_data = {
                        "보증금 유형": deposit,
                        "리드타임": f"{lead_time}일",
                        "ADR": f"${adr:.0f}",
                        "특별 요청": f"{special_requests}건",
                        "마케팅 채널": segment,
                        "주중 숙박": f"{week_nights}박",
                    }
                    for k, v in summary_data.items():
                        st.markdown(f"""
                        <div style='
                            display: flex; justify-content: space-between;
                            font-family: "Jost", sans-serif;
                            font-size: 0.8rem;
                            padding: 0.35rem 0;
                            border-bottom: 1px solid #C9A84C11;
                        '>
                            <span style='color: #6A6460; letter-spacing:0.05em;'>{k}</span>
                            <span style='color: #F0EBE1;'>{v}</span>
                        </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"예측 오류: {e}")

# ── 하단 안내 ─────────────────────────────────────────────────────────
st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style='
    font-family: "Jost", sans-serif;
    font-size: 0.65rem; letter-spacing: 0.15em;
    color: #2A2820;
'>
    나머지 45개 피처는 학습 데이터 기반 기본값으로 자동 적용됩니다.
    예측 결과는 참고용이며 최종 판단은 담당자 재량에 따릅니다.
</div>
""", unsafe_allow_html=True)