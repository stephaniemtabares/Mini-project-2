#create an empty list
services = []

#Populate the list using append
services.append("RDS")
services.append("DynamoDB")
services.append("Cloudfront")
services.append("VPC")

#Print the list and the length of the list
print(services)
print(len(services))

#Remove two specific services from the list by name
services.remove("RDS")
services.remove("DynamoDB")

#Print the new list and the new length of the list
print(services)
print(len(services))