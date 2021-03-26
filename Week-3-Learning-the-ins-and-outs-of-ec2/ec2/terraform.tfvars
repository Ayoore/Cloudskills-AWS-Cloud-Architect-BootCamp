# Amazon Linux 2 AMI
ami = "ami-0efe874dc329d88df"
instance_type = "t2.micro"
key_name = "alphaiocloudskills"
subnet_id = "subnet-44b2f71c"
ip_address = ["172.31.16.5"]


#To be continued. terraform task keeps failing due to incorrect values in tfvar file. (20210324)
#Update (20210326)
#Created an ami using image builder and then used the ami id in the tfvar file and terraform task succeeded.