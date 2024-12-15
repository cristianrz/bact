#!/usr/bin/awk -f

BEGIN {
    # Print CGI header
    print "Content-type: text/html\n"
    print "<!DOCTYPE html>"
    print "<html>"
    print "<head><title>Login</title></head>"
    print "<body>"
    print "<h1>Please Log In</h1>"
    print "<form method='POST' action='verify_login.cgi'>"
    print "Username: <input type='text' name='username'><br>"
    print "Password: <input type='password' name='password'><br>"
    print "<input type='submit' value='Login'>"
    print "</form>"
}

END {
    print "</body>"
    print "</html>"
}

