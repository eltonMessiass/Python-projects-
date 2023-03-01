#collect email from user
# split the email using the @, the first part as the user name,  the second part is gonna be saver as domain


def main():
    print("Welcome to the email slicer ")
    print("")


    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()