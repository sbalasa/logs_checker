# logs_checker
This is a tiny script to check if specified errors are present in the logs.

There can be multiple log files inside the `logs` folder and multiple errors in the `errors.json`.

## Usage:

`python logs_errors_checker.py`

Eg:

```
$ python3 log_checker.py 
error1 is not present in log3.txt
error1 is present in log2.txt
error1 is present in log1.txt
error2 is present in log3.txt
error2 is present in log2.txt
error2 is present in log1.txt
```
