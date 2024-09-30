# ghobadXss
Autometic Reflected Xss Detector
## Instalation

```
$ git clone https://github.com/Dalaho-bangin/ghobadXss
$ cd ghobadXss
$ pip install -r requirements.txt
$ chmod +x ghobadxss
$ ./ghobadxss
```

## Usage
```options:
  -h, --help        show this help message and exit
  -o TEXT_FILE      Path for output file.
  -t THREADS        Number of concurrent threads. (default: 5)
  -i [IMPORT_FILE]  Import target URLs from file.
  -m MODE           Environment mode: L (linux) or W (windows). (default: Windows)
  ```

## Example
For test reflected Xss on a set of urls in linux with 20 threads can use this command
```
$ ./ghobadxss -o output_file.ext -t 20 -i urls_to_test -m L
```

#
Goodluck with bounty hunting :)
