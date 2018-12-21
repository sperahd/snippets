## Create an instance
aws ec2 run-instances  --profile ravtr --image-id ami-0ef1051d6f0313d9e --count 1  --instance-type c5.2xlarge --key-name ravtr --security-group-ids sg-0fd38578 --security-group-ids sg-0dfb87988282cc139
