# can use {} but dict() defines that you are creating a dictionary.  more readable
blogs = dict() # blog_name: Blog object


def menu():
    # Show the user the available blogs
    # Let User make a choice
    # Do something with the choice
    # Eventually Exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items(): # [(blog_name, blog), (blog_name, blog)]
        print('- {}'.format(blog))