# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.80
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class SurveysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def publish_survey(self, list_id, survey_id, **kwargs):  # noqa: E501
        """Publish a Survey  # noqa: E501

        Publish a survey that is in draft, unpublished, or has been previously published and edited.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_survey(list_id, survey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_id: The unique ID for the list. (required)
        :param str survey_id: The ID of the survey. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.publish_survey_with_http_info(list_id, survey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.publish_survey_with_http_info(list_id, survey_id, **kwargs)  # noqa: E501
            return data

    def publish_survey_with_http_info(self, list_id, survey_id, **kwargs):  # noqa: E501
        """Publish a Survey  # noqa: E501

        Publish a survey that is in draft, unpublished, or has been previously published and edited.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_survey_with_http_info(list_id, survey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_id: The unique ID for the list. (required)
        :param str survey_id: The ID of the survey. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'survey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_survey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling ``")  # noqa: E501
        # verify the required parameter 'survey_id' is set
        if ('survey_id' not in params or
                params['survey_id'] is None):
            raise ValueError("Missing the required parameter `survey_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'survey_id' in params:
            path_params['survey_id'] = params['survey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/surveys/{survey_id}/actions/publish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unpublish_survey(self, list_id, survey_id, **kwargs):  # noqa: E501
        """Unpublish a Survey  # noqa: E501

        Unpublish a survey that has been published.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_survey(list_id, survey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_id: The unique ID for the list. (required)
        :param str survey_id: The ID of the survey. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unpublish_survey_with_http_info(list_id, survey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unpublish_survey_with_http_info(list_id, survey_id, **kwargs)  # noqa: E501
            return data

    def unpublish_survey_with_http_info(self, list_id, survey_id, **kwargs):  # noqa: E501
        """Unpublish a Survey  # noqa: E501

        Unpublish a survey that has been published.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_survey_with_http_info(list_id, survey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_id: The unique ID for the list. (required)
        :param str survey_id: The ID of the survey. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'survey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unpublish_survey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling ``")  # noqa: E501
        # verify the required parameter 'survey_id' is set
        if ('survey_id' not in params or
                params['survey_id'] is None):
            raise ValueError("Missing the required parameter `survey_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'survey_id' in params:
            path_params['survey_id'] = params['survey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/surveys/{survey_id}/actions/unpublish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
