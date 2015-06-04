def verifyInterfaces():
    """Minimal method to ensure all interfaces are correctly implementted."""
    import inspect, sys, os, importlib
    frame = inspect.stack()[1]
    module_name = os.path.splitext(inspect.getsourcefile(frame[0]))[0]
    l = lambda member: inspect.isclass(member) and member.__module__ == module_name
    importlib.import_module(module_name)
    clsmembers = inspect.getmembers(sys.modules[module_name], l)
    from zope.interface import implementedBy
    from zope.interface.verify import verifyClass
    for _,the_class in clsmembers:
        for the_interface in implementedBy(the_class):
            verifyClass(the_interface, the_class)
