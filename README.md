# LACT stack

## Overview

This project template leverages the **LACT stack**: **L**ighttpd, **A**WK,
**C**GI, and **T**ext files. It’s a lightweight, modular, and extensible setup
for building web applications without the overhead of databases or large
frameworks. Lighttpd serves as the web server, AWK processes server-side logic
via CGI, and text files provide simple, human-readable data storage.

With strong TLS support, configurable redirects, and a clear directory
structure, this stack is versatile for a wide variety of small to medium-scale
projects.


## Features

- **Lighttpd for Speed and Simplicity:**  
  A high-performance web server with low resource usage and built-in support
for CGI.

- **AWK for Server-Side Logic:**  
  A lightweight, versatile scripting language well-suited for data processing
and web server tasks.

- **Text Files for Data Storage:**  
  No heavy database dependencies—just straightforward flat files for storing
users, sessions, and other data.

- **HTTPS and Redirects:**  
  Full HTTPS support with secure configurations and HTTP-to-HTTPS redirection.

## Directory Structure

```plaintext
lighttpd-app/
├── conf/
│   └── lighttpd.conf     # Lighttpd configuration file
├── data/
│   ├── users.txt         # User data (username:password format)
│   └── sessions.txt      # Session data (session_id:username format)
└── public/
    ├── index.html        # Main HTML file (default page)
    └── cgi-bin/
        ├── hello.cgi     # Example AWK CGI script
        ├── login.cgi     # Login handler
        ├── verify_login.cgi # Verifies user credentials
        ├── protected_page.cgi # Example of restricted content
        └── logout.cgi    # Logout handler
```

**Key Points:**

- **Public Directory:**  
  Files in `public/` are served directly by Lighttpd. The `cgi-bin/` directory
contains AWK scripts for dynamic functionality.

- **Non-Public Data:**  
  Sensitive files like `users.txt` and `sessions.txt` are stored in `data/` and
are not publicly accessible.

- **Configuration:**  
  All settings, such as document root, HTTPS, and CGI handling, are in `conf/lighttpd.conf`.

## Running the Application

### Prerequisites

- **Lighttpd** installed on your system.
- **AWK** installed (most systems have `awk` or `gawk` by default).
- A valid SSL/TLS certificate and private key for HTTPS.

### Steps

1. **Setup the Environment:**

   - Ensure your `lighttpd.conf` points to the correct document root
     (`public/`) and CGI directory (`cgi-bin/`).

     ```bash
     cp conf/lighttpd.conf.example conf/lighttpd.conf
     ```

   - Place your certificate and private key in the project root, or update
     `ssl.pemfile` in `conf/lighttpd.conf` with the correct path.

2. **Run Lighttpd:**

   From the project root, start Lighttpd with the configuration file:

   ```bash
   lighttpd -f conf/lighttpd.conf -D
   ```

3. **Access the Application:**

   - Open a browser and visit:
     - HTTP: `http://localhost:8080/` (Redirects to HTTPS).
     - HTTPS: `https://localhost:8443/`.

## Benefits of the LACT Stack

1. **Minimal Dependencies:**  
   No need for complex databases or frameworks.

2. **Full Transparency:**  
   You control every part of the stack, from server config to CGI logic.

3. **Extremely Lightweight:**  
   Runs efficiently on low-resource systems or containers.

4. **Scalable Simplicity:**  
   Start with text files, and scale to more complex systems as needed.

This template is ready to adapt and grow to fit your application needs. Enjoy the simplicity and power of the **LACT stack**!

