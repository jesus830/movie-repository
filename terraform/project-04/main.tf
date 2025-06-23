resource "aws_db_instance" "mysql" {
  identifier     = "myapp-db"
  engine         = "mysql"
  engine_version = "8.0"
  instance_class = "db.t3.micro"
  
  allocated_storage = 20
  storage_type      = "gp2"
  
  db_name  = "myapp"
  username = "admin"
  password = "changeme123!"
  
  skip_final_snapshot = true
  
  tags = {
    Name = "MyApp Database"
  }
}

output "db_endpoint" {
  value = aws_db_instance.mysql.endpoint
}