# rotimeout_package/rotimeout.py
import threading

def roTimeOut(func, delay, *args, **kwargs):
    """
    Executes the function after a delay in seconds.
    :param func: Function to be executed
    :param delay: Time in seconds to wait before executing the function
    :param args: Arguments to pass to the function
    :param kwargs: Keyword arguments to pass to the function
    """
    threading.Timer(delay, func, *args, **kwargs).start()
