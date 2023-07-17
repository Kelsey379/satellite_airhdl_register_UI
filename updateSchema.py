import json

def generate_ui_schema(data):
    registers = data['registerMap']['registers']

    ui_schema = {
        "type": "VerticalLayout",
        "elements": []
    }

    clock_low_elements = []  # Store clock_low elements here
    clock_high_elements = []  # Store clock_high elements here

    for register in registers:
        group = {
            "type": "Group",
            "label": f"{register['name']} - {register['description']}",
            "elements": []
        }

        for field in register['fields']:
            element = {
                "type": "Control",
                "scope": f"#/properties/registerMap/properties/{register['name']}/properties/{field['name']}"
            }

            if field['bitWidth'] == 1:
                element['options'] = {
                    "type": "boolean",
                    "toggle": True
                }

            if field.get('readOnly', False):
                element['options'] = element.get('options', {})
                element['options']['rule'] = {
                    "readOnly": True,
                    "effect": "disabled"
                }

            group['elements'].append(element)

        # Check if the group should be part of the "clock" section
        if 'clock' in register['name'].lower():
            if 'clock_low' in register['name'].lower():
                clock_low_elements.extend(group['elements'])
            elif 'clock_high' in register['name'].lower():
                clock_high_elements.extend(group['elements'])
        else:
            ui_schema['elements'].append(group)

    # Create a group for clock_low and clock_high elements
    clock_group = {
        "type": "Group",
        "label": "Clock",
        "elements": [
            {
                "type": "HorizontalLayout",
                "elements": [
                    {
                        "type": "Group",
                        "label": "Clock Low",
                        "elements": clock_low_elements
                    },
                    {
                        "type": "Group",
                        "label": "Clock High",
                        "elements": clock_high_elements
                    }
                ]
            }
        ]
    }

    # Add the clock_group to the UI schema
    ui_schema['elements'].append(clock_group)

    return ui_schema

def generate_data_schema(data):
    registers = data['registerMap']['registers']

    properties = {
        "registerMap": {
            "type": "object",
            "properties": {}
        }
    }

    for register in registers:
        register_properties = {}
        for field in register['fields']:
            field_type = "integer" if field['bitWidth'] > 1 else "boolean"

            field_properties = {
                "type": field_type,
                "title": field['name']
            }

            if field.get('readOnly', False):
                field_properties['readOnly'] = True

            register_properties[field['name']] = field_properties

        properties['registerMap']['properties'][register['name']] = {
            "type": "object",
            "properties": register_properties
        }

    data_schema = {
        "type": "object",
        "properties": properties
    }

    return data_schema

def generate_json_files(data):
    ui_schema = generate_ui_schema(data)
    data_schema = generate_data_schema(data)

    with open('src/uischema.json', 'w') as f:
        json.dump(ui_schema, f, indent=2)

    with open('src/schema.json', 'w') as f:
        json.dump(data_schema, f, indent=2)

# Example usage:
with open('src/data.json') as f:
    data = json.load(f)

# Make clock fields read-only
for register in data['registerMap']['registers']:
    if 'clock' in register['name'].lower():
        for field in register['fields']:
            field['readOnly'] = True

# Generate the updated JSON files
generate_json_files(data)
