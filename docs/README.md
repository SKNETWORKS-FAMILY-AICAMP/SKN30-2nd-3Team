# 🏨 호텔 예약 취소 예측 및 운영 최적화 분석

온라인 예약 플랫폼의 확산으로 간소화된 예약/취소 절차 속에서, 호텔의 예약 변동성과 노쇼(No-show) 리스크를 방어하기 위한 프로젝트입니다. 내부 예약 데이터에 날씨, 환율 변동 등 거시적 외부 환경 요인을 결합하여, 보다 정교한 취소 예측 모델(머신러닝 & 딥러닝)을 구축하고 데이터 기반의 객실 운영 최적화 전략을 제안합니다.

---

## 팀원 및 역할 분담 (Team)
- **박세빈**: 프로젝트 총괄, SQL 테이블 구축 및 ERD 작성, 발표자료 제작
- **김효선**: 데이터 전처리 및 외부 환경 데이터(환율, 날씨, 파생 변수 등) 검토 
- **남태식**: 탐색적 데이터 분석(EDA) 및 데이터 시각화 자료 생성
- **이동욱**: 머신러닝(ML) 알고리즘 적용 및 모델링 구축
- **정민규**: 딥러닝(DL) 알고리즘 적용 및 모델 성능 비교 평가

---

## 프로젝트 개요

온라인 예약 플랫폼의 확산으로 호텔 예약과 취소 절차가 간소화되면서 예약 취소율 또한 증가하고 있으며, 이는 객실 운영 계획과 호텔 운영 효율성에 영향을 미치는 주요 관리 요소로 인식되고 있다. 특히 예약 취소는 객실 점유율 예측의 불확실성을 높이고, 운영 자원의 비효율로 이어질 가능성이 있다.

본 프로젝트는 호텔 예약 데이터를 기반으로 고객의 예약 행동 패턴과 예약 취소 요인을 분석하고, 머신러닝 기반 예측 모델을 통해 예약 취소 여부를 예측함으로써 데이터 기반 호텔 운영 전략 수립 가능성을 제시하고자 한다. 또한 추가적으로 노쇼(No-show) 고객 특성을 탐색적으로 분석하여 운영 개선 방향을 함께 도출하고자 한다.

---

## 배경 및 필요성

온라인 예약 플랫폼과 모바일 예약 서비스의 확산으로 호텔 예약 과정은 과거보다 훨씬 간편해졌으며, 고객은 다양한 숙박 옵션을 손쉽게 비교하고 예약할 수 있게 되었다. 그러나 이러한 편의성 증가는 동시에 예약 취소 또한 쉽게 이루어질 수 있는 환경을 만들었으며, 호텔 운영 측면에서는 예약 변동성 관리의 중요성이 더욱 커지고 있다.

특히 예약 취소와 노쇼(No-show)는 객실 점유율 예측의 불확실성을 높이고, 객실 운영 계획·인력 운영·수익 관리 등 호텔 운영 전반에 영향을 미칠 수 있다. 또한 예약금 제도와 같은 운영 정책 역시 이러한 운영 손실을 최소화하기 위한 관리 수단으로 활용되고 있다.

이에 따라 호텔 입장에서는 단순히 예약 건수를 확보하는 것을 넘어, 어떤 고객이 예약을 취소하거나 노쇼를 발생시키는지에 대한 패턴을 파악하고 사전에 대응할 수 있는 운영 전략의 필요성이 점차 증가하고 있다.

본 프로젝트는 이러한 문제 인식을 바탕으로 호텔 예약 취소 및 노쇼 패턴을 분석하고, 고객 예약 행동 특성을 기반으로 보다 효율적인 운영 전략과 데이터 기반 의사결정 지원 가능성을 제시하고자 한다.

---

## 프로젝트 목표 (Goals)
1. **핵심 목표**: 호텔 예약 취소 여부를 예측하는 모델을 구축하고, 예약 취소에 영향을 미치는 핵심 요인을 분석하여 데이터 기반 호텔 운영 전략을 제안.
2. **세부 목표**:
    - 데이터 시각화를 통한 예약 취소 패턴 분석
    - 예약 리드타임, 예약금 유형, 고객 유형 등 핵심 변수 영향 분석
    - 머신러닝 알고리즘 간 예측 성능 비교 및 모델 평가
    - 취소 위험 고객군 식별 및 대응 전략 제안
    - 노쇼(No-show) 고객 특성에 대한 탐색적 분석 수행

---

## 기대효과

