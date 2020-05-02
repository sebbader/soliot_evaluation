import boto3


# Get all instances with tag "Name:solibot"
ec2 = boto3.client('ec2')
response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['solibot']}])

# Get IP-addresses of those instances
solibot_ips = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if 'PublicIpAddress' in instance:
            solibot_ips.append(instance['PublicIpAddress'])


# Read predefined target url query parts
queries = []
with open("url_queries.txt", "r") as f:
    for query in f.readlines():
        queries.append(query.strip())

# Save IP-addrs to file for overview later
with open('bot_ips.txt', 'w') as f:
    for bot_ip in solibot_ips:
        f.write(bot_ip + '\n')

# Generate target urls for http checks
with open("http_uris_soliot.txt", "w") as f:
    for ip in solibot_ips:
        for query in queries:
            if query.endswith('120636') or query.endswith('things'):
                query += '/'
            f.write("https://{}:8443{}\n".format(ip, query))
            
# Generate target urls for coap checks
with open("coap_uris.txt", "w") as f:
    for ip in solibot_ips:
        for query in queries:
            f.write("coap://{}:5683{}\n".format(ip, query))

# Generate unsafe target urls for http checks
with open("http_unsafe_uris_soliot.txt", "w") as f:
    for ip in solibot_ips:
        f.write("https://{}:8443{}\n".format(ip, "/things/3S7PM0CP4BD/120636/2018-10-24T01-22-30-866Z/"))
            
# Generate target urls for coap checks
with open("coap_unsafe_uris.txt", "w") as f:
    for ip in solibot_ips:
        f.write("coap://{}:5683{}\n".format(ip, "/things/3S7PM0CP4BD/120636/2018-10-24T01-22-30-866Z/unsafeTestTemperature"))


################################
# Get solid instances
response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['solid']}])

# Get IP-addresses of those instances
solid_ips = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if 'PublicIpAddress' in instance:
            solid_ips.append(instance['PublicIpAddress'])


# Save IP-addrs to file for overview later
with open('solid_ips.txt', 'w') as f:
    for bot_ip in solid_ips:
        f.write(bot_ip + '\n')

# Generate target urls for http checks
with open("http_uris_solid.txt", "w") as f:
    for ip in solid_ips:
        for query in queries:
            if query.endswith('120636') or query.endswith('things'):
                query += '/'
            f.write("https://{}:8443{}\n".format(ip, query))
            

# Generate unsafe target urls for http checks
with open("http_unsafe_uris_solid.txt", "w") as f:
    for ip in solid_ips:
        f.write("https://{}:8443{}\n".format(ip, "/things/3S7PM0CP4BD/120636/2018-10-24T01-22-30-866Z/"))
      