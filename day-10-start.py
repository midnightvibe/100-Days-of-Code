# functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("marcel", "KAMINSKI")
print(f"{formated_string}")