import subprocess

## Funch which starts process with cmd
def run_process(cmd):
    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    
## Func which finds phrase in file text    
def find_phrase_in_file(filename, phrase_to_search):
    with open(filename, 'r') as file:
            flag = False
            for line in file:
                process = subprocess.Popen(['grep', phrase_to_search], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                output, _ = process.communicate(input=line)
                if phrase_to_search in output:
                    flag = True
            return flag
