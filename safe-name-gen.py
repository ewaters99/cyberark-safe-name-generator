# Author: Eric W. Waters, Gainesville Georgia
# This script generates safe names based on the CyberArk PAM Safe Naming Convention.

import sys
from termcolor import colored

MAX_SAFE_NAME_LENGTH = 28

# Define the choices for each category
ENVIRONMENT_CHOICES = {'P': 'Production', 'D': 'Development', 'T': 'Testing', 'Q': 'Q/A'}
BUSINESS_UNIT_CHOICES = {'INFRA': 'Infrastructure Team', 'SECUR': 'Security Team', 'SDESK': 'Service Desk', 'NTWRK': 'Network Team', 'ERPA': 'ERP Application', 'LOB': 'Line of Business'}
TECHNOLOGY_CHOICES = {'SVR': 'Server', 'WKS': 'Workstation', 'NET': 'Network Device', 'DB': 'Database', 'DOM': 'Domain'}
OS_CHOICES = {'WIN': 'Windows', 'LNX': 'Linux', 'JUN': 'Juniper', 'SQL': 'SQL Database'}
ACCOUNT_TYPE_CHOICES = {'LA': 'Local Account', 'DA': 'Domain Account', 'LS': 'Local Service Account', 'DS': 'Domain Service Account', 'RT': 'Root', 'EN': 'Enable Account', 'SA': 'SQL SA Account'}

# Define the order in which the categories will be displayed
CATEGORY_ORDER = [
    ('ENVIRONMENT', 'cyan', ENVIRONMENT_CHOICES),
    ('BUSINESS_UNIT', 'magenta', BUSINESS_UNIT_CHOICES),
    ('TECHNOLOGY', 'green', TECHNOLOGY_CHOICES),
    ('OS', 'yellow', OS_CHOICES),
    ('ACCOUNT_TYPE', 'red', ACCOUNT_TYPE_CHOICES)
]

def prompt_user_for_category(category_name, category_choices, category_color):
    """
    Prompt the user to select an option from a given category and return the selected option.
    If the user enters an invalid option, prompt them again until they enter a valid option.
    """
    default_choice = list(category_choices.keys())[0]
    prompt = f"Please select an option for the {category_name} ({', '.join([colored(f'{k} ({v})', category_color) for k, v in category_choices.items()])}, default is {colored(default_choice, category_color)}): "
    while True:
        user_input = input(prompt)
        if not user_input:
            return default_choice
        if user_input in category_choices:
            return user_input
        print(f"Invalid choice: {user_input}. Please enter a valid choice.")

def generate_safe_name():
    """
    Prompt the user for each category and generate a safe name based on the user's selections.
    """
    category_selections = {}
    for category_tuple in CATEGORY_ORDER:
        category_name, category_color, category_choices = category_tuple
        category_selections[category_name] = prompt_user_for_category(category_name, category_choices, category_color)
    
    # Concatenate the category selections into a safe name
    safe_name_parts = [category_selections[name] for name, _, _ in CATEGORY_ORDER]
    safe_name = "-".join(safe_name_parts)
    
    # Truncate the safe name if it's too long
    if len(safe_name) > MAX_SAFE_NAME_LENGTH:
        safe_name = safe_name[:MAX_SAFE_NAME_LENGTH]
    
    return safe_name

if __name__ == "__main__":
    print("\nThis tool will help you generate a safe name according to the CyberArk PAM Safe Naming Convention Creation Procedure.")
    print(f"You will be asked to choose from the following options for each category:\n")

    category_selections = {}
    for category in CATEGORY_ORDER:
        category_name, category_color, category_choices = category
        
        category_display_choices = [f"{v} ({k})" for k, v in category_choices.items()]
        category_display_choices = [colored(c, category_color) for c in category_display_choices]
        default_choice = colored(list(category_choices.keys())[0], category_color)
        
        prompt = f"Please select an option for the {category_name} ({', '.join(category_display_choices)}, default is {default_choice}): "
        category_selections[category_name] = prompt_user_for_category(category_name, category_choices, category_color)
    
    # Concatenate the category selections into a safe name
    safe_name_parts = [category_selections[name] for name, _, _ in CATEGORY_ORDER]
    safe_name = "-".join(safe_name_parts)
    
    # Truncate the safe name if it's too long
    if len(safe_name) > MAX_SAFE_NAME_LENGTH:
        safe_name = safe_name[:MAX_SAFE_NAME_LENGTH]
    
    print(f"\nThe safe name is: {colored(safe_name, 'green')}")
    print(f"The safe name uses {len(safe_name)} characters.\n")
