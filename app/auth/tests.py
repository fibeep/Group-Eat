#TODO:

# tests for the signup route. It should:
# - Make a POST request to /signup, sending a username & password
# - Check that the user now exists in the database


# Tests for the signup route. It should:
# - Create a user
# - Make a POST request to /signup, sending the same username & password
# - Check that the form is displayed again with an error message

# Tests for the login route. It should:
# - Create a user
# - Makes a POST request to /login, sending the created username & password
# - Checks that the user's name is now displayed on the homepage
# - Check that the form is displayed again with an error message

# Test for the login route. It should:
# - Make a POST request to /login, sending a username & password
# - Check that the login form is displayed again, with an appropriate
#   error message

# Tests for the login route. It should:
# - Create a user
# - Make a POST request to /login, sending the created username &
#   an incorrect password
# - Checks that the login form is displayed again, with an appropriate
#   error message

# Test for the logout route. It should:
# - Create a user
# - Logs the user in (make a POST request to /login)
# - Make a GET request to /logout
# - Check that the "log in" button is showing
