AUTH_USER_MODEL = 'users.CustomUser'

"bookshelf.CustomUser"

# LibraryProject/settings.py

# SECURITY SETTINGS
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # Set your allowed hosts

# Browser XSS Protection
SECURE_BROWSER_XSS_FILTER = True  # Enable browser-side XSS filter

# Prevent Clickjacking
X_FRAME_OPTIONS = 'DENY'  # Deny embedding this site in frames or iframes

# Prevent content sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from interpreting files as a different MIME type

# Use HTTPS for cookies in production
CSRF_COOKIE_SECURE = True  # CSRF cookie only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie only sent over HTTPS

# Ensure content is only served over HTTPS
SECURE_SSL_REDIRECT = True  # Force redirects to HTTPS (must set `SECURE_PROXY_SSL_HEADER` if behind a proxy)
SECURE_HSTS_SECONDS = 31536000  # HTTP Strict Transport Security (1 year)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Preload this domain in browsers' HSTS list

# Enable Secure Cookies
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # End session when the browser is closed
CSRF_COOKIE_HTTPONLY = True  # CSRF cookie cannot be accessed via JavaScript

# LibraryProject/settings.py

INSTALLED_APPS = [

    'csp',
    
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
]
# Example CSP configuration
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-cdn.com')
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')
CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com')


# LibraryProject/settings.py

# SECURITY SETTINGS
DEBUG = False  # Do not expose sensitive information in production

# Browser XSS Protection
SECURE_BROWSER_XSS_FILTER = True  # Prevent cross-site scripting (XSS) attacks

# CSRF protection: Requires a CSRF token in each form to protect against CSRF attacks
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookie is sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookie is sent over HTTPS

# CSP: Restrict content sources to trusted domains only, preventing XSS attacks
CSP_DEFAULT_SRC = ("'self'",)  # Only allow content from the same origin
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-cdn.com')  # Allow scripts from self and trusted CDN


# settings.py

# 1. Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Ensures that all HTTP traffic is redirected to HTTPS

# 2. HTTP Strict Transport Security (HSTS)
# Tells browsers to only communicate with the server over HTTPS for the specified time.
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains in the HSTS policy
SECURE_HSTS_PRELOAD = True  # Allows the site to be included in the HSTS preload list (prevents HTTP access)

# 3. Set secure cookies
SESSION_COOKIE_SECURE = True  # Ensures the session cookie is only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensures the CSRF cookie is only sent over HTTPS

# settings.py

# 1. Prevent Clickjacking
X_FRAME_OPTIONS = 'DENY'  # Disallows the site from being framed by other sites (prevents clickjacking)

# 2. Prevent content type sniffing by the browser
SECURE_CONTENT_TYPE_NOSNIFF = True  # Ensures the browser doesn't try to sniff the content type, mitigating certain attacks

# 3. Enable browser's built-in XSS filtering
SECURE_BROWSER_XSS_FILTER = True  # Enables the XSS filter built into most modern browsers to protect against XSS attacks

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')