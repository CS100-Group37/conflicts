import json

#TODO: 1
# use json.loads after reading the file to a string
def get_from_db_file(path):
    pass

### arg is a list of strings
### Example: add "class"  2-3p -> { title: class, time: "2-3p" }
### Example: add "shower"  2-3:30a +d -> { title: class, time: "2-3p", repeat: "+d" }
def parse_add_arg(arg):
    ret = {
        "title": arg[0],
        "time": arg[1]
    }

    if len(arg) > 2:
        ret["repeat"] = arg[2]

    return ret

#TODO: 22
# arg is a list of strings
# transform query 1:30p -> { time: "1:30p" }
# transform query 9a +2w -> { time: "9a", date_offset: "+2w" } 
# transform query 9a 2026-09-23 -> { time: "9a", date: "2026-09-23" }
# (whether or not it starts with a "+" determines if it is date_offset or date)
def parse_query_arg(arg):
    pass

def main():
    print(parse_add_arg(["class", "2:30p"]))
    print(parse_add_arg(["class", "2:30p", "+d"]))

main() if __name__ == "__main__" else None
