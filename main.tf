provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0ff8a91507f77f867" # Amazon Linux 2 AMI (update per region)
  instance_type = "t2.micro"

  tags = {
    Name = "GitHubActionsEC2"
  }
}
