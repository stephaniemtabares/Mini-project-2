#create an empty list
services = []

#add services
services.append("RDS")
services.append("DynamoDB")
services.append("Cloudfront")
services.append("VPC")

#print services and length
print(services)
print(len(services))

#remove two services
services.remove("RDS")
services.remove("DynamoDB")

#print new services
print(services)
print(len(services))