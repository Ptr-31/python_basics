# You need to extract data from a log file. The log file contains lines of text that represent HTTP requests. Each
# line may contain information about the request method, path, status code, and response time. Your task is to write a
# Python script that reads the log file and extracts all requests that have a response time greater than 500 milliseconds.
# You should use regex to extract the necessary information from each log line

# 2023-05-15 09:24:36,502 INFO  [worker-1] com.example.myapp.OrderProcessor - POST /api/posts 201 700ms Reserving 3 items for order: 12345

import re

def search(logs_api_file):
    with open(logs_api_file) as logs_file:
        logs_data = logs_file.read()
    result = re.findall(r'\w{3,7} (?:/\w{1,10})+ \d{1,3} [5-9]\d{2}ms', logs_data)
    return result

def new(string):
    with open(string) as logs_file:
        logs_data = logs_file.read()
    result = re.findall(r'\d{3}-\d{3}-\d{3} *-*\d{2}', logs_data)
    # return result
    # result.sort()
    with open('needed_files/done.txt', 'w') as done:
        for line in result:
            done.write(line + '\n')
    return result

def main():
    logs_api_file = 'needed_files/log_api_calls.txt'
    # print(search(logs_api_file))
    test = 'needed_files/test.txt'
    print(new(test))
if __name__ == '__main__':
    main()
