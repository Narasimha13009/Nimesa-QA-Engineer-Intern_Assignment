provider "aws" {
    region = "us-east-1"  
  }
  
  # Create VPC
  resource "aws_vpc" "my_vpc" {
    cidr_block = "10.0.0.0/16"
  }
  
  # Create public subnet
  resource "aws_subnet" "public_subnet" {
    vpc_id     = aws_vpc.my_vpc.id
    cidr_block = "10.0.1.0/24"
    availability_zone = "us-east-1a"  
    map_public_ip_on_launch = true
  }
  
  # Create private subnet
  resource "aws_subnet" "private_subnet" {
    vpc_id     = aws_vpc.my_vpc.id
    cidr_block = "10.0.2.0/24"
    availability_zone = "us-east-1a"  
  }
  
  # Create EC2 instance
  resource "aws_instance" "ec2_instance_public" {
    ami           = "ami-12345678"  
    instance_type = "t2.micro"
    subnet_id     = aws_subnet.public_subnet.id
  
    root_block_device {
      volume_type = "gp2"
      volume_size = 5
    }
  
    tags = {
      Name    = "Assignment Instance (Public)"
      purpose = "Assignment"
    }
  }
  
  # Create security group
  resource "aws_security_group" "instance_sg" {
    vpc_id = aws_vpc.my_vpc.id
  
    egress {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  
    // Inbound rule for SSH
    ingress {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  
  # Attach security group to the instance
  resource "aws_instance" "ec2_instance_public" {
    security_groups = [aws_security_group.instance_sg.name]
  }
  