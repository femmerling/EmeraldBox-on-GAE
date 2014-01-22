def help():
    print '\nThe general usage pattern of the tool is python box.py [options] [extra parameters]\n'
    print 'The following are the available options:\n'
    print ' --initiate or -i        : Generates a new controller handler. You should specify a controller name and the name should not be a number.'
    print '\t\t\t   The pattern is python box.py -i [controller name]'
    print ' --new or -n             : Create new data model.'
    print '\t\t\t   The pattern is box.py -n [model name] [<field name>:<field type>]'
    print '\t\t\t   For more documentation please see https://developers.google.com/appengine/docs/python/ndb/properties#types'
    print ' --add or -a             : Install a new python package from git.'
    print '\t\t\t   The pattern is python box.py -a [git repo address] [package name in lowercase]'
    print ' --help or -h            : Display the help file'
    print ''


# end of file