
# Network Checker

A beginner-friendly Python project for checking website connectivity, HTTP status codes, and response times.

## Project Overview

This project was created as part of my Python learning journey and software testing portfolio.

The tool sends an HTTP/HTTPS request to a website and displays the response status and response time.

## Features

- Accepts a website URL from user input
- Automatically adds HTTPS if the protocol is not provided
- Displays HTTP status codes
- Measures website response time
- Handles connection errors and timeouts
- Uses Python built-in libraries without external dependencies

## Technologies

- Python 3
- urllib
- Exception handling
- Basic performance measurement

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   ```bash
   python network_checker.py
   ```

5. Enter a website URL when prompted.

Example input:

```text
https://www.google.com
```

## Example Output

```text
=== Network Checker v1.0 ===
Check whether a website responds.

Enter a website URL: https://www.google.com

--- Connection Result ---
Website: https://www.google.com
Status Code: 200
Response Time: 0.35 seconds
Result: SUCCESS
```

*Note: Actual response times and status codes may vary.*

## What I Learned

- Writing and organizing Python functions
- Accepting and validating user input
- Sending HTTP/HTTPS requests
- Handling exceptions
- Measuring response time
- Documenting a software project with GitHub

## Limitations

This project checks website HTTP/HTTPS responses only. It does not perform full tunnel, VPN, packet-loss, or network-routing diagnostics.

## Future Improvements

- Check multiple websites in one run
- Export test results to CSV
- Add automated unit tests with pytest
- Improve error reporting and test summaries

## Author

Created as a personal learning project for Python programming and software testing.