본 프로젝트를 통해 호텔 예약 취소 패턴과 고객 행동 특성을 파악함으로써 예약 취소 위험도가 높은 고객군을 사전에 식별할 수 있으며, 이를 기반으로 보다 효율적인 객실 운영 및 데이터 기반 의사결정 지원 가능성을 제시할 수 있다.

또한 예약 리드타임, 예약금 유형, 예약 채널 등 주요 변수 분석 결과를 바탕으로 예약 정책 개선, 고객 맞춤형 대응 전략, 운영 효율성 향상 방안 등 실질적인 운영 인사이트 도출이 가능할 것으로 기대된다.

아울러 추가적인 노쇼(No-show) 패턴 분석을 통해 호텔 운영 리스크 관리 측면의 활용 가능성 또한 함께 제시하고자 한다.

---

## WBS

| 기간 | 작업 내용 |
|------|-----------|
| 5/18 (월) | 데이터셋 최종 선정, 외부 데이터 수집, 역할 분담 및 Git 구조 설계 |
| 5/19 (화) ~ 5/21 (수) | 데이터 병합 및 전처리, EDA 수행, Feature Engineering 및 ML/DL 모델링 착수 |
| 5/22 (목) | 모델 성능 개선 및 메인 모델 선정, 핵심 변수 분석, 시각화 기반 인사이트 및 운영 전략 도출 |
| 5/23 (금) | 발표자료 제작 및 최종 정리 |

---

## 기술 스택

