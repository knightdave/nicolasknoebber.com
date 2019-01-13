from os       import environ
from markdown import markdown
from sys      import argv

"""
global variables for paths
"""
website_dir = environ['HOME'] + '/projects/personal-website'
posts_dir =  website_dir + '/posts'
partial_dir = posts_dir + '/partial'
markdown_dir = posts_dir + '/markdown'


"""
adds a new <tr> element to blog.html
new row will always be the first, to keep reverse chronological order
"""
def add_entry_to_list(post_num) :
  # open the markdown file and get the date and title
  md = open(markdown_dir+'/'+post_num+'.md')
  header = md.readline()[3:-1] # slice omits the beginning hashes and trailing \n
  date   = md.readline()[5:-1]
  md.close()

  # open the blog file and puts its contents into a list of lines
  html = open(website_dir+'/blog.html','r')
  lines = html.readlines()
  html.close()

  # the new table row to be inserted
  new_element = '<tr><td><a href="posts/'+post_num+'.html">'+header+'</a></td><td>'+date+'</td></tr>\n'

  # check if the table row already exists by iterating backwards through the lines
  i = len(lines) - 1
  while i > 0 :
    if lines[i].strip() == new_element.strip() :
      print('list item already exists')
      break
    if lines[i].strip() == '<tbody>' :
      # rewrite blog.html with the new table row
      html = open(website_dir+'/blog.html','w')
      lines.insert(i+1,(' '*8)+new_element) # indent new tag properly and add to file
      html.writelines(lines)
      html.close()
      print('new list item created')
      break
    i -= 1

"""
reads from the markdown file (post_num).md and writes (post_num).html
"""
def add_entry(post_num) :
  post_num = str(post_num)
  try :
    md = open(markdown_dir+'/'+post_num+'.md')
  except :
    return False

  # read header and footer
  h = open(partial_dir+'/header.html')
  header = h.read()
  h.close()
  f = open(partial_dir+'/footer.html')
  footer = f.read()
  f.close()

  # add a post number variable to the footer so it knows how to save comments
  footer = "<script> const postNum = "+post_num + ";</script>" + footer;

  # create post html from header, markdown, and footer
  html = markdown(md.read())
  html = header + '\n' + html + '\n' + footer
  md.close()

  # write html file
  post = open(posts_dir+'/'+post_num+'.html','wt')
  post.write(html)
  post.close()
  print('post updated')
  add_entry_to_list(post_num)
  return True

if __name__ == '__main__' :
  post_num = argv[1]
  if post_num == 'all' :
    n = 0
    while add_entry(n) : n += 1
  else :
    add_entry(post_num)
