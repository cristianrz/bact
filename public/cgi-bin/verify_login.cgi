#!/usr/bin/awk -f

BEGIN {
	LOG="/home/user/lighttpd-app/awk.log"
	print "testing logging" >> LOG
    # read environment variables
    content_length = ENVIRON["CONTENT_LENGTH"]+0
    request_method = ENVIRON["REQUEST_METHOD"]
    # Simple POST parsing
    if (request_method == "POST" && content_length > 0) {
        getline post_data < "/dev/stdin"
        close("/dev/stdin")
        # parse form data
        n = split(post_data, parts, "&")
        for (i=1; i<=n; i++) {
            split(parts[i], kv, "=")
            key = kv[1]
            val = kv[2]
            # URL decode might be needed, here we skip for simplicity
            if (key == "username") username = val
            if (key == "password") password = val
        }
    }

    # Check credentials in users.txt
    user_file = "../../data/users.txt"
    print "will parse file now" >> LOG
    authenticated = 0
    while ((getline line < user_file) > 0) {
        split(line, u, ":")
        if (u[1] == username && u[2] == password) {
		print u[1] username >> LOG
		print u[2] password >> LOG
            authenticated = 1
            break
        }
    }
    close(user_file)

    # Print HTTP header first
    if (authenticated == 1) {
        # generate session id (very naive)
        cmd = "head /dev/urandom | tr -dc a-z0-9 | head -c 16"
        cmd | getline session_id
        close(cmd)
        
        # store session
        session_file = "../../data/sessions.txt"
        # append session record
        print session_id ":" username >> session_file
        close(session_file)

        # redirect to protected page
        print "Status: 302 Found"
        # Send a Set-Cookie header
        print "Set-Cookie: SESSION_ID=" session_id "; Path=/"
        print "Location: /cgi-bin/protected_page.cgi"
        print "Content-type: text/html\n"
        print "<html><body>Redirecting...</body></html>"
    } else {
        print "Content-type: text/html\n"
        print "<html><body>"
        print "<h1>Login Failed</h1>"
        print "<p>Invalid username or password. <a href='login.cgi'>Try again</a>.</p>"
        print "</body></html>"
    }
}

