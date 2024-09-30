def main():
    emails = [ "alice@example.com", "bob@example.com", 
"alice@example.com", "charlie@example.com", 
"dave@example.com", "bob@example.com" ]
    emails=list(set(emails))
    print(emails)
main()
