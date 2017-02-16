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


class V1BuildRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, binary=None, env=None, _from=None, kind=None, last_version=None, metadata=None, revision=None, triggered_by=None, triggered_by_image=None):
        """
        V1BuildRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'binary': 'V1BinaryBuildSource',
            'env': 'list[V1EnvVar]',
            '_from': 'V1ObjectReference',
            'kind': 'str',
            'last_version': 'int',
            'metadata': 'V1ObjectMeta',
            'revision': 'V1SourceRevision',
            'triggered_by': 'list[V1BuildTriggerCause]',
            'triggered_by_image': 'V1ObjectReference'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'binary': 'binary',
            'env': 'env',
            '_from': 'from',
            'kind': 'kind',
            'last_version': 'lastVersion',
            'metadata': 'metadata',
            'revision': 'revision',
            'triggered_by': 'triggeredBy',
            'triggered_by_image': 'triggeredByImage'
        }

        self._api_version = api_version
        self._binary = binary
        self._env = env
        self.__from = _from
        self._kind = kind
        self._last_version = last_version
        self._metadata = metadata
        self._revision = revision
        self._triggered_by = triggered_by
        self._triggered_by_image = triggered_by_image

    @property
    def api_version(self):
        """
        Gets the api_version of this V1BuildRequest.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1BuildRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1BuildRequest.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1BuildRequest.
        :type: str
        """

        self._api_version = api_version

    @property
    def binary(self):
        """
        Gets the binary of this V1BuildRequest.
        binary indicates a request to build from a binary provided to the builder

        :return: The binary of this V1BuildRequest.
        :rtype: V1BinaryBuildSource
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this V1BuildRequest.
        binary indicates a request to build from a binary provided to the builder

        :param binary: The binary of this V1BuildRequest.
        :type: V1BinaryBuildSource
        """

        self._binary = binary

    @property
    def env(self):
        """
        Gets the env of this V1BuildRequest.
        env contains additional environment variables you want to pass into a builder container

        :return: The env of this V1BuildRequest.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1BuildRequest.
        env contains additional environment variables you want to pass into a builder container

        :param env: The env of this V1BuildRequest.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def _from(self):
        """
        Gets the _from of this V1BuildRequest.
        from is the reference to the ImageStreamTag that triggered the build.

        :return: The _from of this V1BuildRequest.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1BuildRequest.
        from is the reference to the ImageStreamTag that triggered the build.

        :param _from: The _from of this V1BuildRequest.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def kind(self):
        """
        Gets the kind of this V1BuildRequest.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1BuildRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1BuildRequest.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1BuildRequest.
        :type: str
        """

        self._kind = kind

    @property
    def last_version(self):
        """
        Gets the last_version of this V1BuildRequest.
        lastVersion (optional) is the LastVersion of the BuildConfig that was used to generate the build. If the BuildConfig in the generator doesn't match, a build will not be generated.

        :return: The last_version of this V1BuildRequest.
        :rtype: int
        """
        return self._last_version

    @last_version.setter
    def last_version(self, last_version):
        """
        Sets the last_version of this V1BuildRequest.
        lastVersion (optional) is the LastVersion of the BuildConfig that was used to generate the build. If the BuildConfig in the generator doesn't match, a build will not be generated.

        :param last_version: The last_version of this V1BuildRequest.
        :type: int
        """

        self._last_version = last_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1BuildRequest.
        metadata for BuildRequest.

        :return: The metadata of this V1BuildRequest.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1BuildRequest.
        metadata for BuildRequest.

        :param metadata: The metadata of this V1BuildRequest.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def revision(self):
        """
        Gets the revision of this V1BuildRequest.
        revision is the information from the source for a specific repo snapshot.

        :return: The revision of this V1BuildRequest.
        :rtype: V1SourceRevision
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this V1BuildRequest.
        revision is the information from the source for a specific repo snapshot.

        :param revision: The revision of this V1BuildRequest.
        :type: V1SourceRevision
        """

        self._revision = revision

    @property
    def triggered_by(self):
        """
        Gets the triggered_by of this V1BuildRequest.
        triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers.

        :return: The triggered_by of this V1BuildRequest.
        :rtype: list[V1BuildTriggerCause]
        """
        return self._triggered_by

    @triggered_by.setter
    def triggered_by(self, triggered_by):
        """
        Sets the triggered_by of this V1BuildRequest.
        triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers.

        :param triggered_by: The triggered_by of this V1BuildRequest.
        :type: list[V1BuildTriggerCause]
        """
        if triggered_by is None:
            raise ValueError("Invalid value for `triggered_by`, must not be `None`")

        self._triggered_by = triggered_by

    @property
    def triggered_by_image(self):
        """
        Gets the triggered_by_image of this V1BuildRequest.
        triggeredByImage is the Image that triggered this build.

        :return: The triggered_by_image of this V1BuildRequest.
        :rtype: V1ObjectReference
        """
        return self._triggered_by_image

    @triggered_by_image.setter
    def triggered_by_image(self, triggered_by_image):
        """
        Sets the triggered_by_image of this V1BuildRequest.
        triggeredByImage is the Image that triggered this build.

        :param triggered_by_image: The triggered_by_image of this V1BuildRequest.
        :type: V1ObjectReference
        """

        self._triggered_by_image = triggered_by_image

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
