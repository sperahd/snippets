# EC2

## Create an instance
aws ec2 run-instances  --profile abcd --image-id ami-0ef1051d6f0313d9e --count 1  --instance-type c5.2xlarge --key-name abcd --security-group-ids sg-0fd38578 --security-group-ids sg-0dfb87988282cc139

## Stop an instance

aws ec2 stop-instances --instance-id i-0ec4e6c79d133a49c

## Terminate and instance

aws ec2 terminate-instances --instance-id i-0ec4e6c79d133a49c

# AutoScaling

## List instances of an autoscaling group

aws autoscaling describe-auto-scaling-instances

## Update capacity of autoscaling group

aws autoscaling update-auto-scaling-group --auto-scaling-group-name abcd-worker-nodes-NodeGroup-JFZ82P --min-size 1 --desired-capacity 1


# Events

## List Events with a prefix

aws events list-rules --name-prefix "abcd_efgh_"

