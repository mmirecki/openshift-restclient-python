# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ClusterPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, kind=None, last_modified=None, metadata=None, roles=None):
        """
        V1ClusterPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'last_modified': 'UnversionedTime',
            'metadata': 'V1ObjectMeta',
            'roles': 'list[V1NamedClusterRole]'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'last_modified': 'lastModified',
            'metadata': 'metadata',
            'roles': 'roles'
        }

        self._api_version = api_version
        self._kind = kind
        self._last_modified = last_modified
        self._metadata = metadata
        self._roles = roles

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ClusterPolicy.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ClusterPolicy.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ClusterPolicy.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ClusterPolicy.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1ClusterPolicy.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ClusterPolicy.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ClusterPolicy.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ClusterPolicy.
        :type: str
        """

        self._kind = kind

    @property
    def last_modified(self):
        """
        Gets the last_modified of this V1ClusterPolicy.
        LastModified is the last time that any part of the ClusterPolicy was created, updated, or deleted

        :return: The last_modified of this V1ClusterPolicy.
        :rtype: UnversionedTime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this V1ClusterPolicy.
        LastModified is the last time that any part of the ClusterPolicy was created, updated, or deleted

        :param last_modified: The last_modified of this V1ClusterPolicy.
        :type: UnversionedTime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")

        self._last_modified = last_modified

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ClusterPolicy.
        Standard object's metadata.

        :return: The metadata of this V1ClusterPolicy.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ClusterPolicy.
        Standard object's metadata.

        :param metadata: The metadata of this V1ClusterPolicy.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def roles(self):
        """
        Gets the roles of this V1ClusterPolicy.
        Roles holds all the ClusterRoles held by this ClusterPolicy, mapped by ClusterRole.Name

        :return: The roles of this V1ClusterPolicy.
        :rtype: list[V1NamedClusterRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this V1ClusterPolicy.
        Roles holds all the ClusterRoles held by this ClusterPolicy, mapped by ClusterRole.Name

        :param roles: The roles of this V1ClusterPolicy.
        :type: list[V1NamedClusterRole]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")

        self._roles = roles

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
