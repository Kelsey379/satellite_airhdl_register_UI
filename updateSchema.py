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
        ui_schema['elements'].append(group)

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

# make certain fields read-only
for register in data['registerMap']['registers']:
    if 'READ_ONLY' in register['access']:
        for field in register['fields']:
            field['readOnly'] = True

# Generate the updated JSON files
generate_json_files(data)
