# coding: utf-8

"""
    Aspose.Storage for Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccessTokenResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'token_type': 'str',
        'expires_in': 'str',
        'refresh_token': 'str',
        'client_id': 'str',
        'client_refresh_token_life_time_in_minutes': 'str',
        'issued': 'str',
        'expires': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'client_id': 'client_id',
        'client_refresh_token_life_time_in_minutes': 'clientRefreshTokenLifeTimeInMinutes',
        'issued': '.issued',
        'expires': '.expires'
    }

    def __init__(self, access_token=None, token_type=None, expires_in=None, refresh_token=None, client_id=None, client_refresh_token_life_time_in_minutes=None, issued=None, expires=None):
        """
        AccessTokenResponse - a model defined in Swagger
        """

        self._access_token = None
        self._token_type = None
        self._expires_in = None
        self._refresh_token = None
        self._client_id = None
        self._client_refresh_token_life_time_in_minutes = None
        self._issued = None
        self._expires = None
        self.discriminator = None

        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_refresh_token_life_time_in_minutes = client_refresh_token_life_time_in_minutes
        self.issued = issued
        self.expires = expires

    @property
    def access_token(self):
        """
        Gets the access_token of this AccessTokenResponse.

        :return: The access_token of this AccessTokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this AccessTokenResponse.

        :param access_token: The access_token of this AccessTokenResponse.
        :type: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")

        self._access_token = access_token

    @property
    def token_type(self):
        """
        Gets the token_type of this AccessTokenResponse.

        :return: The token_type of this AccessTokenResponse.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this AccessTokenResponse.

        :param token_type: The token_type of this AccessTokenResponse.
        :type: str
        """
        if token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")

        self._token_type = token_type

    @property
    def expires_in(self):
        """
        Gets the expires_in of this AccessTokenResponse.

        :return: The expires_in of this AccessTokenResponse.
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this AccessTokenResponse.

        :param expires_in: The expires_in of this AccessTokenResponse.
        :type: str
        """
        if expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this AccessTokenResponse.

        :return: The refresh_token of this AccessTokenResponse.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this AccessTokenResponse.

        :param refresh_token: The refresh_token of this AccessTokenResponse.
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")

        self._refresh_token = refresh_token

    @property
    def client_id(self):
        """
        Gets the client_id of this AccessTokenResponse.

        :return: The client_id of this AccessTokenResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AccessTokenResponse.

        :param client_id: The client_id of this AccessTokenResponse.
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_refresh_token_life_time_in_minutes(self):
        """
        Gets the client_refresh_token_life_time_in_minutes of this AccessTokenResponse.

        :return: The client_refresh_token_life_time_in_minutes of this AccessTokenResponse.
        :rtype: str
        """
        return self._client_refresh_token_life_time_in_minutes

    @client_refresh_token_life_time_in_minutes.setter
    def client_refresh_token_life_time_in_minutes(self, client_refresh_token_life_time_in_minutes):
        """
        Sets the client_refresh_token_life_time_in_minutes of this AccessTokenResponse.

        :param client_refresh_token_life_time_in_minutes: The client_refresh_token_life_time_in_minutes of this AccessTokenResponse.
        :type: str
        """
        if client_refresh_token_life_time_in_minutes is None:
            raise ValueError("Invalid value for `client_refresh_token_life_time_in_minutes`, must not be `None`")

        self._client_refresh_token_life_time_in_minutes = client_refresh_token_life_time_in_minutes

    @property
    def issued(self):
        """
        Gets the issued of this AccessTokenResponse.

        :return: The issued of this AccessTokenResponse.
        :rtype: str
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """
        Sets the issued of this AccessTokenResponse.

        :param issued: The issued of this AccessTokenResponse.
        :type: str
        """
        if issued is None:
            raise ValueError("Invalid value for `issued`, must not be `None`")

        self._issued = issued

    @property
    def expires(self):
        """
        Gets the expires of this AccessTokenResponse.

        :return: The expires of this AccessTokenResponse.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this AccessTokenResponse.

        :param expires: The expires of this AccessTokenResponse.
        :type: str
        """
        if expires is None:
            raise ValueError("Invalid value for `expires`, must not be `None`")

        self._expires = expires

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AccessTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
