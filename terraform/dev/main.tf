provider "aws" {
  region                   = "us-east-1"
  shared_config_files      = ["~/.aws/conf"]
  shared_credentials_files = ["~/.aws/creds"]
}


resource "aws_instance" "lab5-vm" {
  ami                    = "ami-09d56f8956ab235b3"
  instance_type          = "t2.micro"
  key_name               = "devops_lab"
  vpc_security_group_ids = [aws_security_group.main.id]


  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("/home/behouba/.ssh/devops_lab_id_rsa")
    timeout     = "4m"
  }
}


resource "aws_security_group" "main" {
  egress = [
    {
      cidr_blocks      = ["0.0.0.0/0", ]
      description      = ""
      from_port        = 0
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "-1"
      security_groups  = []
      self             = false
      to_port          = 0
    }
  ]
  ingress = [
    {
      cidr_blocks      = ["0.0.0.0/0", ]
      description      = ""
      from_port        = 22
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "tcp"
      security_groups  = []
      self             = false
      to_port          = 22
    }
  ]
}


resource "aws_key_pair" "deployer" {
  key_name   = "devops_lab"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCbHaGlimgnFfRkxwDMc2zLGHiSVLuAj4MMMDGA7eNejF0BFH3eayc79PhEpwQhlxKeAdjMNEuS2yScsoPuXD1/Y8tzAF/PGsISDU4RydV3OGhbmFUb4/xXq0awYSHWP8maq1JDoZOxgPTG1bYo3Z4dushKt/iD59tr3qmiLBXOXVrSm4EQYI7Ce+Th26CAjx8+wppU47617XjVdC9zGeZxJi5gQI82ZBx1WZsXQvBQh/hrh1h2UzCHQ5wZ2kbL3vsXahtlaFDgJP4sPVkJhMN8ig1FcO5xQ4vBZ1SynPQad1ZNBQBMv1BEdSpJmwjhKm06SlkAQjv5ykfl7bhf6WYIKBzIveFOAG82oa6A4Jf+791bzX1MSKqppWzhoBbmDXwHUklwPBVL5dbOm1elDH4x0X+gCBcAUaWz70C35Duzc28KWOZB28gcJOoUNZb/5T1LSL+ZK46PGG18zl2POwjE4BzN1DGu+DPikjuSPddoswmR1QhkHsa3xkh689eZZ/8= behouba@ip5"
}