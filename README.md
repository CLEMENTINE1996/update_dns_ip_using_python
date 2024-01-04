<h1>Cloudflare IP Address Update using Python</h1>

This is a simple python script that will update the cloudflare's IP address of a type "A" DNS record. Its been created using python 3.11.<br>
To use it, simply execute the script below.<br>

python update_dns_ip.py --login-email your_email --api-key your_cloudflare_global_api_key --hostname your_hostname --ttl your_ttl --new-ip-address your_new_ip_address

your_email = Cloudflare login email you use for logging in to your account<br>
your_cloudflare_global_api_key = The Cloudflare global API key to use. NOTE: Domain-specific API tokens will NOT work!<br>
your_hostname = The hostname to updated (example: www.mydomain.com)<br>
your_ttl = The TTL of the records in seconds (or 1 for auto)<br>
your_new_ip_address = The new IP Address value for update<br>
