# Use Bleach when sanitizing user-generated HTML content to prevent XSS attacks by removing or escaping malicious tags and scripts.

import bleach
from icecream import ic

user_content = '<script>console.log("Intruder!")</script><i>Welcome!</i>'
sanitized = bleach.clean(user_content)
ic(sanitized)
# Output example: &lt;script&gt;console.log("Intruder!")&lt;/script&gt;<i>Welcome!</i>

# Whitelist certain tags for controlled formatting
sanitized_with_tags = bleach.clean(user_content, tags=["i", "u"])
ic(sanitized_with_tags)
