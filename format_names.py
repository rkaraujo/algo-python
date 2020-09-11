# Given: an array containing hashes of names
#
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#
# Example:
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    name_values = [n['name'] for n in names]

    if len(name_values) == 0:
        return ''

    if len(name_values) > 1:
        return ', '.join(name_values[:-1]) + ' & ' + name_values[-1]

    return name_values[0]


if __name__ == '__main__':
    names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
    print(namelist(names))
