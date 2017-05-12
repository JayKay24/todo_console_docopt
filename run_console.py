"""
This example uses docopt with the built in cmd module to demonstrate an 
interactive command application.
Usage:
    todo create <collection_name>...
    todo show_collection
    todo item_add <item_name>...
    todo show_items
    todo delete_collection <collection_name>...
    todo open <collection_name>...
    todo (-i | --interactive)
    todo (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""
import sys
import cmd
from docopt import docopt, DocoptExit

from classes.todo import Todo

todo = Todo()
todo.db.connect_db()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
    
class MyInteractive (cmd.Cmd):
    prompt = '(todo) '
    file = None
    
    @docopt_cmd
    def do_create(self, args):
        """Usage: create <collection_name>..."""
        
        name_list = args['<collection_name>']
        full_name = ' '.join(name_list)
        todo.add_a_collection(full_name)
        todo.show_collections()
        
    @docopt_cmd
    def do_show_collection(self, args):
        """Usage: show_collection"""
        
        # Show all the collections in the database.
        todo.show_collections()
        
    @docopt_cmd
    def do_open(self, args):
        """Usage: open <collection_name>..."""
        
        name_list = args['<collection_name>']
        full_name = ' '.join(name_list)
        todo.open_collection(full_name)
        
    @docopt_cmd
    def do_item_add(self, args):
        """Usage: item_add <item_name>..."""
        
        name_list = args['<item_name>']
        full_name = ' '.join(name_list)
        todo.add_an_item(full_name)
        
    @docopt_cmd
    def do_show_items(self, args):
        """Usage: show_items"""
        
        todo.show_items()
        
    @docopt_cmd
    def do_delete_collection(self, args):
        """Usage: delete_collection <collection_name>..."""
        
        name_list = args['<collection_name>']
        full_name = ' '.join(name_list)
        todo.delete_a_collection(full_name)
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        
        print("Good Bye!")
        todo.db.close_db()
        exit()      
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    
    MyInteractive().cmdloop()
print(opt)
