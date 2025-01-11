from .bases import ArgLine, SimpleCommand

desc = """
As if the user was to press the windows/meta key.
"""


class Gui(SimpleCommand):
    names = ["GUI", "WINDOWS", "META"]
    description = desc
    parameters = ["TAB", "DOWNARROW", "UPARROW", "LEFTARROW", "RIGHTARROW", "PRINT"] #All valid arguments to the Windows keys that are not 1 character(s) long
    
    def verify_arg(self, arg: ArgLine) -> str | None:
        i = arg.content
        if i.upper() in self.parameters:
            return None
        elif len(i) == 1:
            return None
        else:
           return "Only one character is required. No more or less."
        
