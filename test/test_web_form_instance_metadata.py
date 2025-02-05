# coding: utf-8

"""
    Web Forms API version 1.1

    The Web Forms API facilitates generating semantic HTML forms around everyday contracts. 

    The version of the OpenAPI document: 1.1.0
    Contact: devcenter@docusign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.web_form_instance_metadata import WebFormInstanceMetadata

class TestWebFormInstanceMetadata(unittest.TestCase):
    """WebFormInstanceMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebFormInstanceMetadata:
        """Test WebFormInstanceMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebFormInstanceMetadata`
        """
        model = WebFormInstanceMetadata()
        if include_optional:
            return WebFormInstanceMetadata(
                expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = openapi_client.models.web_form_user_info.WebFormUserInfo(
                    user_id = '00000000-0000-0000-0000-000000000000', 
                    user_name = 'John Doe', ),
                last_modified_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified_by = openapi_client.models.web_form_user_info.WebFormUserInfo(
                    user_id = '00000000-0000-0000-0000-000000000000', 
                    user_name = 'John Doe', )
            )
        else:
            return WebFormInstanceMetadata(
                expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = openapi_client.models.web_form_user_info.WebFormUserInfo(
                    user_id = '00000000-0000-0000-0000-000000000000', 
                    user_name = 'John Doe', ),
        )
        """

    def testWebFormInstanceMetadata(self):
        """Test WebFormInstanceMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
