import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import Adam

#============================= 딥러닝을 위한 데이터로더 만들기 ========================
def make_DataSet(x_train, x_val, y_train, y_val, batch_size=32):
    #데잍터를 텐서로 변환
    # torch.tensor() : 날 것의 데이터(np.array)를 파이토치 전용 규격(연료)으로 바꾼다.
    
    x_train_tensor = torch.tensor(np.array(x_train), dtype=torch.float32)       
    y_train_tensor = torch.tensor(np.array(y_train), dtype=torch.float32).view(-1, 1)
    x_val_tensor = torch.tensor(np.array(x_val), dtype=torch.float32)
    y_val_tensor = torch.tensor(np.array(y_val), dtype=torch.float32).view(-1, 1)

    # TensorDataset : 문제지(X)와 정답지(y)를 한 세트로 묶어 낱개 상품으로 포장
    train_dataset = TensorDataset(x_train_tensor, y_train_tensor)

    # DataLoader: 낱개 상품들을 batch_size만큼 박스때기로 묶고, 골고루 섞어서 트럭에 실어 모델에게 실시간으로 배달
    train_loader= DataLoader(train_dataset, batch_size = batch_size, shuffle = True)

    return train_loader, x_val_tensor, y_val_tensor

# ============================= train 학습을 위한 함수===============================
def train(dataloader, model, loss_fn, optimizer, device):
    
    model.train()
    total_loss = 0

    for x, y in dataloader:
        x,y = x.to(device), y.to(device)

        optimizer.zero_grad()           # 이전 배치의 gradient 초기화
        pred = model(x)                 # 모델에 지정된 장치에 이동된 입력 데이터를 넣는다.
        loss = loss_fn(pred,y)          # 손실함수에 모델에 들어간 예측값과 실제 레이블 값을 비교하여 저장

        loss.backward()                 # 역전파를 통하여 weight를 구한다.
        optimizer.step()                # weight를 이용하여 모델 파라미터 업데이트

        total_loss +=loss.item() * x.size(0) # loss.item()은 배치의 평균 손실 그 후 평균 손실에 배치만크 곱해야 총 loss

    return total_loss / len(dataloader.dataset)

#=============================== evaluate 검증을 위한 함수=============================

def evaluate(x_val_tensor, y_val_tensor, model, loss_fn, device):

    model.eval()         #모델을 평가 모드로

    with torch.no_grad():              # 지금부터 이 들여쓰기 안쪽 코드가 끝날 때까지, 미분(기울기) 계산 기록 장치를 잠시 꺼두겠다
        x = x_val_tensor.to(device)
        y = y_val_tensor.to(device)
        pred = model(x)
        eval_loss = loss_fn(pred,y).item()

    return eval_loss, pred 

#=============================== 학습 곡선 함수(같은 파일 위치 내 results파일에 저장) =========================================

def dl_learning_curve(tr_loss_list, val_loss_list, save_dir="./results", file_name="learning_curve2.png"):

    # 1. 지정한 폴더가 서버에 없으면 자동으로 생성해 주는 안심 코드
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"📁 폴더가 존재하지 않아 새롭게 생성했습니다: {save_dir}")
        
    epochs = range(1, len(tr_loss_list) + 1)

    plt.figure(figsize=(7, 4))
    plt.plot(epochs, tr_loss_list, label="train_loss", marker=".")
    plt.plot(epochs, val_loss_list, label="val_loss", marker=".")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(alpha=0.3)
    
    # 2. 폴더 경로와 파일 이름을 안전하게 합쳐줍니다. (예: ./results/learning_curve.png)
    save_path = os.path.join(save_dir, file_name)
    
    # 3. plt.show() 대신 저장하는 핵심 메서드
    # bbox_inches='tight'를 넣어주면 축 글자가 잘리지 않고 예쁘게 저장됩니다.
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"📊 학습 곡선 그래프가 성공적으로 저장되었습니다 ➡️ {save_path}")
    
    # 4. 메모리 누수를 막기 위해 현재 축과 피겨를 닫아줍니다. (서버 환경 필수)
    plt.close()

# =================================== main 함수 ============================

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

path = 'hotel_bookings.csv'
df = pd.read_csv(path)

string_cols = df.select_dtypes(include=['object']).columns
number_cols = df.select_dtypes(exclude=['object']).columns

df[string_cols] = df[string_cols].fillna('Unknown')
df[number_cols] = df[number_cols].fillna(0)
#df.drop(['meal', 'country', 'market_segment', 'distribution_channel','deposit_type','customer_type','reservation_status_date','company'], axis=1, inplace=True)

drop_cols = ['reservation_status', 'reservation_status_date', 'arrival_date', 'reservation_date']
X = df.drop(columns=[col for col in drop_cols if col in df.columns] + ['is_canceled'])
y = df['is_canceled']
X = pd.get_dummies(X, drop_first=True, dtype=float)

# target = 'is_canceled'
# features = ['lead_time','stays_in_weekend_nights','stays_in_week_nights','adults']
# X = df.loc[:,features]
# y = df[target]

X_train, X_val, y_train, y_val = train_test_split(X,y,
                                                  test_size = .2,
                                                  random_state = 2026)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

train_loader, X_val_ts, y_val_ts = make_DataSet(X_train,
                                                X_val,
                                                y_train,
                                                y_val,
                                                batch_size =32)

n_feature = X.shape[1]

# 모델 구조 설계
model = nn.Sequential(
    nn.Linear(n_feature,5),         #은닉층
    nn.ReLU(),                      #은닉층 활성화 함수
    nn.Linear(5,1),                 #출력층
    nn.Sigmoid()                    #출력층 활성화 함수
).to(device)

loss_fn = nn.BCELoss()
optimizer = Adam(model.parameters(),lr=0.001)

epochs = 100
tr_loss_list, val_loss_list = [],[]

for t in range(epochs):
    tr_loss = train(train_loader, model, loss_fn, optimizer, device)
    val_loss, _ = evaluate(X_val_ts, y_val_ts, model, loss_fn, device)

    # 리스트에 loss 추가 --> learning curve 그리기 위해.
    tr_loss_list.append(tr_loss)
    val_loss_list.append(val_loss)

    print(f"Epoch {t+1}, train loss : {tr_loss:4f}, val loss : {val_loss:4f}")

dl_learning_curve(tr_loss_list, val_loss_list)

_,pred = evaluate(X_val_ts,y_val_ts, model, loss_fn,device)
pred_class = np.where(pred.cpu().numpy()>0.5,1,0)  #확률이 0.5보다 크면 1, 작으면 0으로 변환
print(confusion_matrix(y_val_ts.numpy(),pred_class))
print(classification_report(y_val_ts.cpu().numpy(),pred_class))