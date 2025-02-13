How to use plant analyzer and auto fertilizing 
 1.install this respiratory into your raspberry pi
 2.install necessary dependencies and liberry
  2.1 if you can't install pigpio you need to do these steps
  2.1.2 first type in bash
  Bash:
      sudo apt update
      sudo apt install git build-essential cmake -y
  step 2.1.3:Download the pigpio source code 
      git clone https://github.com/joan2937/pigpio.git
  step 2.1.4:bulid and install pigpio
  Bash:
      cd pigpio 
      make
      sudo make install
  step 2.1.5:important step start pigpio deamon(you need to run this command every time when you want to use)
  Bash:
      sudo pigpiod
  3.connect pump,relay,wires into your gpio port you can change port in configuration
  4.install plant_analyzer into your discord server
  there are few command in here ,this is list of command
  command:
      !pump when you type this into your chat it will active pump for 100 seconds
      when you send picture of your plant into chat it will analyze your plant health
      
      
  
      


 
