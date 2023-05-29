import os 
from homeassistant.helpers.template import Template

@time_trigger('startup')
#@state_trigger('EVENT_HOMEASSISTANT_STARTED')

def render_template(template,  **kwargs):
    tpl = Template(template, hass)
    return str(tpl.async_render(kwargs))

    
def replace_sensor_id():
    file_path = 'dash-design.yaml'
    sensor_ids =  render_template("{{ state_attr('sensor.sensorids','ids') | list  }}")
    sensor_ids = sensor_ids.strip('[]').replace("'", "").split(", ")
    file_descriptor = os.open(file_path, os.O_RDONLY)
    
    # read the contents of the file using os.read()
    file_contents = os.read(file_descriptor, os.path.getsize(file_path))
    
    # split the contents into lines using splitlines()
    lines = file_contents.decode().splitlines()
    
    os.close(file_descriptor)
    # open the file in write mode using os.open()
    file_descriptor = os.open('dashboards.yaml', os.O_WRONLY | os.O_TRUNC | os.O_CREAT)
    os.write(file_descriptor, b'views:\n')
    current_tab=1;
    for sensor_id in sensor_ids:
        modified_lines = list(lines)
        # iterate over the lines and replace 'arg1' with 'arg2'
        for i in range(len(modified_lines)):
            tab_text=str(current_tab)
            modified_lines[i] = modified_lines[i].replace('newIdHere', sensor_id)
            tab_name =  render_template("{{ states('input_text.dashtab" + tab_text + "') }}")
            modified_lines[i] = modified_lines[i].replace('changeTabId', tab_name)
        # write the modified contents back to the file using os.write()
        for line in modified_lines:
            os.write(file_descriptor, line.encode())
            os.write(file_descriptor, b'\n')
        current_tab+=1
            
            
    os.write(file_descriptor, b'  - title: config\n')
    os.write(file_descriptor, b'    path: config\n')
    os.write(file_descriptor, b'    icon: mdi:cog\n')
    os.write(file_descriptor, b'    cards:\n')
    
    
    os.write(file_descriptor, b'          - type: entities \n')
    os.write(file_descriptor, b'            entities:\n')
    for dash_id_sensor in range(1, len(sensor_ids)+1):
        os.write(file_descriptor, b'              - entity: input_text.dashtab')
        os.write(file_descriptor, str(dash_id_sensor).encode())
        os.write(file_descriptor, b'\n')
    os.close(file_descriptor)
    
task.sleep(3)
replace_sensor_id()
    
    
    
    
    
    
    
    
    