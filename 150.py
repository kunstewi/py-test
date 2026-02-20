# r'^(https?|ftp):\/\/([a-zA-Z0-9\-\.]+)\.([a-zA-Z]{2,})(\/\S*)?$' 

# commnonly used url validation regex pattern

"""
^ : Means the URL must begin exactly here.

(https?|ftp) : http OR https , ftp , s? → makes s optional

:\/\/ : : literal colon. \/ escaped /,  Must match ://

([a-zA-Z0-9\-\.]+) : Matches domain name part:

\. : Matches literal dot before TLD.

([a-zA-Z]{2,}) : Matches top-level domain (TLD): Only letters Minimum 2 characters

(\/\S*)? : Optional path part. / literal slash, \S* → zero or more non-whitespace characters, ? → whole group optional

$ : Ensures nothing extra after URL.


valid : 

https://google.com
http://example.org
ftp://my-site.in
https://sub.domain.com/path


invalid :

google.com               (missing protocol)
https:/google.com        (missing slash)
http://example           (no TLD)
http://.com              (invalid domain)


This regex:

❌ Doesn't validate IP addresses

❌ Doesn't handle query parameters properly

❌ Doesn't handle ports (:8080)

❌ Doesn't handle complex subdomains fully

👉 Real-world URL validation is very complex.
In production, we usually use:

urllib.parse (Python)

OR trusted libraries

"""