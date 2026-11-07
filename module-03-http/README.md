# HTTP Request Investigation

An exercise exploring how a browser communicates with a web server, 
using Developer Tools and curl.

## What I Investigated

- The URL, method, status and content type of a browser request
- Response headers returned by a web server
- How DNS, TCP/IP and TLS support web communication

## Evidence

- [Request investigation and explanations](http-request-notes.md)
- [Selected response headers](curl-headers.txt)

## Command Used

```bash
curl -I https://developer.mozilla.org/en-US/
```

The -I option sends a HEAD request to retrieve response headers. 
The browser request documented in my notes uses GET.

## What I Learned 

How to read an HTTP response and distinguish the roles of DNS, 
IP, TCP, HTTP, and TLS.

The saved headers are a snapshot; current responses may differ.
