# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use openshift.client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a openshift.client. By listing and beginning a watch from the returned resourceVersion, openshift.clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so openshift.clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but openshift.clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import openshift.client
from kubernetes.client.rest import ApiException
from openshift.client.apis.extensions_v1beta1_api import ExtensionsV1beta1Api


class TestExtensionsV1beta1Api(unittest.TestCase):
    """ ExtensionsV1beta1Api unit test stubs """

    def setUp(self):
        self.api = openshift.client.apis.extensions_v1beta1_api.ExtensionsV1beta1Api()

    def tearDown(self):
        pass

    def test_create_daemon_set_for_all_namespaces(self):
        """
        Test case for create_daemon_set_for_all_namespaces

        
        """
        pass

    def test_create_deployment_for_all_namespaces(self):
        """
        Test case for create_deployment_for_all_namespaces

        
        """
        pass

    def test_create_horizontal_pod_autoscaler_for_all_namespaces(self):
        """
        Test case for create_horizontal_pod_autoscaler_for_all_namespaces

        
        """
        pass

    def test_create_ingress_for_all_namespaces(self):
        """
        Test case for create_ingress_for_all_namespaces

        
        """
        pass

    def test_create_job_for_all_namespaces(self):
        """
        Test case for create_job_for_all_namespaces

        
        """
        pass

    def test_create_namespaced_daemon_set(self):
        """
        Test case for create_namespaced_daemon_set

        
        """
        pass

    def test_create_namespaced_deployment(self):
        """
        Test case for create_namespaced_deployment

        
        """
        pass

    def test_create_namespaced_deployment_rollback_rollback(self):
        """
        Test case for create_namespaced_deployment_rollback_rollback

        
        """
        pass

    def test_create_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for create_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_create_namespaced_ingress(self):
        """
        Test case for create_namespaced_ingress

        
        """
        pass

    def test_create_namespaced_job(self):
        """
        Test case for create_namespaced_job

        
        """
        pass

    def test_create_namespaced_network_policy(self):
        """
        Test case for create_namespaced_network_policy

        
        """
        pass

    def test_create_namespaced_replica_set(self):
        """
        Test case for create_namespaced_replica_set

        
        """
        pass

    def test_create_network_policy_for_all_namespaces(self):
        """
        Test case for create_network_policy_for_all_namespaces

        
        """
        pass

    def test_create_pod_security_policy(self):
        """
        Test case for create_pod_security_policy

        
        """
        pass

    def test_create_replica_set_for_all_namespaces(self):
        """
        Test case for create_replica_set_for_all_namespaces

        
        """
        pass

    def test_create_third_party_resource(self):
        """
        Test case for create_third_party_resource

        
        """
        pass

    def test_delete_collection_namespaced_daemon_set(self):
        """
        Test case for delete_collection_namespaced_daemon_set

        
        """
        pass

    def test_delete_collection_namespaced_deployment(self):
        """
        Test case for delete_collection_namespaced_deployment

        
        """
        pass

    def test_delete_collection_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for delete_collection_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_delete_collection_namespaced_ingress(self):
        """
        Test case for delete_collection_namespaced_ingress

        
        """
        pass

    def test_delete_collection_namespaced_job(self):
        """
        Test case for delete_collection_namespaced_job

        
        """
        pass

    def test_delete_collection_namespaced_network_policy(self):
        """
        Test case for delete_collection_namespaced_network_policy

        
        """
        pass

    def test_delete_collection_namespaced_replica_set(self):
        """
        Test case for delete_collection_namespaced_replica_set

        
        """
        pass

    def test_delete_collection_pod_security_policy(self):
        """
        Test case for delete_collection_pod_security_policy

        
        """
        pass

    def test_delete_collection_third_party_resource(self):
        """
        Test case for delete_collection_third_party_resource

        
        """
        pass

    def test_delete_namespaced_daemon_set(self):
        """
        Test case for delete_namespaced_daemon_set

        
        """
        pass

    def test_delete_namespaced_deployment(self):
        """
        Test case for delete_namespaced_deployment

        
        """
        pass

    def test_delete_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for delete_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_delete_namespaced_ingress(self):
        """
        Test case for delete_namespaced_ingress

        
        """
        pass

    def test_delete_namespaced_job(self):
        """
        Test case for delete_namespaced_job

        
        """
        pass

    def test_delete_namespaced_network_policy(self):
        """
        Test case for delete_namespaced_network_policy

        
        """
        pass

    def test_delete_namespaced_replica_set(self):
        """
        Test case for delete_namespaced_replica_set

        
        """
        pass

    def test_delete_pod_security_policy(self):
        """
        Test case for delete_pod_security_policy

        
        """
        pass

    def test_delete_third_party_resource(self):
        """
        Test case for delete_third_party_resource

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_daemon_set_for_all_namespaces(self):
        """
        Test case for list_daemon_set_for_all_namespaces

        
        """
        pass

    def test_list_deployment_for_all_namespaces(self):
        """
        Test case for list_deployment_for_all_namespaces

        
        """
        pass

    def test_list_horizontal_pod_autoscaler_for_all_namespaces(self):
        """
        Test case for list_horizontal_pod_autoscaler_for_all_namespaces

        
        """
        pass

    def test_list_ingress_for_all_namespaces(self):
        """
        Test case for list_ingress_for_all_namespaces

        
        """
        pass

    def test_list_job_for_all_namespaces(self):
        """
        Test case for list_job_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_daemon_set(self):
        """
        Test case for list_namespaced_daemon_set

        
        """
        pass

    def test_list_namespaced_deployment(self):
        """
        Test case for list_namespaced_deployment

        
        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for list_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_list_namespaced_ingress(self):
        """
        Test case for list_namespaced_ingress

        
        """
        pass

    def test_list_namespaced_job(self):
        """
        Test case for list_namespaced_job

        
        """
        pass

    def test_list_namespaced_network_policy(self):
        """
        Test case for list_namespaced_network_policy

        
        """
        pass

    def test_list_namespaced_replica_set(self):
        """
        Test case for list_namespaced_replica_set

        
        """
        pass

    def test_list_network_policy_for_all_namespaces(self):
        """
        Test case for list_network_policy_for_all_namespaces

        
        """
        pass

    def test_list_pod_security_policy(self):
        """
        Test case for list_pod_security_policy

        
        """
        pass

    def test_list_replica_set_for_all_namespaces(self):
        """
        Test case for list_replica_set_for_all_namespaces

        
        """
        pass

    def test_list_third_party_resource(self):
        """
        Test case for list_third_party_resource

        
        """
        pass

    def test_patch_namespaced_daemon_set(self):
        """
        Test case for patch_namespaced_daemon_set

        
        """
        pass

    def test_patch_namespaced_daemon_set_status(self):
        """
        Test case for patch_namespaced_daemon_set_status

        
        """
        pass

    def test_patch_namespaced_deployment(self):
        """
        Test case for patch_namespaced_deployment

        
        """
        pass

    def test_patch_namespaced_deployment_status(self):
        """
        Test case for patch_namespaced_deployment_status

        
        """
        pass

    def test_patch_namespaced_deployments_scale(self):
        """
        Test case for patch_namespaced_deployments_scale

        
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_patch_namespaced_ingress(self):
        """
        Test case for patch_namespaced_ingress

        
        """
        pass

    def test_patch_namespaced_ingress_status(self):
        """
        Test case for patch_namespaced_ingress_status

        
        """
        pass

    def test_patch_namespaced_job(self):
        """
        Test case for patch_namespaced_job

        
        """
        pass

    def test_patch_namespaced_job_status(self):
        """
        Test case for patch_namespaced_job_status

        
        """
        pass

    def test_patch_namespaced_network_policy(self):
        """
        Test case for patch_namespaced_network_policy

        
        """
        pass

    def test_patch_namespaced_replica_set(self):
        """
        Test case for patch_namespaced_replica_set

        
        """
        pass

    def test_patch_namespaced_replica_set_status(self):
        """
        Test case for patch_namespaced_replica_set_status

        
        """
        pass

    def test_patch_namespaced_replicasets_scale(self):
        """
        Test case for patch_namespaced_replicasets_scale

        
        """
        pass

    def test_patch_namespaced_replicationcontrollers_scale(self):
        """
        Test case for patch_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_patch_pod_security_policy(self):
        """
        Test case for patch_pod_security_policy

        
        """
        pass

    def test_patch_third_party_resource(self):
        """
        Test case for patch_third_party_resource

        
        """
        pass

    def test_read_namespaced_daemon_set(self):
        """
        Test case for read_namespaced_daemon_set

        
        """
        pass

    def test_read_namespaced_daemon_set_status(self):
        """
        Test case for read_namespaced_daemon_set_status

        
        """
        pass

    def test_read_namespaced_deployment(self):
        """
        Test case for read_namespaced_deployment

        
        """
        pass

    def test_read_namespaced_deployment_status(self):
        """
        Test case for read_namespaced_deployment_status

        
        """
        pass

    def test_read_namespaced_deployments_scale(self):
        """
        Test case for read_namespaced_deployments_scale

        
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_read_namespaced_ingress(self):
        """
        Test case for read_namespaced_ingress

        
        """
        pass

    def test_read_namespaced_ingress_status(self):
        """
        Test case for read_namespaced_ingress_status

        
        """
        pass

    def test_read_namespaced_job(self):
        """
        Test case for read_namespaced_job

        
        """
        pass

    def test_read_namespaced_job_status(self):
        """
        Test case for read_namespaced_job_status

        
        """
        pass

    def test_read_namespaced_network_policy(self):
        """
        Test case for read_namespaced_network_policy

        
        """
        pass

    def test_read_namespaced_replica_set(self):
        """
        Test case for read_namespaced_replica_set

        
        """
        pass

    def test_read_namespaced_replica_set_status(self):
        """
        Test case for read_namespaced_replica_set_status

        
        """
        pass

    def test_read_namespaced_replicasets_scale(self):
        """
        Test case for read_namespaced_replicasets_scale

        
        """
        pass

    def test_read_namespaced_replicationcontrollers_scale(self):
        """
        Test case for read_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_read_pod_security_policy(self):
        """
        Test case for read_pod_security_policy

        
        """
        pass

    def test_read_third_party_resource(self):
        """
        Test case for read_third_party_resource

        
        """
        pass

    def test_replace_namespaced_daemon_set(self):
        """
        Test case for replace_namespaced_daemon_set

        
        """
        pass

    def test_replace_namespaced_daemon_set_status(self):
        """
        Test case for replace_namespaced_daemon_set_status

        
        """
        pass

    def test_replace_namespaced_deployment(self):
        """
        Test case for replace_namespaced_deployment

        
        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """
        Test case for replace_namespaced_deployment_status

        
        """
        pass

    def test_replace_namespaced_deployments_scale(self):
        """
        Test case for replace_namespaced_deployments_scale

        
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler

        
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler_status

        
        """
        pass

    def test_replace_namespaced_ingress(self):
        """
        Test case for replace_namespaced_ingress

        
        """
        pass

    def test_replace_namespaced_ingress_status(self):
        """
        Test case for replace_namespaced_ingress_status

        
        """
        pass

    def test_replace_namespaced_job(self):
        """
        Test case for replace_namespaced_job

        
        """
        pass

    def test_replace_namespaced_job_status(self):
        """
        Test case for replace_namespaced_job_status

        
        """
        pass

    def test_replace_namespaced_network_policy(self):
        """
        Test case for replace_namespaced_network_policy

        
        """
        pass

    def test_replace_namespaced_replica_set(self):
        """
        Test case for replace_namespaced_replica_set

        
        """
        pass

    def test_replace_namespaced_replica_set_status(self):
        """
        Test case for replace_namespaced_replica_set_status

        
        """
        pass

    def test_replace_namespaced_replicasets_scale(self):
        """
        Test case for replace_namespaced_replicasets_scale

        
        """
        pass

    def test_replace_namespaced_replicationcontrollers_scale(self):
        """
        Test case for replace_namespaced_replicationcontrollers_scale

        
        """
        pass

    def test_replace_pod_security_policy(self):
        """
        Test case for replace_pod_security_policy

        
        """
        pass

    def test_replace_third_party_resource(self):
        """
        Test case for replace_third_party_resource

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
