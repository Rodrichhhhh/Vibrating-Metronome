# Vibrating Metronome project

This project is built with **Python** and **Kivy**.  
It plays sound effects, vibration on mobile and includes both **code** and **audio files** for use..



#  Features
- Interactive GUI made with **Kivy**
- Plays sound effects from the **`TempoBeep.wav`** file
- Vibrates on mobile devices when set up.
- Works on Windows, macOS, Linux, and Android
- Customizable sound assets




  # Mobile set up for Android:

   # Use a WSL (Ubuntu) device to Buildozer (https://buildozer.readthedocs.io/en/latest/installation.html)
  
  1. download the folder **"Vibrating Metronome"** and rename the script to **"main.py"**
     
  2. Open Ubuntu (WSL) and go to the folder where your project is stored
     
  3. Install Buildozer & dependencies (first time only):
    sudo apt update
  sudo apt install -y python3-pip openjdk-11-jdk
  pip install buildozer cython==0.29.34

  4. Initialize the project for Buildozer:
      buildozer init

   # create/edit buildozer.spec ----→ buildozer android debug deploy run

  1. Open and edit buildozer.spec
  2. Change the line title = → title = Vibrating Metronome
  3. Add your sound file in source.include_exts = py,wav,mp3
  4. Set requirements = python3,kivy,plyer
  5. Add android.permissions = VIBRATE
  6. type: "buildozer android debug deploy run"
     inside your Ubuntu terminal
     
  
   # enable USB debugging on phone and connect it
  1. Go to Settings → About phone → tap “Build number” 7 times
  2. Go back → Developer options → enable USB Debugging
  3. Connect your phone via USB
  4. When prompted, tap Allow USB debugging
