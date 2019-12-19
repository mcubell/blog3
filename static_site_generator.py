#!pythonl
about_template = open('./about_template.html').read()
blog_list_template = open('./blog-list_template.html').read()
blog_post_template= open('./blog-post_template.html').read()
index_template = open('./index_template.html').read()

about_content = open('./about_content.html').read()
blog_list_content = open('./blog-list_content.html').read()
blog_post_content = open('./blog-post.html').read()
index_content = open('./index_content.html').read()

about_built = about_template + about_content
blog_list_built = blog_list_template + blog_list_content
blog_post_built = blog_post_template + blog_post_content
index_built = index_template + index_content

def static_pages():
    for page in static_pages
        if page_name == 'about.html'
            open('about.html', 'w+').write(index_built)

    