__author__ = 'girish'


from ghost import Ghost

ghost = Ghost()

USERNAME = "data"
PASSWORD = "data"

session = ghost.start()
page , resources = session.open("http://hackerrank.com/login",timeout=1000)
print(page.content)
session.fill("form",{
    "username": USERNAME,
    "password":PASSWORD
})

page, resources = session.call("form","submit",expect_loading=True)

print(page.status)