### 💻 Core Frameworks
![Python](https://shields.io/badge/Python%203.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://shields.io/badge/Scikit--Learn%201.8.0-F7931E?style=for-the-badge&logo=Scikit-Learn&logoColor=white)
![PyTorch](https://shields.io/badge/PyTorch%202.12.0-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white)

### 🚀 Machine Learning Models
<div>
    <img src="/docs/images/XGBoost.png" height="35" alt="XGBoost"/>
    <img src="/docs/images/LightGBM.png" height="35" alt="LightGBM"/>
    <img src="/docs/images/CatBoost.png" height="35" alt="CatBoost"/>
</div>

### 📦 Data Pipeline
![Pandas](https://shields.io/badge/pandas%203.0.3-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://shields.io/badge/numpy%202.4.5-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://shields.io/badge/scipy%201.17.1-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![Imbalanced-Learn](https://shields.io/badge/Imbalanced--Learn%200.14.1-F0A422?style=for-the-badge)

### 📊 Visualization
<div>
    <img src="/docs/images/Matplotlib.png" height="30" alt="Matplotlib"/>
    <img src="/docs/images/Seaborn.png" height="30" alt="Seaborn"/>
</div>

---

## 데이터 전처리

### 📌 핵심 전처리 방향

* **품질 최적화**: 국적 불명 488건 제거 및 미성년/대행사 누락값 무결성 처리 (최종 118,902행)
* **차원 축소**: 불필요한 도착 연/일 및 객실 코드를 제거하여 기존 32개 열을 24개 열로 압축
* **도메인 피처 생성**: 투숙객 유형(guest_type), 객실 변경 여부(diff_reserved_room_type) 등 모델 해석력을 높이는 파생 변수 4종 확보
* **데이터 누수 방지**: 타겟 사후 변수(reservation_status 등)를 전면 배제하여 예측 모델 유효성 보장

### 📊 전처리 전/후 데이터 구조 비교

| 구분 | 전처리 전 (Raw Data) | 전처리 후 | 변동 사항 |
|---|---|---|---|
| 행 (Rows) | 119,390개 | 118,902개 | 불확실 국적 데이터 삭제 (-488행) |
| 열 (Columns) | 32개 | 24개 | 날짜/원본 피처 제거 및 파생 변수 추가 |
| 타겟 (Target) | is_canceled (int64) | is_canceled (int64) | 변동 없음 (이진 분류 문제) |

---

## ERD

<img src="ERD.png" width="700"/>

---

## 모델링

### 1. 모델 선정 및 불균형 데이터 처리
* **클래스 불균형 해결**: 타겟 변수(`is_canceled`)의 불균형 문제를 해결하기 위해 `Imbalanced-Learn` 패키지를 활용, 오버샘플링(SMOTE) 및 전처리를 수행하여 모델의 예측 편향을 방지했습니다.
* **앙상블 및 딥러닝 최적화**: 정형 데이터 최적화 알고리즘인 **XGBoost, Random Forest**를 교차 검증하며 최적의 하이퍼파라미터를 탐색했고, 거시적 외부 변수(날씨, 환율 등) 결합에 따른 비선형 패턴 포착을 위해 **PyTorch 기반의 MLP** 모델을 구축하여 성능을 비교·평가했습니다.
* **최종 모델(Final Model) 도출**: 개별 모델들의 예측력을 결합하고 과적합을 방지하기 위해 앙상블 기반의 **Final Model**을 구축하여 가장 우수한 성능을 확보했습니다.

### 2. 모델 성능 비교 평가
호텔 수익 관리(Revenue Management) 측면에서 취소 위험 고객을 정확히 식별(Recall)하면서도 오예측으로 인한 리스크를 최소화하기 위해 **Recall**과 **F1-Score**를 주요 지표로 평가했습니다.

| 모델 (구분) | Accuracy (정확도) | Recall (재현율) | F1-Score (종합점수) |
| :--- | :---: | :---: | :---: |
| 🏆 **Final model** | **0.878** | **0.803** | **0.831** |
| Random Forest | 0.877 | 0.793 | 0.828 |
| XGBoost | 0.876 | 0.802 | 0.828 |
| MLP | 0.855 | 0.760 | 0.796 |

---

## 🖥️ 서비스 데모 (Streamlit)

### 홈 대시보드
<img src="main.png" width="700"/>
- 총 예약 건수, 취소율, 평균 ADR 등 핵심 운영 지표를 한눈에 확인할 수 있는 메인 대시보드.


### 취소 확률 예측 페이지
<img src="prediction.png" width="700"/>
- 보증금 유형, 리드타임, ADR 등 주요 피처를 입력하면 MLP 모델 기반으로 취소 확률을 실시간 예측.

> ⚠️ 서비스 구현의 간결성을 위해 주요 피처 6개만 입력값으로 사용하여, 전체 피처 대비 예측 정확도에 일부 차이가 있을 수 있습니다. 

---

## 프로젝트 파이프라인

<img src="pipeline.png" width="700"/>

---
## 프로젝트 구조

```text
SKN30-2nd-3Team/
.
├── dataset/
│   ├── preprocessed/       # 전처리 완료된 CSV 파일
│   └── raw/                # 원본 데이터 (수정 금지)
│
├── docs/
│   ├── Report/             # 최종 결과서 (md / pdf / html)
│   ├── images/             # 라이브러리 로고 이미지
│   ├── AGENTS.md
│   ├── EDA_분석_정리.md
│   ├── ERD.png
│   ├── pipeline.png        # 전체 파이프라인 흐름도
│   └── convention.md       # 코드 컨벤션 정의
│
├── eda/                    # 탐색적 데이터 분석 노트북
│   ├── 02_eda.ipynb
│   ├── clustering.ipynb
│   └── graph.ipynb
│
├── modeling/
│   ├── dl/                 # 딥러닝 (MLP)
│   ├── ml/                 # 머신러닝 (RF, XGBoost 등)
│   └── saved/              # 학습된 모델 .pkl 저장소
│
├── preprocessing/          # 데이터별 전처리 노트북
│
├── results/                # 모델별 예측 결과 CSV
│
├── streamlit/              # 웹 앱 (취소 예측 서비스)
│   ├── home.py             # 메인 페이지
│   └── pages/              # 서브 페이지 (1_취소_예측.py)
│
├── visualization/
│   ├── eda/                # EDA 시각화 결과 이미지 (변수별 분류)
│   └── model_results/      # 모델 비교 결과 시각화
│
├── main.py                 # 프로젝트 진입점
├── pyproject.toml          # 의존성 및 환경 설정
└── uv.lock                 # 패키지 잠금 파일 (uv 사용)
```

---

## Git 협업 가이드

본 프로젝트는 `develop` 브랜치 기반 협업 방식으로 진행됩니다.

자세한 Git 작업 절차 및 커밋 규칙은  
`docs/convention.md`를 참고해주세요.

---

## 🌿 브랜치 전략 (Git Branch Strategy)

본 프로젝트는 짧은 개발 기간과 효율적인 협업을 위해 **단일 develop 브랜치 기반 협업 방식**을 채택합니다.

- **main**: 최종 발표 및 제출용 브랜치
- **develop**: 팀원 공통 작업 브랜치

### 협업 규칙
- 작업 시작 전 `git pull`
- 작업 완료 후 `commit & push`
- 동일 파일 동시 수정 지양
- 충돌 발생 시 즉시 공유 후 해결
- 커밋 메시지 규칙 준수 (`feat`, `fix`, `docs`, `chore` 등)

---

## 📂 최종 산출물 (Deliverables)
- 인공지능 데이터 전처리 결과서
- 인공지능 학습 결과서
- 학습된 인공지능 모델