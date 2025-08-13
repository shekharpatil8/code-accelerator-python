# coding: utf-8

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Union, Optional, get_origin, get_args
from datetime import datetime

class TestDataGenerator:
    
    @staticmethod
    def generate_sample_data(model: BaseModel):
        """Generate sample data based on Pydantic model field types"""
        sample_data = {}
        for field_name, field_info in model.model_fields.items():
            field_type = field_info.annotation
            alias = field_info.alias or field_name  # Use alias if available

            # Handle Optional types (e.g., Optional[StrictStr])
            origin = get_origin(field_type)
            if origin is Union and type(None) in get_args(field_type):
                field_type = next(t for t in get_args(field_type) if t is not type(None))

            # Handle Union types (e.g., Union[StrictFloat, StrictInt])
            if origin is Union:
                if StrictFloat in get_args(field_type) or float in get_args(field_type):
                    sample_data[alias] = 99.99  # Default float value
                elif StrictInt in get_args(field_type) or int in get_args(field_type):
                    sample_data[alias] = 100  # Default int value
                else:
                    sample_data[alias] = "Sample value"  # Default string value for other types
                continue

            # Standard type handling
            if field_type in (int, StrictInt):
                sample_data[alias] = 100
            elif field_type in (float, StrictFloat):
                sample_data[alias] = 99.99
            elif field_type in (str, StrictStr):
                sample_data[alias] = "Sample value"  # Ensure it's a string
            elif field_type == bool:
                sample_data[alias] = True
            elif field_type == list:
                sample_data[alias] = []
            elif field_type == dict:
                sample_data[alias] = {}
            elif field_type == datetime:  # Handle datetime properly
                sample_data[alias] = datetime.utcnow().isoformat() 
            else:
                sample_data[alias] = None  # Default for unknown types
        
        return sample_data

    @staticmethod
    def generate_invalid_data(model: BaseModel):
        """Generate invalid data using Pydantic model field types and aliases"""
        invalid_data = {}
        for field_name, field_info in model.model_fields.items():
            field_type = field_info.annotation
            alias = field_info.alias or field_name  # Use alias if available
            
            if field_type == int:
                invalid_data[alias] = "invalid"
            elif field_type == str:
                invalid_data[alias] = 123
            elif field_type == bool:
                invalid_data[alias] = "not_boolean"
            elif field_type == float:
                invalid_data[alias] = "not_float"
            elif field_type == list:
                invalid_data[alias] = "not_a_list"
            elif field_type == dict:
                invalid_data[alias] = []
                
        return invalid_data
