# take in the data ... tree structure?  Class...dictionary?
# Can you have multiple directories with the same name?  (not in a computer...)

# "total size" aka recursion for interior dirs

# output: sum of directory sizes that are below 100,000
# why wouldn't you look for the largest directories?

import copy

class Directory:
    # def __init__(self, name) -> None:
    name = ""
    # container_size = 0
    files = []
    children = {}
    # parent_directory = {} # should it be an empty Directory?
    parent_directory = None

class File:
    # def __init__(self, name, size) -> None:
    #     self.name = ""
    #     self.size = 0
    name = ""
    size = 0

# able to assume that starting input at root?
# can root have files directly inside?

def get_kth_term(line, k):
    return line.split()[k-1]

def is_command(line):
    return get_kth_term(line, 1) == "$"

def parse_cmd(line):
    return get_kth_term(line, 2)

CMD_CD = "cd"
CMD_LS = "ls"
ARG_UP = ".."
ROOT_PATH = "/"

def is_dir_output(line):
    return get_kth_term(line, 1) == "dir"

def is_root(dir_name):
    return dir_name == ROOT_PATH

root = Directory()
current_dir = Directory()

# gulp down some data
with open("input.txt", "rt") as input:
    for line in input:
        print(line)
        if (is_command(line)):
            cmd = parse_cmd(line)
            if (cmd == CMD_CD):
                arg = get_kth_term(line, 3)
                if (arg == ROOT_PATH):
                    # print("cd root")
                    root = Directory()
                    root.name = ROOT_PATH
                    current_dir = copy.deepcopy(root)
                elif (arg == ARG_UP):
                    # if (current_dir.parent_directory != None):
                    #     current_dir = current_dir.parent_directory
                    # else:
                    #     new_parent_dir = Directory()
                    #     new_parent_dir.children[current_dir.name] = current_dir
                    #     current_dir = new_parent_dir
                    current_dir = copy.deepcopy(current_dir.parent_directory)
                    # print("going up: ", current_dir.name)
                else:

                    # print("going down: ", arg)
                    # new_child_dir = Directory() # should technically check if visited
                    new_child_dir = current_dir.children[arg]
                    new_child_dir.name = arg
                    new_child_dir.parent_directory = current_dir
                    current_dir.children[arg] = new_child_dir
                    current_dir = copy.deepcopy(new_child_dir)



                # print(vars(current_dir))
            # else: # is ls ... do nothing
        else: # is output ... should only be following an ls
            name = get_kth_term(line, 2)
            if (is_dir_output(line)):
                # dir = Directory(name) # way #1 with init-style
                dir = Directory()
                dir.name = name
                # print("dir:", name)
                # print(current_dir.children)

                # print("dir set...")
                # print("root: ", root.name)
                # print("cur:", current_dir.name)

                current_dir.children[name] = dir
                # print("root kids:", root.children)
                # print("cur kids:", current_dir.children)
                # print(current_dir.children)
            else: # is a file
                size = get_kth_term(line, 1)
                size = int(size) # int is probably safe here?
                # file = File(name, size)
                file = File() # way #2 with direct modification of props
                file.name = name
                file.size = size
                # print(vars(file))
                current_dir.files.append(file)
                # current_dir.container_size += size
        print(root.children)



# # recursive size total lookup
# def dir_total_size(dir: Directory):
#     direct_storage = dir_direct_size(dir)
#     # print(direct_storage)
#     child_storage = 0
#     print(vars(dir.children))
#     for child in dir.children: # do we even need as dict vs. list?
#         print(child)
#         child_storage += dir_total_size(child)
#     return direct_storage + child_storage

# def dir_direct_size(dir: Directory):
#     storage = 0
#     for f in dir.files:
#         storage += f.size
#     return storage

# SIZE_THRESHOLD = 100000
# sum_size_small_dirs = 0
# def traverse_sizes(dir: Directory):
#     # size = dir_total_size(dir)
#     size = dir_direct_size(dir)
#     print(dir.name, size)
#     if (size <= SIZE_THRESHOLD):
#         sum_size_small_dirs += size
#         for d in dir.children:
#             traverse_sizes(d)

# report back
