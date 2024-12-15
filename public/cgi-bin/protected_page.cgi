#!/usr/bin/awk -f

function get_session_user(session_id) {
    # check sessions.txt
    session_file = "../../data/sessions.txt"
    while ((getline sline < session_file) > 0) {
        split(sline, s, ":")
        if (s[1] == session_id) {
            close(session_file)
            return s[2]
        }
    }
    close(session_file)
    return ""
}

BEGIN {
    cookie = ENVIRON["HTTP_COOKIE"]
    session_id = ""

    # Parse cookie
    # Cookie looks like: SESSION_ID=abc123; ...
    split(cookie, cparts, ";")
    for (i in cparts) {
        split(cparts[i], kv, "=")
        # trim spaces
        gsub(/^ +| +$/, "", kv[1])
        if (kv[1] == "SESSION_ID") {
            session_id = kv[2]
        }
    }

    username = get_session_user(session_id)

    if (username == "") {
        # no valid session
        print "Status: 302 Found"
        print "Location: /cgi-bin/login.cgi"
        print "Content-type: text/html\n"
        print "<html><body>Redirecting to login...</body></html>"
        exit
    }

    # if we reach here, user is authenticated
    print "Content-type: text/html\n"
    print "<html><body>"
    print "<h1>Welcome, " username "</h1>"
    print "<p>This is the protected content only for logged-in users.</p>"
    print "<p><a href='logout.cgi'>Logout</a></p>"
    print "</body></html>"
}

