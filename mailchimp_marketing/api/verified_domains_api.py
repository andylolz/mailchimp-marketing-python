# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.73
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class VerifiedDomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def create_verified_domain(self, body, **kwargs):  # noqa: E501
        """Add domain to account  # noqa: E501

        Add a domain to the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_verified_domain(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifiedDomains2 body:  (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_verified_domain_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_verified_domain_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_verified_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add domain to account  # noqa: E501

        Add a domain to the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_verified_domain_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifiedDomains2 body:  (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_verified_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/verified-domains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifiedDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_domain(self, domain_name, **kwargs):  # noqa: E501
        """Delete domain  # noqa: E501

        Delete a verified domain from the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_domain(domain_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_domain_with_http_info(domain_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_domain_with_http_info(domain_name, **kwargs)  # noqa: E501
            return data

    def delete_domain_with_http_info(self, domain_name, **kwargs):  # noqa: E501
        """Delete domain  # noqa: E501

        Delete a verified domain from the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_domain_with_http_info(domain_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params or
                params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_name' in params:
            path_params['domain_name'] = params['domain_name']  # noqa: E501

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
            '/verified-domains/{domain_name}', 'DELETE',
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

    def get_domain(self, domain_name, **kwargs):  # noqa: E501
        """Get domain info  # noqa: E501

        Get the details for a single domain on the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domain(domain_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_domain_with_http_info(domain_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_domain_with_http_info(domain_name, **kwargs)  # noqa: E501
            return data

    def get_domain_with_http_info(self, domain_name, **kwargs):  # noqa: E501
        """Get domain info  # noqa: E501

        Get the details for a single domain on the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domain_with_http_info(domain_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params or
                params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_name' in params:
            path_params['domain_name'] = params['domain_name']  # noqa: E501

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
            '/verified-domains/{domain_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifiedDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_verified_domains_all(self, **kwargs):  # noqa: E501
        """List sending domains  # noqa: E501

        Get all of the sending domains on the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_verified_domains_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VerifiedDomains1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_verified_domains_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_verified_domains_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_verified_domains_all_with_http_info(self, **kwargs):  # noqa: E501
        """List sending domains  # noqa: E501

        Get all of the sending domains on the account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_verified_domains_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VerifiedDomains1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_verified_domains_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/verified-domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifiedDomains1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_domain_verification(self, domain_name, body, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Verify a domain for sending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_domain_verification(domain_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :param VerifyADomainForSending_ body:  (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.submit_domain_verification_with_http_info(domain_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.submit_domain_verification_with_http_info(domain_name, body, **kwargs)  # noqa: E501
            return data

    def submit_domain_verification_with_http_info(self, domain_name, body, **kwargs):  # noqa: E501
        """Verify domain  # noqa: E501

        Verify a domain for sending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_domain_verification_with_http_info(domain_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_name: The domain name. (required)
        :param VerifyADomainForSending_ body:  (required)
        :return: VerifiedDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_domain_verification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params or
                params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling ``")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_name' in params:
            path_params['domain_name'] = params['domain_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/verified-domains/{domain_name}/actions/verify', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifiedDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
