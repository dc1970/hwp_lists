import sys

# Global Variables
old_ver = sys.argv[1]
new_ver = sys.argv[2]
old_hwp_dict = {}
new_hwp_dict = {}
diff_hwp_dict = {}

# Load files to Dictionaries
def create_ver_dictinary(dict, file_name):
    lines_list = open(file_name, 'r').read().splitlines()
    lines_list = lines_list[3:] # Remove header
    for line in lines_list:
        line_l = line.split()
        dict[line_l[0]] = line_l[3:]

if __name__ == '__main__':
    outfile = open('dif_hwp_results', 'w')
    create_ver_dictinary(old_hwp_dict, old_ver)
    create_ver_dictinary(new_hwp_dict, new_ver)

    for k in new_hwp_dict.keys():
        if k in old_hwp_dict:
            if old_hwp_dict[k] != new_hwp_dict[k]:
                diff_hwp_dict[k] = [' '.join(old_hwp_dict[k]), ' '.join(new_hwp_dict[k])]

    sorted_keys = list(diff_hwp_dict.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        outfile.write('{}, {}\n'.format(k, ', '.join(diff_hwp_dict[k])))


