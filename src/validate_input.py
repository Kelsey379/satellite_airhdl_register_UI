# import json
# import re

# # Load the data.json file
# with open('src/data.json') as data_file:
#     data = json.load(data_file)

# # Load the mask values from the header file
# from DAMRegisterFilesPRESET_regs import DAMRegisterFilesPRESET_regs as regs

# # Validate input values
# def validate_input_value(value, mask):
#     return vsdalue & mask == value

# # Iterate through the LED elements
# for led_element in data['registerMap']['registers'][0]['fields']:
#     element_name = led_element['name']
#     element_mask = getattr(regs, f'LEDS_{element_name.upper()}_BIT_MASK')
    
#     # Validate input value for the LED element
#     input_value = 0  # Replace with the actual input value from the UI
#     if not validate_input_value(input_value, element_mask):
#         print(f"Invalid input value for LED element '{element_name}'")

# # Iterate through the VEn elements
# for ven_element in data['registerMap']['registers'][1]['fields']:
#     element_name = ven_element['name']
#     element_mask = getattr(regs, f'VEN_{element_name.upper()}_BIT_MASK')
    
#     # Validate input value for the VEn element
#     input_value = 0  # Replace with the actual input value from the UI
#     if not validate_input_value(input_value, element_mask):
#         print(f"Invalid input value for VEn element '{element_name}'")

# # Iterate through the Clock_High elements
# for clock_high_element in data['registerMap']['registers'][3]['fields']:
#     element_name = clock_high_element['name']
#     element_mask = getattr(regs, f'CLOCK_HIGH_VALUE_BIT_MASK')
    
#     # Validate input value for the Clock_High element
#     input_value = 0  # Replace with the actual input value from the UI
#     if not validate_input_value(input_value, element_mask):
#         print(f"Invalid input value for Clock_High element '{element_name}'")

# # Iterate through the Clock_Low elements
# for clock_low_element in data['registerMap']['registers'][2]['fields']:
#     element_name = clock_low_element['name']
#     element_mask = getattr(regs, f'CLOCK_LOW_VALUE_BIT_MASK')
    
#     # Validate input value for the Clock_Low element
#     input_value = 0  # Replace with the actual input value from the UI
#     if not validate_input_value(input_value, element_mask):
#         print(f"Invalid input value for Clock_Low element '{element_name}'")
