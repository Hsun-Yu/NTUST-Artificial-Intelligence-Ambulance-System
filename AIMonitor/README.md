---
languages:
- json
- python
products:
- azure
- azure-iot-edge
---

# About AIMonitor
他在整個系統中負責控制攝像頭並將影像辨識的結果上傳到雲端資料庫，我們使用了azure iot edge進行開發可以方便將程式更新後自動載入所有連上的raspberry pi
，影像辨識的部分使用azure custom vision製作模型，再將它匯出使用tensorflow進行辨識。

# Prerequisites

### raspberry pi image version
2018-03-13-raspbian-stretch.img
下載點：https://downloads.raspberrypi.org/raspbian/images/

# Description of the solution
### Modules

- **Camera capture** - 這個modules可以連接USB攝像頭並將影像資料用到localhost:5012，並將分析的資料回傳iot hub，程式的部分使用python3.5，使用opencv套件來讀取視訊資料。

## Get started
### To deploy the solution on a Raspberry Pi 3
From your mac or PC:
1. 更新'.env'檔案
2. 使用vscode對'deployment.template.json` 按右鍵並選擇 `Build and push IoT Edge Solution` ，它會將你的solution建置好並上傳到你自己的Container registries
3. 對'config/deployment.json'按右鍵，選擇'Create Deployment for Single device'並選擇你要部屬的裝置
