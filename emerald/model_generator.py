import os.path
import sys

from settings import BASEDIR
from settings import WHITE_SPACE

from controller_generator import generate_controller
from template_generator import generate_index_template
from template_generator import generate_controller_template
from template_generator import generate_edit_template
from template_generator import generate_view_template

def add_model(model_name, model_components):
    # This is used to add model to the model file.

    # Get the current model file and open it for writing.
    model_path = os.path.join(BASEDIR, "models/" + model_name.lower() + ".py")
    init_path = os.path.join(BASEDIR, "models/__init__.py")
    model_file = open(model_path, 'w')

    model_file.write("from google.appengine.ext import ndb\n")
    model_file.write("from helpers import generate_key\n")
    model_file.write("from ndbtools import ValidatedIntegerProperty\n")
    model_file.write("from ndbtools import ValidatedFloatProperty\n\n")
    # Write the class definition.
    model_file.write('class ' + model_name.title() + '(ndb.Model):\n')
    model_file.write(WHITE_SPACE+'id = ndb.StringProperty(default=generate_key())\n')

    ## Add the model fields.
    ### First check for the data types and standardize it.
    for component in model_components:
        in_type = component['field_property'][0].lower()
        ### The database field type based on https://developers.google.com/appengine/docs/python/ndb/properties#types
        if in_type == in_type=='int' or in_type=='integer':
            data_type = 'ValidatedIntegerProperty()'
        elif in_type == 'float':
            data_type = 'ValidatedFloatProperty()'
        elif in_type == 'boolean' or in_type == 'bool':
            data_type = 'BooleanProperty()'
        elif in_type == 'string' or in_type == 'str':
            data_type = 'StringProperty()'
        elif in_type == 'text':
            data_type = 'TextProperty()'
        elif in_type == 'blob':
            data_type = 'BlobProperty()'
        elif in_type == 'datetime':
            data_type = 'DateTimeProperty()'
        elif in_type == 'date':
            data_type = 'DateProperty()'
        elif in_type == 'time':
            data_type = 'TimeProperty()'
        elif in_type == 'geo' or in_type == 'geopt':
            data_type = 'GeoPtProperty()'
        elif in_type == 'key':
            data_type = 'KeyProperty()'
        elif in_type == 'blobkey':
            data_type = 'BlobKeyProperty()'
        elif in_type == 'user':
            data_type = 'UserProperty()'
        elif in_type == 'structured':
            data_type = 'StructuredProperty()'
        elif in_type == 'local' or in_type == 'localstructured':
            data_type = 'LocalStructuredProperty()'
        elif in_type == 'json':
            data_type = 'JsonProperty()'
        elif in_type == 'pickle':
            data_type = 'PickleProperty()'
        elif in_type == 'generic':
            data_type = 'GenericProperty()'
        elif in_type == 'computed':
            data_type = 'ComputedProperty()'
        else:

    ### If the data type did not match any of the existing data types, display error message and quit the program.
            print 'Data type ' + component['field_property'][0] + ' not found. Please refer to NDB documentation on https://developers.google.com/appengine/docs/python/ndb/properties#types for valid data types.'
            sys.exit()

    ### If it matches write the model fields into the model files.
        if in_type == 'int' or in_type == 'integer' or in_type == 'float':
            model_file.write(WHITE_SPACE + component['field_name'].lower() + ' = ' + data_type + '\n')
        else:
            model_file.write(WHITE_SPACE + component['field_name'].lower() + ' = ndb.' + data_type + '\n')

    ## Create the class method for data transfer object (dto) for JSON representation.
    model_file.write('\n')
    model_file.write(WHITE_SPACE + '# data transfer object to form JSON\n')
    model_file.write(WHITE_SPACE + 'def dto(self):\n')
    model_file.write(WHITE_SPACE + WHITE_SPACE + 'return dict(\n')

    ### Add the json component for all fields.
    mod_counter = 1
    model_file.write(WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + 'id = self.id,\n')
    max_mod_index = len(model_components)

    for component in model_components:

        if mod_counter != max_mod_index:
            model_file.write(WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + component['field_name'].lower() + ' = self.' + component['field_name'].lower() + ',\n')
        else:
            model_file.write(WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + WHITE_SPACE + component['field_name'].lower() + ' = self.' + component['field_name'].lower() + ')\n')
        mod_counter = mod_counter + 1

    model_file.close()

    init_file = open(init_path, 'a')
    init_file.write("from "+ model_name.lower() + " import " + model_name.title()+"\n")
    init_file.close()

    print '\n...........\n'

    #add the CRUD controllers
    generate_controller(model_name, model_components)
    generate_index_template(model_name, model_components)
    generate_controller_template(model_name, model_components)
    generate_edit_template(model_name, model_components)
    generate_view_template(model_name, model_components)

    print "Model generation complete"


# end of file