import re


def main(input_string):
    pattern = r"\.begin glob\s(\w+).?.?<=\s?\`(\w+)\s\.end."
    matches = re.findall(pattern, input_string, flags=re.DOTALL)
    result = dict(matches)
    return result
  
