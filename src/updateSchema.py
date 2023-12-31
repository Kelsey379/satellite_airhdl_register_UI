import json

# Load the data.json file
with open('src/data.json') as data_file:
    data = json.load(data_file)

# Get the LED, VEn, Clock_High, and Clock_Low elements from the data
led_elements = data['registerMap']['registers'][0]['fields']
ven_elements = data['registerMap']['registers'][1]['fields']
clock_high_elements = data['registerMap']['registers'][3]['fields']
clock_low_elements = data['registerMap']['registers'][2]['fields']

# Load the uischema.json file
with open('src/uischema.json') as uischema_file:
    uischema = json.load(uischema_file)

# Find the LED group in the uischema
led_group = None
for element in uischema['elements']:
    if element['label'] == 'LEDs - Turn the LEDs on/off':
        led_group = element
        break

if led_group is not None:
    # Clear existing LED elements
    led_group['elements'] = []

    # Generate LED elements dynamically based on the number of LED elements in the data
    for led_element in led_elements:
        if led_element['bitWidth'] == 1:
            led_control = {
                "type": "Control",
                "scope": f"#/properties/registerMap/properties/LEDs/properties/{led_element['name']}",
                "options": {
                    "type": "boolean",
                    "toggle": True
                }
            }
            led_group['elements'].append(led_control)

# Find the VEn group in the uischema
ven_group = None
for element in uischema['elements']:
    if element['label'] == 'VEn - Enable the voltages':
        ven_group = element
        break

if ven_group is not None:
    # Clear existing VEn elements
    ven_group['elements'] = []

    # Generate VEn elements dynamically based on the number of VEn elements in the data
    for ven_element in ven_elements:
        if ven_element['bitWidth'] == 1:
            ven_control = {
                "type": "Control",
                "scope": f"#/properties/registerMap/properties/VEn/properties/{ven_element['name']}",
                "options": {
                    "type": "boolean",
                    "toggle": True
                }
            }
            ven_group['elements'].append(ven_control)

# Find the Clock group in the uischema
clock_group = None
for element in uischema['elements']:
    if element['label'] == 'Clock - Clock High and Clock Low':
        clock_group = element
        break

if clock_group is not None:
    # Clear existing Clock elements
    clock_group['elements'] = []

    # Generate Clock_High elements dynamically based on the number of Clock_High elements in the data
    for clock_high_element in clock_high_elements:
        if clock_high_element['bitWidth'] == 1:
            clock_high_control = {
                "type": "Control",
                "scope": f"#/properties/registerMap/properties/Clock/properties/Clock_High/properties/{clock_high_element['name']}",
                "options": {
                    "type": "boolean",
                    "toggle": True,
                    "readonly": True
                }
            }
            clock_group['elements'].append(clock_high_control)

    # Generate Clock_Low elements dynamically based on the number of Clock_Low elements in the data
    for clock_low_element in clock_low_elements:
        if clock_low_element['bitWidth'] == 1:
            clock_low_control = {
                "type": "Control",
                "scope": f"#/properties/registerMap/properties/Clock/properties/Clock_Low/properties/{clock_low_element['name']}",
                "options": {
                    "type": "boolean",
                    "toggle": True,
                    "readonly": True
                }
            }
            clock_group['elements'].append(clock_low_control)

# Save the updated uischema.json file
with open('src/uischema.json', 'w') as uischema_file:
    json.dump(uischema, uischema_file, indent=2)

print("UI schema updated successfully.")


# Update the schema.json file
schema = {
    "type": "object",
    "properties": {
        "registerMap": {
            "type": "object",
            "properties": {
                "VEn": {
                    "type": "object",
                    "properties": {}
                },
                "LEDs": {
                    "type": "object",
                    "properties": {}
                },
                "Clock": {
                    "type": "object",
                    "properties": {
                        "Clock_High": {
                            "type": "object",
                            "properties": {}
                        },
                        "Clock_Low": {
                            "type": "object",
                            "properties": {}
                        }
                    }
                }
            }
        }
    }
}

# Generate schema properties for LED elements
for led_element in led_elements:
    schema["properties"]["registerMap"]["properties"]["LEDs"]["properties"][led_element["name"]] = {
        "type": "boolean",
        "title": led_element["name"]
    }

# Generate schema properties for VEn elements
for ven_element in ven_elements:
    schema["properties"]["registerMap"]["properties"]["VEn"]["properties"][ven_element["name"]] = {
        "type": "boolean" if ven_element['bitWidth'] == 1 else "integer",
        "title": ven_element["name"]
    }

# Generate schema properties for Clock_High elements
for clock_high_element in clock_high_elements:
    schema["properties"]["registerMap"]["properties"]["Clock"]["properties"]["Clock_High"]["properties"][clock_high_element["name"]] = {
        "type": "boolean" if clock_high_element['bitWidth'] == 1 else "string",
        "title": clock_high_element["name"],
        "readOnly": True
    }

# Generate schema properties for Clock_Low elements
for clock_low_element in clock_low_elements:
    schema["properties"]["registerMap"]["properties"]["Clock"]["properties"]["Clock_Low"]["properties"][clock_low_element["name"]] = {
        "type": "boolean" if clock_low_element['bitWidth'] == 1 else "string",
        "title": clock_low_element["name"],
        "readOnly": True
    }

# Save the updated schema.json file
with open('src/schema.json', 'w') as schema_file:
    json.dump(schema, schema_file, indent=2)

print("Schema updated successfully.")
