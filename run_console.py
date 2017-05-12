"""
This example uses docopt with the built in cmd module to demonstrate an 
interactive command application.
Usage:
    run_console create <collection_name>...
    run_console (-i | --interactive)
    run_console (-h | --help)
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
    prompt = '(run_console) '
    file = None
    
    @docopt_cmd
    def do_create(self, args):
        """Usage: create <collection_name>..."""
        
        name_list = args['<collection_name>']
        full_name = ' '.join(name_list)
        todo.add_a_collection(full_name)
        todo.show_collections()
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        
        print("Good Bye!")
        todo.db.close_db()
        exit()      
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    
    MyInteractive().cmdloop()
print(opt)
