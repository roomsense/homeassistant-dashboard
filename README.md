# RoomSense IQ and Home Assistant Dashboard

[RoomSense IQ](https://www.roomsenselabs.com "www.roomsenselabs.com") is an advanced room monitoring device that utilizes cutting-edge mmWave radar technology and PIR sensor to detect and measure people's movement, providing highly accurate occupancy detection. With its ability to measure temperature, humidity, light density and by adjusting the detailed configurations in Home Assistant, you can customize the device to your liking, creating a personalized occupancy detection method that perfectly fits your living space.

This repository contains code and configurations to create a visually appealing dashboard for RoomSense IQ in Home Assistant.  The solution offers real-time plotting capabilities with an update rate of 25ms, allowing users to monitor and analyze movement energy levels in real-time.

<img src="https://drive.google.com/uc?export=view&id=1dLDwZrMXrG-qxOB9Yj37AN5snObpj3An" width="750" height="375" />


# Requirements

| Items | Comments |
| --------------- | --------------- |
| [RoomSense IQ](https://www.roomsenselabs.com "www.roomsenselabs.com") | Used in this project  |
| Raspberry Pi 4 | Any Home Assistant-compatible device should work |
| Home Assistant | V9.5 |
| MQTT Mosquitto* | [Installation Guide](https://www.youtube.com/watch?v=Xg0IR35Inow&t=1s&ab_channel=SinaMoshksar "YouTube Video")|
| MariaDB* | [Installation Guide](https://www.youtube.com/watch?v=Xg0IR35Inow&t=1s&ab_channel=SinaMoshksar "YouTube Video")|

*Note: To enable communication between RoomSense IQ and Home Assistant, you'll require an MQTT broker add-on such as MQTT Mosquitto. Additionally, for real-time visualization of movement energy levels with a 25ms refresh rate, a high-speed database addon such as MariaDB is necessary. The communication takes place via WiFi using the MQTT protocol.

# Description
Within this repository, there are multiple files, and for each file, a brief description has been provided, along with instructions on how to utilize them.

## configuration.yaml
Add the code provided in this file into the configuration.yaml file for your Home Assistant instance.

## dashboards.yaml
Put dashboards.yaml file into your config folder.

## <em>www</em> folder
Copy all the files in this folder and paste them into the 'config/www' directory.

## resources
Go to <em>Settings</em> → <em>Dashboards</em> → <em>Resouces</em> --> Add these urls one by one:

```
- url: /local/cards/card-mod.js
  type: JavaScript module
- url: /local/cards/apexcharts-card.js
  type: JavaScript module
- url: /local/cards/numberbox-card.js
  type: JavaScript module
- url: /local/cards/mini-graph-card-bundle.js
  type: JavaScript module
- url: /local/cards/slider-entity-row.js
  type: JavaScript module
- url: /local/cards/button-card.js
  type: JavaScript module
```

After making all the necessary changes, restart your Home Assistant. Once the system boots up, you should be able to see a new dashboard named "sense".

![Micro Movement](https://drive.google.com/uc?export=view&id=176vOu_IijYFLfRuvFzkdn6PsbpGUzsIT)

