#!/usr/bin/env python
import sys
from settings import VALID_DATA_TYPES

from emerald import help
from emerald import add_model
from emerald import install_package
from emerald import add_controller



if len(sys.argv) > 1:
    sysinput = sys.argv[1].lower()

    if sysinput == '--help' or sysinput == '-h':
        help()

    elif sysinput == '--add' or sysinput == '-a':
        if len(sys.argv) > 3:
            install_package(sys.argv[2], sys.argv[3])
        else:
            print "You need to specify a valid package name"
            sys.exit()

    elif sysinput == '--initiate' or sysinput == '-i':
        if len(sys.argv) > 2 and not sys.argv[2].isdigit():
            add_controller(sys.argv[2])
        else:
            print 'Controller name can not be a number'
            sys.exit()

    elif sysinput == '--new' or sysinput == '-n':
        if len(sys.argv) > 2:
            model_name = sys.argv[2].title()
            raw_component = sys.argv[3:]
            model_components = []
            if raw_component:
                for component in raw_component:
                    raw_field = component.split(':')
                    field_name = raw_field[0]
                    detail_components = raw_field[1].split('--')
                    if detail_components[0].lower() in VALID_DATA_TYPES:
                        insert_components = {
                            'field_name': field_name,
                            'field_property': detail_components
                        }
                    else:
                        print '\n' + detail_components[0].lower() + ' is not a valid data type.'
                        sys.exit()
                    model_components.append(insert_components)
                add_model(model_name, model_components)
            else:
                print '\nNot enough parameters are provided. Model requires field definitions. See box.py -h for info\n'
                sys.exit()
        else:
            print '\nNot enough parameters are provided. See box.py -h for info\n'

    else:
        print '\nCommand not found. Please use --help for command options\n'

else:
    print '\nNot enough parameters found. Please run box.py -h for complete explanations\n'


# end of file