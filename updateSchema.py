import json

def validate_field_value(register_name, field_name, value, bit_width):
    max_value = (1 << bit_width) - 1
    if value < 0 or value > max_value:
        error_message = f"Error: Value '{value}' for '{register_name}.{field_name}' is out of bounds. Valid range is 0 to {max_value}."
        print(error_message)
        return error_message
    return None

def generate_ui_schema(data):
    registers = data['registerMap']['registers']

    ui_schema = {
        "type": "VerticalLayout",
        "elements": []
    }

    for register in registers:
        register_name = register['name']
        register_description = register['description']

        group = {
            "type": "Group",
            "label": f"{register_name}: {register_description}" if register_description else register_name,
            "elements": []
        }

        for field in register['fields']:
            field_name = field['name']
            field_description = field['description']
            field_bit_width = field['bitWidth']

            element = {
                "type": "Control",
                "label": f"{field_name}: {field_description}" if field_description else field_name,
                "scope": f"#/properties/registerMap/properties/{register_name}/properties/{field_name}"
            }

            if field_bit_width == 1:
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
            field_name = field['name']
            field_type = "integer" if field['bitWidth'] > 1 else "boolean"

            field_properties = {
                "type": field_type,
                "title": field['description'],
                "default": 0
            }

            if field.get('readOnly', False):
                field_properties['readOnly'] = True

            # Add validation logic here
            max_value = (1 << field['bitWidth']) - 1
            field_properties['maximum'] = max_value
            field_properties['minimum'] = 0

            register_properties[field_name] = field_properties

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
