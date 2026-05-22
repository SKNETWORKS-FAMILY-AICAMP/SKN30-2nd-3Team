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

## 프로젝트 구조

```text
SKN30-2nd-3Team/
│
├── README.md                       # 프로젝트 개요
├── .gitignore
│
├── data/
│   ├── raw/                        # 원본 데이터
│   ├── external/                   # 날씨/환율
│   └── processed/                  # 최종 병합본
│
├── sql/                            # 테이블 생성, ERD
│   ├── schema.sql
│   └── merge_query.sql
│
├── notebooks/                      # 팀원별 작업
│   ├── 01_preprocessing.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_ml_model.ipynb
│   └── 04_dl_model.ipynb
│
├── images/                         # 그래프 저장
├── presentation/                   # 최종 발표자료
│
└── docs/
    └── convention.md
```
---

## 기술 스택

### 💻 Core Frameworks
<img src="https://shields.io/badge/Python%203.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://shields.io/badge/Scikit--Learn%201.8.0-F7931E?style=for-the-badge&logo=Scikit-Learn&logoColor=white" alt="Scikit-Learn"/>
<img src="https://shields.io/badge/PyTorch%202.12.0-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch"/>

### 🚀 Machine Learning Models
<img src="https://xgboost.ai/images/logo/xgboost-logo-trimmed.png" height="35" alt="XGBoost"/>
<img src="https://velog.velcdn.com/images/sunny10/post/3db85049-365c-4c71-bbb9-b305eb589e20/image.png" height="35" alt="LightGBM"/>
<img src="https://www.tutorialspoint.com/catboost/images/catboost-mini-logo.jpg" height="35 alt="CatBoost"/>

### 📦 Data Pipeline
<img src="https://shields.io/badge/pandas%203.0.3-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
<img src="https://shields.io/badge/numpy%202.4.5-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
<img src="https://shields.io/badge/scipy%201.17.1-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy"/>
<img src="https://shields.io/badge/Imbalanced--Learn%200.14.1-F0A422?style=for-the-badge" alt="Imbalanced-Learn"/>

