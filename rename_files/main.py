import os


def run_rename(path , old_string=" ", new_string=" "):
    if os.path.exists(path):
        os.chdir(path)
        files = os.listdir(path)
        for file in files:
            if old_string in file:
                new_name = rename(file, old_string, new_string)
                os.rename(file, new_name)
            else:
                print("The word to change is not present in the names of the files...  ")


def rename(name , old_string=" ", new_string=""):
    split_name = name.split(old_string)
    if len(split_name) > 1:
        new_name = split_name[0] + new_string + split_name[1]

        return new_name


def addPrefix(name, prefix=""):
    pass



