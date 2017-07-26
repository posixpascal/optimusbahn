"""
Defines multiple helper methods for optimus
"""

def thread_group(total_items, size):
    """
    Split a list into a list containing multiple lists of size <size>
    """
    per_thread = round(len(total_items) / int(size))
    groups = []
    group = []

    for item in total_items:
        group.append(item)
        if len(group) >= per_thread:
            groups.append(group)
            group = []
        
    if len(group) > 0: 
        groups.append(group)

    return groups

def truncate(string):
    return string.strip().replace("\n", "").replace("\r", "")