### 📊 Visualization
<img src="data:image/png;base64,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" height="30" alt="Matplotlib"/>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAaQAAAB4CAMAAACKGXbnAAAAw1BMVEX///9ESHZ9sLxcfaI3PG9BRXQ6PnA/Q3M9QXLCxNEyN2w2Om67vMp0d5ir2NDd3uV6fJwtMmpITHlaXYRTd575+fqPkauDhaKXmbHn5+74+Prx+Pfq9fP09Pd0q7ji8e643tfS092+y9qrrL8cI2ImLGfT6ubq6u+esMVsiqy1w9N3k7FrbpLJyta1tsbB4txRVX+HtsFfYomUlq3f6+6YwMmio7iszNTF2+CHnbnW5umi1cu81tyXv8kYIGCjs8lBa5YmopXGAAAV7klEQVR4nO1dCXuaStuGhE1QEQ0gIlGCStMiUrRkaXP6/f9f9c0zA8oyoGlrjW+5r7MkLMMw9zz7DGGYFi1atGjRokWLFi1atGjxW1DXXmKYgyAYmNskdP1L96dFEVbXGC4Wy8VCZkdBHEka/LKMk/Xk0j1rQeCOJcTOIOm6zuGgtQ7HMWIqDluJujjcLa9pg1ClntTdJF7KLU+XxTrQFLOb12k6/u/U1jdzG/9oecFS2FoX6FwLQCfWIs8pHNrMmdl8OuvPV/3+KjtoGbJk0mWtxXmh9rQ4BCGabqYMY0/xwdmM2Xxfrfrz6XyOj0wxVf6WFRKnvq0WZ4EzVoag5+wVs+lvGBsEZ4NpsVe6vZraSN3ZG4aZ92f4en8rR52L9vjfw3ooG1gykNzM5jNm1kdMrabpWUQbUnebWd9mVht7Smhyg2Wv9SD+IpJllNoYYAiwybQbuAvz1CbpzHTKTPv9lDxP5t1L9PafhBMsTD33+4q4CDPQbt83yEatNki24CDSgsiL6MPvNmJPHS69i/T434M1XIbkp6kNY585chuk3WbILvX7fULhZoNIQsdWc8QVUocIg4V5oV7/W1BFKVN13/vAQqrZ9kCU2HNEif39O+i+1QYpPHQV0XnJsvf3u/zPwRUiMP/zOWJhDuM/A3U335CzOtAys8EWIUGbTrFLMZ8idYeuxuFtqAVtQu/McLkAu2iIGGyKVuCCr0DxITpW08zjJkByNrPB7wMHbwqqD2HNtSydFyobk5jUngIDYJawMgPxQSEsOAmMjY0V/DuFX2fI4ev3kYyBdIH74Cqtxjsn/CHWdboOQSry2WzEygw53CBGc302myFfwe6jfzag5sAekQTebIZumMJVQGxHa72H82ESsThTupnjuAgiWCQr9kwHzbZh9Dl24RAZmxWwhgMmdA6UHZE7CHHRFeFye9H3+J/GQCN+3WaD093g1oE3gEIie6rbM/ARDhfbOjADmhBkCgnTbD6fgTyhO5PFh0wR6Q7g0r34PYT/hYXf7Q2JYtHIz7HWW5HsHWOj2HVl2ysUIa1W2PtDhK42xFWHcIoJ5I+YIeouNFlbXnW+Xl0O9j+vkPKa9udZ6ltHygyLEejAGQMS1p9DvITVIIBkiuzphlmBJ+7I8SVe4Qg6HMuy0lWTFLE4YsVRKTBCDMwKKTDbtqcgOyi8taffwUlAcrWZ979PsdYDzOYrcO0234knwawXyaXeox7XT1KyxNnR2fc5Q/Kq09QXABcPh0lIRNJUqo41HpKj3StgZ+9bsYEtgPEB1crVk2Qpqd+8mqa1Bxz0AGapewApvA2JWBn79cfT15ube4Kbm7en5x2WqQ1SkpAqd8SPFy1dPUkDPjP1Nna705orTpxOkXzMNrgkMQeSdj++3gAzBQBTz6AVUycwXH44D+/aSXK1kMFOASEJSnqIJBukCAmIDr72jBRmp8DQDR33N2+v4N/N4cpg9NHSQ9dOUm+kA0lTyPasVpAKYkB1IW8OBz7ztDxhP3+rZSjl6evTjlguV+te8o0ouHKSsCCBQ0AWAs02uCBLDNBsvmFIJWL39LWZoZSntx/YcAWx3vDIC6CjXDVJg8hBsWua2CFFvs1cZ/BYz/sk9f367RSGUrX3hG5dfzSrdN2SpCrJ3vme2ZuNjvjawG9QJFrhBN3zSUJ0oOn+aarHHyyivW6SEsji6CvsNuCSEQ527PlqRWoT9o8jlogqTYwnf6wBuW6SWEgI2VA+mq4OWdQN1MlRBLv7VvG3T2Lp2Zc/VtrhqknCfhh43tO9RQKbtMJ5ude3X2EI8MYM2Mu+WAlXTZIpQP4e6TmoIMH6oDnhjHm3KSpi2tE+1EK8qyaJZIRgkclqAwnTDQRFqxVyud9vinK4/zHhPlT175pJUg9Rp83oeLUW+lF/PRa3HgXSd9EF36uCayYpXPhIbkhMtGKwj6fvfvyOnstgJ9pHKoReM0mDITNL3QVSHbIRQ3+Aopv7nbtcX/bdCrjmjINgpNERAMnQ2x9hCEh6YrSP5IRfsSTp/3lp7Uh//fGtWoP4DXxj4sHR5/89XDFJKk6x2a9Pb/d/kiDAV8YcXvr1crhikjoLa/f1vp6g+3359f0k2cni0q+XwxWT5P3HPNEZAGa+PT3jdQyvz09vN++matpdUDam6+twEIyiwEy6R1Z++d3EDKJRYHpHv+uhqx3P6MVRBBfTmy2TpHbHgzga9cxkfdr2eQc9At0RmOOajyZUoYbohig2PWrZxuoaAfR43DkyEFuZeaIRdPP0PN2p7sPnTy9fXl5+fn5wLXv34115PHDvKjkH1RQ5QeQRJIETYq+2e5Y3QhdI+EqOk3oNjqLTDVBjnATNiuhiIaBdXCDJSoaodVGEG9APw/ExnnwvyB4BN7BGTX/cKI7jEWktjAT8CF4SSSyyhpNROiadGLUHryei9qLGEqnJMt8qo/v1x853f365vQPc3qb/f3z5rDqvp+ch7l/Vsg/um5zE5iAKLN0BdLa8wBeuVIKaJJNvsJzIFiByo+qg50jyDbHYOi9IRhNN/pbnijdI3IhaL3NlNOwKPMUJ9rdky3LWCqJMxhVWNy70gBeikNYcwWDEvBWH9uZpZz283GJ2Sri7e/yk7p5PrP/dv1qlBcduJLAl8NS9Mt6wciErSiYtNkaX8pVrWZGvzPQDSSFbbR0d2taF3pMxpTtogsUUaVJlaEuF3amH6SiM0/eHZgTYtDqWSvOK5eX6JFovYL7mR/bb8+4BiVCVoBxP7utJGYn7Z2dRkOI1i4cTybcsSLKQdlMIKoNiynw6vxRZ5GSkFfCvXFyZ7Wovna48uk6WREVOKeOlsuBlJOmGzGd3KKgrSnYHF9NNjR9zh+4I6BGZNhCV6ibhjCRVTB8CkNNhUKELQsLogZKOA7QmppNMqY0qg96BJBAi91MDQxlPXz7vTqhh3D9PFnkZtoaYFiEaeK5luWEvnU3KuNglpCcIe3yQrFVLdbtGTC6VylrMish4iVw0CF3VQhePA8K+OCwJRppx0HsKoWQ46KI7VHWdxKm6FIc0Q6NG6VkuRt3B/Rlk0isbZY/AwiRZDr4JPSTomWYvSrttpSQFAjA+7KFxUN3QHKWtCXV2N9hLEliihxealqPwdPtJfa3YMook5Unq4QEVtntfQe0RLaIVZrAT4KMibxwO626PIywVR97HYyEiTyF33CUkc0aJJDgqqgaexNwo9+Eq3R2QYeK5qt1TyfzghYF7IMTyUsWtlDdj+UCSZG3hNDdK/aKscw4clRIPdUFkx/sOOOGQPD6ucWIHcWqTEEU/jwpRXpxe3CNOxP2rn7dJLuZIKdhHAyvpYWFoDDLEQUn3hHgchdKgqOj1hLJLoZMmhOJhTBKLT4lDrzQc65FElGTZLjkRHj+pbH+cLdHB5fKzo0EzHRFoTcpiNoHX5QPcXuH1VGIIlJq1O2YE3t39t53/6TQhyvH0+GA3lQVL3h2eXFJpehscr5iFAfMUmhgwhA90ouQErRWOosoHMPulIqGEJDghxBTHf0BOl1fPEPHnBtVAZ52yVBxYHUhiYxHxTbFwWPx44Kg0SVT8GLFingkMifl2/2RbJ+q5Ek23nyevtTSV4qQRj9VN8fGTSCxOUQubUaqng30jlisNV0iLMHw8n4u6kZAEHNEzimOFYr09GR+sThkmm/58yfZphAdepEWAqZPIjypnEnKKHgckS+bVdh9/gSFC090nf1fnku86uc0VOtEblTctTSlToii1FB62uyd9dgU3Ixf0XUaSVDNdmQEeJyU/uA6WXqlm94GLCRGKfo9GnsJRPcWUJJnCBZkidNchXPhWrSm6O6CBphe1ptJue//lbC2eQscyrip2imoquhMQRl480gTGGt6ZKwhZShIf1aWYHCzrQl5qxtiIDOvSIlg188XprxBppbvThKQSrQRkdtLOoNmwdNW78rCneHnY46VRmh4/+xTj9JUxlMODMEmseCT9MsBdrXNFQ65qBOjATlZxpFKShPrVMWus27hDF32s0JT6XEBUoZXhmmZCapNoUXNHqJdZfxH6xTF/+ZTBNYIUA7dZH949/lQrvt4b+Pd7TLDmEBqSHwhOk/kEg0XxPejQKlemjkPDxik9FovUhlhShvWL2rscZiQ/6EKDIKUnqeLi46ZqXn2ZMI+FAbe8DCiOEQmiIySBD/HlYVfcdfHEiPlRwsqEb/7e2lqoaKk8JoFYrwyLgIbEgmkjJFUSEXlgSc3RiJ3ERiPIV4QT81BXEREaZBl0CF+zNBvN9qIuU5cCgdYdiJk3cpSkWxLh5niCMCk/3MR/4fmwYXXKFno6rFeJWHFrp+xtB7ktkaQ0jAKBQwxK1r6PtRnNyu9hVCyJUPUrSycj+klscKtuH4a31D8XGMDZJ6yc30lSmtjbPT+RjWZ2qOXfzydhNatEW7fOdg9xR+uLR9uq07bHxPHddacbhl6CwNIl6YiuDLANyoyeSxRk0w240cLQCk06VWiSlgaSkOdg/SmSME+3Lw/O7vXp6xvEYHl0lbQ1SY6MUKVo+glHXkKvAZFGjuI5WN4gZmVZUTiOw2qghiSleVEtbn8vGNjllxq/wuNXQiWh6R7MYM3Cj55YT5KuJZOCUaKRFDB+BvUEnpBAPfi6HpX6mmQtQzlGZgdeecR84hpptSDhbNn58McjWchyyTnQbFKzd9ktSBuZEs1xGVEPuVZpeZWTTpoNJDFBzLzk5YRGUq+zkAkW7okC9X+uuih7AKGWq6JAqYArflFc5dgTUHKdfFMrV5R4nqeTxEfN9gzbrf1t2OBUpkQRmCQ+9xaNSrWRJKmBpO5CRZHS4x4WlaRs+JTTSLq9fUQGpGIh/Z5WqMyykpav5LmU2toxkrx9i7wkKDISN4UfDoc1JNVZ9KwD8O57i0Kcu+awLMYpiZxKOCpJNQFrM0mOsGUQNZ0ME+1PkHT3U49oylc1xKJqknLTkJDEK83Q8m9ppoZOVJR463VUP/U6KN7dCZLkKnmSQAFRLWAOo79DEtOL9J+P3SWHoQh/RpLu/LpFxrrrmdG+2gpFnD1LFgno1p1m5JQLybexEjfoFH3CGpIa3HtAt+AqbE9Vd2yuR2ciqbNcO1+6e3PwR0i6e2HMcmk0h4nqmUM5a30fmDik3tI4KgUkxNOQzYqA0EmqZOFL8KreXV3ygEDHz88n985Ekh71mM9/miTVkms6k8FZmxIxJ9JeL5Jg7+TPdJCFBNSqt0S1SXVp5gxjHJtm/hyOGeo8ZgKLJIRz4cSZSEK2152EJ5P0eJyi29svjHEsl8rAIjzC0n4LdFRWHs3APjJPvV6rkqQ0DR8BdgPkjEgSzApNN3Rx5JMPT89FkoNEyTuRJNl3M6hf6gXJ9cWT8qBeMR+Z7Nc8nYSoNmfrUEgiyYGmT4Dg3PlBeZHaReMmejxChdrwuUhCUaa7p+YYSaogEydr6dXXL14YQzlNHrAs7f0pvA6iqacFOFLZIOyxVugksVKTvvNKGYGmGg/GpJpOPRtJzjAmSxBOIWmYnQ5rSbrzVfkkQUqd3sMyGVLPOHHvmVpPaVKXBW/KsE6wZOZSDB2y3qLeAfKEinSejSQmXIRpSfFPkHT3k4mpJX4KfEzSPjFsENfhtHvdikHYAw83jaSGQggpH7HSoedkqVCDf0dWqRRG/XwkMYEwWcvvJqmuuM50l9TogjIlcXVA3EsSqYXW5suCwqodV6iTJPIuVJJ4qW76WGyFknTpUp3mNimlhzOSpGoD8sjTSRLCh88ZCjJ1ZzkcLdZRY8qHu0gi5mAGSORTU40YK8IoN8QW8Q2rQ0hKrHSSWJ6nqy8H31Q8S1yHumRSupSoOKPOSBKToLlPXu1kSeqMeynG+YrU3Wcm0ChzzxNFyiogbJtzL5Wuz6UWUGFZiMgezuhkSWz1pQ0y3Yohzv4VxIgWHPgBbk0uqoAuHgwpoEkfiVrEEoPnJAkNrEViw9NJyqrrQu/hS4bHuxcmWVSVnY83glQ6iOOMguC46VLSShMOWZQs5N6jR1aIl/0MQyCLICUKSXgKsNV8nEqWsFbW5Bnp8ubKrNPHxBHhS2fOSpIjjpgOJNTeQVKafhNNNcygftFd2l+rUBV8MdcrzLsuNgNioWvEDvCCWZzva7I2X8x73MT7Kq2bUAcc8ssNsVwgJa+Q8KTx4tDqCU8UZFRWyDoRMJFNinkQl6xYZ+WyH3JWkpj1coAXXL+fJMkINbIsgtNcR2WpeZ00pSFF+819zjpdJy8XRcFIl64Nx/uVk866R0gWo/zopraH58d+Ori6lbASZH/gccUsIMk4WMSQSOz28HfC/TAmnRMp+Vcn3Wck5P42teMa6Y6Q6pfIzksS4y0NJlF+jaQ0yEJv6Ud1a2VT74rjB1sv9MZmlGZYlfKaYrLgF7YDxcYYLh1kl0pRUQLcNJcuSIGZeGFiBByupiZ4ThRjomx/kofp5iV5ZIyT0EuMnpRufZGq+58YcCiEtONCz4CHQM+l9FDVDT0zSch5GCPj/BskIXs/GdUmmpOsgIq3qe6LSlx11UaYbWTkJSF3KS9UDLjHHdrEW2xxiwYpOhS9sv1OvzDdvpY2nu2547kBPbOrm8WHCFmVRapuJzw/SYyxTBiPXj4/hSRRVCexXJ8uWFO2QYrUT3m5o+IWVQxBpIRPHV4qXcbjNffrSvXosB3TCiitc2x9yjCkbfmUOOpf1j07SYy5MBlr8YskiaLvD7WmQqaTyEp+r6goaOVtSBk6kVwYGFHRDGq04pjLPPWiPMJuhCpLklSIQjsaOpJmFFHrUq51XlS48o6lAvRQLHWH03r0nsNza3Ni+GTN3lhTQR0+KdeSLHoovpR+hSQlZlSucYEooNvjZAXpJaTxZC32GsoZbjLSZEUglwqD+myONRZkjoPLFFkw0w44BkLBh3NNOJRNfnUbaTLqh8BxsjzqHf+I+Xocke7AY+ReWNdzeIhRV82FLpg1z/LgxiM1uOzSZeRPyLbSd5EESiaUh6ekvtUOsvDbJHSPfjh8ona8rYkuPdas1fW2RhKu3/W9E8ftesbW6x7vR3YD6s4YPcY97eMcZ0SHU7qMJ0rvI2kZq4y5pO2ga3EOqPHSmPimwr+HpASF7MvKVuwWZ4NuLEdrxo2XJ5IkymPdGXP8R/vjFP/j6ETawGfCTk86TpLIITcHbri4ov7XMEkkKXGYzogsj6sjSeQFCVGkDpb0D+20OC/UnsyhwMQ1h4gnkU5SwEWJyri9pVT5YkGLvwPV1JbmmpmszaESdOQCSfD5L8ULXcYJ44XkfaSPFv9r8MfyQoEPu/muG0uaDPt/Fqoga9qwF8LhbrBcNH+prcVfgGvIiIcER4m+6rrrtaWqDg4zTW6xiOo/Ktjib8JNguVSkyMzCTtrRFM3HAeSrC1YszY10uIC0NUQajrLxWIJ/wqxkXT81lf4gJg4jmO5qo/+1/LTokWLFi1atGjRokWLFi1atGjRokWLFi1atGjRosXF8f93VC52YZ47IQAAAABJRU5ErkJggg==" height="30" alt="Seaborn"/>
  
---

## Git 협업 가이드

본 프로젝트는 `develop` 브랜치 기반 협업 방식으로 진행됩니다.

자세한 Git 작업 절차 및 커밋 규칙은  
`docs/convention.md`를 참고해주세요.

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

> 프로젝트 진행 후 업데이트 예정

---

## 프로젝트 파이프라인

<img src="pipeline.png" width="700"/>

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
- 호텔 예약 및 취소 패턴 데이터 분석 결과 보고서
- 인사이트 발굴을 위한 데이터 시각화 자료
- 적용 알고리즘 간 머신러닝/딥러닝 모델 성능 비교 결과
- 취소 여부에 가장 큰 영향을 미치는 핵심 변수 영향 분석(Feature Importance) 결과 
- 데이터 기반 예약 취소 대응 및 운영 개선 전략 제안서
