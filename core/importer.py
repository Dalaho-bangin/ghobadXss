import subprocess
import core.config as mem
def importer(file_path):
   requests = []
   
   if (mem.var['mode']).upper()=='W':
    with open(file_path, 'r') as f:
        li = [x.strip() for x in f.readlines()]
        for line in li:
           if line.startswith("http") and ".js" not in line:
              requests.append(line)
        return requests
   elif (mem.var['mode']).upper()=='L':
        result = subprocess.run(
            [f"cat {file_path} | grep '^http'| sort -u  | grep -v -F '.js'"],
          stdout=subprocess.PIPE,  # Capture standard output
          stderr=subprocess.PIPE,  # Capture standard error
          text=True,               # Work with text data instead of binary
          shell=True               # Use shell to interpret the command
      )
        if not result.stderr:
            for line in result.stdout.splitlines():
                requests.append(line)
            return requests



