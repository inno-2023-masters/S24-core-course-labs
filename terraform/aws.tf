provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "app_server" {
  ami           = "ami-0faab6bdbac9486fb"
  instance_type = "t2.micro"
  tags = {
    Name = "app-server"
  }
}