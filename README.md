# python_templates
This shows an example of how to use the timedRotatingFileHandler to rotate log files in Python.

## Example
Run the Python script 'myapp.py'. This will generate a log entry in the log/ directory.  Run the script again after 1 second. It will rotate off the previous log file. 
```sh
  python myapp.py
```
You can change the frequency of log rotation by changing this variable in logging_config.ini. This example means the log file is rotated off every second, it keeps 5 old log files at most.
```sh
args=(os.environ['mylogfile'], 's', 1, 5)
```
