Methodize
=========

Is a module to read from and write to the keys of a python dict using methods. This is baseado in http://github.com/lfcipriani/methodize ruby code.
::
    import methodize

The advantage of using Methodize is that you can easily access the values of complex or big Hash objects, such as converted JSONs returned from Web Services, RESTful APIs, etc.


Instead of using::
    mydict['article']['info']['category']
You can use::
    mydict.article.info.category

To install::
    easy_install methodize


Interested? Let's see more examples

Let's suppose that we have the following hash object::
    >>> from methodize import Methodize
    >>> response = Methodize({
    ...   'article':[
    ...         {
    ...           'title' :'Article 1',
    ...           'author':'John Doe',
    ...           'url'   :'http://a.url.com'
    ...         },{
    ...           'title' :'Article 2',
    ...           'author':'Foo Bar',
    ...           'url'   :'http://another.url.com'
    ...         },{
    ...           'title' :'Article 3',
    ...           'author':'Biff Tannen',
    ...           'url'   :['http://yet.another.url.com', 'http://localhost'],
    ...           'info'  :{
    ...                 'published':'2010-05-31',
    ...                 'category' :['sports', 'entertainment']
    ...           }
    ...         }
    ...   ],
    ...   'type':'text',
    ...   'size':3,
    ...   'id'  :123456789
    ... })

You can change the title of the third article using::
    
    >>> response.id
    123456789
    >>> response.article[2].title = 'New title'
    >>> response.article[2].title
    'New title'


Hash public methods that conflicts with keys will be automatically freed::

    >>> response.type
    'text'
    >>> response.size
    3
    >>> response.id
    123456789

Another examples

Writing::

    >>> response.article[2].title = 'Article 3'
    >>> response.article[1].info = {
    ...                    'published':'2010-08-31',
    ...                    'category' :['sports', 'entertainment']
    ...                 }
    >>> response.article.append({
    ...               'title':'A new title',
    ...               'author':'Marty Mcfly'
    ...          })
    >>> response.shift  = 12
    >>> response['inspect'] = False
    >>> response.size = 4

Accessing::

    >>> response.article[2].title
    'Article 3'
    >>> response.article[1].info.published
    '2010-08-31'
    >>> response.article[-1].author
    'Marty Mcfly'
    >>> response.shift
    12
    >>> response.inspect
    False
    >>> response.size
    4

You can access the methodize as usual using [] or []=.
::
    >>> response['size']
    4

