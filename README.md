# 🖐️ Hand Gesture Controlled Temple Run
## Temple Run with Hand Gestures 


Control **Temple Run** (or similar PC games) using **hand gestures** captured from your webcam.  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand landmarks and map gestures to keyboard/game actions.  


![Image](https://github.com/user-attachments/assets/f8868272-fa91-467b-b858-f53e0f844b19)


## >> [Temple Run with Hand Gestures on my linkedin]([path/to/video.mp4](https://www.linkedin.com/feed/update/urn:li:activity:7205340333583380481?utm_source=share&utm_medium=member_desktop&rcm=ACoAADFDWiQBAag4YObBANI9SkmubOqXJADVKkc))

---

## 📂 Repository Structure

- **gesture_temple_run.py** → Main script (hand tracking + gesture control).  
- **pyautogui_templeRun.py** → Helper file with mapped keyboard/game actions.  
- **README.md** → Project documentation.  

---

## 🎮 How It Works

1. The webcam captures live video frames.  
2. **MediaPipe Hands** detects hand landmarks in real time.  
3. Gestures (finger counts + thumb position) are translated into actions:  

   - ✋ **5 Fingers → UP** (Jump)  
   - 👉 **2 Fingers → RIGHT**  
   - 👈 **4 Fingers → LEFT**  
   - 👊 **1 or 3 Fingers → DOWN** (Slide)  
   
4. Actions are sent to the game using **PyAutoGUI**.  

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/your-username/temple-run-gesture-control.git
cd temple-run-gesture-control
```



## 🚀 Usage

Run the script:

```bash
python gesture_temple_run.py
```

## 🔧 Requirements

- Python 3.8+  
- OpenCV  
- MediaPipe  
- PyAutoGUI  

*(Install all dependencies with:)*  

```bash
pip install -r requirements.txt
```

# 👨‍💻 Author

- **Ahmed Gwely**  
- Passionate about Computer Vision, Embedded Systems, and AI-driven IoT.  
- 🌐 [LinkedIn Profile](https://www.linkedin.com/in/ahmed-gwely-2589611b0/)  
