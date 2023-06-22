import os
from homeassistant.helpers.template import Template

def render_template(template, hass, **kwargs):
    tpl = Template(template, hass)
    return str(tpl.async_render(kwargs))

@service
def generate_automation():
    r_var="{{ state_attr('sensor.sensorids','ids') | list  }}"
    sensor_ids =  render_template(r_var,hass)
    sensor_ids =  sensor_ids.strip('[]').replace("'", "").split(", ")

    yaml_template1 = '''automation:
    alias: CalSense automation
    description: ""
    trigger:
      - platform: state
        entity_id:'''
        
    yaml_template2 = '''
        to: "on"
    condition: []
    action:
      - service: switch.turn_off
        data_template:
          entity_id: >

            {% set excluded_entity_id = trigger.entity_id %} {% set sensor_entity_id
            = 'sensor.sensorids' %} {% set other_ids = state_attr(sensor_entity_id,
            'ids') | default([]) %} {% set switch_entity_ids = states.switch |
                selectattr('entity_id', 'match', 'switch.roomsense_calsense_.*') |
                map(attribute='entity_id') | list %}
            {% set data = namespace(switch_entity_ids_to_turn_off=[]) %} {% for
            entity_id in switch_entity_ids %}
                {% set dynamic_id = entity_id.split('_')[-1] %}
                {% if dynamic_id != excluded_entity_id.split('_')[-1] and dynamic_id in other_ids %}
                    {% set data.switch_entity_ids_to_turn_off = data.switch_entity_ids_to_turn_off + [entity_id] %}

                {% endif %}
            {% endfor %}  {{ data.switch_entity_ids_to_turn_off | join(', ') }} {%
            if data.switch_entity_ids_to_turn_off | length == 0 %} none {% endif %}
    mode: single'''
    sensor_count = len(sensor_ids)
    file_path = 'packages/calsense_automation.yaml'
    if sensor_count >= 2:
        entity_id_lines = ''
        for sensor_id in sensor_ids:
            entity_id_lines += f'\n            - switch.roomsense_calsense_{sensor_id}'
        entity_id_lines = entity_id_lines.rstrip()  # Remove the last newline character
        yaml_code = yaml_template1 + entity_id_lines + yaml_template2
        generated_yaml = yaml_code.encode('utf-8')
        fd = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
        os.write(fd, generated_yaml)
        os.close(fd)
    else:
        yaml_code1 = " "
        generated_yaml1 = yaml_code1.encode('utf-8')
        fd1 = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
        os.write(fd1, generated_yaml1)
        os.close(fd1)
        
