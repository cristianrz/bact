#!/usr/bin/awk -f

function remove_session(session_id) {
    # We'll rewrite sessions.txt without the current session_id
    session_file = "../../data/sessions.txt"
    temp_file = "../../data/sessions.tmp"

    while ((getline line < session_file) > 0) {
        split(line, f, ":")
        if (f[1] != session_id) {
            print line >> temp_file
        }
    }
    close(session_file)
    close(temp_file)
    # Move temp to original
    system("mv " temp_file " " session_file)
}

BEGIN {
    cookie = ENVIRON["HTTP_COOKIE"]
    session_id = ""

    # Parse cookie
    split(cookie, cparts, ";")
    for (i in cparts) {
        split(cparts[i], kv, "=")
        gsub(/^ +| +$/, "", kv[1])
        if (kv[1] == "SESSION_ID") {
            session_id = kv[2]
        }
    }

    if (session_id != "") {
        remove_session(session_id)
    }

    # Clear the cookie by setting it empty and expired
    print "Set-Cookie: SESSION_ID=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"
    print "Status: 302 Found"
    print "Location: /index.html"
    print "Content-type: text/html\n"
    print "<html><body>Logging out...</body></html>"
}

