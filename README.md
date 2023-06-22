# RoomSense IQ and Home Assistant Dashboard

**SightSense**  an innovative user interface that adds a whole new dimension to the [RoomSense IQ](https://www.roomsenselabs.com "www.roomsenselabs.com") platform. SightSense auto-populates a visually appealing dashboard in the popular home assistant that offers exceptional insights into your room environment. With its advanced features such as **ProxiSense**, **CalSense**, **BedSense**, and **EnergySense**, users gain unparalleled control over their living environments. It effortlessly manages multiple sensors, enhancing the overall user experience.


This repository contains code and configurations for SightSense. 

<img src="https://drive.google.com/uc?export=view&id=1dLDwZrMXrG-qxOB9Yj37AN5snObpj3An" width="750" height="375" />

# Requirements

 Install MQTT mosquitto and make sure the RoomSense entities are accessible on your Home Assistant.

# Installation

To set up SightSense, please follow the steps below:

1. Open an SSH terminal to your Home Assistant instance.
2. Use the following commands to get the required files:
   
```bash
cd ~/config
curl -sL https://raw.githubusercontent.com/roomsense/homeassistant-dashboard/main/get-all.sh | bash -s
```
4. Add the yaml code below into your configuration.yaml file:
```yaml
homeassistant:
  packages: !include_dir_named packages
#config for pyscript
pyscript:
  allow_all_imports: true
  hass_is_global: true
#config for lovelace dash
lovelace:
  mode: storage
  dashboards:
    lovelace-roomsense:
      mode: yaml
      title: RoomSense IQ
      icon: mdi:script
      show_in_sidebar: true
      filename: dashboards.yaml
```

5. Go to the Profile tab in Home Assistant and scroll down to turn on Advanced Mode.
   
7. Go to Settings → Dashboards → Top right corner icon and add these resources if the related card is not already installed with HACS.

| URL                                  | Type                |
| ------------------------------------ | ------------------- |
| /local/cards/apexcharts-card.js       | JavaScript Module   |
| /local/cards/button-card.js           | JavaScript Module   |
| /local/cards/card-mod.js              | JavaScript Module   |
| /local/cards/mini-graph-card-bundle.js| JavaScript Module   |
| /local/cards/numberbox-card.js        | JavaScript Module   |
| /local/cards/slider-entity-row.js     | JavaScript Module   |


8. Run the reboot command:
```bash
ha core restart
```

Once the system boots up completely, you should be able to see a new tab named "RoomsSnse IQ". Press Refresh on the top right corner to make the loading faster. 
