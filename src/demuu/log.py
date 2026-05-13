import sys

# Output on : stderr
def info( txt ):
    print( f"Log Demuu >> {txt}", file=sys.stderr )

def error( txt ):
    print( f"Err Demuu >> {txt}", file=sys.stderr )
