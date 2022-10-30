
def read_file(filename):
    with open(filename , 'rt', encoding="utf-8") as data:
        line = data.readlines()
        for i in range(len(line)):
            line[i] = line[i].rstrip()        
        return line

def write_file(work_data):
    with open('pb.txt' , 'w', encoding="utf-8") as data:
        data.writelines(work_data)



    
