import CloudFlare, argparse, sys

argParser = argparse.ArgumentParser()

argParser.add_argument("-e", "--login-email", required=True, help="Cloudflare login email you use for logging in to your account")
argParser.add_argument("-k", "--api-key", required=True, help="The Cloudflare global API key to use. NOTE: Domain-specific API tokens will NOT work!")
argParser.add_argument("-n", "--hostname", required=True, help="The hostname to updated (example: www.mydomain.com)")
argParser.add_argument("-t", "--ttl", default=60, type=int, help="The TTL of the records in seconds (or 1 for auto)")
argParser.add_argument("-i", "--new-ip-address", required=True, help="The new IP Address value for update")
args = argParser.parse_args()
    # Initialize Cloudflare API client

try:
    cf = CloudFlare.CloudFlare(
        email=args.login_email,
        token=args.api_key
    )

    main_hostname = args.hostname.split(".")

    zone = main_hostname[1]+"."+main_hostname[2]
    name = main_hostname[0]

    zones = cf.zones.get(params={"name": zone})
    if len(zones) == 0:
        print(f"\n\nNo zone {zone} in Cloudflare has been found!")
        sys.exit(2)

    zone_id = zones[0]["id"]
    records = cf.zones.dns_records.get(zone_id, params={"name": args.hostname, "type": "A"})

    if len(records) > 0:

        try:
            record = records[0]
            record["ttl"] = args.ttl
            record["content"] = args.new_ip_address

            updated_record = cf.zones.dns_records.put(zone_id, record["id"], data=record)
            print("\nSuccessfully updated!\n")
            for key, val in updated_record.items():
                print(key + ": " + str(val))


        except CloudFlare.exceptions.CloudFlareAPIError as e:
            print("\n")
            print(e)

    else:
        print(f"\n\nNo records of DNS hostname with name '{ name }' and type 'A' has been found! ")

except CloudFlare.exceptions.CloudFlareAPIError as e:
    print("\n")
    print(e)

